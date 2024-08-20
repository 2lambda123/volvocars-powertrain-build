# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for Dids."""
from copy import deepcopy
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import mock_open
from pathlib import Path
from powertrain_build.build_proj_config import BuildProjConfig
from powertrain_build.dids import DIDs, HIDIDs, ZCDIDs
from test_data.powertrain_build.test_dids.zc_dids import (
    dummy_project_dids,
    bad_dummy_project_dids,
    valid_dids,
    bad_valid_dids,
    test_valid_dids_setter_expected,
    test_get_operation_data_did_data,
    test_get_operation_data_expected,
    TEST_GET_HEADER_FILE_CONTENT_EXPECTED,
    TEST_GET_SOURCE_FILE_CONTENT_EXPECTED,
)


class TestDIDsTL(unittest.TestCase):
    """Test case for testing the DIDs class."""

    unit_cfg_res = {
        'VcFnc1': {
            'dids': {
                "rVcNoxSensMgr_Z_UsCorO2P": {
                    "name": "rVcNoxSensMgr_Z_UsCorO2P",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "Float32",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0.45",
                    "max": "0.61",
                    "class": "CVC_DISP"
                },
                "dummy_f32did": {
                    "name": "dummy_f32did",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "Float32",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0.45",
                    "max": "0.61",
                    "class": "CVC_DISP"
                }
            }
        },
        'VcFnc2': {
            'dids': {
                "did2": {
                    "name": "did2",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "UInt32",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0",
                    "max": "32000",
                    "class": "CVC_DISP"
                },
                "dummy_uintdid": {
                    "name": "dummy_uintdid",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "Int8",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0",
                    "max": "32000",
                    "class": "CVC_DISP"
                }
            }
        }
    }

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(config_set=BuildProjConfig)
        prj_cnf_dir = str(Path(Path(__file__).parent, 'cnfg_files'))
        self.build_cfg.get_prj_cfg_dir = MagicMock(return_value=prj_cnf_dir)
        self.build_cfg.get_did_cfg_file_name = MagicMock(return_value='DIDIds_FullRange')
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')

        self._unit_cfg = MagicMock()
        type(self._unit_cfg).code_generators = {'target_link'}
        type(self._unit_cfg).base_types_headers = '#include "tl_basetypes.h"\n'
        self._unit_cfg.get_per_unit_cfg = MagicMock(return_value=self.unit_cfg_res)

        self.dids = DIDs(self.build_cfg, self._unit_cfg)

    def test_get_did_config(self):
        """Test parsing of did config files."""
        result = self.dids.get_did_config()
        expected_result = {
            'Float32': {
                'dids': {'rVcDepTre_Tq_WhlMotSysTqEstForDID': 58112,
                         'rVcNoxSensMgr_Z_UsCorO2P': 58113},
                'end_did': 58879,
                'start_did': 58112
            },
            'UInt32': {
                'dids': {'rVcDepTre_D_CompositeDID1': 58368,
                         'did2': 58369},
                'end_did': 58623,
                'start_did': 58368
            }
        }
        self.assertEqual(result, expected_result)

    def test_check_dids(self):
        """Test validity check."""
        pass_dids = {
            'dids': {'rVcDepTre_Tq_WhlMotSysTqEstForDID': 58112},
            'end_did': 58879,
            'start_did': 58112
        }
        self.assertIsNone(DIDs._check_dids(pass_dids))

        fail_low_dids = {
            'dids': {'rVcDepTre_Tq_WhlMotSysTqEstForDID': 48112},
            'end_did': 58879,
            'start_did': 58112
        }
        self.assertRaisesRegex(ValueError, ' has a too low did ', DIDs._check_dids, fail_low_dids)

        fail_high_dids = {
            'dids': {'rVcDepTre_Tq_WhlMotSysTqEstForDID': 68112},
            'end_did': 58879,
            'start_did': 58112
        }
        self.assertRaisesRegex(ValueError, ' has a too high did ', DIDs._check_dids, fail_high_dids)

    def test_gen_did_def_files(self):
        """Test generation of DID def files."""
        expected_result = [
            '#include "VcDidDefinitions.h"\n\n',
            '#include "CVC_CODE_START.h"\n\n',
            '/* The table shall be sorted in ascending Did is order!\n'
            ' If not the search algorithm does not work */\n',
            'const struct DID_Mapping_Float32 DID_data_struct_Float32[] = {\n',
            '\t{0xE301, &rVcNoxSensMgr_Z_UsCorO2P}  /* '
            'VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/1_NoxSensUsMgrRecv/'
            '12_NoxSensUsCorrectionFactors/UnitDelay8 '
            '*/ \n',
            '};\n\n',
            'const struct DID_Mapping_UInt32 DID_data_struct_UInt32[] = {\n',
            '\t{0xE401, &did2, UInt32_}  /* '
            'VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/1_NoxSensUsMgrRecv/'
            '12_NoxSensUsCorrectionFactors/UnitDelay8 '
            '*/ \n',
            '};\n\n',
            '/* *** DIDs not in the definition file! ****\n',
            'Did for Float32 signal "dummy_f32did" not defined\n',
            'Did for UInt32 signal "dummy_uintdid" not defined\n',
            '*/\n',
            '\n#include "CVC_CODE_END.h"\n',
            '\n'
            '/*----------------------------------------------------------------------------*\\\n'
            '  END OF FILE\n'
            '\\*----------------------------------------------------------------------------*/',
            '#ifndef VCDIDDEFINITIONS_H\n',
            '#define VCDIDDEFINITIONS_H\n\n',
            '#include "tl_basetypes.h"\n',
            'enum Datatypes {UInt8_, Int8_, UInt16_, Int16_, UInt32_, Int32_, Float32_, Bool_};\n\n',
            '#define DID_DATASTRUCT_LEN_FLOAT32 1\n',
            '#define DID_DATASTRUCT_LEN_UINT32 1\n\n',
            'struct DID_Mapping_UInt32 {\n'
            '\tUInt16 DID;\n'
            '\tvoid* data;\n'
            '\tenum Datatypes type;\n'
            '};\n'
            '\n',
            'struct DID_Mapping_Float32 {\n\tUInt16 DID;\n\tFloat32* data;\n};\n\n',
            '#include "PREDECL_START.h"\n',
            'extern const struct DID_Mapping_UInt32 DID_data_struct_UInt32[];\n',
            'extern const struct DID_Mapping_Float32 DID_data_struct_Float32[];\n',
            '/* Floats */\n',
            'extern Float32 rVcNoxSensMgr_Z_UsCorO2P; /* Did id: 0xE301 */\n',
            '/* Integers & Bools */\n',
            'extern UInt32 did2; /* Did id: 0xE401 */\n',
            '#include "PREDECL_END.h"\n',
            '\n#endif /* VCDIDDEFINITIONS_H */\n'
        ]
        result = []
        mopen = mock_open()
        mopen.return_value.write = result.append
        mopen.return_value.name = 'C:/foo/VcDidDefinitions.h'
        with patch('builtins.open', mopen, create=True):
            self.dids.gen_did_def_files('VcDidDefinitions')
        self.assertEqual(result, expected_result)

    def test_gen_did_def_files_no_dids(self):
        """Test generation of DID def files."""
        expected_result = [
            '#include "VcDidDefinitions.h"\n\n',
            '#include "CVC_CODE_START.h"\n\n',
            '/* The table shall be sorted in ascending Did is order!\n'
            ' If not the search algorithm does not work */\n',
            'const struct DID_Mapping_Float32 DID_data_struct_Float32[] = {\n',
            '\t{0x0000, 0L} /* Dummy entry */ \n',
            '};\n\n',
            'const struct DID_Mapping_UInt32 DID_data_struct_UInt32[] = {\n',
            '\t{0x0000, 0L, UInt32_} /* Dummy entry */ \n',
            '};\n\n',
            '\n#include "CVC_CODE_END.h"\n',
            '\n'
            '/*----------------------------------------------------------------------------*\\\n'
            '  END OF FILE\n'
            '\\*----------------------------------------------------------------------------*/',
            '#ifndef VCDIDDEFINITIONS_H\n',
            '#define VCDIDDEFINITIONS_H\n\n',
            '#include "tl_basetypes.h"\n',
            'enum Datatypes {UInt8_, Int8_, UInt16_, Int16_, UInt32_, Int32_, Float32_, Bool_};\n\n',
            '#define DID_DATASTRUCT_LEN_FLOAT32 0\n',
            '#define DID_DATASTRUCT_LEN_UINT32 0\n\n',
            'struct DID_Mapping_UInt32 {\n'
            '\tUInt16 DID;\n'
            '\tvoid* data;\n'
            '\tenum Datatypes type;\n'
            '};\n'
            '\n',
            'struct DID_Mapping_Float32 {\n\tUInt16 DID;\n\tFloat32* data;\n};\n\n',
            '#include "PREDECL_START.h"\n',
            'extern const struct DID_Mapping_UInt32 DID_data_struct_UInt32[];\n',
            'extern const struct DID_Mapping_Float32 DID_data_struct_Float32[];\n',
            '/* Floats */\n',
            '/* Integers & Bools */\n',
            '#include "PREDECL_END.h"\n',
            '\n#endif /* VCDIDDEFINITIONS_H */\n'
        ]
        result = []
        unit_cfg = self._unit_cfg
        unit_cfg.get_per_unit_cfg = MagicMock(return_value={})

        self.dids = DIDs(self.build_cfg, unit_cfg)
        mopen = mock_open()
        mopen.return_value.write = result.append
        mopen.return_value.name = 'C:/foo/VcDidDefinitions.h'
        with patch('builtins.open', mopen, create=True):
            self.dids.gen_did_def_files('VcDidDefinitions')
        self.assertEqual(result, expected_result)


class TestDIDsEC(unittest.TestCase):
    """Test case for testing the DIDs class."""

    unit_cfg_res = {
        'VcFnc1': {
            'code_generator': 'embedded_coder',
            'dids': {
                "rVcNoxSensMgr_Z_UsCorO2P": {
                    "name": "rVcNoxSensMgr_Z_UsCorO2P",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "real32_T",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0.45",
                    "max": "0.61",
                    "class": "CVC_DISP"
                },
                "dummy_f32did": {
                    "name": "dummy_f32did",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "real32_T",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0.45",
                    "max": "0.61",
                    "class": "CVC_DISP"
                }
            }
        },
        'VcFnc2': {
            'code_generator': 'embedded_coder',
            'dids': {
                "did2": {
                    "name": "did2",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "int_T",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0",
                    "max": "32000",
                    "class": "CVC_DISP"
                },
                "dummy_uintdid": {
                    "name": "dummy_uintdid",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "uint32_T",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0",
                    "max": "32000",
                    "class": "CVC_DISP"
                }
            }
        }
    }

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(config_set=BuildProjConfig)
        prj_cnf_dir = str(Path(Path(__file__).parent, 'cnfg_files'))
        self.build_cfg.get_prj_cfg_dir = MagicMock(return_value=prj_cnf_dir)
        self.build_cfg.get_did_cfg_file_name = MagicMock(return_value='DIDIds_FullRange')
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')

        self._unit_cfg = MagicMock()
        type(self._unit_cfg).code_generators = {'embedded_coder'}
        type(self._unit_cfg).base_types_headers = '#include "rtwtypes.h"\n'
        self._unit_cfg.get_per_unit_cfg = MagicMock(return_value=self.unit_cfg_res)

        self.dids = DIDs(self.build_cfg, self._unit_cfg)

    def test_get_did_config(self):
        """Test parsing of did config files."""
        result = self.dids.get_did_config()
        expected_result = {
            'Float32': {
                'dids': {'rVcDepTre_Tq_WhlMotSysTqEstForDID': 58112,
                         'rVcNoxSensMgr_Z_UsCorO2P': 58113},
                'end_did': 58879,
                'start_did': 58112
            },
            'UInt32': {
                'dids': {'rVcDepTre_D_CompositeDID1': 58368,
                         'did2': 58369},
                'end_did': 58623,
                'start_did': 58368
            }
        }
        self.assertEqual(result, expected_result)

    def test_check_dids(self):
        """Test validity check."""
        pass_dids = {
            'dids': {'rVcDepTre_Tq_WhlMotSysTqEstForDID': 58112},
            'end_did': 58879,
            'start_did': 58112
        }
        self.assertIsNone(DIDs._check_dids(pass_dids))

        fail_low_dids = {
            'dids': {'rVcDepTre_Tq_WhlMotSysTqEstForDID': 48112},
            'end_did': 58879,
            'start_did': 58112
        }
        self.assertRaisesRegex(ValueError, ' has a too low did ', DIDs._check_dids, fail_low_dids)

        fail_high_dids = {
            'dids': {'rVcDepTre_Tq_WhlMotSysTqEstForDID': 68112},
            'end_did': 58879,
            'start_did': 58112
        }
        self.assertRaisesRegex(ValueError, ' has a too high did ', DIDs._check_dids, fail_high_dids)

    def test_gen_did_def_files(self):
        """Test generation of DID def files."""
        expected_result = [
            '#include "VcDidDefinitions.h"\n\n',
            '#include "CVC_CODE_START.h"\n\n',
            '/* The table shall be sorted in ascending Did is order!\n'
            ' If not the search algorithm does not work */\n',
            'const struct DID_Mapping_Float32 DID_data_struct_Float32[] = {\n',
            '\t{0xE301, &rVcNoxSensMgr_Z_UsCorO2P}  /* '
            'VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/1_NoxSensUsMgrRecv/'
            '12_NoxSensUsCorrectionFactors/UnitDelay8 '
            '*/ \n',
            '};\n\n',
            'const struct DID_Mapping_UInt32 DID_data_struct_UInt32[] = {\n',
            '\t{0xE401, &did2, int_T_}  /* '
            'VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/1_NoxSensUsMgrRecv/'
            '12_NoxSensUsCorrectionFactors/UnitDelay8 '
            '*/ \n',
            '};\n\n',
            '/* *** DIDs not in the definition file! ****\n',
            'Did for Float32 signal "dummy_f32did" not defined\n',
            'Did for UInt32 signal "dummy_uintdid" not defined\n',
            '*/\n',
            '\n#include "CVC_CODE_END.h"\n',
            '\n'
            '/*----------------------------------------------------------------------------*\\\n'
            '  END OF FILE\n'
            '\\*----------------------------------------------------------------------------*/',
            '#ifndef VCDIDDEFINITIONS_H\n',
            '#define VCDIDDEFINITIONS_H\n\n',
            '#include "rtwtypes.h"\n',
            'enum Datatypes {uint8_T_, int8_T_, uint16_T_, int16_T_, uint32_T_, int32_T_, real32_T_, boolean_T_};\n\n',
            '#define DID_DATASTRUCT_LEN_FLOAT32 1\n',
            '#define DID_DATASTRUCT_LEN_UINT32 1\n\n',
            'struct DID_Mapping_UInt32 {\n'
            '\tuint16_T DID;\n'
            '\tvoid* data;\n'
            '\tenum Datatypes type;\n'
            '};\n'
            '\n',
            'struct DID_Mapping_Float32 {\n\tuint16_T DID;\n\treal32_T* data;\n};\n\n',
            '#include "PREDECL_START.h"\n',
            'extern const struct DID_Mapping_UInt32 DID_data_struct_UInt32[];\n',
            'extern const struct DID_Mapping_Float32 DID_data_struct_Float32[];\n',
            '/* Floats */\n',
            'extern real32_T rVcNoxSensMgr_Z_UsCorO2P; /* Did id: 0xE301 */\n',
            '/* Integers & Bools */\n',
            'extern int_T did2; /* Did id: 0xE401 */\n',
            '#include "PREDECL_END.h"\n',
            '\n#endif /* VCDIDDEFINITIONS_H */\n'
        ]
        result = []
        mopen = mock_open()
        mopen.return_value.write = result.append
        mopen.return_value.name = 'C:/foo/VcDidDefinitions.h'
        with patch('builtins.open', mopen, create=True):
            self.dids.gen_did_def_files('VcDidDefinitions')
        self.assertEqual(result, expected_result)

    def test_gen_did_def_files_no_dids(self):
        """Test generation of DID def files."""
        expected_result = [
            '#include "VcDidDefinitions.h"\n\n',
            '#include "CVC_CODE_START.h"\n\n',
            '/* The table shall be sorted in ascending Did is order!\n'
            ' If not the search algorithm does not work */\n',
            'const struct DID_Mapping_Float32 DID_data_struct_Float32[] = {\n',
            '\t{0x0000, 0L} /* Dummy entry */ \n',
            '};\n\n',
            'const struct DID_Mapping_UInt32 DID_data_struct_UInt32[] = {\n',
            '\t{0x0000, 0L, uint32_T_} /* Dummy entry */ \n',
            '};\n\n',
            '\n#include "CVC_CODE_END.h"\n',
            '\n'
            '/*----------------------------------------------------------------------------*\\\n'
            '  END OF FILE\n'
            '\\*----------------------------------------------------------------------------*/',
            '#ifndef VCDIDDEFINITIONS_H\n',
            '#define VCDIDDEFINITIONS_H\n\n',
            '#include "rtwtypes.h"\n',
            'enum Datatypes {uint8_T_, int8_T_, uint16_T_, int16_T_, uint32_T_, int32_T_, real32_T_, boolean_T_};\n\n',
            '#define DID_DATASTRUCT_LEN_FLOAT32 0\n',
            '#define DID_DATASTRUCT_LEN_UINT32 0\n\n',
            'struct DID_Mapping_UInt32 {\n'
            '\tuint16_T DID;\n'
            '\tvoid* data;\n'
            '\tenum Datatypes type;\n'
            '};\n'
            '\n',
            'struct DID_Mapping_Float32 {\n\tuint16_T DID;\n\treal32_T* data;\n};\n\n',
            '#include "PREDECL_START.h"\n',
            'extern const struct DID_Mapping_UInt32 DID_data_struct_UInt32[];\n',
            'extern const struct DID_Mapping_Float32 DID_data_struct_Float32[];\n',
            '/* Floats */\n',
            '/* Integers & Bools */\n',
            '#include "PREDECL_END.h"\n',
            '\n#endif /* VCDIDDEFINITIONS_H */\n'
        ]
        result = []
        unit_cfg = self._unit_cfg
        unit_cfg.get_per_unit_cfg = MagicMock(return_value={})

        self.dids = DIDs(self.build_cfg, unit_cfg)
        mopen = mock_open()
        mopen.return_value.write = result.append
        mopen.return_value.name = 'C:/foo/VcDidDefinitions.h'
        with patch('builtins.open', mopen, create=True):
            self.dids.gen_did_def_files('VcDidDefinitions')
        self.assertEqual(result, expected_result)


class TestDIDsMixed(TestDIDsTL):
    """Test case for testing the DIDs class."""

    unit_cfg_res = {
        'VcFnc1': {
            'code_generator': 'target_link',
            'dids': {
                "rVcNoxSensMgr_Z_UsCorO2P": {
                    "name": "rVcNoxSensMgr_Z_UsCorO2P",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "Float32",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0.45",
                    "max": "0.61",
                    "class": "CVC_DISP"
                },
                "dummy_f32did": {
                    "name": "dummy_f32did",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "Float32",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0.45",
                    "max": "0.61",
                    "class": "CVC_DISP"
                }
            }
        },
        'VcFnc2': {
            'code_generator': 'embedded_coder',
            'dids': {
                "did2": {
                    "name": "did2",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "int_T",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0",
                    "max": "32000",
                    "class": "CVC_DISP"
                },
                "dummy_uintdid": {
                    "name": "dummy_uintdid",
                    "description": "Stored  O2 pressure correction value for upstream sensor",
                    "handle": "VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/"
                              "1_NoxSensUsMgrRecv/12_NoxSensUsCorrectionFactors/UnitDelay8",
                    "configs": [
                        "all"],
                    "type": "uint32_T",
                    "unit": "",
                    "offset": 0,
                    "lsb": 1,
                    "min": "0",
                    "max": "32000",
                    "class": "CVC_DISP"
                }
            }
        }
    }

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(config_set=BuildProjConfig)
        prj_cnf_dir = str(Path(Path(__file__).parent, 'cnfg_files'))
        self.build_cfg.get_prj_cfg_dir = MagicMock(return_value=prj_cnf_dir)
        self.build_cfg.get_did_cfg_file_name = MagicMock(return_value='DIDIds_FullRange')
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')

        self._unit_cfg = MagicMock()
        type(self._unit_cfg).code_generators = {'target_link', 'embedded_coder'}
        type(self._unit_cfg).base_types_headers = '#include "rtwtypes.h"\n#include "tl_basetypes.h"\n'
        self._unit_cfg.get_per_unit_cfg = MagicMock(return_value=self.unit_cfg_res)

        self.dids = DIDs(self.build_cfg, self._unit_cfg)

    def test_gen_did_def_files(self):
        """Test generation of DID def files."""
        expected_result = [
            '#include "VcDidDefinitions.h"\n\n',
            '#include "CVC_CODE_START.h"\n\n',
            '/* The table shall be sorted in ascending Did is order!\n'
            ' If not the search algorithm does not work */\n',
            'const struct DID_Mapping_Float32 DID_data_struct_Float32[] = {\n',
            '\t{0xE301, &rVcNoxSensMgr_Z_UsCorO2P}  /* '
            'VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/1_NoxSensUsMgrRecv/'
            '12_NoxSensUsCorrectionFactors/UnitDelay8 '
            '*/ \n',
            '};\n\n',
            'const struct DID_Mapping_UInt32 DID_data_struct_UInt32[] = {\n',
            '\t{0xE401, &did2, int_T_}  /* '
            'VcNoxSensMgr/VcNoxSensMgr/Subsystem/VcNoxSensMgr/NoxSensManager/1_NoxSensUsMgrRecv/'
            '12_NoxSensUsCorrectionFactors/UnitDelay8 '
            '*/ \n',
            '};\n\n',
            '/* *** DIDs not in the definition file! ****\n',
            'Did for Float32 signal "dummy_f32did" not defined\n',
            'Did for UInt32 signal "dummy_uintdid" not defined\n',
            '*/\n',
            '\n#include "CVC_CODE_END.h"\n',
            '\n'
            '/*----------------------------------------------------------------------------*\\\n'
            '  END OF FILE\n'
            '\\*----------------------------------------------------------------------------*/',
            '#ifndef VCDIDDEFINITIONS_H\n',
            '#define VCDIDDEFINITIONS_H\n\n',
            '#include "rtwtypes.h"\n#include "tl_basetypes.h"\n',
            'enum Datatypes {UInt8_, Int8_, UInt16_, Int16_, UInt32_, Int32_, Float32_, Bool_};\n\n',
            '#define DID_DATASTRUCT_LEN_FLOAT32 1\n',
            '#define DID_DATASTRUCT_LEN_UINT32 1\n\n',
            'struct DID_Mapping_UInt32 {\n'
            '\tUInt16 DID;\n'
            '\tvoid* data;\n'
            '\tenum Datatypes type;\n'
            '};\n'
            '\n',
            'struct DID_Mapping_Float32 {\n\tUInt16 DID;\n\tFloat32* data;\n};\n\n',
            '#include "PREDECL_START.h"\n',
            'extern const struct DID_Mapping_UInt32 DID_data_struct_UInt32[];\n',
            'extern const struct DID_Mapping_Float32 DID_data_struct_Float32[];\n',
            '/* Floats */\n',
            'extern Float32 rVcNoxSensMgr_Z_UsCorO2P; /* Did id: 0xE301 */\n',
            '/* Integers & Bools */\n',
            'extern int_T did2; /* Did id: 0xE401 */\n',
            '#include "PREDECL_END.h"\n',
            '\n#endif /* VCDIDDEFINITIONS_H */\n'
        ]
        result = []
        mopen = mock_open()
        mopen.return_value.write = result.append
        mopen.return_value.name = 'C:/foo/VcDidDefinitions.h'
        with patch('builtins.open', mopen, create=True):
            self.dids.gen_did_def_files('VcDidDefinitions')
        self.assertEqual(result, expected_result)

    def test_gen_did_def_files_no_dids(self):
        """Test generation of DID def files."""
        expected_result = [
            '#include "VcDidDefinitions.h"\n\n',
            '#include "CVC_CODE_START.h"\n\n',
            '/* The table shall be sorted in ascending Did is order!\n'
            ' If not the search algorithm does not work */\n',
            'const struct DID_Mapping_Float32 DID_data_struct_Float32[] = {\n',
            '\t{0x0000, 0L} /* Dummy entry */ \n',
            '};\n\n',
            'const struct DID_Mapping_UInt32 DID_data_struct_UInt32[] = {\n',
            '\t{0x0000, 0L, UInt32_} /* Dummy entry */ \n',
            '};\n\n',
            '\n#include "CVC_CODE_END.h"\n',
            '\n'
            '/*----------------------------------------------------------------------------*\\\n'
            '  END OF FILE\n'
            '\\*----------------------------------------------------------------------------*/',
            '#ifndef VCDIDDEFINITIONS_H\n',
            '#define VCDIDDEFINITIONS_H\n\n',
            '#include "rtwtypes.h"\n#include "tl_basetypes.h"\n',
            'enum Datatypes {UInt8_, Int8_, UInt16_, Int16_, UInt32_, Int32_, Float32_, Bool_};\n\n',
            '#define DID_DATASTRUCT_LEN_FLOAT32 0\n',
            '#define DID_DATASTRUCT_LEN_UINT32 0\n\n',
            'struct DID_Mapping_UInt32 {\n'
            '\tUInt16 DID;\n'
            '\tvoid* data;\n'
            '\tenum Datatypes type;\n'
            '};\n'
            '\n',
            'struct DID_Mapping_Float32 {\n\tUInt16 DID;\n\tFloat32* data;\n};\n\n',
            '#include "PREDECL_START.h"\n',
            'extern const struct DID_Mapping_UInt32 DID_data_struct_UInt32[];\n',
            'extern const struct DID_Mapping_Float32 DID_data_struct_Float32[];\n',
            '/* Floats */\n',
            '/* Integers & Bools */\n',
            '#include "PREDECL_END.h"\n',
            '\n#endif /* VCDIDDEFINITIONS_H */\n'
        ]
        result = []
        unit_cfg = self._unit_cfg
        unit_cfg.get_per_unit_cfg = MagicMock(return_value={})

        self.dids = DIDs(self.build_cfg, unit_cfg)
        mopen = mock_open()
        mopen.return_value.write = result.append
        mopen.return_value.name = 'C:/foo/VcDidDefinitions.h'
        with patch('builtins.open', mopen, create=True):
            self.dids.gen_did_def_files('VcDidDefinitions')
        self.assertEqual(result, expected_result)


class TestHIDIDs(unittest.TestCase):
    """Test case for testing HIDIDs class."""

    def setUp(self):
        build_cfg = MagicMock()
        build_cfg.get_a2l_cfg.return_value = {'name': 'DUMMY'}

        unit_cfg = MagicMock()

        self.dummy_project_dids = {
            'dummy_did_one': {
                'handle': 'VcDummy/VcDummy/Subsystem/VcDummy/VcDummy/1_VcDummy/Rel',
                'name': 'dummy_did_one',
                'configs': '((ALWAYS_ACTIVE))',
                'description': 'Dummy DID',
                'type': 'Bool',
                'unit': '',
                'offset': '',
                'lsb': '',
                'min': '-',
                'max': '-',
                'class': 'ASIL_D/CVC_DISP_ASIL_D'
            },
            'dummy_did_two': {
                'handle': 'VcDummyTwo/VcDummyTwo/Subsystem/VcDummyTwo/VcDummyTwo/1_VcDummyTwo/Rel',
                'name': 'dummy_did_two',
                'configs': '((ALWAYS_ACTIVE))',
                'description': 'Dummy DID number 2',
                'type': 'UInt8',
                'unit': '',
                'offset': '',
                'lsb': '',
                'min': '-',
                'max': '-',
                'class': 'ASIL_D/CVC_DISP_ASIL_D'
            }
        }
        self.dummy_dids = {
            'dummy_did_one': {
                'id': 'DA00',
                'data_type': 'Dcm_NegativeResponseCodeType',
                'function_type': 'condition_check'
            },
            'dummy_did_two': {
                'id': 'DA01',
                'data_type': 'uint8',
                'function_type': 'read_data_max',
                'nr_of_bytes': 1
            }
        }
        self.dummy_did_dict = {
            'dummy_did_one': {
                'id': 'DA00',
                'data_type': 'Dcm_NegativeResponseCodeType',
                'function_type': 'condition_check',
                'handle': 'VcDummy/VcDummy/Subsystem/VcDummy/VcDummy/1_VcDummy/Rel',
                'name': 'dummy_did_one',
                'configs': '((ALWAYS_ACTIVE))',
                'description': 'Dummy DID',
                'type': 'Bool',
                'unit': '',
                'offset': '',
                'lsb': '',
                'min': '-',
                'max': '-',
                'class': 'ASIL_D/CVC_DISP_ASIL_D'
            },
            'dummy_did_two': {
                'id': 'DA01',
                'data_type': 'uint8',
                'function_type': 'read_data_max',
                'nr_of_bytes': 1,
                'handle': 'VcDummyTwo/VcDummyTwo/Subsystem/VcDummyTwo/VcDummyTwo/1_VcDummyTwo/Rel',
                'name': 'dummy_did_two',
                'configs': '((ALWAYS_ACTIVE))',
                'description': 'Dummy DID number 2',
                'type': 'UInt8',
                'unit': '',
                'offset': '',
                'lsb': '',
                'min': '-',
                'max': '-',
                'class': 'ASIL_D/CVC_DISP_ASIL_D'
            }
        }
        compose_did_data_return = deepcopy(self.dummy_did_dict)
        compose_did_data_return['dummy_did_one'].update({
            'function': 'DID_DA00_Runnable_ConditionCheckRead(Dcm_NegativeResponseCodeType *ErrorCode)'
        })
        compose_did_data_return['dummy_did_two'].update({
            'function': 'DID_DA01_Runnable_MAX_ReadData(uint8 *Data)'
        })
        with patch.object(HIDIDs, '_compose_did_data', return_value=compose_did_data_return):
            self.hi_dids = HIDIDs(build_cfg, unit_cfg)

    def test_verify_did_config_dict_good(self):
        """Test HIDIDs._verify_did_config_dict, proper DID configuration file."""
        result = self.hi_dids._verify_did_config_dict(self.dummy_dids)
        self.assertDictEqual(result, self.dummy_dids)

    def test_verify_did_config_dict_bad(self):
        """Test HIDIDs._verify_did_config_dict, improper DID configuration file."""
        dummy_dids = {
            'dummy_did_one': {
                'id': 'DA00',
                'data_type': 'uint8',
                'function_type': 'read_data',
                'unknown': 'dummy'
            },
            'dummy_did_two': {
                'id': 'DA01',
                'data_type': 'uint8'
            },
            'dummy_did_three': {
                'id': 'DA02',
                'data_type': 'uint8',
                'function_type': 'dummy',
            }
        }
        expected = {
            'dummy_did_one': {
                'id': 'DA00',
                'data_type': 'uint8',
                'function_type': 'read_data'
            },
            'dummy_did_two': {
                'id': 'DA01',
                'data_type': 'uint8',
                'function_type': "<missing>"
            },
            'dummy_did_three': {
                'id': 'DA02',
                'data_type': 'uint8',
                'function_type': '<missing>',
            }
        }
        result = self.hi_dids._verify_did_config_dict(dummy_dids)
        self.assertDictEqual(result, expected)

    def test_compose_did_function(self):
        """Test HIDIDs.compose_did_function."""
        expected = {
            'dummy_did_one': 'DID_DA00_Runnable_ConditionCheckRead(Dcm_NegativeResponseCodeType *ErrorCode)',
            'dummy_did_two': 'DID_DA01_Runnable_MAX_ReadData(uint8 *Data)'
        }
        for did, data in self.dummy_dids.items():
            result = self.hi_dids.compose_did_function(data)
            self.assertEqual(result, expected[did])

    def test_compose_did_function_with_missing_key(self):
        """Test HIDIDs.compose_did_function with missing key."""
        bad_did = {
            'id': 'DA00',
            'data_type': 'uint8',
            'function_type': '<missing>'
        }
        result = self.hi_dids.compose_did_function(bad_did)
        self.assertEqual(result, 'DID_DA00_Missing(uint8 *Data)')

    def test_verify_dids_pass(self):
        """Test HIDIDs.verify_dids, all as expected."""
        result = self.hi_dids.verify_dids(self.dummy_project_dids, self.dummy_dids)
        self.assertDictEqual(result, self.dummy_did_dict)

    def test_verify_dids_undefined(self):
        """Test HIDIDs.verify_dids, DID without definition in project."""
        dummy_dids = {
            'dummy_did_three': {
                'id': 'DA02',
                'data_type': 'Dcm_NegativeResponseCodeType',
                'function_type': 'condition_check'
            }
        }
        result = self.hi_dids.verify_dids(self.dummy_project_dids, dummy_dids)
        self.assertDictEqual(result, {})

    def test_verify_dids_same_id(self):
        """Test HIDIDs.verify_dids, DIDs with equal IDs, which would generate the same function calls (overwrite)."""
        dummy_dids = {
            'dummy_did_one': {
                'id': 'DA00',
                'data_type': 'Dcm_NegativeResponseCodeType',
                'function_type': 'condition_check'
            },
            'dummy_did_two': {
                'id': 'DA00',
                'data_type': 'Dcm_NegativeResponseCodeType',
                'function_type': 'condition_check'
            }
        }
        expected = {
            'dummy_did_one': self.dummy_did_dict['dummy_did_one']
        }
        result = self.hi_dids.verify_dids(self.dummy_project_dids, dummy_dids)
        self.assertDictEqual(result, expected)

    def test_verify_dids_no_project_dids(self):
        """Test HIDIDs.verify_dids, no project DIDs."""
        result = self.hi_dids.verify_dids({}, self.dummy_dids)
        self.assertDictEqual(result, {})

    def test_get_header_file_content(self):
        """Test HIDIDs.get_header_file_content."""
        result = self.hi_dids.get_header_file_content()
        expected = [
            '#ifndef VCDIDAPI_H\n',
            '#define VCDIDAPI_H\n',
            '\n',
            '#include "tl_basetypes.h"\n',
            '#include "Rte_DUMMY.h"\n',
            '\n',
            '#include "PREDECL_DISP_ASIL_D_START.h"\n',
            'extern CVC_DISP_ASIL_D Bool dummy_did_one;\n',
            'extern CVC_DISP_ASIL_D UInt8 dummy_did_two;\n',
            '#include "PREDECL_DISP_ASIL_D_END.h"\n',
            '\n#include "PREDECL_CODE_ASIL_D_START.h"\n',
            'void DID_DA00_Runnable_ConditionCheckRead(Dcm_NegativeResponseCodeType *ErrorCode);\n',
            'void DID_DA01_Runnable_MAX_ReadData(uint8 *Data);\n',
            '#include "PREDECL_CODE_ASIL_D_END.h"\n',
            '\n#endif /* VCDIDAPI_H */\n'
        ]
        self.assertListEqual(expected, result)

    def test_get_header_file_content_no_dids(self):
        """Test HIDIDs.get_header_file_content without DIDs."""
        self.hi_dids.did_dict = {}
        result = self.hi_dids.get_header_file_content()
        expected = [
            '#ifndef VCDIDAPI_H\n',
            '#define VCDIDAPI_H\n',
            '\n',
            '#include "tl_basetypes.h"\n',
            '#include "Rte_DUMMY.h"\n',
            '\n',
            '\n#endif /* VCDIDAPI_H */\n'
        ]
        self.assertListEqual(expected, result)

    def test_get_source_file_content(self):
        """Test HIDIDs.get_source_file_content."""
        result = self.hi_dids.get_source_file_content()
        expected = [
            '#include "VcDIDAPI.h"\n',
            '\n',
            '#include "CVC_CODE_ASIL_D_START.h"\n',
            'void DID_DA00_Runnable_ConditionCheckRead(Dcm_NegativeResponseCodeType *ErrorCode)\n',
            '{\n',
            '    memcpy(ErrorCode, &dummy_did_one, sizeof(Dcm_NegativeResponseCodeType));\n',
            '}\n',
            'void DID_DA01_Runnable_MAX_ReadData(uint8 *Data)\n',
            '{\n',
            '    memcpy(Data, &dummy_did_two, 1);\n',
            '}\n',
            '#include "CVC_CODE_ASIL_D_END.h"\n'
        ]
        self.assertListEqual(expected, result)

    def test_get_source_file_content_no_dids(self):
        """Test HIDIDs.get_source_file_content without DIDs."""
        self.hi_dids.did_dict = {}
        result = self.hi_dids.get_source_file_content()
        expected = [
            '#include "VcDIDAPI.h"\n',
            '\n'
        ]
        self.assertListEqual(expected, result)


class TestZCDIDs(unittest.TestCase):
    """Test case for testing ZCDIDs class."""

    def setUp(self):
        build_cfg = MagicMock()
        build_cfg.get_swc_name.return_value = 'DUMMY'
        unit_cfg = MagicMock()
        self.zc_dids = ZCDIDs(build_cfg, unit_cfg)
        self.zc_dids.project_dids = dummy_project_dids
        self.zc_dids.valid_dids = valid_dids

    def test_valid_dids_setter(self):
        """Test setting property ZCDIDs.valid_dids."""
        self.zc_dids.valid_dids = bad_valid_dids
        self.assertDictEqual(self.zc_dids.valid_dids, test_valid_dids_setter_expected)

    def test_valid_dids_setter_none(self):
        """Test setting property ZCDIDs.valid_dids with no dids."""
        self.zc_dids.valid_dids = {}
        self.assertDictEqual(self.zc_dids.valid_dids, {})

    def test_valid_dids_setter_bad_project_dids(self):
        """Test setting property ZCDIDs.valid_dids with project DIDs of wrong data type."""
        self.zc_dids.project_dids = bad_dummy_project_dids
        self.zc_dids.valid_dids = valid_dids
        self.assertDictEqual(self.zc_dids.valid_dids, {})

    def test_get_operation_data_none(self):
        """Test ZCDIDs.get_operation_data with unsupported operation."""
        self.assertIsNone(self.zc_dids.get_operation_data('Dummy', test_get_operation_data_did_data['dummy_did_one']))

    def test_get_operation_data(self):
        """Test ZCDIDs.get_operation_data."""
        result = self.zc_dids.get_operation_data('ReadData', test_get_operation_data_did_data['dummy_did_one'])
        self.assertDictEqual(result, test_get_operation_data_expected['dummy_did_one']['ReadData'])

    def test_get_operation_data_array(self):
        """Test ZCDIDs.get_operation_data with DID byte size bigger than one."""
        result = self.zc_dids.get_operation_data('ReadData', test_get_operation_data_did_data['dummy_did_two'])
        self.assertDictEqual(result, test_get_operation_data_expected['dummy_did_two']['ReadData'])

    def test_get_header_file_content_no_dids(self):
        """Test ZCDIDs._get_header_file_content without DIDs."""
        self.zc_dids.valid_dids = {}
        result = self.zc_dids._get_header_file_content()
        expected = [
            '#ifndef VCDIDAPI_H\n',
            '#define VCDIDAPI_H\n',
            '\n',
            '#include "tl_basetypes.h"\n',
            '#include "Rte_DUMMY.h"\n',
            '\n',
            '\n#endif /* VCDIDAPI_H */\n'
        ]
        self.assertListEqual(expected, result)

    def test_get_source_file_content_no_dids(self):
        """Test ZCDIDs._get_source_file_content without DIDs."""
        self.zc_dids.valid_dids = {}
        result = self.zc_dids._get_source_file_content()
        expected = [
            '#include "VcDIDAPI.h"\n',
            '\n'
        ]
        self.assertListEqual(expected, result)

    def test_get_header_file_content(self):
        """Test ZCDIDs._get_header_file_content."""
        result = ''.join(self.zc_dids._get_header_file_content())
        self.assertEqual(result, TEST_GET_HEADER_FILE_CONTENT_EXPECTED)

    def test_get_source_file_content(self):
        """Test ZCDIDs._get_source_file_content."""
        result = ''.join(self.zc_dids._get_source_file_content())
        self.assertEqual(result, TEST_GET_SOURCE_FILE_CONTENT_EXPECTED)
