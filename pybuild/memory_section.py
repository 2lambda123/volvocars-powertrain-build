# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

# -*- coding: utf-8 -*-
"""Module containing cvc classes for VCC - defines and includes for memory sections."""

import time
from pathlib import Path
from pybuild import build_defs
from pybuild.problem_logger import ProblemLogger


class MemorySection(ProblemLogger):
    """Handle headers for CVC_* definitions."""

    calibration_definitions = [
        'CVC_CAL',
        'CVC_CAL_ASIL_A',
        'CVC_CAL_ASIL_B',
        'CVC_CAL_ASIL_C',
        'CVC_CAL_ASIL_D',
        'CVC_CAL_MERGEABLE_ASIL_A',
        'CVC_CAL_MERGEABLE_ASIL_B',
        'CVC_CAL_MERGEABLE_ASIL_C',
        'CVC_CAL_MERGEABLE_ASIL_D'
    ]
    measurable_definitions = [
        'CVC_DISP',
        'CVC_DISP_ASIL_A',
        'CVC_DISP_ASIL_B',
        'CVC_DISP_ASIL_C',
        'CVC_DISP_ASIL_D'
    ]
    project_defines = {
        'HI': {
            'START': {
                'const': '#define {software_component_name}_START_SEC_CONST_UNSPECIFIED\n',
                'disp': '#define {software_component_name}_START_SEC_VAR_INIT_UNSPECIFIED\n',
                'cal': '#pragma section ".XcpCalibrationSection"\n'
            },
            'STOP': {
                'const': '#define {software_component_name}_STOP_SEC_CONST_UNSPECIFIED\n',
                'disp': '#define {software_component_name}_STOP_SEC_VAR_INIT_UNSPECIFIED\n',
                'cal': '#pragma section\n'
            }
        },
        'ZC': {
            'START': {
                'const': '#define {software_component_name}_START_SEC_VCC_CONST\n',
                'disp': '#define {software_component_name}_START_SEC_VCC_DISP\n',
                'cal': '#define {software_component_name}_START_SEC_VCC_CAL\n'
            },
            'STOP': {
                'const': '#define {software_component_name}_STOP_SEC_VCC_CONST\n',
                'disp': '#define {software_component_name}_STOP_SEC_VCC_DISP\n',
                'cal': '#define {software_component_name}_STOP_SEC_VCC_CAL\n'
            },
        }
    }

    def __init__(self, build_cfg):
        super().__init__()
        self.build_cfg = build_cfg
        self.a2l_cfg_name = self.build_cfg.get_a2l_cfg()['name']
        self.ecu_supplier = self.build_cfg.get_ecu_info()[0]
        if self.ecu_supplier == 'HI':
            self.include_header_guards = True
            self.software_component_name = self.a2l_cfg_name
            self.mem_map_include = f'#include "{self.a2l_cfg_name}_MemMap.h"\n'
        else:
            self.include_header_guards = False
            self.software_component_name = self.build_cfg.get_swc_name()
            self.mem_map_include = f'#include "{self.software_component_name}_MemMap.h"\n'
        self.xcp_enabled = self.build_cfg.get_xcp_enabled()
        self.use_volatile_globals = self.build_cfg.get_use_volatile_globals()

    @staticmethod
    def _get_mem_map_section(section):
        return 'STOP' if section == 'END' else section

    @staticmethod
    def _get_header(section_file):
        section_file_header_guard = section_file.split('.')[0].upper()
        return [
            f'#ifndef {section_file_header_guard}_H\n',
            f'#define {section_file_header_guard}_H\n\n'
        ]

    @staticmethod
    def _get_footer(section_file):
        section_file_header_guard = section_file.split('.')[0].upper()
        return [f'\n#endif /* {section_file_header_guard}_H */\n']

    def _get_cal(self, section):
        cvc_undefines = [f'#undef {definition}\n' for definition in self.calibration_definitions]
        if section == 'START':
            volatile_string = 'volatile' if self.use_volatile_globals else ''
            cvc_defines = [f'#define {definition} {volatile_string}\n' for definition in self.calibration_definitions]
        else:
            cvc_defines = []
        section_type = 'cal' if self.xcp_enabled else 'disp'
        memory_section_handling = [
            self.project_defines[self.ecu_supplier][self._get_mem_map_section(section)][section_type].format(
                software_component_name=self.software_component_name
            )
        ]
        if self.ecu_supplier != 'HI' or not self.xcp_enabled:
            memory_section_handling.append(self.mem_map_include)
        return cvc_undefines, cvc_defines, memory_section_handling

    def _get_disp(self, section):
        cvc_undefines = [f'#undef {definition}\n' for definition in self.measurable_definitions]
        if section == 'START':
            volatile_string = 'volatile' if self.use_volatile_globals else ''
            cvc_defines = [f'#define {definition} {volatile_string}\n' for definition in self.measurable_definitions]
        else:
            cvc_defines = []
        memory_section_handling = [
            self.project_defines[self.ecu_supplier][self._get_mem_map_section(section)]['disp'].format(
                software_component_name=self.software_component_name
            ),
            self.mem_map_include
        ]
        return cvc_undefines, cvc_defines, memory_section_handling

    def _get_code(self, section):
        mem_map_section = self._get_mem_map_section(section)
        cvc_undefines = []
        cvc_defines = []
        memory_section_handling = [
            f'#define {self.software_component_name}_{mem_map_section}_SEC_CODE\n',
            self.mem_map_include
        ]
        return cvc_undefines, cvc_defines, memory_section_handling

    def _get_const(self, section):
        cvc_undefines = []
        cvc_defines = []
        memory_section_handling = [
            self.project_defines[self.ecu_supplier][self._get_mem_map_section(section)]['const'].format(
                software_component_name=self.software_component_name
            ),
            self.mem_map_include
        ]
        return cvc_undefines, cvc_defines, memory_section_handling

    def _get_rest(self):
        cvc_undefines = []
        cvc_defines = []
        memory_section_handling = [
            self.mem_map_include
        ]
        return cvc_undefines, cvc_defines, memory_section_handling

    def _get_predecl(self):
        cvc_undefines = []
        cvc_defines = []
        memory_section_handling = [
            self.mem_map_include
        ]
        return cvc_undefines, cvc_defines, memory_section_handling

    def generate_cvc_header(self, section, section_file):
        """Generate CVC headers.

        Args:
            section (str): Name of the CVC section
            section_file (str): Name of the header file
        Returns:
            lines_to_write (list(str)): Lines to write to given section file.
        """
        header = self._get_header(section_file) if self.include_header_guards else []
        footer = self._get_footer(section_file) if self.include_header_guards else []
        if '_CAL_' in section_file:
            cvc_undefines, cvc_defines, memory_section_handling = self._get_cal(section)
        elif '_DISP_' in section_file:
            cvc_undefines, cvc_defines, memory_section_handling = self._get_disp(section)
        elif not section_file.startswith('PREDECL_'):
            if section_file.startswith('CVC_CAL') or section_file.startswith('CVC_DISP'):
                self.critical('Should not find CVC_CAL/DISP here. Check logic. File: %s.', section_file)
            elif section_file.startswith('CVC_CODE'):
                cvc_undefines, cvc_defines, memory_section_handling = self._get_code(section)
            elif section_file.startswith('CVC_CONST'):
                cvc_undefines, cvc_defines, memory_section_handling = self._get_const(section)
            else:
                cvc_undefines, cvc_defines, memory_section_handling = self._get_rest()
        else:
            cvc_undefines, cvc_defines, memory_section_handling = self._get_predecl()

        return header + cvc_undefines + cvc_defines + memory_section_handling + footer

    def generate_required_header_files(self):
        """Generate required header files to delivery folder.

        Generate required header files such as memory protection files.
        NOTE: Currently, only one ASIL level can be selected for an SWC.
        """
        self.info('******************************************************')
        self.info('Start generating required header files')
        start_time = time.time()
        src_dst_dir = self.build_cfg.get_src_code_dst_dir()
        for section_dict in build_defs.PREDECL_EXTRA.values():
            for section_file in section_dict.values():
                header = self._get_header(section_file) if self.include_header_guards else []
                footer = self._get_footer(section_file) if self.include_header_guards else []
                with Path(src_dst_dir, section_file).open('w', encoding="utf-8") as header_file_handler:
                    header_file_handler.writelines(header + footer)

        for asil_dict in build_defs.ASIL_LEVEL_MAP.values():
            for type_dict in asil_dict.values():
                for section_dict in type_dict.values():
                    for section, section_file in section_dict.items():
                        lines_to_write = self.generate_cvc_header(section, section_file)
                        with Path(src_dst_dir, section_file).open('w', encoding="utf-8") as header_file_handler:
                            header_file_handler.writelines(lines_to_write)

        for nvm_dict in build_defs.NVM_LEVEL_MAP.values():
            for section_dict in nvm_dict.values():
                for section_file in section_dict.values():
                    header = self._get_header(section_file) if self.include_header_guards else []
                    footer = self._get_footer(section_file) if self.include_header_guards else []
                    with Path(src_dst_dir, section_file).open('w', encoding="utf-8") as header_file_handler:
                        header_file_handler.writelines(header + footer)
        self.info('Finished generating required header files (in %4.2f s)', time.time() - start_time)
