# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for UserDefinedTypes class."""

import unittest
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
from pybuild.build_proj_config import BuildProjConfig
from pybuild.unit_configs import UnitConfigs
from pybuild.user_defined_types import UserDefinedTypes

REF_DIR = Path(Path(__file__).parent, 'reference_files')
CFG_DIR = Path(Path(__file__).parent, 'cnfg_files')
INTERFACE_ENUM = {
    "EnumTest": [
        {
            "item": "ClimaOff",
            "in": "ENUMTEST_CLIMAOFF",
            "out": "namespace::types::EnumTest::ClimaOff"
        },
        {
            "item": "ClimaHeatgToHvacAndHvBatt",
            "in": "ENUMTEST_CLIMAHEATGTOHVACANDHVBATT",
            "out": "namespace::types::EnumTest::ClimaHeatgToHvacAndHvBatt"
        },
        {
            "item": "ClimaHeatgToHvBatt",
            "in": "ENUMTEST_CLIMAHEATGTOHVBATT",
            "out": "namespace::types::EnumTest::ClimaHeatgToHvBatt"
        },
        {
            "item": "ClimaHeatgToHvac",
            "in": "ENUMTEST_CLIMAHEATGTOHVAC",
            "out": "namespace::types::EnumTest::ClimaHeatgToHvac"
        },
        {
            "item": "ClimaFlow",
            "in": "ENUMTEST_CLIMAFLOW",
            "out": "namespace::types::EnumTest::ClimaFlow"
        },
        {
            "item": "Degas",
            "in": "ENUMTEST_DEGAS",
            "out": "namespace::types::EnumTest::Degas"
        },
        {
            "item": "FailSafe",
            "in": "ENUMTEST_FAILSAFE",
            "out": "namespace::types::EnumTest::FailSafe"
        },
        {
            "default": "ClimaOff",
            "in": "ENUMTEST_CLIMAOFF",
            "out": "namespace::types::EnumTest::ClimaOff"
        }
    ]
}
INTERFACE_UNIT_CFG = {
    "VcTestModel": {
        "version": "0.2.1",
        "includes": [],
        "integrity_level": "QM",
        "outports": {},
        "inports": {
            "sVcTestModel_Enm_EnumTest": {
                "handle": "Path/To/Block",
                "name": "sVcTestModel_Enm_TestEnum",
                "configs": "((ALWAYS_ACTIVE))",
                "description": "Some description.",
                "type": "EnumTest",
                "unit": "-,$EnumTest",
                "offset": 0,
                "lsb": 1,
                "min": "-",
                "max": "-",
                "class": "CVC_EXT",
                "width": 1,
                "default": "ClimaOff"
            },
            "sVcTestModel_Enm_EnumTestTwo": {
                "handle": "Path/To/Block",
                "name": "sVcTestModel_Enm_EnumTestTwo",
                "configs": "((ALWAYS_ACTIVE))",
                "description": "Some description.",
                "type": "EnumTestTwo",
                "unit": "-,$EnumTestTwo",
                "offset": 0,
                "lsb": 1,
                "min": "-",
                "max": "-",
                "class": "CVC_EXT",
                "width": 1,
                "default": "ClimaOff"
            },
            "sVcTestModel_Enm_EnumTestThree": {
                "handle": "Path/To/Block",
                "name": "sVcTestModel_Enm_EnumTestThree",
                "configs": "((ALWAYS_ACTIVE))",
                "description": "Some description.",
                "type": "EnumTestThree",
                "unit": "-,$EnumTestThree",
                "offset": 0,
                "lsb": 1,
                "min": "-",
                "max": "-",
                "class": "CVC_EXT",
                "width": 1,
                "default": "ClimaOff"
            }
        },
        "core": {
            "Events": {},
            "IUMPR": {},
            "FIDs": {},
            "Ranking": {},
            "TstId": {}
        },
        "dids": {},
        "nvm": {},
        "pre_procs": [],
        "local_vars": {},
        "calib_consts": {}
    },
    "VcTestModel3": {
        "version": "0.2.1",
        "includes": [],
        "integrity_level": "QM",
        "outports": {},
        "inports": {
            "sVcTestModel3_Enm_TestEnum": {
                "handle": "Path/To/Block",
                "name": "sVcTestModel3_Enm_TestEnum",
                "configs": "((ALWAYS_ACTIVE))",
                "description": "Some description.",
                "type": "EnumTest",
                "unit": "-,$EnumTest",
                "offset": 0,
                "lsb": 1,
                "min": "-",
                "max": "-",
                "class": "CVC_EXT",
                "width": 1,
                "default": "ClimaOff"
            }
        },
        "core": {
            "Events": {},
            "IUMPR": {},
            "FIDs": {},
            "Ranking": {},
            "TstId": {}
        },
        "dids": {},
        "nvm": {},
        "pre_procs": [],
        "local_vars": {},
        "calib_consts": {}
    }
}


class TestUserDefinedTypes(unittest.TestCase):
    """Test case for testing the UserDefinedTypes class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        self.build_cfg.get_enum_def_dir = MagicMock(return_value='.')
        self.build_cfg.get_root_dir = MagicMock(return_value='.')
        self.unit_cfg = MagicMock(spec_set=UnitConfigs)
        self.unit_cfg.get_unit_code_generator.return_value = 'target_link'
        UserDefinedTypes.clear_log()

    def test_init(self):
        """Test normal class initialization.

        NOTE: It is okay for two units to define the same enums/structs, as long as they are consistent.
        """
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={
                'VcTestModel': str(Path(REF_DIR, 'SS1', 'test_model')),
                'VcTestModel1': str(Path(REF_DIR, 'SS1', 'test_model1'))
            }
        )
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        expected_enums = {
            'VcTestModel': {
                'EnumTest': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTEST_CLIMAOFF': 0,
                        'ENUMTEST_CLIMAHEATGTOHVACANDHVBATT': 1,
                        'ENUMTEST_CLIMAHEATGTOHVBATT': 2,
                        'ENUMTEST_CLIMAHEATGTOHVAC': 3,
                        'ENUMTEST_CLIMAFLOW': 4,
                        'ENUMTEST_DEGAS': 5,
                        'ENUMTEST_FAILSAFE': 6
                    },
                    'default_value': None
                },
                'EnumTestTwo': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTESTTWO_COOLGREQ': 0,
                        'ENUMTESTTWO_HEATGREQ': 1
                    },
                    'default_value': None
                },
                'EnumTestThree': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTESTTHREE_DTELECCOOLG': 0,
                        'ENUMTESTTHREE_DTELECPASCOOLG': 1,
                        'ENUMTESTTHREE_DTELECHEATG': 2,
                        'ENUMTESTTHREE_DTELECPASHEATG': 3,
                        'ENUMTESTTHREE_DTELECACTVHEATG': 4,
                        'ENUMTESTTHREE_DTELECPASACTVHEATG': 5,
                        'ENUMTESTTHREE_DTELECPAS': 6,
                        'ENUMTESTTHREE_DEGAS': 7,
                        'ENUMTESTTHREE_FAILSAFE': 8
                    },
                    'default_value': None
                }
            },
            'VcTestModel1': {
                'EnumTest': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTEST_CLIMAOFF': 0,
                        'ENUMTEST_CLIMAHEATGTOHVACANDHVBATT': 1,
                        'ENUMTEST_CLIMAHEATGTOHVBATT': 2,
                        'ENUMTEST_CLIMAHEATGTOHVAC': 3,
                        'ENUMTEST_CLIMAFLOW': 4,
                        'ENUMTEST_DEGAS': 5,
                        'ENUMTEST_FAILSAFE': 6
                    },
                    'default_value': None
                },
                'EnumTestTwo': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTESTTWO_COOLGREQ': 0,
                        'ENUMTESTTWO_HEATGREQ': 1
                    },
                    'default_value': None
                }
            }
        }
        expected__struct_members = {
            'sVcTestModel_D_One': 'Float32',
            'yVcTestModel_B_One': 'Bool'
        }
        expected_structs = {
            'VcTestModel': {
                'sVcTestModel_Bus_Dummy': {
                    'members': expected__struct_members
                }
            },
            'VcTestModel1': {
                'sVcTestModel_Bus_Dummy': {
                    'members': expected__struct_members
                }
            }
        }
        self.assertDictEqual(expected_structs, udt.structs_per_unit)
        self.assertDictEqual(expected_enums, udt.enums_per_unit)
        self.assertDictEqual({'critical': 0, 'warning': 6}, udt.get_nbr_problems())

    def test_init_interface_enums(self):
        """Test initialization with interface enumerations."""
        self.build_cfg.get_root_dir = MagicMock(return_value=CFG_DIR.resolve())
        self.unit_cfg.get_per_unit_cfg = MagicMock(return_value=INTERFACE_UNIT_CFG)

        # Enum EnumTest not defined in project
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        self.assertDictEqual({'critical': 1, 'warning': 0}, udt.get_nbr_problems())
        result = udt.get_interface_data_types()
        self.assertDictEqual({'enums': {}}, result)
        udt.clear_log()

        # Enum is defined in project
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={
                'VcTestModel': str(Path(REF_DIR, 'SS1', 'test_model'))
            }
        )
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        self.assertDictEqual({'critical': 0, 'warning': 0}, udt.get_nbr_problems())
        result = udt.get_interface_data_types()
        self.assertDictEqual({'enums': INTERFACE_ENUM}, result)
        udt.clear_log()

        # Enum is wrong in interface, number of members differ
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={
                'VcTestModel3': str(Path(REF_DIR, 'SS1', 'test_model3'))
            }
        )
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        self.assertDictEqual({'critical': 1, 'warning': 0}, udt.get_nbr_problems())
        result = udt.get_interface_data_types()
        self.assertDictEqual({'enums': {}}, result)
        udt.clear_log()

    def test_init_multiply_defined_in_unit(self):
        """Test initialization when a unit defines the same enum/struct twice, inconsistently.

        NOTE: Multiply defined enums/structs are ignored, old is NOT overwritten.
        """
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={
                'VcTestModel2': str(Path(REF_DIR, 'SS1', 'test_model2'))
            }
        )
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        expected_structs = {
            'VcTestModel2': {
                'sVcTestModel2_Bus_Dummy': {
                    'members': {
                        'sVcTestModel2_D_One': 'Float32',
                        'yVcTestModel2_B_One': 'Bool'
                    }
                },
                'sVcTestModel_Bus_Dummy': {
                    'members': {
                        'sVcTestModel_D_One': 'Float32',
                        'yVcTestModel_B_One': 'UInt8'
                    }
                }
            }
        }
        expected_enums = {
            'VcTestModel2': {
                'EnumTest': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTEST_CLIMAOFF': 0,
                        'ENUMTEST_CLIMAHEATGTOHVACANDHVBATT': 1,
                        'ENUMTEST_CLIMAHEATGTOHVBATT': 2,
                        'ENUMTEST_CLIMAHEATGTOHVAC': 3,
                        'ENUMTEST_CLIMAFLOW': 4,
                        'ENUMTEST_DEGAS': 5,
                        'ENUMTEST_FAILSAFE': 6
                    },
                    'default_value': None
                },
                'EnumTestThree': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTESTTHREE_DTELECCOOLG': 0,
                        'ENUMTESTTHREE_DTELECPASCOOLG': 1,
                        'ENUMTESTTHREE_DTELECHEATG': 2,
                        'ENUMTESTTHREE_DTELECPASHEATG': 3,
                        'ENUMTESTTHREE_DTELECACTVHEATG': 4,
                        'ENUMTESTTHREE_DTELECPASACTVHEATG': 5,
                        'ENUMTESTTHREE_DTELECPAS': 6,
                        'ENUMTESTTHREE_DEGAS': 7,
                        'ENUMTESTTHREE_FAILSAFE': 8,
                        'ENUMTESTTHREE_EXTRAVERSUSUNITONE': 9
                    },
                    'default_value': None
                }
            }
        }
        self.assertDictEqual(expected_enums, udt.enums_per_unit)
        self.assertDictEqual(expected_structs, udt.structs_per_unit)
        self.assertDictEqual({'critical': 2, 'warning': 4}, udt.get_nbr_problems())

    def test_init_multiply_defined_in_project(self):
        """Test initialization where two units define the same enumeration/struct differently.

        NOTE: Multiply defined enums/structs are ignored, old is NOT overwritten.
        """
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={
                'VcTestModel': str(Path(REF_DIR, 'SS1', 'test_model')),
                'VcTestModel2': str(Path(REF_DIR, 'SS1', 'test_model2'))
            }
        )
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        expected_enums = {
            'VcTestModel': {
                'EnumTest': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTEST_CLIMAOFF': 0,
                        'ENUMTEST_CLIMAHEATGTOHVACANDHVBATT': 1,
                        'ENUMTEST_CLIMAHEATGTOHVBATT': 2,
                        'ENUMTEST_CLIMAHEATGTOHVAC': 3,
                        'ENUMTEST_CLIMAFLOW': 4,
                        'ENUMTEST_DEGAS': 5,
                        'ENUMTEST_FAILSAFE': 6
                    },
                    'default_value': None
                },
                'EnumTestTwo': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTESTTWO_COOLGREQ': 0,
                        'ENUMTESTTWO_HEATGREQ': 1
                    },
                    'default_value': None
                },
                'EnumTestThree': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTESTTHREE_DTELECCOOLG': 0,
                        'ENUMTESTTHREE_DTELECPASCOOLG': 1,
                        'ENUMTESTTHREE_DTELECHEATG': 2,
                        'ENUMTESTTHREE_DTELECPASHEATG': 3,
                        'ENUMTESTTHREE_DTELECACTVHEATG': 4,
                        'ENUMTESTTHREE_DTELECPASACTVHEATG': 5,
                        'ENUMTESTTHREE_DTELECPAS': 6,
                        'ENUMTESTTHREE_DEGAS': 7,
                        'ENUMTESTTHREE_FAILSAFE': 8
                    },
                    'default_value': None
                }
            },
            'VcTestModel2': {
                'EnumTest': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTEST_CLIMAOFF': 0,
                        'ENUMTEST_CLIMAHEATGTOHVACANDHVBATT': 1,
                        'ENUMTEST_CLIMAHEATGTOHVBATT': 2,
                        'ENUMTEST_CLIMAHEATGTOHVAC': 3,
                        'ENUMTEST_CLIMAFLOW': 4,
                        'ENUMTEST_DEGAS': 5,
                        'ENUMTEST_FAILSAFE': 6
                    },
                    'default_value': None
                },
                'EnumTestThree': {
                    'underlying_data_type': 'UInt8',
                    'members': {
                        'ENUMTESTTHREE_DTELECCOOLG': 0,
                        'ENUMTESTTHREE_DTELECPASCOOLG': 1,
                        'ENUMTESTTHREE_DTELECHEATG': 2,
                        'ENUMTESTTHREE_DTELECPASHEATG': 3,
                        'ENUMTESTTHREE_DTELECACTVHEATG': 4,
                        'ENUMTESTTHREE_DTELECPASACTVHEATG': 5,
                        'ENUMTESTTHREE_DTELECPAS': 6,
                        'ENUMTESTTHREE_DEGAS': 7,
                        'ENUMTESTTHREE_FAILSAFE': 8,
                        'ENUMTESTTHREE_EXTRAVERSUSUNITONE': 9
                    },
                    'default_value': None
                }
            }
        }
        expected_structs = {
            'VcTestModel': {
                'sVcTestModel_Bus_Dummy': {
                    'members': {
                        'sVcTestModel_D_One': 'Float32',
                        'yVcTestModel_B_One': 'Bool'
                    }
                }
            },
            'VcTestModel2': {
                'sVcTestModel2_Bus_Dummy': {
                    'members': {
                        'sVcTestModel2_D_One': 'Float32',
                        'yVcTestModel2_B_One': 'Bool'
                    }
                },
                'sVcTestModel_Bus_Dummy': {
                    'members': {
                        'sVcTestModel_D_One': 'Float32',
                        'yVcTestModel_B_One': 'UInt8'
                    }
                }
            }
        }
        self.assertDictEqual(expected_structs, udt.structs_per_unit)
        self.assertDictEqual(expected_enums, udt.enums_per_unit)
        self.assertDictEqual({'critical': 4, 'warning': 7}, udt.get_nbr_problems())

    def test_calculate_underlying_data_type(self):
        """Test the _calculate_underlying_data_type method.

        NOTE: This method is part of initializing UserDefinedTypes, however, it shall be tested further.
        """
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        udt.clear_log()  # Clear to only count warnings/criticals regarding underlying data types

        # 8 bit integers
        self.unit_cfg.get_unit_code_generator.return_value = 'target_link'
        expected = 'Int8'
        enum_members = [('MIN_VALUE', -1), ('FILLER', 0), ('MAX_VALUE', 1)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 0, 'warning': 0}, udt.get_nbr_problems())

        expected = 'UInt8'
        enum_members = [('MIN_VALUE', 0), ('FILLER', 0), ('MAX_VALUE', 1)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 0, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

        self.unit_cfg.get_unit_code_generator.return_value = 'embedded_coder'
        expected = 'int8_T'
        enum_members = [('MIN_VALUE', -1), ('FILLER', 0), ('MAX_VALUE', 1)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 0, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

        expected = 'uint8_T'
        enum_members = [('MIN_VALUE', 0), ('FILLER', 0), ('MAX_VALUE', 1)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 0, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

        # 16 bit integers
        self.unit_cfg.get_unit_code_generator.return_value = 'target_link'
        expected = 'Int16'
        enum_members = [('MIN_VALUE', -200), ('FILLER', 0), ('MAX_VALUE', 1)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 0, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

        expected = 'UInt16'
        enum_members = [('MIN_VALUE', 0), ('FILLER', 0), ('MAX_VALUE', 256)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 0, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

        self.unit_cfg.get_unit_code_generator.return_value = 'embedded_coder'
        expected = 'int16_T'
        enum_members = [('MIN_VALUE', -200), ('FILLER', 0), ('MAX_VALUE', 1)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 0, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

        expected = 'uint16_T'
        enum_members = [('MIN_VALUE', 0), ('FILLER', 0), ('MAX_VALUE', 256)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 0, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

        # Invalid sizes
        self.unit_cfg.get_unit_code_generator.return_value = 'target_link'
        expected = None
        enum_members = [('MIN_VALUE', -32769), ('FILLER', 0), ('MAX_VALUE', 1)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 1, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

        expected = None
        enum_members = [('MIN_VALUE', -32768), ('FILLER', 0), ('MAX_VALUE', 32768)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 1, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

        self.unit_cfg.get_unit_code_generator.return_value = 'embedded_coder'
        expected = None
        enum_members = [('MIN_VALUE', -200), ('FILLER', 0), ('MAX_VALUE', 32768)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 1, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

        expected = None
        enum_members = [('MIN_VALUE', 0), ('FILLER', 0), ('MAX_VALUE', 65536)]
        underlying_data_type = udt._calculate_underlying_data_type('dummy_unit', 'dummy_enum_name', enum_members)
        self.assertEqual(expected, underlying_data_type)
        self.assertDictEqual({'critical': 1, 'warning': 0}, udt.get_nbr_problems())
        udt.clear_log()

    def test_generate_enum_header_file_tl(self):
        """Test the _generate_target_link_enum_header_file method.

        NOTE: This method is part of UserDefinedTypes.generate_common_header_files, which is not tested on its own.
        """
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={'VcTestModel2': str(Path(REF_DIR, 'SS1', 'test_model2'))}
        )
        unit_cfg = self.unit_cfg
        type(unit_cfg).base_types_headers = '#include "tl_basetypes.h"\n'
        udt = UserDefinedTypes(self.build_cfg, unit_cfg)

        result = []
        m_open = mock_open()
        m_open.return_value.write = result.append
        with patch.object(Path, 'open', m_open, create=True):
            udt._generate_enum_header_file(Path("VcEnumerations.h"))

        expected = [
            '#ifndef VCENUMERATIONS_H\n',
            '#define VCENUMERATIONS_H\n',
            '#include "tl_basetypes.h"\n',
            '/* VCC Enumerations */\n',
            '\n',
            'typedef enum EnumTest_tag {\n',
            "   ENUMTEST_CLIMAOFF = 0, \n",
            "   ENUMTEST_CLIMAHEATGTOHVACANDHVBATT = 1, \n",
            "   ENUMTEST_CLIMAHEATGTOHVBATT = 2, \n",
            "   ENUMTEST_CLIMAHEATGTOHVAC = 3, \n",
            "   ENUMTEST_CLIMAFLOW = 4, \n",
            "   ENUMTEST_DEGAS = 5, \n",
            "   ENUMTEST_FAILSAFE = 6 \n",
            '} EnumTest;\n',
            '\n',
            'typedef enum EnumTestThree_tag {\n',
            "   ENUMTESTTHREE_DTELECCOOLG = 0, \n",
            "   ENUMTESTTHREE_DTELECPASCOOLG = 1, \n",
            "   ENUMTESTTHREE_DTELECHEATG = 2, \n",
            "   ENUMTESTTHREE_DTELECPASHEATG = 3, \n",
            "   ENUMTESTTHREE_DTELECACTVHEATG = 4, \n",
            "   ENUMTESTTHREE_DTELECPASACTVHEATG = 5, \n",
            "   ENUMTESTTHREE_DTELECPAS = 6, \n",
            "   ENUMTESTTHREE_DEGAS = 7, \n",
            "   ENUMTESTTHREE_FAILSAFE = 8, \n",
            "   ENUMTESTTHREE_EXTRAVERSUSUNITONE = 9 \n",
            '} EnumTestThree;\n',
            '#endif /* VCENUMERATIONS_H */\n'
        ]

        self.assertEqual("".join(result), "".join(expected))

    def test_generate_enum_header_file_ec(self):
        """Test the _generate_target_link_enum_header_file method.

        NOTE: This method is part of UserDefinedTypes.generate_common_header_files, which is not tested on its own.
        """
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={'VcTestModel2': str(Path(REF_DIR, 'SS1', 'test_model2'))}
        )
        unit_cfg = self.unit_cfg
        type(unit_cfg).base_types_headers = '#include "rtwtypes.h"\n'
        udt = UserDefinedTypes(self.build_cfg, unit_cfg)

        result = []
        m_open = mock_open()
        m_open.return_value.write = result.append
        with patch.object(Path, 'open', m_open, create=True):
            udt._generate_enum_header_file(Path("VcEnumerations.h"))

        expected = [
            '#ifndef VCENUMERATIONS_H\n',
            '#define VCENUMERATIONS_H\n',
            '#include "rtwtypes.h"\n',
            '/* VCC Enumerations */\n',
            '\n',
            'typedef enum EnumTest_tag {\n',
            "   ENUMTEST_CLIMAOFF = 0, \n",
            "   ENUMTEST_CLIMAHEATGTOHVACANDHVBATT = 1, \n",
            "   ENUMTEST_CLIMAHEATGTOHVBATT = 2, \n",
            "   ENUMTEST_CLIMAHEATGTOHVAC = 3, \n",
            "   ENUMTEST_CLIMAFLOW = 4, \n",
            "   ENUMTEST_DEGAS = 5, \n",
            "   ENUMTEST_FAILSAFE = 6 \n",
            '} EnumTest;\n',
            '\n',
            'typedef enum EnumTestThree_tag {\n',
            "   ENUMTESTTHREE_DTELECCOOLG = 0, \n",
            "   ENUMTESTTHREE_DTELECPASCOOLG = 1, \n",
            "   ENUMTESTTHREE_DTELECHEATG = 2, \n",
            "   ENUMTESTTHREE_DTELECPASHEATG = 3, \n",
            "   ENUMTESTTHREE_DTELECACTVHEATG = 4, \n",
            "   ENUMTESTTHREE_DTELECPASACTVHEATG = 5, \n",
            "   ENUMTESTTHREE_DTELECPAS = 6, \n",
            "   ENUMTESTTHREE_DEGAS = 7, \n",
            "   ENUMTESTTHREE_FAILSAFE = 8, \n",
            "   ENUMTESTTHREE_EXTRAVERSUSUNITONE = 9 \n",
            '} EnumTestThree;\n',
            '#endif /* VCENUMERATIONS_H */\n'
        ]
        self.assertEqual("".join(result), "".join(expected))

    def test_generate_enum_header_file_mixed(self):
        """Test the _generate_target_link_enum_header_file method.

        NOTE: This method is part of UserDefinedTypes.generate_common_header_files, which is not tested on its own.
        """
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={'VcTestModel2': str(Path(REF_DIR, 'SS1', 'test_model2'))}
        )
        unit_cfg = self.unit_cfg
        type(unit_cfg).base_types_headers = '#include "rtwtypes.h"\n#include "tl_basetypes.h"\n'
        udt = UserDefinedTypes(self.build_cfg, unit_cfg)

        result = []
        m_open = mock_open()
        m_open.return_value.write = result.append
        with patch.object(Path, 'open', m_open, create=True):
            udt._generate_enum_header_file(Path("VcEnumerations.h"))

        expected = [
            '#ifndef VCENUMERATIONS_H\n',
            '#define VCENUMERATIONS_H\n',
            '#include "rtwtypes.h"\n#include "tl_basetypes.h"\n',
            '/* VCC Enumerations */\n',
            '\n',
            'typedef enum EnumTest_tag {\n',
            "   ENUMTEST_CLIMAOFF = 0, \n",
            "   ENUMTEST_CLIMAHEATGTOHVACANDHVBATT = 1, \n",
            "   ENUMTEST_CLIMAHEATGTOHVBATT = 2, \n",
            "   ENUMTEST_CLIMAHEATGTOHVAC = 3, \n",
            "   ENUMTEST_CLIMAFLOW = 4, \n",
            "   ENUMTEST_DEGAS = 5, \n",
            "   ENUMTEST_FAILSAFE = 6 \n",
            '} EnumTest;\n',
            '\n',
            'typedef enum EnumTestThree_tag {\n',
            "   ENUMTESTTHREE_DTELECCOOLG = 0, \n",
            "   ENUMTESTTHREE_DTELECPASCOOLG = 1, \n",
            "   ENUMTESTTHREE_DTELECHEATG = 2, \n",
            "   ENUMTESTTHREE_DTELECPASHEATG = 3, \n",
            "   ENUMTESTTHREE_DTELECACTVHEATG = 4, \n",
            "   ENUMTESTTHREE_DTELECPASACTVHEATG = 5, \n",
            "   ENUMTESTTHREE_DTELECPAS = 6, \n",
            "   ENUMTESTTHREE_DEGAS = 7, \n",
            "   ENUMTESTTHREE_FAILSAFE = 8, \n",
            "   ENUMTESTTHREE_EXTRAVERSUSUNITONE = 9 \n",
            '} EnumTestThree;\n',
            '#endif /* VCENUMERATIONS_H */\n'
        ]

        self.assertEqual("".join(result), "".join(expected))

    def test_generate_struct_header_file_tl(self):
        """Test the _generate_target_link_struct_header_file method.

        NOTE: This method is part of UserDefinedTypes.generate_common_header_files, which is not tested on its own.
        """
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={'VcTestModel2': str(Path(REF_DIR, 'SS1', 'test_model2'))}
        )
        unit_cfg = self.unit_cfg
        type(unit_cfg).base_types_headers = '#include "tl_basetypes.h"\n'
        udt = UserDefinedTypes(self.build_cfg, unit_cfg)

        result = []
        m_open = mock_open()
        m_open.return_value.write = result.append
        with patch.object(Path, 'open', m_open, create=True):
            udt._generate_struct_header_file(Path("VcStructs.h"))

        expected = [
            '#ifndef VCSTRUCTS_H\n',
            '#define VCSTRUCTS_H\n',
            '#include "tl_basetypes.h"\n',
            '#include "VcEnumerations.h"\n',
            '/* VCC Structs */\n',
            '\n',
            'struct sVcTestModel2_Bus_Dummy {\n',
            '   Float32 sVcTestModel2_D_One;\n',
            '   Bool yVcTestModel2_B_One;\n',
            '};\n',
            '\n',
            'struct sVcTestModel_Bus_Dummy {\n',
            '   Float32 sVcTestModel_D_One;\n',
            '   UInt8 yVcTestModel_B_One;\n',
            '};\n',
            '#endif /* VCSTRUCTS_H */\n'
        ]

        self.assertEqual("".join(result), "".join(expected))

    def test_get_enumerations(self):
        """Test the get_enumerations method."""
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={
                'VcTestModel': str(Path(REF_DIR, 'SS1', 'test_model')),
                'VcTestModel2': str(Path(REF_DIR, 'SS1', 'test_model2'))
            }
        )
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        expected = {
            'EnumTest': {
                'underlying_data_type': 'UInt8',
                'members': {
                    'ENUMTEST_CLIMAOFF': 0,
                    'ENUMTEST_CLIMAHEATGTOHVACANDHVBATT': 1,
                    'ENUMTEST_CLIMAHEATGTOHVBATT': 2,
                    'ENUMTEST_CLIMAHEATGTOHVAC': 3,
                    'ENUMTEST_CLIMAFLOW': 4,
                    'ENUMTEST_DEGAS': 5,
                    'ENUMTEST_FAILSAFE': 6
                },
                'default_value': None,
                'units': ['VcTestModel', 'VcTestModel2']
            },
            'EnumTestTwo': {
                'underlying_data_type': 'UInt8',
                'members': {
                    'ENUMTESTTWO_COOLGREQ': 0,
                    'ENUMTESTTWO_HEATGREQ': 1
                },
                'default_value': None,
                'units': ['VcTestModel']
            },
            'EnumTestThree': {
                'underlying_data_type': 'UInt8',
                'members': {
                    'ENUMTESTTHREE_DTELECCOOLG': 0,
                    'ENUMTESTTHREE_DTELECPASCOOLG': 1,
                    'ENUMTESTTHREE_DTELECHEATG': 2,
                    'ENUMTESTTHREE_DTELECPASHEATG': 3,
                    'ENUMTESTTHREE_DTELECACTVHEATG': 4,
                    'ENUMTESTTHREE_DTELECPASACTVHEATG': 5,
                    'ENUMTESTTHREE_DTELECPAS': 6,
                    'ENUMTESTTHREE_DEGAS': 7,
                    'ENUMTESTTHREE_FAILSAFE': 8
                },
                'default_value': None,
                'units': ['VcTestModel', 'VcTestModel2']
            }
        }
        self.assertDictEqual(expected, udt.get_enumerations())
        self.assertDictEqual({'critical': 4, 'warning': 7}, udt.get_nbr_problems())

    def test_get_structs(self):
        """Test the get_structs method."""
        self.build_cfg.get_unit_src_dirs = MagicMock(
            return_value={
                'VcTestModel': str(Path(REF_DIR, 'SS1', 'test_model')),
                'VcTestModel2': str(Path(REF_DIR, 'SS1', 'test_model2'))
            }
        )
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        expected = {
            'sVcTestModel_Bus_Dummy': {
                'members': {
                    'sVcTestModel_D_One': 'Float32',
                    'yVcTestModel_B_One': 'Bool'
                },
                'units': ['VcTestModel', 'VcTestModel2']
            },
            'sVcTestModel2_Bus_Dummy': {
                'members': {
                    'sVcTestModel2_D_One': 'Float32',
                    'yVcTestModel2_B_One': 'Bool'
                },
                'units': ['VcTestModel2']
            }
        }
        self.assertDictEqual(expected, udt.get_structs())
        self.assertDictEqual({'critical': 4, 'warning': 7}, udt.get_nbr_problems())

    def test_get_default_enum_value(self):
        """Test the get_default_enum_value method."""
        unit = 'VcTestModel'
        unit_cfg = {
            "VcTestModel": {
                "version": "0.2.1",
                "includes": [],
                "integrity_level": "QM",
                "outports": {},
                "inports": {
                    "sVcTestModel_Enm_TestEnum": {
                        "handle": "Path/To/Block",
                        "name": "sVcTestModel_Enm_TestEnum",
                        "configs": "((ALWAYS_ACTIVE))",
                        "description": "Some description.",
                        "type": "SimulinkEnum",
                        "unit": "-,$SimulinkEnum",
                        "offset": 0,
                        "lsb": 1,
                        "min": "-",
                        "max": "-",
                        "class": "CVC_EXT",
                        "width": 1,
                        "default": "One"
                    }
                },
                "core": {
                    "Events": {},
                    "IUMPR": {},
                    "FIDs": {},
                    "Ranking": {},
                    "TstId": {}
                },
                "dids": {},
                "nvm": {},
                "pre_procs": [],
                "local_vars": {},
                "calib_consts": {}
            }
        }
        self.unit_cfg.get_per_unit_cfg = MagicMock(return_value=unit_cfg)
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)

        result = udt.get_default_enum_value(unit, 'SimulinkEnum')
        expected = 'SIMULINKENUM_ONE'
        self.assertEqual(expected, result)
        # interface_data_types.yml "not found"
        self.assertDictEqual({'critical': 0, 'warning': 1}, udt.get_nbr_problems())

        result = udt.get_default_enum_value(unit, 'SimulinkEnumTwo')
        self.assertIsNone(result)
        # interface_data_types.yml "not found" and real warnings (not in config and no m-file)
        self.assertDictEqual({'critical': 0, 'warning': 3}, udt.get_nbr_problems())

    def test_convert_interface_enum_to_simulink(self):
        """Test the convert_interface_enum_to_simulink method."""
        udt = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        expected = {
            'underlying_data_type': None,
            'members': {
                'ENUMTEST_CLIMAOFF': 0,
                'ENUMTEST_CLIMAHEATGTOHVACANDHVBATT': 1,
                'ENUMTEST_CLIMAHEATGTOHVBATT': 2,
                'ENUMTEST_CLIMAHEATGTOHVAC': 3,
                'ENUMTEST_CLIMAFLOW': 4,
                'ENUMTEST_DEGAS': 5,
                'ENUMTEST_FAILSAFE': 6
            },
            'default_value': 'ENUMTEST_CLIMAOFF'
        }
        result = udt.convert_interface_enum_to_simulink(INTERFACE_ENUM['EnumTest'])
        self.assertDictEqual(expected, result)
