# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

# -*- coding: utf-8 -*-
"""Module for handling of NVM definitions and for generation of c&h-files defining the memory layout of the NVM."""
import re
import os
import json

import pybuild.build_defs as bd
from pybuild.types import byte_size, get_bitmask
from pybuild.a2l import A2l
from pybuild.problem_logger import ProblemLogger


class NVMDef(ProblemLogger):
    """A class that holds the NVM definitions for the build.

    Provides methods for generating NVM structs and header files.
    The header files includes defines which reference the
    struct elements as variables.
    """

    class WrongTypeException(Exception):
        """WrongTypeException."""

    _allowed_nvm_memory_areas = [
        "NVM_LIST_32",
        "NVM_LIST_16",
        "NVM_LIST_8",
        "NVM_LIST_32_PER",
        "NVM_LIST_16_PER",
        "NVM_LIST_8_PER",
        "NVM_LIST_CRITICAL1",
        "NVM_LIST_CRITICAL2",
    ]

    _nvm_header_footer = "\n#endif /* VCC_NVM_STRUCT_H */\n"

    def __init__(self, project_config, unit_cfg, nvm_vars):
        """Constructor.

        Args:
            project_config (BuildProjConfig): current project configuration
            unit_cfg (UnitConfigs): unit definitions
            nvm_vars (dict): NVM variables from unit configurations (:doc:`UnitConfigs <unit_configs>`)

        """
        super().__init__()
        self._project_config = project_config
        self._nvm_vars = nvm_vars
        # get the size of areas and c-file names
        self._nvm_defs = project_config.get_nvm_defs()
        self._nvm_signals = {}
        self._nvm_memory_areas = tuple()
        self._mem_area_elem_size = {}
        self._area_section = {}
        self._mem_area_pragmas = tuple()
        self._nvm_header_head = self._get_nvm_header_head(unit_cfg)

        with open(
            os.path.join(project_config.get_root_dir(), self._nvm_defs["baseNvmStructs"]), "r", encoding="utf-8"
        ) as nvm_json:
            self.nvm_definitions = json.load(nvm_json)
        for memory_area in self.nvm_definitions:
            self._add_memory_area(memory_area)
        self._order_nvm_per_area()
        for memory_area in self.nvm_definitions:
            memory_index = self._get_nvm_areas_index(memory_area["name"])
            self.info("Updating %s with index %s", memory_area["name"], memory_index)
            self.nvm_definitions[memory_index]["signals"] = self._get_signal_list(memory_area["signals"])

    @staticmethod
    def _get_nvm_header_head(unit_cfg):
        _nvm_header_head = (
            "/*\n"
            " *  vcc_nvm_struct.h - struct for NVM signals\n"
            " */\n\n"
            "#ifndef VCC_NVM_STRUCT_H\n"
            "#define VCC_NVM_STRUCT_H\n\n"
        )
        _nvm_header_head += unit_cfg.base_types_headers
        return _nvm_header_head

    def _add_memory_area(self, memory_area):
        """Add non-default areas."""
        if memory_area["name"] not in self._allowed_nvm_memory_areas:
            msg = f"Memory area: {memory_area['name']} not allowed"
            self.critical(msg)
            raise NVMDef.WrongTypeException(msg)

        self._nvm_memory_areas = (*self._nvm_memory_areas, memory_area["name"])
        self._mem_area_elem_size.update({memory_area["name"]: byte_size(memory_area["default_datatype"])})

        if memory_area["persistent"]:
            self._area_section.update({memory_area["name"]: "CVC_NVM_P"})
            self._mem_area_pragmas = (*self._mem_area_pragmas, (bd.CVC_NVM_P_START, bd.CVC_NVM_P_END))
        else:
            self._area_section.update({memory_area["name"]: "CVC_NVM"})
            self._mem_area_pragmas = (*self._mem_area_pragmas, (bd.CVC_NVM_START, bd.CVC_NVM_END))

    def _var_to_area(self, var_info):
        """Find the NVM area for the variable.

        Args:
            var_info (dict): a dict with the variable attributes.

        Returns:
            area (str): a string with the area the variable should be
                        defined in.

        """
        mtch = re.match(r"\D+(\d+)?", var_info["type"])
        if mtch.group(1) is None:
            size = "8"
        else:
            size = mtch.group(1)
        if var_info["class"] == "CVC_DISP_NVM":
            return "NVM_LIST_" + size
        if var_info["class"] == "CVC_DISP_NVM_P":
            return "NVM_LIST_" + size + "_PER"
        self.critical("%s is not a NVM variable!", var_info["name"])
        return None

    def _order_nvm_per_area(self):
        """Order the NVM in the areas, based on the definitions."""
        for var, unit_attrib in self._nvm_vars.items():
            for _, var_attribs in unit_attrib.items():
                area = self._var_to_area(var_attribs)
                self._nvm_signals[var] = var_attribs
                self._nvm_signals[var]["area"] = area
                # only use one units definition
                # TODO:Make a nicer solution #
                break

    def nvm_area_iterator(self, nvm_area_name):
        """Get an iterator for NVM 'area'.

        The iterator yields data_type and and variable name for the
        variables defined in the area.

        Args:
            nvm_area_name (str): the name of the NVM area

        Returns:
            tuple: (data_type, variable name, size)

        """
        for nvm_signal_name, nvm_attributes in self._nvm_signals.items():
            if nvm_attributes["area"] == nvm_area_name:
                yield nvm_attributes.get("type"), nvm_signal_name, nvm_attributes.get("width", 1)

    def _a2l_dict(self, use_prefix):
        """Return a dict defining all parameters for a2l-generation.

        Args:
            use_prefix (bool): Patch the nvm header file definitions with the SWC name as prefix.
        """
        res = {}
        prefix = f"{self._project_config.get_swc_name()}_" if use_prefix else ""
        for var, var_attrib in self._nvm_signals.items():
            res[var] = {
                "var": {"var": var, "type": var_attrib["type"], "cvc_type": "CVC_NVM"},
                "a2l_data": {
                    "bitmask": get_bitmask(var_attrib["type"]),
                    "description": var_attrib["description"],
                    "lsb": var_attrib.get("lsb", 1),
                    "max": var_attrib.get("max"),
                    "min": var_attrib.get("min"),
                    "offset": var_attrib.get("offset"),
                    "unit": var_attrib["unit"],
                    "symbol": prefix.lower() + var_attrib["area"].lower(),
                    "symbol_offset": var_attrib.get("struct_off"),
                },
            }
            width = var_attrib.get("width", 1)
            if width:
                if isinstance(width, list):
                    res[var]["array"] = width
                elif int(width) > 1:
                    res[var]["array"] = [width]
        return {"vars": res, "function": "VcNvm"}

    @staticmethod
    def _compare_size(signal, widths):
        """Compare a json signal object with widths array.

        :param signal: signal name
        :param widths: array matrix size
        :return: bool True if size is the same

        """
        return signal["x_size"] == widths[0] and signal["y_size"] == widths[1]

    @staticmethod
    def _clean_values(widths):
        """Get clean width values.

        Sometimes width array i set to -1,
        (This data is read out from the simulink model in the matlab scripts,
        -1 is simulink logic for the values should be inherited).
        :param widths:
        :return: a correct widths array
        """
        if widths in ("-1", 1):
            widths = [1, 1]
        return widths

    def _assert_data_type(self, signal, memory_area):
        memory_area_index = self._get_nvm_areas_index(memory_area)
        if "NotApplicable" in self.nvm_definitions[memory_area_index]["allowed_datatypes"]:
            # Special case for NVM_LIST_CRITICAL1 and 2. Any type is acceptable.
            self.debug("Data type is not checked for %s", self.nvm_definitions[memory_area_index]["name"])
            return
        if signal["type"] not in self.nvm_definitions[memory_area_index]["allowed_datatypes"]:
            msg = f"Signal type:{signal['type']} for {signal['name']} not allowed in area:{memory_area}"
            self.critical(msg)
            raise NVMDef.WrongTypeException(msg)

    def _compare_signal(self, signal, data_type, widths, persistent_signal):
        """Compare signal and warn if there is a mismatch in data type or size.

        :param signal: signal object from nvm_structs.json file
        :param data_type: str
        :param widths: array matrix size
        :return: True if the signal is the same in both json struct and values read from simulink model.

        """
        if data_type != signal["type"]:
            log = self.critical if persistent_signal else self.warning
            log("NVM signal: %s type mismatch %s != %s ", signal["name"], data_type, signal["type"])
            return False
        if not self._compare_size(signal, widths):
            self.critical(
                "signal:%s  size mismatch %s != %s,%s ", signal["name"], widths, signal["x_size"], signal["y_size"]
            )
            return False

        return True

    def _get_nvm_areas_index(self, area):
        """Get array index of nvm area.

        :param area: wanted nvm area as string
        :return: (int) nvm areas index in self.nvm_definitions
        """
        return next(
            (index for index, nvm_definition in enumerate(self.nvm_definitions) if nvm_definition["name"] == area), -1
        )

    def _find_empty_index(self, memory_index, signal):
        """Find empty index in array of signals.

        :param memory_index: array index (NVM area)
        :param signal: signal to add at empty index
        :return: (int) empty index, (-1 if not found)
        """
        for signal_index in range(len(self.nvm_definitions[memory_index]["signals"])):
            signal_candidate = self.nvm_definitions[memory_index]["signals"][signal_index]
            if self._compare_size(signal, (signal_candidate["x_size"], signal_candidate["y_size"])) and (
                signal_candidate["name"].startswith("Pos_") or signal_candidate["name"].startswith("Position_")
            ):
                return signal_index
        return -1

    def _add_signal_to_nvm_struct(self, memory_index, signal_name, data_type, widths):
        """Add a signal to nvm struct at first empty index.

        :param memory_index: array index (NVM area)
        :param signal_name: str signal_nameiable name
        :param data_type: str
        :param widths: array matrix size
        """
        if widths == "-1":
            widths = [1, 1]
        elif widths == "-":
            self.critical("Bad widths value (%s), cannot add: %s", widths, signal_name)
            return

        new_signal = self._get_memory_area_signal_template(memory_index)
        new_signal["name"] = signal_name
        new_signal["type"] = data_type
        new_signal["x_size"] = int(widths[0])
        new_signal["y_size"] = int(widths[1])
        signal_index = self._find_empty_index(memory_index, new_signal)
        if signal_index > -1:
            self.debug("Add at empty signal_index %s", signal_index)
            self._update_nvm_signal(memory_index, signal_index, new_signal)
        else:
            self.nvm_definitions[memory_index]["signals"].append(new_signal)

    def _get_signals_in_nvm_structs(self):
        signals_in_nvm_structs = {}
        for memory_area in self._nvm_memory_areas:
            memory_area_index = self._get_nvm_areas_index(memory_area)
            signals = self.nvm_definitions[memory_area_index]["signals"]
            for signal_index, signal in enumerate(signals):
                signals_in_nvm_structs.update(
                    {signal["name"]: {"memory_area": memory_area, "signal_index": signal_index}}
                )
        return signals_in_nvm_structs

    def _dummify_nvm_signal(self, memory_area, signal_index):
        dummy_name = f"Pos_{memory_area}bit{'_P' if memory_area.endswith('PER') else ''}_{signal_index}"
        memory_index = self._get_nvm_areas_index(memory_area)
        self.nvm_definitions[memory_index]["signals"][signal_index]["name"] = dummy_name
        self.debug("Name of signal in nvm_structs.json was set to %s", dummy_name)

    def _get_nvm_signal(self, memory_index, signal_index):
        return self.nvm_definitions[memory_index]["signals"][signal_index]

    def _update_nvm_signal(self, memory_index, signal_index, signal):
        self.debug("Replacing %s with %s", self.nvm_definitions[memory_index]["signals"][signal_index], signal)
        self.nvm_definitions[memory_index]["signals"][signal_index] = signal

    def _update_duplicate_nvm_definition(self, nvm_structs_signals, model_signal, model_memory_area):
        """Check if already existing nvm signal is correctly configured."""
        nvm_structs_memory_area = nvm_structs_signals[model_signal["name"]]["memory_area"]
        nvm_structs_signal_index = nvm_structs_signals[model_signal["name"]]["signal_index"]
        nvm_structs_memory_index = self._get_nvm_areas_index(nvm_structs_memory_area)
        nvm_structs_signal = self._get_nvm_signal(nvm_structs_memory_index, nvm_structs_signal_index)
        model_memory_index = self._get_nvm_areas_index(model_memory_area)
        model_signal_widths = (model_signal["x_size"], model_signal["y_size"])

        if "NVM_LIST_CRITICAL" in nvm_structs_memory_area:
            # In this case, we need to update the signal memory area.
            # _var_to_area cannot guess the right area for signals located in the critical sections due to varying data
            # types
            self.debug("Keeping signal %s in %s", model_signal["name"], nvm_structs_memory_area)
            self._nvm_signals[model_signal["name"]]["area"] = nvm_structs_memory_area
            return

        persistent_signal = "_PER" in model_memory_area or "_PER" in nvm_structs_memory_area
        if model_memory_area != nvm_structs_memory_area:
            self.warning("NVM signal memory area mismatch for signal: '%s'", model_signal["name"])
            self.warning("nvm_structs.json: '%s' - Memory area: %s", nvm_structs_memory_area, model_memory_area)
            self._dummify_nvm_signal(nvm_structs_memory_area, nvm_structs_signal_index)
            self._add_signal_to_nvm_struct(
                model_memory_index, model_signal["name"], model_signal["type"], model_signal_widths
            )
        elif not self._compare_signal(nvm_structs_signal, model_signal["type"], model_signal_widths, persistent_signal):
            if persistent_signal:
                self.warning("NVM signal type or size mismatch for signal: '%s'", model_signal["name"])
                self._dummify_nvm_signal(nvm_structs_memory_area, nvm_structs_signal_index)
                self._add_signal_to_nvm_struct(
                    model_memory_index, model_signal["name"], model_signal["type"], model_signal_widths
                )
                self.warning("%s relocated to fitting position", model_signal["name"])
            else:
                self._update_nvm_signal(nvm_structs_memory_index, nvm_structs_signal_index, model_signal)

    def _get_memory_area_signal_template(self, memory_area_index):
        memory_area = self.nvm_definitions[memory_area_index]
        signals = memory_area["signals"]
        if signals:
            return signals[0].copy()

        return {"name": "", "type": "", "x_size": "", "y_size": ""}

    def _update_nvm_base_struct(self):
        """Gather and update all nvm signals.

        1) Updates existing signals,
        2) Deletes/Dummy declares non- and persistent unused signals respectively,
        3) Adds new signals,
        in the nvm struct.
        """

        def remove_unused_signals_from_nvm_struct():
            """Remove unused signals from the nvm struct.

            The signals are listed in an array and accessed through calculated indices, therefore,
            all unused signals must be removed at once.
            """
            for mem_area in self._nvm_memory_areas:
                mem_area_index = self._get_nvm_areas_index(mem_area)
                unused_signals_in_area = [
                    signal_name
                    for signal_name, signal_info in unused_nvm_structs_signals.items()
                    if signal_info["memory_area"] == mem_area
                ]

                # Cannot remove signals from the persistent memory areas,
                # however, they can be exchanged for dummy signals
                if "_PER" in self.nvm_definitions[mem_area_index]["name"]:
                    for unused_signal_name in unused_signals_in_area:
                        if unused_signal_name.startswith("Pos"):
                            self.debug("Found unused signal: '%s' in memory area: %s", unused_signal_name, mem_area)
                        else:
                            self.warning("Found unused signal: '%s' in memory area: %s", unused_signal_name, mem_area)
                        self._dummify_nvm_signal(
                            mem_area, unused_nvm_structs_signals[unused_signal_name]["signal_index"]
                        )
                else:
                    self.nvm_definitions[mem_area_index]["signals"] = [
                        signal
                        for signal in self.nvm_definitions[mem_area_index]["signals"]
                        if signal["name"] not in unused_signals_in_area
                    ]

        nvm_structs_signals = self._get_signals_in_nvm_structs()
        unused_nvm_structs_signals = self._get_signals_in_nvm_structs()
        new_nvm_structs_signals = []

        for nvm_memory_area in self._nvm_memory_areas:
            memory_area_index = self._get_nvm_areas_index(nvm_memory_area)
            if "NVM_LIST_CRITICAL" in nvm_memory_area:
                # NVM_LIST_CRITICAL.* only exists in some projects
                continue
            if memory_area_index == -1:
                self.critical("NVM area not found for: %s", nvm_memory_area)
                continue
            for nvm_data_type, nvm_signal_name, nvm_widths in self.nvm_area_iterator(nvm_memory_area):
                nvm_widths = self._clean_values(nvm_widths)
                nvm_signal = self._get_memory_area_signal_template(memory_area_index)
                nvm_signal["name"] = nvm_signal_name
                nvm_signal["type"] = nvm_data_type
                nvm_signal["x_size"] = int(nvm_widths[0])
                nvm_signal["y_size"] = int(nvm_widths[1])
                if nvm_signal_name in nvm_structs_signals:
                    self.debug("Deleting %s", nvm_signal_name)
                    del unused_nvm_structs_signals[nvm_signal_name]
                    self._update_duplicate_nvm_definition(nvm_structs_signals, nvm_signal, nvm_memory_area)
                else:
                    new_nvm_structs_signals.append((memory_area_index, nvm_signal["name"], nvm_data_type, nvm_widths))
        remove_unused_signals_from_nvm_struct()

        for new_signal in new_nvm_structs_signals:
            self._add_signal_to_nvm_struct(*new_signal)

    def _generate_nvm_structs_updated(self):
        self.info("Start generating updated nvm json file")

        self._update_nvm_base_struct()

        nvm_structs_updated_path = os.path.abspath(
            os.path.join(self._project_config.get_root_dir(), "output", "nvm_structs_updated.json")
        )

        self.info("Created %s", nvm_structs_updated_path)

        with open(nvm_structs_updated_path, "w", encoding="utf-8") as nvm_structs_file:
            json.dump(self.nvm_definitions, nvm_structs_file, indent=4)

    def _generate_nvm_config_headers(self, use_prefix):
        """Generate nvm config h file.

        Args:
            use_prefix (bool): Patch the nvm header file definitions with the SWC name as prefix.
        """
        self.info("Start generating nvm header file")
        prefix = f"{self._project_config.get_swc_name()}_" if use_prefix else ""

        def write_signals():
            for memory_area in self._nvm_memory_areas:
                memory_area_index = self._get_nvm_areas_index(memory_area)
                section = self._area_section[memory_area]
                elem_size = self._mem_area_elem_size[memory_area]
                hptr.write(f'#include "{section}_START.h"\n')
                hptr.write(f"struct {prefix}{memory_area} {{\n")
                struct_off = 0

                signals = self.nvm_definitions[memory_area_index]["signals"]
                for signal in signals:
                    self._assert_data_type(signal, memory_area)
                    hptr.write(f'   {signal["type"]:7} _{signal["name"]}')
                    size_string = ""
                    size = max(signal["x_size"], 1) * max(signal["y_size"], 1)
                    if size > 1:
                        if signal["x_size"] > 1:
                            size_string += f'[{signal["x_size"]}]'
                        if signal["y_size"] > 1:
                            if signal["x_size"] < 2:
                                self.critical("NVM signal size incorrect. x_size should not be 1 if y_size > 1")
                                size_string += "[1]"
                            size_string += f'[{signal["y_size"]}]'
                        hptr.write(size_string)
                    hptr.write(";\n")
                    defines.append((signal["name"], f"{prefix.lower()}{memory_area.lower()}._{signal['name']}"))

                    if signal["name"] in self._nvm_signals:
                        self._nvm_signals[signal["name"]]["struct_off"] = struct_off

                    struct_off += size * byte_size(signal["type"])

                max_nr_signals = self.nvm_definitions[memory_area_index]["size"]
                tot_memory = max_nr_signals * elem_size
                free = tot_memory - struct_off
                if free > 0:
                    hptr.write(
                        f'   {self.nvm_definitions[memory_area_index]["default_datatype"]} '
                        f'unused[{int(free / elem_size)}];\n'
                    )
                elif free < 0:
                    self.critical("NVM area %s overrun!", self.nvm_definitions[memory_area_index]["name"])
                hptr.write(f"}}; /* {struct_off} bytes used of {tot_memory} */\n")
                hptr.write(f'#include "{section}_END.h"\n\n')

        def write_extern():
            hptr.write(f'#include "{bd.PREDECL_START}"\n')
            for area in self._nvm_memory_areas:
                hptr.write(f"extern struct {prefix}{area.upper()} {prefix.lower()}{area.lower()};\n")
            hptr.write(f'#include "{bd.PREDECL_END}"\n\n')

        def write_defines():
            hptr.write("\n")
            for var, define in defines:
                hptr.write(f"#define {var:40} {define}\n")

        src_file_dst = self._project_config.get_src_code_dst_dir()
        file_name = os.path.join(src_file_dst, self._nvm_defs["fileName"])
        defines = []

        with open(file_name + ".h", "w", encoding="utf-8") as hptr:
            hptr.write(self._nvm_header_head)
            write_signals()
            write_extern()
            write_defines()
            hptr.write(self._nvm_header_footer)

    def _generate_nvm_config_source(self, use_prefix):
        """Generate the c-file containing the NVM definition.

        Args:
            use_prefix (bool): Patch the nvm source file definitions with the SWC name as prefix.
        """
        # TODO: Add memory from previous builds!!! and mark old positions #
        self.info("Start generating nvm source file")
        prefix = f"{self._project_config.get_swc_name()}_" if use_prefix else ""
        src_file_dst = self._project_config.get_src_code_dst_dir()
        file_name = os.path.join(src_file_dst, self._nvm_defs["fileName"])
        with open(file_name + ".c", "w", encoding="utf-8") as cptr:
            cptr.write(f'#include "{self._nvm_defs["fileName"]}.h"\n\n')
            for area, pragma in zip(self._nvm_memory_areas, self._mem_area_pragmas):
                cptr.write(f'#include "{pragma[0]}"\n')
                cptr.write(f"struct {prefix}{area.upper()} {prefix.lower()}{area.lower()};\n")
                cptr.write(f'#include "{pragma[1]}"\n\n')

    def _generate_nvm_config_a2l(self, use_prefix):
        """Generate the a2l-file describing the NVM definition.

        Args:
            use_prefix (bool): Patch the nvm header file definitions with the SWC name as prefix.
        """
        self.info("Start generating nvm a2l file")

        src_file_dst = self._project_config.get_src_code_dst_dir()
        file_name = os.path.join(src_file_dst, self._nvm_defs["fileName"])
        a2l_dict = self._a2l_dict(use_prefix)
        a2l = A2l(a2l_dict, self._project_config)
        a2l.gen_a2l(file_name + ".a2l")

    def generate_nvm_config_files(self, no_nvm_a2l, use_prefix=False):
        """Generate all files for variables in the NVM definition.

        Args:
            no_nvm_a2l (bool): Do not generate a2l file.
            use_prefix (bool): Patch the nvm header file definitions with the SWC name as prefix.
        """
        self._generate_nvm_structs_updated()
        self._generate_nvm_config_headers(use_prefix)
        self._generate_nvm_config_source(use_prefix)
        if not no_nvm_a2l:
            self._generate_nvm_config_a2l(use_prefix)

    @staticmethod
    def _get_signal_list(signals):
        return signals if isinstance(signals, list) else [signals]
