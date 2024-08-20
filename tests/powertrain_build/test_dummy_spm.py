# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for DummySpm class."""

import unittest
import os

from unittest.mock import patch, mock_open, MagicMock
from powertrain_build.dummy_spm import DummySpm
from powertrain_build.build_proj_config import BuildProjConfig
from powertrain_build.feature_configs import FeatureConfigs
from powertrain_build.unit_configs import UnitConfigs
from powertrain_build.user_defined_types import UserDefinedTypes


UNDEFINED_OUTPORTS = [
    {
        "handle": "yVcAcCtrl_handle",
        "name": "yVcAcCtrl_B_AirCondCluReq",
        "configs": ["all"],
        "description": "yVcAcCtrl_description",
        "type": "Bool",
        "unit": "",
        "offset": 0,
        "lsb": 1,
        "min": "-",
        "max": "-",
        "class": "CVC_EXT",
        "width": 1
    },
    {
        "handle": "sVcEac_handle",
        "name": "sVcEac_n_ElacCmprReq",
        "configs": [["Vc_Ac_Ctrl_B_CodeGenMecAC"], ["Vc_Ac_Ctrl_B_CodeGenX"]],
        "description": "sVcEac_description",
        "type": "Float32",
        "unit": "rpm",
        "offset": 0,
        "lsb": 1,
        "min": 0,
        "max": 12750,
        "class": "CVC_EXT",
        "width": 1
    }
]


class TestDummySpm(unittest.TestCase):
    """Test case for testing the DummySpm class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        self.build_cfg.get_ecu_info = MagicMock(return_value=('Denso', 'G2'))
        self.build_cfg.get_src_code_dst_dir = MagicMock(return_value=os.path.join('pybuild', 'test', 'output'))
        self.build_cfg.get_enum_def_dir = MagicMock(return_value=None)
        self.build_cfg.get_root_dir = MagicMock(return_value='.')
        self.build_cfg.get_use_volatile_globals = MagicMock(return_value=False)
        self.feature_config = MagicMock(spec_set=FeatureConfigs)
        self.feature_config.get_preprocessor_macro = MagicMock(return_value='')
        self.unit_cfg = MagicMock(spec_set=UnitConfigs)
        type(self.unit_cfg).base_types_headers = '#include "tl_basetypes.h"\n'
        self.user_defined_types = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        self.out_var = DummySpm(
            UNDEFINED_OUTPORTS,
            self.build_cfg,
            self.feature_config,
            self.unit_cfg,
            self.user_defined_types,
            'VcDummy_spm'
        )

    def test_restruct_data(self):
        """Check restructuring of variable dict."""
        result = self.out_var._restruct_input_data(UNDEFINED_OUTPORTS)
        expected = {
            'QM': [
                {
                            "handle": "sVcEac_handle",
                            "name": "sVcEac_n_ElacCmprReq",
                            "configs": [["Vc_Ac_Ctrl_B_CodeGenMecAC"], ["Vc_Ac_Ctrl_B_CodeGenX"]],
                            "description": "sVcEac_description",
                            "type": "Float32",
                            "cvc_type": "CVC_DISP",
                            "unit": "rpm",
                            "offset": 0,
                            "lsb": 1,
                            "min": 0,
                            "max": 12750,
                            "class": "CVC_EXT",
                            "width": 1
                },
                {
                            "handle": "yVcAcCtrl_handle",
                            "name": "yVcAcCtrl_B_AirCondCluReq",
                            "configs": ["all"],
                            "description": "yVcAcCtrl_description",
                            "type": "Bool",
                            "cvc_type": "CVC_DISP",
                            "unit": "",
                            "offset": 0,
                            "lsb": 1,
                            "min": "-",
                            "max": "-",
                            "class": "CVC_EXT",
                            "width": 1
                }
            ]
        }
        self.maxDiff = None
        self.assertDictEqual(result, expected)

    def test_restruct_data_empty(self):
        """Check restructuring of empty variable dict."""
        out_var = DummySpm([], self.build_cfg, None, self.unit_cfg, self.user_defined_types, 'VcDummy_spm')
        result = out_var._restruct_input_data([])
        expected = {}
        self.assertEqual(result, expected)

    def test_generate_code_files(self):
        """Check generated h-/c-file."""
        result = []  # Will contain content from VcDummy_spm.c and VcDummy_spm.h
        mopen = mock_open()
        mopen.return_value.write = result.append
        dst_src_dir = self.build_cfg.get_src_code_dst_dir()
        with patch('builtins.open', mopen, create=True):
            self.out_var.generate_code_files(dst_src_dir)

        current_directory = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(current_directory, 'reference_files', 'VcDummy_spm.h'), 'r') as h_fh:
            expected = h_fh.readlines()
        with open(os.path.join(current_directory, 'reference_files', 'VcDummy_spm.c'), 'r') as c_fh:
            expected += c_fh.readlines()

        self.assertCountEqual(result, expected)

    def test_generate_code_files_with_enum(self):
        """Check generated h-/c-file, with enums."""
        self.user_defined_types.common_header_files = ['tl_enumerations.h']
        out_var = DummySpm(
            UNDEFINED_OUTPORTS,
            self.build_cfg,
            self.feature_config,
            self.unit_cfg,
            self.user_defined_types,
            'VcDummy_spm'
        )
        result = []  # Will contain content from VcDummy_spm.c and VcDummy_spm.h
        mopen = mock_open()
        mopen.return_value.write = result.append
        dst_src_dir = self.build_cfg.get_src_code_dst_dir()
        with patch('builtins.open', mopen, create=True):
            out_var.generate_code_files(dst_src_dir)

        current_directory = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(current_directory, 'reference_files', 'VcDummy_spm_with_enum.h'), 'r') as h_fh:
            expected = h_fh.readlines()
        with open(os.path.join(current_directory, 'reference_files', 'VcDummy_spm.c'), 'r') as c_fh:
            expected += c_fh.readlines()

        self.assertCountEqual(result, expected)
