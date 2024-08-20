# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for ExtDbg class."""

import unittest
from unittest.mock import MagicMock
from powertrain_build.ext_dbg import ExtDbg
from powertrain_build.build_proj_config import BuildProjConfig
from powertrain_build.unit_configs import UnitConfigs
from .io_cnfg import DBG_CNFG_DICT


class TestExtDbg(unittest.TestCase):
    """Test case for testing the ExtDbg class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        self.unit_cfg = MagicMock(spec_set=UnitConfigs)
        self.build_cfg.get_ecu_info = MagicMock(return_value=('Denso', 'G2'))
        self.ext_dbg = ExtDbg(DBG_CNFG_DICT['VED4_GENIII'], self.build_cfg, self.unit_cfg)

    def test_restruct_data(self):
        """Check restructuring of variable dict."""
        result = self.ext_dbg._restruct_data()
        expected = {
            'inputs': {
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
            },
            'outputs': {
                '1': {
                    'sVcAc_D_AirCondCmpsrStats': {
                        'IOType': 'd',
                        'description': 'Aircond compressor status',
                        'element_index': 5,
                        'init': 0,
                        'max': 7,
                        'min': 0,
                        'type': 'UInt8',
                        'unit': '-'
                    }
                }
            }
        }
        self.assertDictEqual(result, expected)
