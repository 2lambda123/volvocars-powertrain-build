# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for CsvSignalInterfaces. Read data from file."""

import copy
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch, mock_open, call

from pybuild.build_proj_config import BuildProjConfig
from pybuild.unit_configs import UnitConfigs
from pybuild.signal_interfaces import CsvSignalInterfaces


class RawIOCfg:
    """Hold a default consistent configuration matching the interface requirements file bundled with the tests.

    Instances can be modified to inject inconsistencies.
    """

    _tot_cfg = {
        'CAN-Input': {
            'sVcAc_D_EngRunReqClim': {
                'description':
                'Engine running '
                'request (inhibit '
                'stop) from climate',
                'element_index': 5,
                'init':
                0,
                'max':
                3,
                'min':
                0,
                'IOType': 'd',
                'type':
                'UInt8',
                'unit':
                '-'
            },
            'sVcAcc_a_Max': {
                'description':
                'Max acceleration request from '
                'ACC',
                'element_index': 6,
                'init':
                0,
                'max':
                5,
                'min':
                -5,
                'IOType': 's',
                'type':
                'Float32',
                'unit':
                'm/s2'
            }
        },
        'CAN-Output': {
            'sVcAc_D_AirCondCmpsrStats': {
                'description': 'Aircond compressor status',
                'element_index': 5,
                'init': 0,
                'max': 7,
                'min': 0,
                'IOType': 'd',
                'type': 'UInt8',
                'unit': '-'
            }
        },
        'EMS-Input': {},
        'EMS-Output': {},
        'LIN-Input': {},
        'LIN-Output': {},
        'Private CAN-Input': {
            'sVcTc_p_LockUp': {
                'description': 'AW Pressure request to LU',
                'element_index': 5,
                'init': 0,
                'max': 16383,
                'min': 0,
                'IOType': 'x',
                'type': 'Float32',
                'unit': 'gf/cm2'
            }
        },
        'Private CAN-Output': {}
    }

    def __init__(self):
        self.restore()

    def restore(self):
        """Restore something the tot_cfg."""
        self.tot_cfg = copy.deepcopy(self._tot_cfg)

    def get_raw_io_cnfg(self):
        """Generate consistent data of total unit configuration."""
        return self.tot_cfg


class BaseSetUp(unittest.TestCase):
    """Inerhitence from this class for all testcases.

    Start the calling this setUpClass method from the setUpClass method in the
    test case, and then modify the base setup in the test case (if needed).
    """

    CNFG_DIR = Path(Path(__file__).parent, 'cnfg_files')
    ACTIVE_INTERFACE_DIRECTORY = str(Path(CNFG_DIR, 'ActiveInterfaces'))

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        super().setUp()
        self.raw_io_cfg = RawIOCfg()
        self.ucfg = MagicMock(spec_set=UnitConfigs)
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        self.build_cfg.get_prj_config = MagicMock(
            return_value='VED4_GENIII')
        self.build_cfg.get_prj_cfg_dir = MagicMock(
            return_value=str(self.CNFG_DIR))
        self.build_cfg.get_if_cfg_dir = MagicMock(
            return_value=self.ACTIVE_INTERFACE_DIRECTORY)
        self.maxDiff = None


class TestSignalIterfacesRead(BaseSetUp):
    """Test the CsvSignalInterfaces class."""

    def setUp(self):
        """Read interface definition file."""
        super().setUp()
        self.csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)

    def test_get_raw_io_cnfg(self):
        """Check raw config read from file."""
        result = self.csi.get_raw_io_cnfg()
        expected_res = self.raw_io_cfg.get_raw_io_cnfg()
        self.assertDictEqual(result, expected_res)

    @patch('pybuild.signal_interfaces.open', new_callable=mock_open())
    def test_verify_files_read(self, m):
        """Verify that files are opened and read."""
        private_can_input_call = call(Path(BaseSetUp.ACTIVE_INTERFACE_DIRECTORY,
                                           'Private CAN-Input.csv'),
                                      newline='')
        private_can_output_call = call(Path(BaseSetUp.ACTIVE_INTERFACE_DIRECTORY,
                                            'Private CAN-Output.csv'),
                                       newline='')
        can_input_call = call(Path(BaseSetUp.ACTIVE_INTERFACE_DIRECTORY,
                                   'CAN-Input.csv'),
                              newline='')
        can_output_call = call(Path(BaseSetUp.ACTIVE_INTERFACE_DIRECTORY,
                                    'CAN-Output.csv'),
                               newline='')
        ems_input_call = call(Path(BaseSetUp.ACTIVE_INTERFACE_DIRECTORY,
                                   'EMS-Input.csv'),
                              newline='')
        ems_output_call = call(Path(BaseSetUp.ACTIVE_INTERFACE_DIRECTORY,
                                    'EMS-Output.csv'),
                               newline='')
        lin_input_call = call(Path(BaseSetUp.ACTIVE_INTERFACE_DIRECTORY,
                                   'LIN-Input.csv'),
                              newline='')
        lin_output_call = call(Path(BaseSetUp.ACTIVE_INTERFACE_DIRECTORY,
                                    'LIN-Output.csv'),
                               newline='')
        calls = [
                    private_can_input_call,
                    private_can_output_call,
                    can_input_call,
                    can_output_call,
                    ems_input_call,
                    ems_output_call,
                    lin_input_call,
                    lin_output_call
                ]
        CsvSignalInterfaces(self.build_cfg, self.ucfg)
        m.assert_has_calls(calls, any_order=True)
