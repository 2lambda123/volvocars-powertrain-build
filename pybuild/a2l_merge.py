# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

# -*- coding: utf-8 -*-
"""Module for merging of a2l-files."""

import json
import os
import re
from string import Template

from pybuild.lib.helper_functions import deep_dict_update
from pybuild.problem_logger import ProblemLogger
from pybuild.a2l_templates import A2lProjectTemplate, A2lSilverTemplate


class A2lMerge(ProblemLogger):
    """Class for merging of a2l-files."""

    def __init__(self, prj_cfg, ucfg, a2l_files_unit, a2l_files_gen):
        """Merge a2l-files based on provided project configuration.

        Removes symbols not included in the projects unit-config files.

        Args:
            prj_cfg (obj): Project config.
            ucfg (obj): Unit config.
            a2l_files_unit (list of str): Files to merge.
            a2l_files_gen (list of str): Files to merge.
        """
        super().__init__()
        self._prj_cfg = prj_cfg
        self._unit_cfg = ucfg
        self._per_unit_cfg = ucfg.get_per_unit_cfg()
        # generate the a2l string
        self._blks = {}
        self._removed_symbols = []
        self.a2l = ""

        # ----- Example blocks in a2l (TargetLink) -----
        #
        # /begin CHARACTERISTIC
        #     cVc_B_SeriesHev	/* Name */
        #     "Series hybrid"	/* LongIdentifier */
        #     VALUE	/* Type */
        #     0x00000000    /* address: cVc_B_SeriesHev */
        #     UBYTE_COL_DIRECT	/* Deposit */
        #     0	/* MaxDiff */
        #     Scaling_3	/* Conversion */
        #     0	/* LowerLimit */
        #     1	/* UpperLimit */
        # /end CHARACTERISTIC
        #
        #  Example of Bosch-nvm signal in nvm:
        #
        # /begin MEASUREMENT
        #     nvm_list_32._sVcDclVu_D_Markow /* Name */
        #     "No description given" /* LongIdentifier */
        #     ULONG   /* Datatype */
        #     VcNvm_1_0_None   /* Conversion */
        #     1   /* Resolution */
        #     0   /* Accuracy */
        #     0   /* LowerLimit */
        #     4294967295   /* UpperLimit */
        #     READ_WRITE
        #     MATRIX_DIM 152 1 1
        #     ECU_ADDRESS 0x00000000
        # /end MEASUREMENT
        #
        # ----- Example blocks in a2l (Embedded Coder) -----
        #
        # /begin MEASUREMENT
        #   /* Name                   */      sVcAesVe_md_VolmcOffs
        #   /* Long identifier        */      "Volumetric cylinder mass flow offset"
        #   /* Data type              */      FLOAT32_IEEE
        #   /* Conversion method      */      VcAesVe_CM_Float32_g_s
        #   /* Resolution (Not used)  */      0
        #   /* Accuracy (Not used)    */      0
        #   /* Lower limit            */      -100.0
        #   /* Upper limit            */      100.0
        #   ECU_ADDRESS                       0x0000 /* @ECU_Address@sVcAesVe_md_VolmcOffs@ */
        # /end MEASUREMENT
        #
        # /begin CHARACTERISTIC
        #   /* Name                   */      cVcAesVe_D_VolmcCmpSel
        #   /* Long Identifier        */      "Select compensation factor characterizing deviation from nominal voleff"
        #   /* Type                   */      VALUE
        #   /* ECU Address            */      0x0000 /* @ECU_Address@cVcAesVe_D_VolmcCmpSel@ */
        #   /* Record Layout          */      Scalar_UBYTE
        #   /* Maximum Difference     */      0
        #   /* Conversion Method      */      VcAesVe_CM_uint8
        #   /* Lower Limit            */      1.0
        #   /* Upper Limit            */      3.0
        # /end CHARACTERISTIC

        self._block_finder = re.compile(r'(?:\s*\n)*'           # Optional blank lines
                                        r'(\s*/begin (\w+)\s*'  # begin <something> block
                                        r'\n\s*([\w.]+).*?\n'   # label. (Bosch-nvm contains the .)
                                        r'.*?'                  # block definition
                                        r'/end\s+\2)',          # end <something> block. Same something as before
                                        flags=re.M | re.DOTALL)

        self._tl_compu_method_parser = re.compile(
            r'(?:\s*\n)*(?P<compu_method>'
            r'\s*/begin COMPU_METHOD\s*\n'
            r'\s*(?P<name>\w*)\s*(/\* Name \*/)?\s*\n'              # Name
            r'\s*"(?P<ID>.*?)"\s*(/\* LongIdentifier \*/.*?)\s*\n'  # Long Identifier
            r'\s*(?P<conv_type>[A-Z_]*).*\s*\n'                     # ConversionType
            r'\s*"(?P<disp_format>.*)"\s*(/\* Format \*/)?\s*\n'    # Format
            r'\s*"(?P<unit>.*?)"\s*(/\* Unit \*/)?\s*\n'            # Unit
            r'\s*(?P<conversion>.*)\s*\n'                           # COEFFS
            r'(?P<indentation>\s*)/end COMPU_METHOD)', flags=re.M)  # No DOTALL, so .* is [^\n]*

        # COMPU_METHOD parser that works with files generated by Embedded Coder
        self._ec_compu_method_parser = re.compile(
            r'(?:\s*\n)*(?P<compu_method>'
            r'\s*/begin COMPU_METHOD\s*\n'
            r'\s*(/\* Name of CompuMethod\s*\*/)?\s*(?P<name>\w*)\s*\n'    # Name
            r'\s*(/\* Long identifier\s*\*/)?\s*"(?P<ID>.*?)"\s*\n'        # Long Identifier
            r'\s*/\* Conversion Type\s*\*/\s*(?P<conv_type>[A-Z_]*)\s*\n'  # ConversionType
            r'\s*(/\* Format\s*\*/)?\s*"(?P<disp_format>.*?)"\s*\n'        # Format
            r'\s*(/\* Units\s*\*/)?\s*"(?P<unit>.*?)"\s*\n'                # Unit
            r'\s*/\* Coefficients\s*\*/\s*(?P<conversion>.*?)\s*\n'        # COEFFS
            r'(?P<indentation>\s*)/end COMPU_METHOD)', flags=re.M)         # No DOTALL, so .* is [^\n]*

        self._expr_block_meas_kp_blob_parser = re.compile(
            r'\/begin\s+(?P<keyword>\w+)\s+(?P<class>\w+)\s*\n'
            r'\s*KP_BLOB\s+(?P<address>0x[0-9a-fA-F]+)\s*\n'
            r'\s*\/end\s+\1'
        )

        self._compu_methods = {}
        self._included_compu_methods = []

        self._tl_compu_method_template = Template(
            '$indentation/begin COMPU_METHOD\n'
            '$indentation    $name   /* Name */\n'
            '$indentation    "$ID"    /* LongIdentifier */\n'
            '$indentation    $conv_type    /* ConversionType */\n'
            '$indentation    "$disp_format"   /* Format */\n'
            '$indentation    "$unit" /* Unit */\n'
            '$indentation    $conversion\n'
            '$indentation/end COMPU_METHOD'
        )

        # COMPU_METHOD template that looks similar to COMPU_METHOD generated by Embedded Coder
        self._ec_compu_method_template = Template(
            '$indentation/begin COMPU_METHOD\n'
            '$indentation  /* Name of CompuMethod    */      $name\n'
            '$indentation  /* Long identifier        */      "$ID"\n'
            '$indentation  /* Conversion Type        */      $conv_type\n'
            '$indentation  /* Format                 */      "$disp_format"\n'
            '$indentation  /* Units                  */      "$unit"\n'
            '$indentation  /* Coefficients           */      $conversion\n'
            '$indentation/end COMPU_METHOD'
        )

        for filename in a2l_files_unit:
            removed_symbols = self._parse_unit(filename)
            self._removed_symbols.extend(removed_symbols)
            self.debug('Loaded %s', filename)
        for filename in a2l_files_gen:
            self._parse_gen(filename)
            self.debug('Loaded %s', filename)

    def _parse_unit(self, filename):
        """Parse the unit a2l-files and apply a filter to only active parameters."""
        self.debug('Processing %s', filename)
        with open(filename, 'r', encoding="ISO-8859-1") as a2lfp:
            a2ld = a2lfp.read()
            file_path_parts = os.path.split(filename)
            unit = file_path_parts[1].split('.')[0]
            base_path = file_path_parts[0]
            dcl_match = re.search(r'VcDcl[\w]+Mdl(__[\w]+)', base_path)
            if dcl_match is not None and 'Mdl' not in unit:
                # Hand coded model names including "__" will lead to this, due to name mismatch of .a2l and .json files.
                # E.g. VcDclPtrlMdl__denso:
                #     1. config_VcDclPtrlMdl__denso.json vs VcDclPtrlMdl__denso.a2l.
                #         1.1. Match: unit in self._per_unit_cfg.
                #     2. config_VcDclPtrl__denso.json vs VcDclPtrl.a2l.
                #         2.1. No match: unit not in self._per_unit_cfg.
                old_unit = unit
                unit = unit + dcl_match.group(1)
                self.info(
                    'Found unit %s with .a2l and .json file name mismatch. Using new unit name: %s',
                    old_unit,
                    unit
                )

            if unit in self._per_unit_cfg:
                u_conf = self._per_unit_cfg[unit]
                code_generator = u_conf['code_generator'] if 'code_generator' in u_conf else 'target_link'
            else:
                u_conf = {}
                code_generator = 'target_link'

            if code_generator == 'embedded_coder':
                blks = re.findall(r'(?:\s*\n)*(\s*/begin '
                                  r'(?!PROJECT|HEADER|MODULE|MOD_PAR|MOD_COMMON)(\w+)\s*(?:\n\s*)?'
                                  r'(?:/\*\s*[\w ]+\s*\*/\s*)?(\w+)([\[\d+\]]*).*?\n.*?/end\s+\2)',
                                  a2ld, flags=re.M | re.DOTALL)
            else:
                blks = re.findall(r'(?:\s*\n)*(\s*/begin (?!PROJECT|MODULE)(\w+)[\n\s]*'
                                  r'(\w+(?:\.\w+)?)([\[\d+\]]*).*?\n.*?/end\s+\2)', a2ld,
                                  flags=re.M | re.DOTALL)

            compu_method_translators = self._parse_compu_methods(a2ld, unit)
            unit_blks = {}
            removed_symbols = []
            if unit not in self._per_unit_cfg:
                # Handcoded a2l without json-files will lead to this.
                # Add json files for the handcoded a2l!
                # NOTE: Assuming TargetLink
                self.debug('%s is not in the units list. Looking for json.', unit)
                config_filename = os.path.join(
                    self._prj_cfg.get_unit_cfg_deliv_dir(),
                    f'config_{unit}.json')
                self.debug('Looking for %s', config_filename)
                if os.path.isfile(config_filename):
                    with open(config_filename, 'r', encoding="utf-8") as config_file:
                        u_conf = json.load(config_file)
                    self._handle_config(
                        code_generator, unit, u_conf, blks, unit_blks, removed_symbols, compu_method_translators
                    )
                else:
                    self.warning('%s does not have a unit_cfg json, '
                                 'including all a2l-parameters', unit)
                    for blk_def, type_, label, size in blks:
                        if type_ == 'COMPU_METHOD':
                            blk_def, label = self._replace_compu_method(blk_def, label, compu_method_translators)
                        self.add_block_definition(unit_blks, type_, label, size, blk_def, compu_method_translators)
            else:
                self._handle_config(
                    code_generator, unit, u_conf, blks, unit_blks, removed_symbols, compu_method_translators
                )
        deep_dict_update(self._blks, unit_blks)
        return removed_symbols

    def _handle_config(self, code_generator, unit, u_conf, blks, unit_blks, removed_symbols, compu_method_translators):
        """Merge all types of ram for the unit."""
        ram = u_conf['inports']
        ram.update(u_conf['outports'])
        ram.update(u_conf['local_vars'])
        # TODO: Function the variables and labels needs to be removed from
        # the FUNCTION block too
        for blk_def, type_, label, size in blks:
            remove_excluded_symbol = True
            inc = False
            if type_ == 'AXIS_PTS':
                if label in u_conf['calib_consts']:
                    inc = True
            elif type_ == 'CHARACTERISTIC':
                if label in u_conf['calib_consts']:
                    if label in [axis_label for _, axis_type, axis_label, _ in blks if axis_type == 'AXIS_PTS']:
                        # AXIS_PTS can be used as CHARACTERISTC but not the other way around.
                        # If there are duplicates, use the AXIS_PTS.
                        self.debug('Will not add the block for CHARACTERISTC %s, but will keep it as a symbol,'
                                   ' since it exists as AXIS_PTS', label)
                        remove_excluded_symbol = False
                        inc = False
                    else:
                        inc = self._handle_axis_ptr_ref_config(u_conf, blk_def, unit)
            elif type_ == 'MEASUREMENT':
                if label in ram:
                    key = label if size is None else label + size
                    if label in u_conf['outports']:
                        # This unit is producing the measurement.
                        inc = True
                    elif key in unit_blks.get(type_, {}):
                        # This unit is not producing it, and it has already been added
                        inc = False
                    else:
                        # This unit is not producing it, but it has not been added
                        # Could be external signal, etc.
                        inc = True
            elif type_ == 'COMPU_METHOD':
                inc = True
                blk_def, label = self._replace_compu_method(blk_def, label, compu_method_translators)
            else:
                inc = True
            if inc:
                self.add_block_definition(unit_blks, type_, label, size, blk_def, compu_method_translators)
            else:
                if remove_excluded_symbol:
                    removed_symbols.append(label + size)
                self.debug('Did not include A2L-blk %s%s', label, size)
                if not self._unit_cfg.check_if_in_unit_cfg(unit, label):
                    if type_ != 'COMPU_METHOD':
                        self.warning('A2l block %s not in config json file for %s', label, unit)

        if 'FUNCTION' in unit_blks:
            unit_blks['FUNCTION'] = self._remove_symbols_from_func_blks(
                code_generator, unit_blks['FUNCTION'], removed_symbols
            )

        if 'GROUP' in unit_blks:
            unit_blks['GROUP'] = self._remove_symbols_from_grp_blks(unit_blks['GROUP'], removed_symbols)

    def _handle_axis_ptr_ref_config(self, u_conf, blk, unit):
        """Remove blocks referencing undefined blocks."""
        ref_re = re.compile(r'\s*AXIS_PTS_REF\s*([\w]*)')
        for axis_ptr_ref in ref_re.findall(blk):
            if axis_ptr_ref not in u_conf['calib_consts']:
                self.debug('Excluding due to %s missing in config', axis_ptr_ref)
                return False
            if not self._unit_cfg.check_if_in_unit_cfg(unit, axis_ptr_ref):
                self.debug('Excluding due to %s not active in config', axis_ptr_ref)
                return False
        return True

    def add_block_definition(self, unit_blks, type_, label, size, blk_def, compu_method_translators):
        """Add block definition to A2L-file."""
        size = '' if size is None else size
        blk_def = self._replace_conversions(blk_def, compu_method_translators)
        if type_ not in unit_blks:
            unit_blks[type_] = {}
        unit_blks[type_][label + size] = blk_def

    @staticmethod
    def _parse_func_blk(code_generator, fnc_blk):
        """Remove the unused symbols from the FUNCTION blocks in the A2L-file.
        Parse the FUNCTION block, TL or EC style based on code_generator.
        """

        if code_generator == 'target_link':
            pattern = r'\s*/begin\s+FUNCTION\s*?\n\s*(\w+).*?\n\s*"(.*?)".*?\n(.*)'
        else:
            pattern = r'\s*/begin\s+FUNCTION\s*?\n\s*.*\*/\s*(\w+).*?\n\s*.*\*/\s*"(.*?)".*?\n(.*)'
        res = re.match(pattern, fnc_blk, flags=re.M | re.DOTALL)
        fnc_name = res.group(1)
        long_id = res.group(2)
        fnc_dict = {
            'fnc_name': fnc_name,
            'long_id': long_id,
            'body': {}
        }
        fnc_body = res.group(3)
        sb_res = re.findall(r'\s*/begin\s+(\w+[\[\d\]]*)\s*\n\s*'
                            r'(.*?\n)\s*/end \1', fnc_body, flags=re.M | re.DOTALL)
        for sb_name, sub_blk in sb_res:
            symbols = set(re.findall(r'\s*(\w+(?:\.\w+)?[\[\d\]]*).*?\n', sub_blk, flags=re.M))
            fnc_dict['body'][sb_name] = symbols
        return fnc_dict

    @staticmethod
    def _parse_grp_blk(grp_blk):
        """Remove the unused symbols from the GROUP blocks in the A2L-file."""
        # parse the GROUP block
        res = re.match(r'\s*/begin\s+GROUP\s*?\n\s*.*\*/\s*(\w+).*?\n\s*.*\*/\s*"(.*?)".*?\n(.*)',
                       grp_blk, flags=re.M | re.DOTALL)
        fnc_name = res.group(1)
        long_id = res.group(2)
        fnc_dict = {
            'fnc_name': fnc_name,
            'long_id': long_id,
            'body': {}
        }
        fnc_body = res.group(3)
        sb_res = re.findall(r'\s*/begin\s+(\w+[\[\d\]]*)\s*\n\s*'
                            r'(.*?\n)\s*/end \1', fnc_body, flags=re.M | re.DOTALL)
        for sb_name, sub_blk in sb_res:
            symbols = set(re.findall(r'\s*(\w+(?:\.\w+)?[\[\d\]]*).*?\n', sub_blk, flags=re.M))
            fnc_dict['body'][sb_name] = symbols
        return fnc_dict

    def _recursive_remove(self, a2l_dict, name):
        """Remove symbols from A2L dict (e.g. group or function)."""
        if name in a2l_dict:
            blk = a2l_dict[name]
            if 'SUB_FUNCTION' in blk:
                for sub_fnc in blk['SUB_FUNCTION']:
                    if self._recursive_remove(a2l_dict, sub_fnc):
                        blk['SUB_FUNCTION'] = blk['SUB_FUNCTION'] - set([sub_fnc])
            elif 'SUB_GROUP' in blk:
                for sub_grp in blk['SUB_GROUP']:
                    if self._recursive_remove(a2l_dict, sub_grp):
                        blk['SUB_GROUP'] = blk['SUB_GROUP'] - set([sub_grp])
            empty = True
            for key in blk:
                if blk[key]:
                    empty = False
                    break
            if empty:
                a2l_dict.pop(name)
                return True
        return False

    def _remove_symbols_from_func_blks(self, code_generator, fnc_blks, removed_symbols):
        """Remove the unused symbols from function blocks.

        If the function block is empty, it too will be removed.
        first iteration - remove all symbols that have been removed
        second iteration - recusively remover all functions without symbols
        """
        fnc_dict = {}
        for fnc_name, fnc_blk in fnc_blks.items():
            fnc_dict[fnc_name] = {}
            u_fnc_bdy = self._parse_func_blk(code_generator, fnc_blk)['body']
            sub_blk_types = set(u_fnc_bdy.keys()) - set(['SUB_FUNCTION'])
            for type_ in list(sub_blk_types):
                fnc_dict[fnc_name][type_] = u_fnc_bdy[type_] - set(removed_symbols)
            if 'SUB_FUNCTION' in u_fnc_bdy:
                fnc_dict[fnc_name]['SUB_FUNCTION'] = u_fnc_bdy['SUB_FUNCTION']
        # second iteration - remove empty FUNCTION blocks
        # TODO: Add functionality which parses the the function tree structures
        # And the run recursive remove on all tree roots.
        for fnc_name in fnc_blks.keys():
            self._recursive_remove(fnc_dict, fnc_name)
        # generate new function blocks
        new_fnc_blks = {}
        for fnc_name, fnc_data in fnc_dict.items():
            fnc_blk = f'    /begin FUNCTION\n        {fnc_name}\t/* Name */\n'
            fnc_blk += "        \"\"\t/* LongIdentifier */\n"
            for sub_sec in sorted(fnc_data.keys()):
                sub_sec_data = fnc_data[sub_sec]
                if sub_sec_data:
                    fnc_blk += f"        /begin {sub_sec}\n"
                    for param in sorted(sub_sec_data):
                        fnc_blk += f"            {param}\t/* Identifier */\n"
                    fnc_blk += f"        /end {sub_sec}\n"
            fnc_blk += "    /end FUNCTION"
            new_fnc_blks[fnc_name] = fnc_blk
        return new_fnc_blks

    def _remove_symbols_from_grp_blks(self, grp_blks, removed_symbols):
        """Remove the unused symbols from group blocks.

        If the group block is empty, it too will be removed.
        first iteration - remove all symbols that have been removed
        second iteration - recusively remover all groups without symbols
        """
        grp_dict = {}
        for grp_name, grp_blk in grp_blks.items():
            grp_dict[grp_name] = {}
            u_grp_bdy = self._parse_grp_blk(grp_blk)['body']
            sub_blk_types = set(u_grp_bdy.keys()) - set(['SUB_GROUP'])
            for type_ in list(sub_blk_types):
                grp_dict[grp_name][type_] = u_grp_bdy[type_] - set(removed_symbols)
            if 'SUB_GROUP' in u_grp_bdy:
                grp_dict[grp_name]['SUB_GROUP'] = u_grp_bdy['SUB_GROUP']
        # second iteration - remove empty GROUP blocks
        # TODO: Add functionality which parses the the group tree structures
        # And the run recursive remove on all tree roots.
        for grp_name in grp_blks.keys():
            self._recursive_remove(grp_dict, grp_name)
        # generate new group blocks
        new_grp_blks = {}
        for grp_name, grp_data in grp_dict.items():
            grp_blk = f"    /begin GROUP \n      /* Name                   */       {grp_name}\n"
            grp_blk += "      /* Long identifier        */       \"\"\n"
            for sub_sec in sorted(grp_data.keys()):
                sub_sec_data = grp_data[sub_sec]
                if sub_sec_data:
                    grp_blk += f"      /begin {sub_sec}\n"
                    for param in sorted(sub_sec_data):
                        grp_blk += f"        {param}\n"
                    grp_blk += f"      /end {sub_sec}\n"
            grp_blk += "    /end GROUP"
            new_grp_blks[grp_name] = grp_blk

        return new_grp_blks

    def _parse_gen(self, filename):
        """Parse the generated a2l-files, without filter."""
        self.debug('parsing gen a2l: %s', filename)
        with open(filename, 'r', encoding="utf-8") as a2lfp:
            a2ld = a2lfp.read()
            for blk_def, type_, label in self._block_finder.findall(a2ld):
                self._blks.setdefault(type_, {}).setdefault(label, blk_def)

    @staticmethod
    def _replace_compu_method(blk_def, label, compu_method_translators):
        """Replace the compu method block and label."""
        for translator in compu_method_translators:
            if translator['old_compu_method'] == blk_def:
                return translator['new_compu_method'], translator['new_name']
        return blk_def, label

    def _store_compu_method(self, ID, conv_type, disp_format, unit, conversion, indentation, u_conf):
        """Stash compu methods that exists in the resulting a2l."""
        key = (ID, conv_type, disp_format, unit, conversion)
        if key in self._compu_methods:
            new_name = self._compu_methods[key]['name']
            new_compu_method = self._compu_methods[key]['method']
        else:
            new_name = 'Scaling_' + str(len(self._compu_methods))
            if 'code_generator' in u_conf and u_conf['code_generator'] == 'embedded_coder':
                new_compu_method = self._ec_compu_method_template.substitute(
                    name=new_name,
                    ID=ID,
                    conv_type=conv_type,
                    disp_format=disp_format,
                    unit=unit,
                    conversion=conversion,
                    indentation=indentation
                )
            else:
                new_compu_method = self._tl_compu_method_template.substitute(
                    name=new_name,
                    ID=ID,
                    conv_type=conv_type,
                    disp_format=disp_format,
                    unit=unit,
                    conversion=conversion,
                    indentation=indentation
                )
            self._compu_methods.update({key: {'name': new_name,
                                              'method': new_compu_method}})
        return new_name, new_compu_method

    @staticmethod
    def _replace_conversions(blk_def, compu_method_translators):
        """Replace conversion identifiers in a2l block."""
        for translator in compu_method_translators:
            # The following check is faster than running the regex on the block.
            # It DOES give false positives, which is why the regex is used for substitution
            # and we do not immidiately return after one positive
            if translator['old_name'] in blk_def:
                blk_def = translator['regex'].sub(translator['replacement'], blk_def)
        return blk_def

    def _parse_compu_methods(self, blk_def, unit):
        """Replace compu methods to not overwrite any of them."""
        compu_method_translators = []  # Translators for one processed a2l file. Needs to be reset between files
        u_conf = self._per_unit_cfg[unit] if unit in self._per_unit_cfg else {}
        if 'code_generator' in u_conf and u_conf['code_generator'] == 'embedded_coder':
            for match in self._ec_compu_method_parser.finditer(blk_def):
                new_name, new_compu_method = self._store_compu_method(
                    match['ID'],
                    match['conv_type'],
                    match['disp_format'],
                    match['unit'],
                    match['conversion'],
                    match['indentation'],
                    u_conf
                )
                compu_method_translators.append(
                    {
                        'new_name': new_name,
                        'old_name': match['name'],
                        'regex': re.compile(
                            r'(\s*)'                                     # beginning
                            r'\s*(/\* Conversion [Mm]ethod\s*\*/\s*)'    # optional comment
                            r'\b{name}\b'                                # word
                            r'('
                            r'\s*\n'                                     # newline
                            r')'.format(name=match['name'])              # end of end-match
                        ),
                        'replacement': r'\1\2{name}\3'.format(name=new_name),
                        'old_compu_method': match['compu_method'],
                        'new_compu_method': new_compu_method
                    }
                )
        else:
            for match in self._tl_compu_method_parser.finditer(blk_def):
                new_name, new_compu_method = self._store_compu_method(
                    match['ID'],
                    match['conv_type'],
                    match['disp_format'],
                    match['unit'],
                    match['conversion'],
                    match['indentation'],
                    u_conf
                )
                compu_method_translators.append(
                    {
                        'new_name': new_name,
                        'old_name': match['name'],
                        'regex': re.compile(
                            r'(\s*)'                         # beginning
                            r'\b{name}\b'                    # word
                            r'('                             # start of end-match
                            r'\s*(/\* Conversion \*/)?'      # optional comment
                            r'\s*\n'                         # newline
                            r')'.format(name=match['name'])  # end of end-match
                        ),
                        'replacement': r'\1{name}\2'.format(name=new_name),
                        'old_compu_method': match['compu_method'],
                        'new_compu_method': new_compu_method
                    }
                )
        return compu_method_translators

    def _patch_kp_blob(self, block):
        """Return updated measurement block text.
        Args:
            block (str): A2L text block
        Returns:
            a2l_text (str): A2L text without KP_BLOB.
        """
        ecu_address = '0x00000000'
        for match in self._expr_block_meas_kp_blob_parser.finditer(block):
            start, end = match.span()
            block = f'{block[:start]}ECU_ADDRESS {ecu_address}{block[end:]}'
        return block

    def merge(self, f_name, complete_a2l=False, silver_a2l=False):
        """Write merged a2l-file.

        Args:
            f_name (str): Output filename.
        """
        a2l = ''
        a2l_config = self._prj_cfg.get_a2l_cfg()
        for _, data in self._blks.items():
            for _, blk in data.items():
                if not a2l_config['allow_kp_blob']:
                    blk = self._patch_kp_blob(blk)
                a2l += blk + '\n\n'

        if complete_a2l:
            events = []
            time_unit_10ms = '0x07'
            rasters = self._prj_cfg.get_units_raster_cfg()
            for xcp_id, evt_data in enumerate(rasters['SampleTimes'].items(), 1):
                events.append({
                    'time_cycle': '0x%02X' % int(evt_data[1] * 100),
                    'time_unit': time_unit_10ms,
                    'name': evt_data[0],
                    'channel_id': '0x%04X' % xcp_id
                })
            a2l_template = A2lProjectTemplate(
                a2l,
                a2l_config['asap2_version'],
                a2l_config['name'],
                events,
                a2l_config['ip_address'],
                a2l_config['ip_port']
            )
            a2l = a2l_template.render()
        elif silver_a2l:
            a2l_template = A2lSilverTemplate(a2l)
            a2l = a2l_template.render()

        self.a2l = a2l

        with open(f_name, 'w', encoding="ISO-8859-1") as ma2l:
            ma2l.write(a2l)
            self.info('Written the merged A2L-file %s', f_name)

    def get_characteristic_axis_data(self):
        """Get characteristic map axis data from merged a2l-file."""
        axis_data = {}
        for blk_def, type_, label in self._block_finder.findall(self.a2l):
            if type_ == "CHARACTERISTIC":
                axes = re.findall('AXIS_PTS_REF (.*)', blk_def)
                if label in axis_data:
                    self.critical("Multiple CHARACTERISTIC for %s in merged a2l.", label)
                axis_data[label] = {'axes': axes}
        return axis_data
