# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

# -*- coding: utf-8 -*-
"""
module for testing the reading of core id legacy config files
"""
import json
import logging
import os
import unittest
from unittest.mock import MagicMock, mock_open, patch, call
from pathlib import Path

from powertrain_build.lib import helper_functions
from powertrain_build.nvm_def import NVMDef
from powertrain_build.unit_configs import UnitConfigs

SRC_DIR = Path(__file__).parent


class TestNVMDef(unittest.TestCase):
    """
    Test case for testing the TestNVMDef class
    """

    @classmethod
    def setUpClass(cls):
        """Set-up common data structures for all tests in the test case
        """
        cls.create_new = False
        cls.unit_cfg = MagicMock(spec_set=UnitConfigs)
        type(cls.unit_cfg).base_types_headers = '#include "tl_basetypes.h"\n'
        cls.nvm_vars_test = {
            'sVcAcCtrl_t_CmprRunTiNVM': {
                'VcAcCtrl': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcAcCtrl/VcAcCtrl/Subsystem/VcAcCtrl/CoolingManager/'
                              '3_SystemInfo/36_CompressorRunTime/sVcAcCtrl_t_CmprRunTiNVM/Unit Delay',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcAcCtrl_t_CmprRunTiNVM',
                    'offset': 0,
                    'type': 'UInt32',
                    'unit': '-',
                    'width': 1}},
            'sVcAesHw_X_VntAdpnOffs': {
                'VcAesVnt': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['Vc_Aes_Vnt_B_CodeGenVntGvnr '
                                '== 0'],
                    'description': 'Enter a nice '
                                   'description of your '
                                   'variable here',
                    'handle': 'VcAesVnt/VcAesVnt/Subsystem/VcAesVnt/VcAesVnt/1_Vnt/11_VntGvnr/'
                              '111_VntGvnrExe/1111_VntGvnrFct/11112_VntAdpn/sVcAesHw_X_VntAdpnOffs/Unit Delay',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcAesHw_X_VntAdpnOffs',
                    'offset': 0,
                    'type': 'Float32',
                    'unit': '-',
                    'width': 1
                }
            },
            'sVcAesMo_Ar_ArrayTest': {
                'VcAesMoAdp': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice '
                                   'description of your '
                                   'variable here',
                    'handle': 'VcAesMoAdp/VcAesMoAdp/Subsystem/VcAesMoAdp/VcAesMoAdp/'
                              '2_ThrArAdpn/sVcAesMo_Ar_NvmThrAdpn/Unit Delay',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcAesMo_Ar_NvmThrAdpn',
                    'offset': 0,
                    'type': 'Float32',
                    'unit': '-',
                    'width': [4, 2]
                }
            },
            'sVcAesMo_Ar_NvmThrAdpn': {
                'VcAesMoAdp': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice '
                                   'description of your '
                                   'variable here',
                    'handle': 'VcAesMoAdp/VcAesMoAdp/Subsystem/VcAesMoAdp/VcAesMoAdp/'
                              '2_ThrArAdpn/sVcAesMo_Ar_NvmThrAdpn/Unit Delay',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcAesMo_Ar_NvmThrAdpn',
                    'offset': 0,
                    'type': 'Float32',
                    'unit': '-',
                    'width': 1
                }
            },
            'sVcAesMo_rt_NvmMafLrngLd1Ne1': {
                'VcAesMfl': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice '
                                   'description of '
                                   'your variable '
                                   'here',
                    'handle': 'VcAesMfl/VcAesMfl/Subsystem/VcAesMfl/VcAesMfl/4_Nvm/41_Ld1Ne1/'
                              'sVcAesMo_rt_NvmMafLrngLd1Ne1/Unit Delay',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcAesMo_rt_NvmMafLrngLd1Ne1',
                    'offset': 0,
                    'type': 'Bool',
                    'unit': '-',
                    'width': 1
                }
            },
            'sVcAcCtrl_t_Test1': {
                'VcAcCtrl': {
                    'class': 'CVC_DISP_NVM_P',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcAcCtrl/VcAcCtrl/Subsystem/VcAcCtrl/CoolingManager/3_SystemInfo/'
                              '36_CompressorRunTime/sVcAcCtrl_t_CmprRunTiNVM/Unit Delay',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcAcCtrl_t_Test1',
                    'offset': 0,
                    'type': 'UInt32',
                    'unit': '-',
                    'width': 1
                },
                'VcAcCtrl2': {
                    'class': 'CVC_DISP_NVM_P',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcAcCtrl/VcAcCtrl/Subsystem/VcAcCtrl/CoolingManager/3_SystemInfo/'
                              '36_CompressorRunTime/sVcAcCtrl_t_CmprRunTiNVM/Unit Delay',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcAcCtrl_t_Test1',
                    'offset': 0,
                    'type': 'UInt32',
                    'unit': '-',
                    'width': 1
                }
            }
        }

        cls.nvm_configs_single = {
            "fileName": "vcc_nvm_struct_single",
            "baseNvmStructs": "nvm_structs_ref_single_signal.json"
        }
        cls.nvm_configs = {
            "fileName": "vcc_nvm_struct",
            "baseNvmStructs": "nvm_structs_ref_empty.json"
        }
        cls.nvm_configs_small = {
            "fileName": "vcc_nvm_structs__small",
            "baseNvmStructs": "nvm_structs_ref_small.json"
        }
        cls.nvm_configs_empty_small = {
            "fileName": "vcc_nvm_structs_empty_small",
            "baseNvmStructs": "nvm_structs_ref_empty_small.json"
        }
        cls.nvm_configs_signal_overwritten = {
            "fileName": "vcc_nvm_structs_ref_used_positions",
            "baseNvmStructs": "nvm_structs_ref_used_positions.json"
        }
        cls.nvm_configs_critical = {
            "fileName": "vcc_nvm_structs_critical",
            "baseNvmStructs": "nvm_structs_ref_critical.json"
        }
        cls.nvm_configs_critical_remove = {
            "fileName": "vcc_nvm_struct_critical_remove",
            "baseNvmStructs": "nvm_structs_ref_critical.json"
        }
        cls.nvm_configs_critical_duplicate = {
            "fileName": "vcc_nvm_struct_critical_duplicate",
            "baseNvmStructs": "nvm_structs_ref_critical_duplicate.json"
        }
        cls.nvm_configs_wrong_type = {
            "fileName": "vcc_nvm_structs_ref_used_positions",
            "baseNvmStructs": "nvm_structs_ref_wrong_type.json"
        }
        cls.nvm_configs_dcl = {
            "fileName": "vcc_nvm_structs_ref_dcl",
            "baseNvmStructs": "nvm_structs_ref_dcl.json"
        }

    def setUp(self):
        """Set-up common data structures for all tests in the test case
        """
        helper_functions.create_dir(Path(SRC_DIR, 'output'))
        helper_functions.create_dir(Path(SRC_DIR, 'cnfg_files', 'output'))
        self.proj_cnfg = MagicMock()
        projdir = Path(SRC_DIR, 'cnfg_files').resolve()
        self.proj_cnfg.get_root_dir = MagicMock(return_value=projdir)
        self.proj_cnfg.get_src_code_dst_dir = MagicMock(return_value=str(Path(SRC_DIR, 'output')))
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs)
        self.proj_cnfg.get_ecu_info = MagicMock(return_value=('Denso', 'G2'))
        self.proj_cnfg.get_swc_name = MagicMock(return_value='DummySwc')
        self.nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, self.nvm_vars_test)

        self.small_nvm_struct = {
            "sVcDummy_t_DummyNvm": {
                "class": "CVC_DISP_NVM",
                "configs": [
                    "all"
                ],
                "description": "Enter a nice description of your variable here",
                "handle": "VcDummy/VcDummy/Subsystem/VcDummy/Dummy/1_Nvm/Dummy",
                "lsb": 1,
                "max": "nan",
                "min": "nan",
                "name": "sVcDummy_t_DummyNvm",
                "offset": 0,
                "type": "UInt32",
                "unit": "-",
                "width": 1,
                "area": "NVM_LIST_32",
                "struct_off": 0
            }
        }

    def test_create_new(self):
        """Test to verify that we do not overwrite the reference files."""
        self.assertFalse(self.create_new)

    def test_get_signals_in_nvm_structs(self):
        """Test getting nvm definition dictionary"""
        project_config = MagicMock()
        projdir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'cnfg_files'))
        project_config.get_root_dir = MagicMock(return_value=projdir)
        project_config.get_nvm_defs = MagicMock(return_value=self.nvm_configs_small)
        nvm_def = NVMDef(project_config, self.unit_cfg, self.nvm_vars_test)
        nvm_structs_signals = nvm_def._get_signals_in_nvm_structs()
        expected_signals_path = os.path.join(os.path.dirname(__file__),
                                             'cnfg_files',
                                             'expected_signals_in_nvm_structs.json')
        if self.create_new:
            with open(expected_signals_path, 'w') as expected_signals_file:
                json.dump(nvm_structs_signals, expected_signals_file)
        with open(expected_signals_path, 'r') as expected_signals_file:
            expected_signals = json.load(expected_signals_file)
        self.assertDictEqual(nvm_structs_signals, expected_signals)

    def test_gen_h_file(self):
        """test for generating the h-file for NVM definitions
        """
        no_nvm_a2l = False
        self.nvm_def.generate_nvm_config_files(no_nvm_a2l)
        h_file_name = Path(SRC_DIR, 'output', self.nvm_configs['fileName'] + '.h')
        with h_file_name.open() as hfptr:
            h_file = hfptr.read()
        with Path(SRC_DIR, 'reference_files', 'vcc_nvm_struct_ref.h').open() as hfptr_ref:
            h_ref_file = hfptr_ref.read()
        self.maxDiff = None
        self.assertEqual(h_ref_file, h_file)

    def test_gen_c_file(self):
        """test for generating the c-file for NVM definitions
        """
        no_nvm_a2l = False
        self.nvm_def.generate_nvm_config_files(no_nvm_a2l)
        c_file_name = Path(SRC_DIR, 'output', self.nvm_configs['fileName'] + '.c')
        with c_file_name.open() as cfptr:
            c_file = cfptr.read()
        with Path(SRC_DIR, 'reference_files', 'vcc_nvm_struct_ref.c').open() as cfptr_ref:
            c_ref_file = cfptr_ref.read()
        self.assertEqual(c_ref_file, c_file)

    def test_gen_a2l_file(self):
        """test for generating the a2l-file for NVM definitions
        """
        no_nvm_a2l = False
        self.nvm_def.generate_nvm_config_files(no_nvm_a2l)
        a_file_name = Path(SRC_DIR, 'output', self.nvm_configs['fileName'] + '.a2l')
        with a_file_name.open() as fptr:
            a2l_file = fptr.read()
        ref_file = Path(SRC_DIR, 'reference_files', 'vcc_nvm_struct_ref.a2l')
        if self.create_new:
            with ref_file.open(mode='w') as fptr_ref:
                fptr_ref.write(a2l_file)
        with ref_file.open() as fptr_ref:
            a2l_ref_file = fptr_ref.read()
        self.maxDiff = None
        self.assertEqual(a2l_ref_file, a2l_file)

    @patch('builtins.open', new_callable=mock_open())
    def test_generate_nvm_config_a2l_patch(self, mock_open_file):
        """Test nvm_def.NVMDef._generate_nvm_config_a2l with use_prefix=True."""
        expected = (
            '\n'
            '    /begin MEASUREMENT\n'
            '        sVcDummy_t_DummyNvm /* Name */\n'
            '        "Enter a nice description of your variable here" /* LongIdentifier */\n'
            '        ULONG   /* Datatype */\n'
            '        VcNvm_1_0_0_None   /* Conversion */\n'
            '        1   /* Resolution */\n'
            '        0   /* Accuracy */\n'
            '        nan   /* LowerLimit */\n'
            '        nan   /* UpperLimit */\n''        READ_WRITE\n'
            '        SYMBOL_LINK "dummyswc_nvm_list_32" 0\n'
            '    /end MEASUREMENT\n'
            '\n'
            '    /begin COMPU_METHOD\n'
            '        VcNvm_1_0_0_None   /* Name */\n'
            '        ""    /* LongIdentifier */\n'
            '        RAT_FUNC    /* ConversionType */\n'
            '        "%11.3"   /* Format */\n'
            '        "-" /* Unit */\n'
            '        COEFFS 0 1 0.0 0 0 1\n'
            '    /end COMPU_METHOD\n'
            '\n'
            '    /begin FUNCTION\n'
            '        VcNvm /* Name */\n'
            '        ""  /* LongIdentifier */\n'
            '        /begin LOC_MEASUREMENT\n'
            '            sVcDummy_t_DummyNvm /* Identifier */\n'
            '        /end LOC_MEASUREMENT\n'
            '    /end FUNCTION\n'
            '\n'
            '    /begin RECORD_LAYOUT\n'
            '        ULONG_COL_DIRECT /* Name */\n'
            '        FNC_VALUES 1 ULONG COLUMN_DIR DIRECT\n'
            '    /end RECORD_LAYOUT\n'
        )
        self.nvm_def._nvm_signals = self.small_nvm_struct
        self.nvm_def._generate_nvm_config_a2l(True)
        mock_open_file().__enter__().write.assert_called_once_with(expected)

    @patch('builtins.open', new_callable=mock_open())
    def test_generate_nvm_config_headers_patch(self, mock_open_file):
        """Test nvm_def.NVMDef._generate_nvm_config_headers with use_prefix=True."""
        expected = [
            call(
                '/*\n *  vcc_nvm_struct.h - struct for NVM signals\n */\n\n'
                '#ifndef VCC_NVM_STRUCT_H\n'
                '#define VCC_NVM_STRUCT_H\n\n'
                '#include "tl_basetypes.h"\n'
            ),
            call('#include "CVC_NVM_START.h"\n'),
            call('struct DummySwc_NVM_LIST_8 {\n'),
            call('   UInt8 unused[56];\n'),
            call('}; /* 0 bytes used of 56 */\n'),
            call('#include "CVC_NVM_END.h"\n\n'),
            call('#include "CVC_NVM_START.h"\n'),
            call('struct DummySwc_NVM_LIST_16 {\n'),
            call('   UInt16 unused[240];\n'),
            call('}; /* 0 bytes used of 480 */\n'),
            call('#include "CVC_NVM_END.h"\n\n'),
            call('#include "CVC_NVM_START.h"\n'),
            call('struct DummySwc_NVM_LIST_32 {\n'),
            call('   UInt32 unused[975];\n'),
            call('}; /* 0 bytes used of 3900 */\n'),
            call('#include "CVC_NVM_END.h"\n\n'),
            call('#include "CVC_NVM_P_START.h"\n'),
            call('struct DummySwc_NVM_LIST_8_PER {\n'),
            call('   UInt8 unused[56];\n'),
            call('}; /* 0 bytes used of 56 */\n'),
            call('#include "CVC_NVM_P_END.h"\n\n'),
            call('#include "CVC_NVM_P_START.h"\n'),
            call('struct DummySwc_NVM_LIST_16_PER {\n'),
            call('   UInt16 unused[240];\n'),
            call('}; /* 0 bytes used of 480 */\n'),
            call('#include "CVC_NVM_P_END.h"\n\n'),
            call('#include "CVC_NVM_P_START.h"\n'),
            call('struct DummySwc_NVM_LIST_32_PER {\n'),
            call('   UInt32 unused[190];\n'),
            call('}; /* 0 bytes used of 760 */\n'),
            call('#include "CVC_NVM_P_END.h"\n\n'),
            call('#include "PREDECL_START.h"\n'),
            call('extern struct DummySwc_NVM_LIST_8 dummyswc_nvm_list_8;\n'),
            call('extern struct DummySwc_NVM_LIST_16 dummyswc_nvm_list_16;\n'),
            call('extern struct DummySwc_NVM_LIST_32 dummyswc_nvm_list_32;\n'),
            call('extern struct DummySwc_NVM_LIST_8_PER dummyswc_nvm_list_8_per;\n'),
            call('extern struct DummySwc_NVM_LIST_16_PER dummyswc_nvm_list_16_per;\n'),
            call('extern struct DummySwc_NVM_LIST_32_PER dummyswc_nvm_list_32_per;\n'),
            call('#include "PREDECL_END.h"\n\n'),
            call('\n'),
            call('\n#endif /* VCC_NVM_STRUCT_H */\n')
        ]
        self.nvm_def._nvm_signals = self.small_nvm_struct
        self.nvm_def._generate_nvm_config_headers(True)
        mock_open_file().__enter__().write.assert_has_calls(expected)

    @patch('builtins.open', new_callable=mock_open())
    def test_generate_nvm_config_source_patch(self, mock_open_file):
        """Test nvm_def.NVMDef._generate_nvm_config_source with use_prefix=True."""
        expected = [
            call('#include "vcc_nvm_struct.h"\n\n'),
            call('#include "CVC_NVM_START.h"\n'),
            call('struct DummySwc_NVM_LIST_8 dummyswc_nvm_list_8;\n'),
            call('#include "CVC_NVM_END.h"\n\n'),
            call('#include "CVC_NVM_START.h"\n'),
            call('struct DummySwc_NVM_LIST_16 dummyswc_nvm_list_16;\n'),
            call('#include "CVC_NVM_END.h"\n\n'),
            call('#include "CVC_NVM_START.h"\n'),
            call('struct DummySwc_NVM_LIST_32 dummyswc_nvm_list_32;\n'),
            call('#include "CVC_NVM_END.h"\n\n'),
            call('#include "CVC_NVM_P_START.h"\n'),
            call('struct DummySwc_NVM_LIST_8_PER dummyswc_nvm_list_8_per;\n'),
            call('#include "CVC_NVM_P_END.h"\n\n'),
            call('#include "CVC_NVM_P_START.h"\n'),
            call('struct DummySwc_NVM_LIST_16_PER dummyswc_nvm_list_16_per;\n'),
            call('#include "CVC_NVM_P_END.h"\n\n'),
            call('#include "CVC_NVM_P_START.h"\n'),
            call('struct DummySwc_NVM_LIST_32_PER dummyswc_nvm_list_32_per;\n'),
            call('#include "CVC_NVM_P_END.h"\n\n')
        ]
        self.nvm_def._nvm_signals = self.small_nvm_struct
        self.nvm_def._generate_nvm_config_source(True)
        mock_open_file().__enter__().write.assert_has_calls(expected)

    def test_gen_h_file_fail(self):
        """test for generating the h-file for NVM definitions
        """
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs_empty_small)
        NVMDef.init_logger(logging.getLogger())
        self.nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, self.nvm_vars_test)
        with self.assertLogs(level='WARNING') as log:
            no_nvm_a2l = False
            self.nvm_def.generate_nvm_config_files(no_nvm_a2l)
        self.assertEqual(['CRITICAL:root:NVM area NVM_LIST_32 overrun!'], log.output)

    def test_gen_h_file_signal_is_overwritten(self):
        """test that the NVM definitions is overwritten if signal is named position_*
        """
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs_signal_overwritten)
        self.nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, self.nvm_vars_test)
        nvm_list_32_pos = self.nvm_def._get_nvm_areas_index('NVM_LIST_32')
        dummy_signal = {'name': 'dummy', 'type': 'Int32', 'x_size': 1, 'y_size': 1}
        # find_empty_index should find next empty index to be 2 since that's
        # the position for the first signal named Position_*
        index_before_generation = self.nvm_def._find_empty_index(nvm_list_32_pos, dummy_signal)
        self.assertEqual(index_before_generation, 2)
        # Generate the files
        no_nvm_a2l = False
        self.nvm_def.generate_nvm_config_files(no_nvm_a2l)
        # find_empty_index should find next empty index to be -1 which means no more empty position
        index_after_generation = self.nvm_def._find_empty_index(nvm_list_32_pos, dummy_signal)
        self.assertNotEqual(index_after_generation, index_before_generation)
        self.assertEqual(index_after_generation, -1)

        h_file_name = Path(SRC_DIR, 'output', self.nvm_configs_signal_overwritten['fileName'] + '.h')
        with h_file_name.open() as hfptr:
            h_file = hfptr.read()
        with Path(SRC_DIR, 'reference_files', 'vcc_nvm_structs_ref_used_positions.h').open() as hfptr_ref:
            h_ref_file = hfptr_ref.read()
        self.maxDiff = None
        self.assertEqual(h_ref_file, h_file)

    def test_add_signal_with_nondefault_type_c(self):
        """Test that we can add different types of signals to critical area - c-file
        """
        self.proj_cnfg.get_ecu_info = MagicMock(return_value=('Bosch', ''))
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs_critical)
        nvm_vars_test = {
            'sVcTest_t_UInt32': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_UInt32',
                    'lsb': 2,
                    'name': 'sVcTest_t_UInt32',
                    'offset': 1,
                    'type': 'UInt32',
                    'unit': 's',
                    'width': 1
                    }
                },
            'sVcTest_t_Int16': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_Int16',
                    'lsb': 1,
                    'name': 'sVcTest_t_UInt16',
                    'offset': 0,
                    'type': 'Int16',
                    'unit': '-',
                    'width': 1
                    }
                },
            'sVcTest_t_UInt8': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_UInt8',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcTest_t_UInt8',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-',
                    'width': 1
                    }
                },
            }
        NVMDef.init_logger(logging.getLogger())
        nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, nvm_vars_test)
        no_nvm_a2l = False
        nvm_def.generate_nvm_config_files(no_nvm_a2l)
        self.maxDiff = None

        c_file_name = Path(SRC_DIR, 'output', 'vcc_nvm_structs_critical.c')
        with c_file_name.open() as cfptr:
            c_file = cfptr.read()
        with Path(SRC_DIR, 'reference_files', 'vcc_nvm_structs_critical.c').open() as cfptr_ref:
            c_ref_file = cfptr_ref.read()
        self.assertEqual(c_ref_file, c_file)

    def test_add_signal_with_nondefault_type_h(self):
        """Test that we can add different types of signals to critical area - h-file
        """
        self.proj_cnfg.get_ecu_info = MagicMock(return_value=('Bosch', ''))
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs_critical)
        nvm_vars_test = {
            'sVcTest_t_UInt32': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_UInt32',
                    'lsb': 2,
                    'name': 'sVcTest_t_UInt32',
                    'offset': 1,
                    'type': 'UInt32',
                    'unit': 's',
                    'width': 1
                    }
                },
            'sVcTest_t_Int16': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_Int16',
                    'lsb': 1,
                    'name': 'sVcTest_t_UInt16',
                    'offset': 0,
                    'type': 'Int16',
                    'unit': '-',
                    'width': 1
                    }
                },
            'sVcTest_t_UInt8': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_UInt8',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcTest_t_UInt8',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-',
                    'width': 1
                    }
                },
            }
        NVMDef.init_logger(logging.getLogger())
        nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, nvm_vars_test)
        no_nvm_a2l = False
        nvm_def.generate_nvm_config_files(no_nvm_a2l)
        self.maxDiff = None

        h_file_name = Path(SRC_DIR, 'output', 'vcc_nvm_structs_critical.h')
        with h_file_name.open() as hfptr:
            h_file = hfptr.read()
        with Path(SRC_DIR, 'reference_files', 'vcc_nvm_structs_critical.h').open() as hfptr_ref:
            h_ref_file = hfptr_ref.read()
        self.assertEqual(h_ref_file, h_file)

    def test_add_signal_with_nondefault_type_a2l_bosch(self):
        """Test that we can add different types of signals to critical area - a2l-file
        """
        self.proj_cnfg.get_ecu_info = MagicMock(return_value=('Bosch', ''))
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs_critical)
        nvm_vars_test = {
            'sVcTest_t_UInt32': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_UInt32',
                    'lsb': 2,
                    'name': 'sVcTest_t_UInt32',
                    'offset': 1,
                    'type': 'UInt32',
                    'unit': 's',
                    'width': 1
                    }
                },
            'sVcTest_t_Int16': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_Int16',
                    'lsb': 1,
                    'name': 'sVcTest_t_UInt16',
                    'offset': 0,
                    'type': 'Int16',
                    'unit': '-',
                    'width': 1
                    }
                },
            'sVcTest_t_UInt8': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_UInt8',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcTest_t_UInt8',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-',
                    'width': 1
                    }
                },
            }
        NVMDef.init_logger(logging.getLogger())
        nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, nvm_vars_test)
        no_nvm_a2l = False
        nvm_def.generate_nvm_config_files(no_nvm_a2l)
        self.maxDiff = None

        a_file_name = Path(SRC_DIR, 'output', 'vcc_nvm_structs_critical.a2l')
        with a_file_name.open() as fptr:
            a2l_file = fptr.read()
        ref_file = Path(SRC_DIR, 'reference_files', 'vcc_nvm_structs_critical_bosch.a2l')
        if self.create_new:
            with ref_file.open(mode='w') as fptr_ref:
                fptr_ref.write(a2l_file)
        with ref_file.open() as fptr_ref:
            a2l_ref_file = fptr_ref.read()
        self.assertEqual(a2l_ref_file, a2l_file)

    def test_add_signal_with_nondefault_type_a2l_denso(self):
        """Test that we can add different types of signals to critical area - a2l-file.

        Note: Denso does not have any area like this at the time of writing this test
        """
        self.proj_cnfg.get_ecu_info = MagicMock(return_value=('Denso', 'G2'))
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs_critical)
        nvm_vars_test = {
            'sVcTest_t_UInt32': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_UInt32',
                    'lsb': 2,
                    'name': 'sVcTest_t_UInt32',
                    'offset': 1,
                    'type': 'UInt32',
                    'unit': 's',
                    'width': 1
                    }
                },
            'sVcTest_t_Int16': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_Int16',
                    'lsb': 1,
                    'name': 'sVcTest_t_UInt16',
                    'offset': 0,
                    'type': 'Int16',
                    'unit': '-',
                    'width': 1
                    }
                },
            'sVcTest_t_UInt8': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_UInt8',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcTest_t_UInt8',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-',
                    'width': 1
                    }
                }
            }
        NVMDef.init_logger(logging.getLogger())
        nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, nvm_vars_test)
        no_nvm_a2l = False
        nvm_def.generate_nvm_config_files(no_nvm_a2l)
        self.maxDiff = None

        a_file_name = Path(SRC_DIR, 'output', 'vcc_nvm_structs_critical.a2l')
        with a_file_name.open() as fptr:
            a2l_file = fptr.read()
        ref_file = Path(SRC_DIR, 'reference_files', 'vcc_nvm_structs_critical_denso.a2l')
        if self.create_new:
            with ref_file.open(mode='w') as fptr_ref:
                fptr_ref.write(a2l_file)
        with ref_file.open() as fptr_ref:
            a2l_ref_file = fptr_ref.read()
        self.assertEqual(a2l_ref_file, a2l_file)

    def test_add_signal_with_wrong_type(self):
        """test that its not possible to add a signal of wrong type to a specific nwm area
        """
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs_wrong_type)
        self.nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, self.nvm_vars_test)
        NVMDef.init_logger(logging.getLogger())

        no_nvm_a2l = False
        self.assertRaises(NVMDef.WrongTypeException, self.nvm_def.generate_nvm_config_files, no_nvm_a2l)

    def test_add_duplicate_signal_different_attributes(self):
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs_single)
        nvm_vars_test = {
            'sVcAcCtrl_t_CmprRunTiNVM': {
                'VcAcCtrl': {
                    'class': 'CVC_DISP_NVM_P',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcAcCtrl/VcAcCtrl/Subsystem/VcAcCtrl/CoolingManager/'
                              '3_SystemInfo/36_CompressorRunTime/sVcAcCtrl_t_CmprRunTiNVM/Unit Delay',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcAcCtrl_t_CmprRunTiNVM',
                    'offset': 0,
                    'type': 'Float32',
                    'unit': '-',
                    'width': 1
                    }
                }
            }
        no_nvm_a2l = False
        nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, nvm_vars_test)
        NVMDef.init_logger(logging.getLogger())
        NVMDef.clear_log()
        nvm_def.generate_nvm_config_files(no_nvm_a2l)
        self.assertEqual(nvm_def.get_nbr_problems()['critical'], 1)

    def test_add_duplicate_signal_different_memory_area(self):
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs_single)
        self.nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, self.nvm_vars_test)
        nvm_vars_test = {
            'sVcAcCtrl_t_CmprRunTiNVM': {
                'VcAcCtrl': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcAcCtrl/VcAcCtrl/Subsystem/VcAcCtrl/CoolingManager/'
                              '3_SystemInfo/36_CompressorRunTime/sVcAcCtrl_t_CmprRunTiNVM/Unit Delay',
                    'lsb': 1,
                    'max': 'nan',
                    'min': 'nan',
                    'name': 'sVcAcCtrl_t_CmprRunTiNVM',
                    'offset': 0,
                    'type': 'UInt32',
                    'unit': '-',
                    'width': 1
                    }
                }
            }
        NVMDef.init_logger(logging.getLogger())
        NVMDef.clear_log()
        nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, nvm_vars_test)
        no_nvm_a2l = False
        nvm_def.generate_nvm_config_files(no_nvm_a2l)
        self.assertEqual(nvm_def.get_nbr_problems()['warning'], 2)

    def test_remove_signal_from_critical(self):
        """Test that a2l- and h-files are updated when removing a signal from the critical area."""
        self.proj_cnfg.get_nvm_defs = MagicMock(return_value=self.nvm_configs_critical_remove)
        nvm_vars_test = {
            'sVcTest_t_UInt32': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_UInt32',
                    'lsb': 2,
                    'name': 'sVcTest_t_UInt32',
                    'offset': 1,
                    'type': 'UInt32',
                    'unit': 's',
                    'width': 1
                }
            },
            'sVcTest_t_Int16': {
                'VcTest': {
                    'class': 'CVC_DISP_NVM',
                    'configs': ['all'],
                    'description': 'Enter a nice description of your variable here',
                    'handle': 'VcTest/VcTest_t_Int16',
                    'lsb': 1,
                    'name': 'sVcTest_t_UInt16',
                    'offset': 0,
                    'type': 'Int16',
                    'unit': '-',
                    'width': 1
                }
            }
        }
        NVMDef.init_logger(logging.getLogger())
        NVMDef.clear_log()
        self.nvm_def = NVMDef(self.proj_cnfg, self.unit_cfg, nvm_vars_test)
        no_nvm_a2l = False
        self.nvm_def.generate_nvm_config_files(no_nvm_a2l)

        h_file_name = Path(SRC_DIR, 'output', self.nvm_configs_critical_remove['fileName'] + '.h')
        with h_file_name.open() as h_ptr:
            h_file = h_ptr.read()
        with Path(SRC_DIR, 'reference_files', 'vcc_nvm_struct_ref_critical_remove.h').open() as h_ref_ptr:
            h_ref_file = h_ref_ptr.read()
        self.maxDiff = None
        self.assertEqual(h_ref_file, h_file)

        a2l_file_name = Path(SRC_DIR, 'output', self.nvm_configs_critical_remove['fileName'] + '.a2l')
        with a2l_file_name.open() as a2l_ptr:
            a2l_file = a2l_ptr.read()
        ref_file = Path(SRC_DIR, 'reference_files', 'vcc_nvm_struct_ref_critical_remove.a2l')
        if self.create_new:
            with ref_file.open(mode='w') as a2l_ref_ptr:
                a2l_ref_ptr.write(a2l_file)
        with ref_file.open() as a2l_ref_ptr:
            a2l_ref_file = a2l_ref_ptr.read()
        self.assertEqual(a2l_ref_file, a2l_file)
