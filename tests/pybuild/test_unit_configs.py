# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for FeatureConfigs."""
import unittest
from unittest.mock import MagicMock
from pathlib import Path
from copy import deepcopy

from pybuild.unit_configs import UnitConfigs
from pybuild.build_proj_config import BuildProjConfig
from pybuild.feature_configs import FeatureConfigs

CNFG_DIR = Path(Path(__file__).parent, 'cnfg_files')


def check_if_active_in_config(config_def):
    """Check if unit is active."""
    if config_def == ['not_in_config']:
        return False
    return True


class TestUnitConfigs(unittest.TestCase):
    """Test case for testing the UnitConfigs class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.mock_build_cfg = MagicMock(spec_set=BuildProjConfig)
        self.mock_build_cfg.get_unit_cfg_dirs.return_value = {
            'VcAesSupM__gen3': str(Path(CNFG_DIR, 'unit_cfgs'))}
        self.mock_build_cfg.get_local_defs_name.return_value = "*_LocalDefs.h"
        self.mock_build_cfg.get_feature_conf_header_name.return_value = "VcCodeSwDefines.h"
        self.mock_build_cfg.get_included_units.return_value = ['VcAesSupM__gen3']

        self.mock_feat_cfg = MagicMock(spec_set=FeatureConfigs)
        self.mock_feat_cfg.check_if_active_in_config = check_if_active_in_config

        UnitConfigs.clear_log()
        self.unit_cfgs = UnitConfigs(self.mock_build_cfg, self.mock_feat_cfg)

        self.expected_unit_cfgs = {
            'VcAesSupM__gen3': {
                'version': '0.2.1',
                'calib_consts': {
                    'cVcAesSupM_B_SupMonrHiBypFiMPerm': {
                        'class': 'CVC_CAL',
                        'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                        'description': 'Switch to bypass FiM permission  '
                                       'supercharger high boost monitor',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                  '1_SupMonr/11_SupChrgrSys/112_EnaCond/B_SupMonrHiBypFiMPerm',
                        'lsb': '1',
                        'max': ' ',
                        'min': ' ',
                        'offset': '0',
                        'width': '1',
                        'type': 'Bool',
                        'unit': ''}
                    },
                'core': {
                    'Events': {
                        'VcEvSupChrPMdlPlausHi': {
                            'API_blk': [
                                {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                                 'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                         '1_SupMonr/11_SupChrgrSys/114_InformationStorage/'
                                         '141_CoreHiBoost/Dem_SetEventStatusPF1'},
                                {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                                 'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                         '1_SupMonr/11_SupChrgrSys/114_InformationStorage/'
                                         '141_CoreHiBoost/Dem_SetEventStatusPP1'}],
                            'API_blk_type': 'Dem_SetEventStatus Pre-Passed',
                            'blk_name': 'NamedConstant2',
                            'class': '-',
                            'description': '-',
                            'lsb': '-',
                            'max': '-',
                            'min': '-',
                            'offset': '-',
                            'subsystem': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                         '1_SupMonr/11_SupChrgrSys/114_InformationStorage/'
                                         '141_CoreHiBoost',
                            'type': '-',
                            'unit': '-'}},
                    'FIDs': {
                        'VcFiSupChrPMdlPlausHi': {
                            'API_blk': [
                                {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                                 'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM'
                                         '/VcAesSupM/1_SupMonr/11_SupChrgrSys/112_EnaCond/'
                                         'FiM_GetFunctionPermission'}],
                            'API_blk_type': 'FiM_GetFunctionPermission',
                            'blk_name': 'NamedConstant2',
                            'class': '-',
                            'description': '-',
                            'lsb': '-',
                            'max': '-',
                            'min': '-',
                            'offset': '-',
                            'subsystem': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                         'VcAesSupM/1_SupMonr/11_SupChrgrSys/112_EnaCond',
                            'type': '-',
                            'unit': '-'}},
                    'IUMPR': {},
                    'Ranking': {
                        'VcRvSupChrPMdlPlausHi': {
                            'API_blk': [
                                {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                                 'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                         'VcAesSupM/1_SupMonr/11_SupChrgrSys/'
                                         '114_InformationStorage/141_CoreHiBoost/Vc_SetRanking'}],
                            'API_blk_type': 'Vcc_SetRanking',
                            'blk_name': 'NamedConstant1',
                            'class': '-',
                            'description': '-',
                            'lsb': '-',
                            'max': '-',
                            'min': '-',
                            'offset': '-',
                            'subsystem': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                         'VcAesSupM/1_SupMonr/11_SupChrgrSys/'
                                         '114_InformationStorage/141_CoreHiBoost',
                            'type': '-',
                            'unit': '-'}},
                    'TstId': {}
                },
                'dids': {},
                'inports': {
                    'sVcEc_p_Amb': {
                        'class': 'CVC_EXT',
                        'configs': [['Vc_Aes_SupM_B_CodeGenSprChrg']],
                        'description': 'Ambient pressure sensor',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                  'tlop_VcXx_insignal3',
                        'lsb': 1,
                        'max': 200,
                        'min': 0,
                        'name': 'sVcEc_p_Amb',
                        'offset': 0,
                        'type': 'Float32',
                        'unit': 'kPa'},
                    'yVcEc_B_ObdExe': {
                        'class': 'CVC_EXT',
                        'configs': [['Vc_Aes_SupM_B_CodeGenSprChrg']],
                        'description': 'OBD execution flag',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                  'tlop_VcXx_insignal1',
                        'lsb': 1,
                        'max': '-',
                        'min': '-',
                        'name': 'yVcEc_B_ObdExe',
                        'offset': 0,
                        'type': 'Bool',
                        'unit': '-'}},
                'local_vars': {
                    'rVcAesSupM_p_SupChrgrPDsAtmDiff': {
                        'class': 'CVC_DISP',
                        'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                        'description': 'Over pressure downstream supercharger',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                  '2_EngProtn/21_SupChrgrPPeak/211_PPeakTest/Sum5',
                        'lsb': '1',
                        'max': ' ',
                        'min': ' ',
                        'offset': '0',
                        'width': '1',
                        'type': 'Float32',
                        'unit': 'kPa'},
                    'rVcAesSupM_p_SupMonrSCTarDly': {
                        'class': 'CVC_DISP',
                        'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                        'description': 'Low pass filtered supercharger '
                                       'target pressure',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                  '1_SupMonr/11_SupChrgrSys/111_SignalCalc/FirstOrderFilter/Sum2',
                        'lsb': '1',
                        'max': '300',
                        'min': '0',
                        'offset': '0',
                        'width': '1',
                        'type': 'Float32',
                        'unit': 'kPa'}},
                'nvm': {},
                'outports': {
                    'yVcAesSupM_B_SupChrgrErr': {
                        'class': 'CVC_DISP',
                        'configs': ['all'],
                        'description': 'Supercharger Peak Pressure engine '
                                       'protection activation flag',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                  'tlop_VcAesAct_posn_EgrTar1',
                        'lsb': 1,
                        'max': '-',
                        'min': '-',
                        'name': 'yVcAesSupM_B_SupChrgrErr',
                        'offset': 0,
                        'type': 'Bool',
                        'unit': '%'}},
                'pre_procs': ['Vc_Aes_SupM_B_CodeGenSprChrg']
            }
        }

    def test_unit_config_init_args(self):
        """Check that constructor arguments are validated."""
        # Call with arguments reversed
        self.assertRaises(TypeError, UnitConfigs, self.mock_feat_cfg, self.mock_build_cfg)

    def test_unit_config_init_valid(self):
        """Check that no errors are logged with valid data."""
        ucnf = UnitConfigs(self.mock_build_cfg, self.mock_feat_cfg)
        self.assertIsInstance(ucnf, UnitConfigs)
        self.assertEqual(UnitConfigs.get_nbr_problems(), {'critical': 0, 'warning': 0})

    def test_unit_config_init_invalid_cfg(self):
        """Check that errors are logged with invalid build config."""
        self.mock_build_cfg.get_included_units.return_value = ['VcAesSupM__gen3', 'dummy_unit']
        ucnf = UnitConfigs(self.mock_build_cfg, self.mock_feat_cfg)
        self.assertIsInstance(ucnf, UnitConfigs)
        self.assertEqual(UnitConfigs.get_nbr_problems(), {'critical': 1, 'warning': 0})

    def test_unit_config_init_invalid_files(self):
        """Check that errors are logged with invalid config files."""
        self.mock_build_cfg.get_unit_cfg_dirs.return_value = {
            'VcAesSupM__gen3': str(Path(CNFG_DIR, 'unit_cfgs')),
            ' invalid name': str(Path(CNFG_DIR, 'invalid_unit_cfgs')),
            'InvalidConfig': str(Path(CNFG_DIR, 'invalid_unit_cfgs')),
            'InvalidJsonData': str(Path(CNFG_DIR, 'invalid_unit_cfgs')),
            }
        ucnf = UnitConfigs(self.mock_build_cfg, self.mock_feat_cfg)
        self.assertIsInstance(ucnf, UnitConfigs)
        self.assertEqual(UnitConfigs.get_nbr_problems(), {'critical': 1, 'warning': 0})

    def test_unit_config_init_invalid_unit_files(self):
        """Check that errors are logged with invalid units and config files."""
        self.mock_build_cfg.get_included_units.return_value = ['VcAesSupM__gen3', 'InvalidConfig']
        self.mock_build_cfg.get_unit_cfg_dirs.return_value = {
            'VcAesSupM__gen3': str(Path(CNFG_DIR, 'unit_cfgs')),
            ' invalid name': str(Path(CNFG_DIR, 'invalid_unit_cfgs')),
            'InvalidConfig': str(Path(CNFG_DIR, 'invalid_unit_cfgs')),
            'InvalidJsonData': str(Path(CNFG_DIR, 'invalid_unit_cfgs')),
            }
        ucnf = UnitConfigs(self.mock_build_cfg, self.mock_feat_cfg)
        self.assertIsInstance(ucnf, UnitConfigs)
        self.assertEqual(UnitConfigs.get_nbr_problems(), {'critical': 1, 'warning': 2})

    def test_per_unit_configs(self):
        """Check that unit cfgs are parsed and filtered correctly. Project VEP4_GENIII."""
        result = self.unit_cfgs.get_per_unit_cfg()
        self.maxDiff = None
        self.assertEqual(result, self.expected_unit_cfgs)

    def test_all_unit_configs(self):
        """Check that unit cfgs are parsed and filtered correctly. All projects."""
        result = self.unit_cfgs.get_per_unit_cfg_total()
        self.maxDiff = None
        handle = 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/1_SupMonr/11_SupChrgrSys/111_SignalCalc/Sum5'
        addition = {
            'rVcAesSupM_p_SupMonrPDif': {
                'class': 'CVC_DISP',
                'configs': ['not_in_config'],
                'description': 'Supercharger '
                               'actual  '
                               'and '
                               'target '
                               'pressure '
                               'difference',
                'handle': handle,
                'lsb': '1',
                'max': '300',
                'min': ' 300',
                'offset': '0',
                'type': 'Float32',
                'unit': 'kPa',
                'width': '1'},
        }
        expected = deepcopy(self.expected_unit_cfgs)
        expected['VcAesSupM__gen3']['local_vars'].update(addition)
        self.assertDictEqual(result, expected)

    def test_per_cfg_configs(self):
        """Check that unit cfgs are re-formatted and filtered correctly. Project VEP4_GENIII."""
        result = self.unit_cfgs.get_per_cfg_unit_cfg()
        expected = {
            'version': self.expected_unit_cfgs,
            'calib_consts': {
                'cVcAesSupM_B_SupMonrHiBypFiMPerm': {
                    'VcAesSupM__gen3': {
                        'class': 'CVC_CAL',
                        'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                        'description': 'Switch to bypass FiM permission  supercharger '
                                       'high boost monitor',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                  '1_SupMonr/11_SupChrgrSys/112_EnaCond/B_SupMonrHiBypFiMPerm',
                        'lsb': '1',
                        'max': ' ',
                        'min': ' ',
                        'offset': '0',
                        'width': '1',
                        'type': 'Bool',
                        'unit': ''}}},
            'core': {
                'VcEvSupChrPMdlPlausHi': {
                    'VcAesSupM__gen3': {
                        'API_blk': [
                            {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                             'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                     '1_SupMonr/11_SupChrgrSys/114_InformationStorage/'
                                     '141_CoreHiBoost/Dem_SetEventStatusPF1'},
                            {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                             'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                     '1_SupMonr/11_SupChrgrSys/114_InformationStorage/'
                                     '141_CoreHiBoost/Dem_SetEventStatusPP1'}],
                        'API_blk_type': 'Dem_SetEventStatus Pre-Passed',
                        'blk_name': 'NamedConstant2',
                        'class': '-',
                        'description': '-',
                        'lsb': '-',
                        'max': '-',
                        'min': '-',
                        'offset': '-',
                        'subsystem': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                     '1_SupMonr/11_SupChrgrSys/114_InformationStorage/'
                                     '141_CoreHiBoost',
                        'type': '-',
                        'unit': '-'}},
                'VcFiSupChrPMdlPlausHi': {
                    'VcAesSupM__gen3': {
                        'API_blk': [
                            {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                             'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM'
                                     '/VcAesSupM/1_SupMonr/11_SupChrgrSys/112_EnaCond/'
                                     'FiM_GetFunctionPermission'}],
                        'API_blk_type': 'FiM_GetFunctionPermission',
                        'blk_name': 'NamedConstant2',
                        'class': '-',
                        'description': '-',
                        'lsb': '-',
                        'max': '-',
                        'min': '-',
                        'offset': '-',
                        'subsystem': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                     'VcAesSupM/1_SupMonr/11_SupChrgrSys/112_EnaCond',
                        'type': '-',
                        'unit': '-'}},
                'VcRvSupChrPMdlPlausHi': {
                    'VcAesSupM__gen3': {
                        'API_blk': [
                            {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                             'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                     'VcAesSupM/1_SupMonr/11_SupChrgrSys/'
                                     '114_InformationStorage/141_CoreHiBoost/Vc_SetRanking'}],
                        'API_blk_type': 'Vcc_SetRanking',
                        'blk_name': 'NamedConstant1',
                        'class': '-',
                        'description': '-',
                        'lsb': '-',
                        'max': '-',
                        'min': '-',
                        'offset': '-',
                        'subsystem': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                     'VcAesSupM/1_SupMonr/11_SupChrgrSys/'
                                     '114_InformationStorage/141_CoreHiBoost',
                        'type': '-',
                        'unit': '-'}}
            },
            'inports': {
                'sVcEc_p_Amb': {
                    'VcAesSupM__gen3': {
                        'class': 'CVC_EXT',
                        'configs': [['Vc_Aes_SupM_B_CodeGenSprChrg']],
                        'description': 'Ambient pressure sensor',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                  'tlop_VcXx_insignal3',
                        'lsb': 1,
                        'max': 200,
                        'min': 0,
                        'name': 'sVcEc_p_Amb',
                        'offset': 0,
                        'type': 'Float32',
                        'unit': 'kPa'}},
                'yVcEc_B_ObdExe': {
                    'VcAesSupM__gen3': {
                        'class': 'CVC_EXT',
                        'configs': [['Vc_Aes_SupM_B_CodeGenSprChrg']],
                        'description': 'OBD execution flag',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                  'tlop_VcXx_insignal1',
                        'lsb': 1,
                        'max': '-',
                        'min': '-',
                        'name': 'yVcEc_B_ObdExe',
                        'offset': 0,
                        'type': 'Bool',
                        'unit': '-'}}},
            'local_vars': {
                'rVcAesSupM_p_SupChrgrPDsAtmDiff': {
                    'VcAesSupM__gen3': {
                        'class': 'CVC_DISP',
                        'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                        'description': 'Over pressure downstream supercharger',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                  '2_EngProtn/21_SupChrgrPPeak/211_PPeakTest/Sum5',
                        'lsb': '1',
                        'max': ' ',
                        'min': ' ',
                        'offset': '0',
                        'width': '1',
                        'type': 'Float32',
                        'unit': 'kPa'}},
                'rVcAesSupM_p_SupMonrSCTarDly': {
                    'VcAesSupM__gen3': {
                        'class': 'CVC_DISP',
                        'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                        'description': 'Low pass filtered '
                                       'supercharger target pressure',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                  '1_SupMonr/11_SupChrgrSys/111_SignalCalc/FirstOrderFilter/Sum2',
                        'lsb': '1',
                        'max': '300',
                        'min': '0',
                        'offset': '0',
                        'width': '1',
                        'type': 'Float32',
                        'unit': 'kPa'}}},
            'outports': {
                'yVcAesSupM_B_SupChrgrErr': {
                    'VcAesSupM__gen3': {
                        'class': 'CVC_DISP',
                        'configs': ['all'],
                        'description': 'Supercharger Peak Pressure engine protection '
                                       'activation flag',
                        'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                  'tlop_VcAesAct_posn_EgrTar1',
                        'lsb': 1,
                        'max': '-',
                        'min': '-',
                        'name': 'yVcAesSupM_B_SupChrgrErr',
                        'offset': 0,
                        'type': 'Bool',
                        'unit': '%'
                    }
                }
            }
        }
        self.maxDiff = None
        self.assertDictEqual(result, expected)

    def test_if_in_unit_cfg(self):
        """Check that symbol existence test is correct."""
        self.assertTrue(self.unit_cfgs.check_if_in_unit_cfg('VcAesSupM__gen3', 'sVcEc_p_Amb'))
        self.assertFalse(self.unit_cfgs.check_if_in_unit_cfg('VcAesSupM__gen3', 'dummy_symbol'))

    def test_if_in_per_cfg_unit_cfg(self):
        """Check that per project symbol existence test is correct."""
        self.assertTrue(self.unit_cfgs.check_if_in_per_cfg_unit_cfg('core', 'VcRvSupChrPMdlPlausHi'))
        self.assertFalse(self.unit_cfgs.check_if_in_per_cfg_unit_cfg('core', 'dummy_symbol'))

    def test_code_generators(self):
        """Check that code generators are correctly identified."""
        unit_cfgs = UnitConfigs(self.mock_build_cfg, self.mock_feat_cfg)
        self.assertEqual(unit_cfgs.code_generators, {'target_link'})
        self.assertEqual(unit_cfgs.base_types_headers, '#include "tl_basetypes.h"\n')

    def test_code_generators_ec(self):
        """Check that code generators are correctly identified for embedded coder."""
        mock_build_cfg = self.mock_build_cfg
        mock_build_cfg.get_unit_cfg_dirs.return_value = {
            'VcAesSupM__gen3': str(Path(CNFG_DIR, 'unit_cfgs_ec'))}
        unit_cfgs = UnitConfigs(self.mock_build_cfg, self.mock_feat_cfg)
        self.assertEqual(unit_cfgs.code_generators, {'embedded_coder'})
        self.assertEqual(unit_cfgs.base_types_headers, '#include "rtwtypes.h"\n')
