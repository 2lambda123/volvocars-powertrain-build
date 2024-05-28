# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for Core class."""
import unittest
from unittest.mock import MagicMock
from pathlib import Path
from pybuild.build_proj_config import BuildProjConfig
from pybuild.unit_configs import UnitConfigs
from pybuild.core import Core, HICore

from .core_cnfg import CORE_CFG


def get_core_ids_proj(conf):
    """Function returning a fake core config."""
    return CORE_CFG[conf]


class TestCore(unittest.TestCase):
    """Test case for testing the FeatureConfigs class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        prj_cnf_dir = str(Path(Path(__file__).parent, 'cnfg_files'))
        self.build_cfg.get_prj_cfg_dir = MagicMock(return_value=prj_cnf_dir)
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        self.unit_cfg = MagicMock(spec_set=UnitConfigs)
        self.unit_cfg.get_per_cfg_unit_cfg = MagicMock(return_value={'core': {'VcEvAmbPCompPlausMon': {'unit': {}}}})
        self.unit_cfg.check_if_in_per_cfg_unit_cfg = MagicMock(return_value=True)

    def test_get_current_core_cfg(self):
        """Check return core cfg."""
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG')
        core = Core(self.build_cfg, self.unit_cfg)
        result = core.get_current_core_config()
        self.assertEqual(result, {})

    def test_get_current_core_cfg1(self):
        """Check return core cfg."""
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        core = Core(self.build_cfg, self.unit_cfg)
        result = core.get_current_core_config()
        self.assertEqual(result, CORE_CFG['CFG1'])

    def test_get_current_core_cfg1_no_warnings(self):
        """Check for warnings or errors. Should be none."""
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        Core.clear_log()
        core = Core(self.build_cfg, self.unit_cfg)
        core.get_current_core_config()
        self.assertEqual(Core.get_nbr_problems(), {'critical': 0, 'warning': 0})

    def test_get_current_core_cfg2(self):
        """Check return core cfg."""
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG2')
        core = Core(self.build_cfg, self.unit_cfg)
        result = core.get_current_core_config()
        self.assertEqual(result, CORE_CFG['CFG2'])

    def test_get_current_core_cfg11(self):
        """Check return core cfg."""
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG11')
        core = Core(self.build_cfg, self.unit_cfg)
        result = core.get_current_core_config()
        self.assertEqual(result, {})

    def test_get_current_core_cfg_empty(self):
        """Check return core cfg."""
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG11')
        self.unit_cfg.get_per_cfg_unit_cfg = MagicMock(return_value={})
        core = Core(self.build_cfg, self.unit_cfg)
        result = core.get_current_core_config()
        self.assertEqual(result, {})


class TestHICore(unittest.TestCase):
    """Test case for testing class HICore."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        project_config = MagicMock()
        project_config.get_a2l_cfg.return_value = {'name': 'DUMMY'}
        project_config.get_prj_cfg_dir.return_value = 'dummy'
        unit_configs = MagicMock()
        unit_configs.get_per_unit_cfg.return_value = {}

        self.dummy_yaml_dtcs = {
            'VcEventOne': 0x123ABC,
            'VcEventTwo': 0xABC123,
            'VcEventThree': 0xFFFFFF
        }
        self.hi_core = HICore(project_config, unit_configs)
        self.hi_core._get_project_dtcs = MagicMock(return_value={'VcEventOne', 'VcEventTwo', 'VcEventThree'})
        self.hi_core._read_dtc_yaml_file = MagicMock(return_value=self.dummy_yaml_dtcs)

    def test_get_diagnostic_trouble_codes(self):
        """Test the get_diagnostic_trouble_codes function."""
        result = self.hi_core.get_diagnostic_trouble_codes()
        self.assertEqual(result, self.dummy_yaml_dtcs)

    def test_get_diagnostic_trouble_codes_missing_in_project(self):
        """Test the get_diagnostic_trouble_codes function, when a DTC is in yaml but not project."""
        self.hi_core._get_project_dtcs.return_value = {'VcEventOne', 'VcEventTwo'}
        result = self.hi_core.get_diagnostic_trouble_codes()
        expected = {
            'VcEventOne': 0x123ABC,
            'VcEventTwo': 0xABC123
        }
        self.assertEqual(result, expected)

    def test_get_diagnostic_trouble_codes_missing_in_yaml(self):
        """Test the get_diagnostic_trouble_codes function, when a DTC is in project but not in yaml."""
        self.hi_core._read_dtc_yaml_file.return_value = {
            'VcEventOne': 0x123ABC,
            'VcEventTwo': 0xABC123
        }
        result = self.hi_core.get_diagnostic_trouble_codes()
        expected = {
            'VcEventOne': 0x123ABC,
            'VcEventTwo': 0xABC123
        }
        self.assertEqual(result, expected)

    def test_get_header_content(self):
        """Test get_header_content."""
        self.hi_core.diagnostic_trouble_codes = self.dummy_yaml_dtcs
        result = self.hi_core.get_header_content()
        expected = [
            '#ifndef VCCORESUPPLIERABSTRACTION_H\n',
            '#define VCCORESUPPLIERABSTRACTION_H\n',
            '\n',
            '/* Core API Supplier Abstraction */\n',
            '\n',
            '#include "tl_basetypes.h"\n',
            '#include "Rte_DUMMY.h"\n',
            '\n',
            '/* enum EventStatus {passed=0, failed=1, prepassed=2, prefailed=3} */\n',
            '#define Dem_SetEventStatus(EventName, EventStatus)',
            '  ',
            'VcCoreSupplierAbstraction_##EventName##_SetEventStatus(EventStatus)\n',
            '\n#include "PREDECL_CODE_ASIL_D_START.h"\n',
            'UInt8 VcCoreSupplierAbstraction_VcEventOne_SetEventStatus(UInt8 EventStatus);\n',
            'UInt8 VcCoreSupplierAbstraction_VcEventTwo_SetEventStatus(UInt8 EventStatus);\n',
            'UInt8 VcCoreSupplierAbstraction_VcEventThree_SetEventStatus(UInt8 EventStatus);\n',
            '#include "PREDECL_CODE_ASIL_D_END.h"\n',
            '\n#endif /* VCCORESUPPLIERABSTRACTION_H */\n'
        ]
        self.assertListEqual(expected, result)

    def test_get_header_content_no_dtcs(self):
        """Test get_header_content without DTCs."""
        self.hi_core.did_dict = {}
        result = self.hi_core.get_header_content()
        expected = [
            '#ifndef VCCORESUPPLIERABSTRACTION_H\n',
            '#define VCCORESUPPLIERABSTRACTION_H\n',
            '\n',
            '/* Core API Supplier Abstraction */\n',
            '\n',
            '#include "tl_basetypes.h"\n',
            '#include "Rte_DUMMY.h"\n',
            '\n',
            '\n#endif /* VCCORESUPPLIERABSTRACTION_H */\n'
        ]
        self.assertListEqual(expected, result)

    def test_get_source_content(self):
        """Test get_source_content."""
        self.maxDiff = None
        self.hi_core.diagnostic_trouble_codes = self.dummy_yaml_dtcs
        result = self.hi_core.get_source_content()
        expected = [
            '#include "VcCoreSupplierAbstraction.h"\n',
            '\n',
            '#include "CVC_CODE_ASIL_D_START.h"\n',
            'UInt8 VcCoreSupplierAbstraction_VcEventOne_SetEventStatus(UInt8 EventStatus)\n',
            '{\n',
            '    Rte_Call_Event_DTC_0x123ABC_SetEventStatus(EventStatus);\n',
            '    return 0;\n',
            '}\n',
            '\n',
            'UInt8 VcCoreSupplierAbstraction_VcEventTwo_SetEventStatus(UInt8 EventStatus)\n',
            '{\n',
            '    Rte_Call_Event_DTC_0xABC123_SetEventStatus(EventStatus);\n',
            '    return 0;\n',
            '}\n',
            '\n',
            'UInt8 VcCoreSupplierAbstraction_VcEventThree_SetEventStatus(UInt8 EventStatus)\n',
            '{\n',
            '    Rte_Call_Event_DTC_0xFFFFFF_SetEventStatus(EventStatus);\n',
            '    return 0;\n',
            '}\n',
            '\n',
            '#include "CVC_CODE_ASIL_D_END.h"\n'
        ]
        self.assertListEqual(expected, result)

    def test_get_source_file_content_no_dtcs(self):
        """Test get_source_content without DTCs."""
        self.hi_core.did_dict = {}
        result = self.hi_core.get_source_content()
        expected = [
            '#include "VcCoreSupplierAbstraction.h"\n',
            '\n'
        ]
        self.assertListEqual(expected, result)
