# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for ExtVarCsv class."""

import unittest
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
from pybuild.ext_var import ExtVarCsv
from pybuild.build_proj_config import BuildProjConfig
from pybuild.unit_configs import UnitConfigs
from pybuild.user_defined_types import UserDefinedTypes

from .io_cnfg import DBG_CNFG_DICT, EC_CNFG_DICT


class TestExtVarCsv(unittest.TestCase):
    """Test case for testing the ExtVarCsv class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        self.build_cfg.get_ecu_info = MagicMock(return_value=('Denso', 'G2'))
        self.build_cfg.get_enum_def_dir = MagicMock(return_value=None)
        self.build_cfg.get_root_dir = MagicMock(return_value='.')
        self.unit_cfg = MagicMock(spec_set=UnitConfigs)
        type(self.unit_cfg).base_types_headers = '#include "tl_basetypes.h"\n'
        self.user_defined_types = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        self.ext_var = ExtVarCsv(DBG_CNFG_DICT['VED4_GENIII'], self.build_cfg, self.unit_cfg, self.user_defined_types)

    def test_restruct_data(self):
        """Check restructuring of variable dict."""
        self.ext_var._restruct_input_data()
        result = self.ext_var._ext_vars
        expected = {
            '1': {
                'sVcAc_D_EngRunReqClim': {
                    'IOType': 'd',
                    'description': 'Engine running request (inhibit stop) from climate',
                    'element_index': 5,
                    'init': 0,
                    'max': 3,
                    'min': 0,
                    'type': 'UInt8',
                    'unit': '-'
                }
            }
        }
        self.assertDictEqual(result[0], expected)

    def test_restruct_data_empty(self):
        """Check restructuring of empty variable dict."""
        ext_var = ExtVarCsv({}, self.build_cfg, self.unit_cfg, self.user_defined_types)
        ext_var._restruct_input_data()
        result = ext_var._ext_vars
        expected = ({}, {})
        self.assertEqual(result, expected)

    def test_a2l_dict(self):
        """Check generation of a2l-dict."""
        result = self.ext_var._a2l_dict()
        expected = {
            'function': 'VcExtVar',
            'vars': {
                'sVcAc_D_EngRunReqClim': {
                    'a2l_data': {
                        'bitmask': None,
                        'description': 'Engine running request (inhibit stop) from climate',
                        'lsb': '2^0',
                        'max': 3,
                        'min': 0,
                        'offset': '0',
                        'unit': '-',
                        'x_axis': None,
                        'y_axis': None
                    },
                    'array': [],
                    'function': ['VcEc'],
                    'var': {
                        'cvc_type': 'CVC_DISP',
                        'type': 'UInt8',
                        'var': 'sVcAc_D_EngRunReqClim'
                    }
                }
            }
        }
        self.assertDictEqual(result, expected)

    def test_a2l_dict_empty(self):
        """Check restructuring of empty variable dict."""
        ext_var = ExtVarCsv({}, self.build_cfg, self.unit_cfg, self.user_defined_types)
        result = ext_var._a2l_dict()
        expected = {'vars': {}, 'function': 'VcExtVar'}
        self.assertEqual(result, expected)

    def test_generate_c_file(self):
        """Check generated c-file."""
        result = []
        mopen = mock_open()
        mopen.return_value.write = result.append
        with patch.object(Path, 'open', mopen, create=True):
            self.ext_var._restruct_input_data()
            self.ext_var._generate_c_file(Path("outfile"))
        expected = [
            '#include "outfile.h"\n',
            '#include "CVC_DISP_START.h"\n\n',
            '/* Variables of size 1 bytes */\n\n',
            'CVC_DISP UInt8 sVcAc_D_EngRunReqClim = 0;\n',
            '\n',
            '\n#include "CVC_DISP_END.h"\n']
        self.assertEqual(result, expected)

    def test_generate_h_file(self):
        """Check generated h-file."""
        result = []
        mopen = mock_open()
        mopen.return_value.write = result.append
        with patch.object(Path, 'open', mopen, create=True):
            self.ext_var._restruct_input_data()
            self.ext_var._generate_h_file(Path("outfile"))
        expected = (
            '#ifndef OUTFILE_H\n'
            '#define OUTFILE_H\n'
            '#define CVC_DISP\n'
            '#include "tl_basetypes.h"\n'
            '\n'
            '#include "PREDECL_DISP_START.h"\n'
            '/* VCC Inports */\n'
            '/* Variables of size 1 bytes */\n'
            '\n'
            'extern CVC_DISP UInt8 sVcAc_D_EngRunReqClim;\n'
            '\n'
            '/* VCC Outports */\n'
            '/* Variables of size 1 bytes */\n'
            '\n'
            'extern CVC_DISP UInt8 sVcAc_D_AirCondCmpsrStats;\n'
            '\n'
            '#include "PREDECL_DISP_END.h"\n'
            '#endif\n')
        self.assertEqual(''.join(result).splitlines(), expected.splitlines())


class TestExtVarCsvEC(unittest.TestCase):
    """Test case for testing the ExtVarCsv class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        self.build_cfg.get_ecu_info = MagicMock(return_value=('CSP', ''))
        self.build_cfg.get_enum_def_dir = MagicMock(return_value=None)
        self.build_cfg.get_root_dir = MagicMock(return_value='.')
        self.unit_cfg = MagicMock(spec_set=UnitConfigs)
        type(self.unit_cfg).base_types_headers = '#include "rtwtypes.h"\n'
        self.unit_cfg.get_per_unit_cfg = MagicMock(return_value={
            'VcScBCoord': {'code_generator': 'embedded_coder'},
            'VcScCVehMtn': {'code_generator': 'embedded_coder'},
            'VcScFeh': {'code_generator': 'embedded_coder'}})
        self.user_defined_types = UserDefinedTypes(self.build_cfg, self.unit_cfg)
        self.ext_var = ExtVarCsv(EC_CNFG_DICT['ADAS'], self.build_cfg, self.unit_cfg, self.user_defined_types)

    def test_generate_c_file(self):
        """Check generated c-file."""
        result = []
        mopen = mock_open()
        mopen.return_value.write = result.append
        with patch.object(Path, 'open', mopen, create=True):
            self.ext_var._restruct_input_data()
            self.ext_var._generate_c_file(Path("outfile"))
        expected = [
            '#include "outfile.h"\n',
            '#include "CVC_DISP_START.h"\n\n',
            '/* Variables of size 4 bytes */\n\n',
            'CVC_DISP ulong_T sVcAc_D_EngRunReqClim = 0;\n',
            '\n',
            '\n#include "CVC_DISP_END.h"\n']
        self.assertEqual(result, expected)

    def test_generate_h_file(self):
        """Check generated h-file."""
        result = []
        mopen = mock_open()
        mopen.return_value.write = result.append
        with patch.object(Path, 'open', mopen, create=True):
            self.ext_var._restruct_input_data()
            self.ext_var._generate_h_file(Path("outfile"))
        expected = (
            '#ifndef OUTFILE_H\n'
            '#define OUTFILE_H\n'
            '#define CVC_DISP\n'
            '#include "rtwtypes.h"\n'
            '\n'
            '#include "PREDECL_DISP_START.h"\n'
            '/* VCC Inports */\n'
            '/* Variables of size 4 bytes */\n'
            '\n'
            'extern CVC_DISP ulong_T sVcAc_D_EngRunReqClim;\n'
            '\n'
            '/* VCC Outports */\n'
            '/* Variables of size 4 bytes */\n'
            '\n'
            'extern CVC_DISP real32_T sVcAc_D_AirCondCmpsrStats;\n'
            '\n'
            '#include "PREDECL_DISP_END.h"\n'
            '#endif\n')
        self.assertEqual(''.join(result).splitlines(), expected.splitlines())
