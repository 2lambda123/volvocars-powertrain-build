# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for FeatureConfigs."""
import re
import unittest
from unittest.mock import MagicMock
from pathlib import Path
from powertrain_build.build_proj_config import BuildProjConfig
from powertrain_build.feature_configs import FeatureConfigs
from .sw_cnfg import SW_FILE_DICT

SRC_DIR = Path(__file__).parent


class TestFeatureConfigs(unittest.TestCase):
    """Test case for testing the FeatureConfigs class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        prj_cnf_dir = Path(SRC_DIR, 'cnfg_files')
        self.build_cfg.get_prj_cfg_dir = MagicMock(return_value=str(prj_cnf_dir))
        self.build_cfg.get_did_cfg_file_name = MagicMock(return_value='DIDIds_FullRange')
        self.build_cfg.get_prj_config = MagicMock(return_value='VED4_GENIII')
        self.build_cfg.get_unit_src_dirs = MagicMock(return_value={'mocked': str(Path(prj_cnf_dir, 'unit_cfgs'))})
        self.build_cfg.get_local_defs_name = MagicMock(return_value='*_LocalDefs.h')
        self.build_cfg.get_codeswitches_name = MagicMock(return_value='SPM_Codeswitch_Setup*.csv')
        self.build_cfg.get_feature_conf_header_name = MagicMock(return_value='VcCodeSwDefines.h')

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
        """Test that the c-header file is correctly generated for VED4_GENIII
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='VED4_GENIII')
        f_cfg = FeatureConfigs(self.build_cfg)
        res_dict = self.check_header_file(f_cfg)
        self.assertEqual(res_dict, SW_FILE_DICT['VED4_GENIII'])

    def test_gen_unit_cfg_header_file_cfg2(self):
        """Test that the c-header file is correctly generated for VEP4_GENIII
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='VEP4_GENIII')
        f_cfg = FeatureConfigs(self.build_cfg)
        res_dict = self.check_header_file(f_cfg)
        self.maxDiff = None
        self.assertDictEqual(res_dict, SW_FILE_DICT['VEP4_GENIII'])

    def test_check_if_active_in_config_cfg1(self):
        """Check active in VED4_GENIII
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='VED4_GENIII')
        f_cfg = FeatureConfigs(self.build_cfg)
        config_def = [['Vc_Aes_B_CodeGenGsl == 1']]
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, False)
        config_def = ['Vc_Aes_B_CodeGenGsl']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, False)
        config_def = ['Vc_Pvc_Hw_B_Petrol']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, False)
        config_def = ['Vc_Pvc_Hw_B_Diesel']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)
        config_def = ['VcDeDa_111_EcoIndcn_1']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)
        config_def = ['VcDeDa_112_PwrIndcn_2']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)

    def test_check_if_active_in_config_cfg2(self):
        """Check active in VEP4_GENIII
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='VEP4_GENIII')
        f_cfg = FeatureConfigs(self.build_cfg)
        config_def = 'Vc_Aes_B_CodeGenGsl == 1'
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)
        config_def = ['Vc_Aes_B_CodeGenGsl']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)
        result = f_cfg.check_if_active_in_config(['all'])
        self.assertEqual(result, True)
        config_def = ['Vc_Pvc_Hw_B_Petrol']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)
        config_def = ['Vc_Pvc_Hw_B_Diesel']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, False)
        config_def = ('(((Vc_Pvc_Hw_B_Erad==0)&&(Vc_Pvc_Hw_B_Efad==0)&&((Vc_Pvc_Hw_B_VeaGen1==1)||'
                      '(Vc_Pvc_Hw_B_VeaGen2==1)||(Vc_Pvc_Hw_B_VeaGen3==1)||(Vc_Pvc_Hw_B_Gep3Gen1==1))))')
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)
        config_def = 'VcDeDa_111_EcoIndcn_1'
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)
        config_def = ['VcDeDa_112_PwrIndcn_2']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)

    def test_check_if_active_in_config_empty(self):
        """Check empty active config
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='VEP4_GENIII')
        f_cfg = FeatureConfigs(self.build_cfg)
        config_def = []
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, True)

    def test_check_invalid_in_config_cfg1(self):
        """Check active in VED4_GENIII
        """
        self.build_cfg.get_prj_config = MagicMock(return_value='VED4_GENIII')
        f_cfg = FeatureConfigs(self.build_cfg)
        config_def = [['Vc_AcReg_B_Invalid == 1']]
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, False)
        config_def = ['Vc_AcReg_B_Invalid']
        result = f_cfg.check_if_active_in_config(config_def)
        self.assertEqual(result, False)
