# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for FeatureConfigs."""
import re
import unittest

from unittest.mock import MagicMock, patch
from pathlib import Path
from pybuild.build_proj_config import BuildProjConfig
from pybuild.feature_configs import FeatureConfigs
from .sw_cnfg import SW_DICT

SRC_DIR = Path(__file__).parent


def overwrite_read_config(f_cfg, wanted_config):
    """Overwrite the read config function in FeatureConfigs.

    Args:
        f_cfg (FeatureConfigs): The FeatureConfigs object.
        wanted_config (dict): The wanted config.
    """
    f_cfg._set_config(wanted_config)


class TestFeatureConfigs(unittest.TestCase):
    """Test case for testing the FeatureConfigs class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        prj_cnf_dir = str(Path(SRC_DIR, 'cnfg_files'))
        self.build_cfg.get_prj_cfg_dir = MagicMock(return_value=prj_cnf_dir)
        self.build_cfg.get_did_cfg_file_name = MagicMock(return_value='DIDIds_FullRange')
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        patcher_read_config_sw = patch(
            'tests.pybuild.test_feature_configs.FeatureConfigs._parse_all_code_sw_configs',
            MagicMock())
        self.mock_read_config_sw = patcher_read_config_sw.start()
        self.addCleanup(patcher_read_config_sw.stop)

    @staticmethod
    def check_header_file(f_cfg):
        """Helper function for reading config definition c-header file
        """
        header_file = Path(SRC_DIR, 'output', 'cnfg_def.h')
        f_cfg.gen_unit_cfg_header_file(str(header_file))
        res_dict = {}
        with header_file.open(encoding="utf-8") as f_ptr:
            for define in re.finditer(r'#define\s+(\w+)\s+([\w\.]+)', f_ptr.read()):
                res_dict[define.group(1)] = float(define.group(2))
        return res_dict

    def test_gen_unit_cfg_header_file_cfg1(self):
        """Test that the c-header file is correctly generated for CFG1
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        f_cfg = FeatureConfigs(self.build_cfg)
        overwrite_read_config(f_cfg, SW_DICT['CFG1'])
        res_dict = self.check_header_file(f_cfg)
        self.assertEqual(res_dict, SW_DICT['CFG1'])

    def test_gen_unit_cfg_header_file_cfg2(self):
        """Test that the c-header file is correctly generated for CFG2
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG2')
        f_cfg = FeatureConfigs(self.build_cfg)
        overwrite_read_config(f_cfg, SW_DICT['CFG2'])
        res_dict = self.check_header_file(f_cfg)
        self.assertEqual(res_dict, SW_DICT['CFG2'])

    def test_check_if_active_in_config_cfg1(self):
        """Check active in cfg1
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        f_cfg = FeatureConfigs(self.build_cfg)
        overwrite_read_config(f_cfg, SW_DICT['CFG1'])
        config_def = [['Vc_AcReg_B_CodegenPHEV == 1']]
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, False)
        config_def = ['Vc_AcReg_B_CodegenPHEV']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, False)

    def test_check_if_active_in_config_cfg2(self):
        """Check active in cfg1
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG2')
        f_cfg = FeatureConfigs(self.build_cfg)
        overwrite_read_config(f_cfg, SW_DICT['CFG2'])
        config_def = 'Vc_AcReg_B_CodegenPHEV == 1'
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)
        config_def = ['Vc_AcReg_B_CodegenPHEV']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)
        result = f_cfg.check_if_active_in_config(['all'])
        self.assertEqual(result, True)

    def test_get_if_macro_string(self):
        """Test generation if macro string."""
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG2')
        f_cfg = FeatureConfigs(self.build_cfg)
        overwrite_read_config(f_cfg, SW_DICT['CFG2'])
        config_def = [['CS1', 'CS2'], ['CS3']]
        result = f_cfg.get_preprocessor_macro(config_def)
        expected = "#if ( CS1 && CS2 ) || ( CS3 )"
        self.assertEqual(result, expected)

        config_def = [['all']]
        result = f_cfg.get_preprocessor_macro(config_def)
        expected = ""
        self.assertEqual(result, expected)

        config_def = ['all']
        result = f_cfg.get_preprocessor_macro(config_def)
        expected = ""
        self.assertEqual(result, expected)

        config_def = 'all'
        result = f_cfg.get_preprocessor_macro(config_def)
        expected = ""
        self.assertEqual(result, expected)

        config_def = ['CS1', 'CS2']
        f_cfg.clear_log()
        result = f_cfg.get_preprocessor_macro(config_def)
        expected = "#if ( CS1 && CS2 )"
        self.assertEqual(result, expected)

        warnings_count = len(f_cfg.get_problems()['warning'])
        self.assertEqual(warnings_count, 1)

    def test_check_if_active_in_config_empty(self):
        """Check empty active config
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG2')
        f_cfg = FeatureConfigs(self.build_cfg)
        overwrite_read_config(f_cfg, SW_DICT['CFG2'])
        config_def = []
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)

    def test_check_invalid_in_config_cfg1(self):
        """Check active in cfg1
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        f_cfg = FeatureConfigs(self.build_cfg)
        overwrite_read_config(f_cfg, SW_DICT['CFG1'])
        config_def = [['Vc_AcReg_B_Invalid == 1']]
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, False)
        config_def = ['Vc_AcReg_B_Invalid']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, False)
