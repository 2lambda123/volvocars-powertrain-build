# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for run_gen_label_split.py."""

from pathlib import Path
from unittest import TestCase
from unittest.mock import MagicMock, patch
from pybuild.build_proj_config import BuildProjConfig
from pybuild.gen_label_split import LabelSplit

CNFG_DIR = Path(Path(__file__).parent, 'cnfg_files')
REF_DIR = Path(Path(__file__).parent, 'reference_files')


class TestGenLabelSplit(TestCase):
    """Test functions defined in gen_label_split.py

    get_symbols_and_groups not tested, mostly calls other already tested functions.
    generate_label_split_xml_file not tested, basically only generates a file.
    """

    def setUp(self):
        build_prj_cfg = BuildProjConfig(str(Path(CNFG_DIR, 'LabelsplitCfg.json')))
        project = "GEP3_BEV"
        json_file = Path(CNFG_DIR, "label_split_cfg.json")
        cmt_source_folder = Path('')
        self.label_split = LabelSplit(project, build_prj_cfg, json_file, cmt_source_folder)

    def test_read_json(self):
        expected_symbol_group = {
            'HYBRID': 4,
            'HEP': 4,
            'VEP': 3,
            'GEP': 3,
            'VED': 2,
            'CSP': 4
        }
        test_symbol_group = self.label_split.labelsplit_cfg.get("SGP_SYMBOL_GROUPS")
        self.assertEqual(test_symbol_group, expected_symbol_group)

    def test_get_project_a2l_symbols(self):
        test_file_path = Path(CNFG_DIR, 'test.a2l')
        symbols = self.label_split.get_project_a2l_symbols(test_file_path)
        expected_symbols = [
            'cVcAesTrboM_B_EngProtnTrboPPeakUseAbsolutP',
            'cVcAesTrboM_B_IsObdExeSpm',
            'cVcAesTrboM_B_PpLkExhFiMPerm',
            'mVcAesTrboM_rt_TrboMonrTgtLim_c',
            'mVcAesTrboM_rt_TrboMonrTgtLim_r',
            'tVcAesTrboM_n_EngSpdMinLim_x',
            'tVcAesTrboM_t_TrboMonrLoBoostTiDly_x',
        ]
        self.assertListEqual(symbols, expected_symbols)

    def test_get_sgp_symbols(self):
        test_file_path = Path(REF_DIR, 'SS1', 'test_model', 'VcTestModel_sgp.xml')
        symbols = self.label_split.get_sgp_symbols(test_file_path)
        expected_symbols = {
            'Calibrationlabel': [
                (2, 'Symbolgroupdiesel'),
                (3, 'Symbolgrouppetrol'),
                (4, 'Symbolgrouphybrid'),
                (5, 'Subsystem')
            ],
            'mVcTestModel_fac_BoostMaxTCmp': [
                (3, 'EC_ACS_TURBO'),
                (4, 'EC_ACS_TURBO'),
                (5, 'NotApplicable')
            ],
            'tVcTestModel_n_PreIgnitionRpm': [
                (2, 'DD_DCL'),
                (3, 'DD_DCL'),
                (4, 'DD_DCL'),
                (5, 'NotApplicable')
            ],
            'cVcTestModel_n_PreIgnitionTrigger': [
                (2, 'DD_DCL'),
                (3, 'DD_DCL'),
                (4, 'DD_DCL'),
                (5, 'NotApplicable')
            ],
            'cVcTestModel_B_WhlMotSysLimnIndcnReLeOk_db': [
                (2, 'PVC_DEP'),
                (3, 'PVC_DEP'),
                (4, 'PVC_DEP')
            ]
        }
        self.assertDictEqual(symbols, expected_symbols)

    def test_get_sgp_symbol_group(self):
        no_diesel_group = [(3, 'SG_P'), (4, 'SG_H')]
        no_petrol_group = [(2, 'SG_D'), (4, 'SG_H')]
        no_hybrid_group = [(2, 'SG_D'), (3, 'SG_P')]
        all_groups = [(2, 'SG_D'), (3, 'SG_P'), (4, 'SG_H')]
        expected_group = {
            'GEP3_SPA': 'SG_P',
            'VED4_GEN3': 'SG_D',
            'VEP4_GEN2_HYBRID': 'SG_H',
            'VEP4_GEN3': 'SG_P'
        }

        for project in ['GEP3_SPA', 'VED4_GEN3', 'VEP4_GEN2_HYBRID', 'VEP4_GEN3']:
            self.label_split.project = project
            symbol_group = self.label_split.get_sgp_symbol_group(all_groups)
            self.assertEqual(symbol_group, expected_group[project])

        self.label_split.project = 'VED4_GEN3'
        no_diesel_test = self.label_split.get_sgp_symbol_group(no_diesel_group)
        self.assertEqual(no_diesel_test, '')
        self.label_split.project = 'GEP3_SPA'
        no_petrol_test = self.label_split.get_sgp_symbol_group(no_petrol_group)
        self.assertEqual(no_petrol_test, '')
        self.label_split.project = 'VEP4_GEN2_HYBRID'
        no_hybrid_test = self.label_split.get_sgp_symbol_group(no_hybrid_group)
        self.assertEqual(no_hybrid_test, '')

    @patch('pybuild.gen_label_split.LabelSplit.get_sgp_symbol_group', autospec=True)
    def test_get_interface_symbols_and_groups(self, sg_mock):
        sg_mock.return_value = 'SG_P'
        interface_dict = {
            'CAN-Input': {
                'sInsig_1': {'In_Data_1': 'SomeInData1'},
                'sInsig_2': {'In_Data_2': 'SomeInData2'}
            },
            'EMS-Output': {
                'yOutsig_1': {'Out_Data_1': 'SomeOutData1'},
                'yOutsig_2': {'Out_Data_2': 'SomeOutData2'}
            }
        }
        in_symbol_sgp_dict = {
            'cInsig_2_sw': [(2, 'SG_D'), (3, 'SG_P'), (4, 'SG_H')],
            'cInsig_2_db': [(2, 'SG_D'), (3, 'SG_P'), (4, 'SG_H')]
        }
        out_symbol_sgp_dict = {
            'cOutsig_1_sw': [(2, 'SG_D'), (3, 'SG_P'), (4, 'SG_H')],
            'cOutsig_1_db': [(2, 'SG_D'), (3, 'SG_P'), (4, 'SG_H')]
        }
        self.label_split.project = 'VED4_GEN3'
        symbols_and_groups = self.label_split.get_interface_symbols_and_groups(
            interface_dict,
            in_symbol_sgp_dict,
            out_symbol_sgp_dict
        )
        expected = [
            ('cInsig_2_db', 'SG_P'),
            ('cInsig_2_sw', 'SG_P'),
            ('cOutsig_1_db', 'SG_P'),
            ('cOutsig_1_sw', 'SG_P')
        ]
        self.assertListEqual(symbols_and_groups, expected)

    @patch('pybuild.gen_label_split.LabelSplit.get_interface_symbols_and_groups', autospec=True)
    @patch('pybuild.gen_label_split.LabelSplit.get_sgp_symbols', autospec=True)
    def test_get_debug_symbols_and_groups(self, sgp_symbols_mock, interface_symbols_and_groups_mock):
        # This function calls other (already tested functions), however, it has an important check in the end tp test.
        self.label_split.signal_interface = MagicMock()
        self.label_split.signal_interface.get_io_config.return_value = ({}, {}, {})

        # Return value of "get_sgp_symbols" does not matter, it is fed to "get_interface_symbols_and_groups"
        sgp_symbols_mock.return_value = {}
        interface_symbols_and_groups_mock.return_value = [('cInsig_1_db', 'SG_P'), ('cInsig_1_sw', '')]

        # Since "get_interface_symbols_and_groups" is called twice, expected contains duplicates
        expected = [('cInsig_1_db', 'SG_P'), ('cInsig_1_db', 'SG_P')]

        self.label_split.project = 'VED4_GEN3'
        symbols_and_groups = self.label_split.get_debug_symbols_and_groups()
        self.assertListEqual(symbols_and_groups, expected)

    @patch('glob.glob', autospec=True)
    def test_check_unit_par_file(self, glob_mock):
        # Cannot test VcDcl*Mdl due to glob overriding
        test_model_path = Path(REF_DIR, 'SS1', 'test_model', 'VcTestModel_par.m')
        test_model_1_path = Path(REF_DIR, 'SS1', 'test_model1', 'VcTestModel1_par.m')

        # With SgpDefault
        glob_mock.return_value = [test_model_path]
        has_sgp_default, default_symbol_group = self.label_split.check_unit_par_file('VcTestModel')
        self.assertTrue(has_sgp_default)
        self.assertEqual(default_symbol_group, 'SG_P')

        # Without SgpDefault
        glob_mock.return_value = [test_model_1_path]
        has_sgp_default, default_symbol_group = self.label_split.check_unit_par_file('VcTestModel1')
        self.assertFalse(has_sgp_default)
        self.assertEqual(default_symbol_group, '')

        # Found several
        glob_mock.return_value = [test_model_path, test_model_1_path]
        has_sgp_default, default_symbol_group = self.label_split.check_unit_par_file('VcTestModel')
        self.assertTrue(has_sgp_default)
        self.assertEqual(default_symbol_group, 'SG_P')

        # Found none
        glob_mock.return_value = []
        has_sgp_default, default_symbol_group = self.label_split.check_unit_par_file('VcTestModel')
        self.assertFalse(has_sgp_default)
        self.assertEqual(default_symbol_group, '')

    @patch('glob.glob', autospec=True)
    def test_get_unit_sgp_file(self, glob_mock):
        # Cannot test VcDcl*Mdl due to glob overriding
        test_sgp_path = Path(REF_DIR, 'SS1', 'test_model', 'VcTestModel_sgp.xml')
        test_none_existent_sgp_path = Path('no_sgp_file_here.xml')

        # Found one
        glob_mock.return_value = [test_sgp_path]
        sgp_file = self.label_split.get_unit_sgp_file('VcTestModel')
        self.assertTrue(sgp_file.is_file())

        # Found several
        glob_mock.return_value = [test_sgp_path, test_none_existent_sgp_path]
        sgp_file = self.label_split.get_unit_sgp_file('VcTestModel')
        self.assertTrue(sgp_file.is_file())

        # Found none
        glob_mock.return_value = []
        sgp_file = self.label_split.get_unit_sgp_file('VcTestModel')
        self.assertFalse(sgp_file.is_file())

    @patch('pybuild.gen_label_split.LabelSplit.get_unit_sgp_file', autospec=True)
    @patch('pybuild.gen_label_split.LabelSplit.check_unit_par_file', autospec=True)
    def test_get_unit_symbols_and_groups(self, unit_par_file_mock, sgp_file_mock):
        sgp_file_mock.return_value = Path(REF_DIR, 'SS1', 'test_model', 'VcTestModel_sgp.xml')
        unit_calibration_symbols = [
            'mVcTestModel_fac_BoostMaxTCmp',  # Not for diesel
            'tVcTestModel_n_PreIgnitionRpm',
            'cVcTestModel_n_PreIgnitionTrigger',
            'cVcTestModel_B_WhlMotSysLimnIndcnReLeOk_db',
            'cVcTestModel_in_config_and_a2l',  # Also in project a2l, depends on SgpDefault
            'cVcTestModel_only_in_config'
        ]
        project_a2l_symbols = [
            'mVcTestModel_fac_BoostMaxTCmp',
            'tVcTestModel_n_PreIgnitionRpm',
            'cVcTestModel_n_PreIgnitionTrigger',
            'cVcTestModel_B_WhlMotSysLimnIndcnReLeOk_db',
            'cVcTestModel_in_config_and_a2l',
            'cVcTestModel3_only_in_a2l'
        ]

        # VED with SgpDefault
        unit_par_file_mock.return_value = (True, 'SG_P')
        expected = [
            ('mVcTestModel_fac_BoostMaxTCmp', ''),
            ('tVcTestModel_n_PreIgnitionRpm', 'DD_DCL'),
            ('cVcTestModel_n_PreIgnitionTrigger', 'DD_DCL'),
            ('cVcTestModel_B_WhlMotSysLimnIndcnReLeOk_db', 'PVC_DEP'),
            ('cVcTestModel_in_config_and_a2l', 'SG_P')
        ]
        self.label_split.project = 'VED4_GEN3'
        self.label_split.project_a2l_symbols = project_a2l_symbols

        unit_symbols_and_groups = self.label_split.get_unit_symbols_and_groups(
            'VcTestModel',
            unit_calibration_symbols
        )
        self.assertListEqual(unit_symbols_and_groups, expected)

        # VED without SgpDefault
        unit_par_file_mock.return_value = (False, '')
        expected = [
            ('mVcTestModel_fac_BoostMaxTCmp', ''),
            ('tVcTestModel_n_PreIgnitionRpm', 'DD_DCL'),
            ('cVcTestModel_n_PreIgnitionTrigger', 'DD_DCL'),
            ('cVcTestModel_B_WhlMotSysLimnIndcnReLeOk_db', 'PVC_DEP')
        ]
        unit_symbols_and_groups = self.label_split.get_unit_symbols_and_groups(
            'VcTestModel',
            unit_calibration_symbols
        )
        self.assertListEqual(unit_symbols_and_groups, expected)

        # GEP with SgpDefault
        unit_par_file_mock.return_value = (True, 'SG_P')
        expected = [
            ('mVcTestModel_fac_BoostMaxTCmp', 'EC_ACS_TURBO'),
            ('tVcTestModel_n_PreIgnitionRpm', 'DD_DCL'),
            ('cVcTestModel_n_PreIgnitionTrigger', 'DD_DCL'),
            ('cVcTestModel_B_WhlMotSysLimnIndcnReLeOk_db', 'PVC_DEP'),
            ('cVcTestModel_in_config_and_a2l', 'SG_P')
        ]
        self.label_split.project = 'GEP3_SPA'
        unit_symbols_and_groups = self.label_split.get_unit_symbols_and_groups(
            'VcTestModel',
            unit_calibration_symbols
        )
        self.assertListEqual(unit_symbols_and_groups, expected)

        # GEP without SgpDefault
        unit_par_file_mock.return_value = (False, '')
        expected = [
            ('mVcTestModel_fac_BoostMaxTCmp', 'EC_ACS_TURBO'),
            ('tVcTestModel_n_PreIgnitionRpm', 'DD_DCL'),
            ('cVcTestModel_n_PreIgnitionTrigger', 'DD_DCL'),
            ('cVcTestModel_B_WhlMotSysLimnIndcnReLeOk_db', 'PVC_DEP')
        ]
        unit_symbols_and_groups = self.label_split.get_unit_symbols_and_groups(
            'VcTestModel',
            unit_calibration_symbols
        )
        self.assertListEqual(unit_symbols_and_groups, expected)

    def test_get_calibration_constants(self):
        self.label_split.unit_cfg = MagicMock()
        self.label_split.unit_cfg.get_per_cfg_unit_cfg.return_value = {
            'calib_consts': {
                'mVcTestModel_fac_BoostMaxTCmp': {'VcTestModel': {'class': 'ASIL_A/CVC_CAL_ASIL_A'}},
                'tVcTestModel_n_PreIgnitionRpm': {'VcTestModel': {'class': 'ASIL_B/CVC_CAL_ASIL_B'}},
                'cVcTestModel_n_PreIgnitionTrigger': {'VcTestModel': {'class': 'CVC_CAL_MERGEABLE'}},
                'cVcTestModel_B_WhlMotSysLimnIndcnReLeOk_db': {'VcTestModel': {'class': 'CVC_CAL'}},
                'cVcTestModel_in_config_and_a2l': {'VcTestModel': {'class': 'ASIL_A/CVC_CAL_ASIL_A'}},
                'cVcTestModel_only_in_config': {'VcTestModel': {'class': 'CVC_CAL'}},
                'sVcTestModel_D_SomeSkippedConst': {'VcTestModel': {'class': 'CVC_CONST'}},
                'sVcModel_D_SecurityTwo': {'VcSecurityModel': {}}
            }
        }

        expected_calibration_symbols = {
            'VcTestModel': [
                'mVcTestModel_fac_BoostMaxTCmp',
                'tVcTestModel_n_PreIgnitionRpm',
                'cVcTestModel_n_PreIgnitionTrigger',
                'cVcTestModel_B_WhlMotSysLimnIndcnReLeOk_db',
                'cVcTestModel_in_config_and_a2l',
                'cVcTestModel_only_in_config'
            ]
        }
        calibration_symbols = self.label_split.get_calibration_constants()
        self.assertDictEqual(calibration_symbols, expected_calibration_symbols)
