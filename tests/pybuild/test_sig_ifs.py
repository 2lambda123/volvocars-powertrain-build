# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for CsvSignalInterfaces."""

import copy
import unittest
import pprint
from unittest.mock import MagicMock, patch
from pathlib import Path
from pybuild.build_proj_config import BuildProjConfig
from pybuild.unit_configs import UnitConfigs
from pybuild.signal_interfaces import CsvSignalInterfaces


class SigIfCfg:
    """Hold a reference configuration."""
    _sig_if_cfg_orig = {
        'CAN-Input': {},
        'EMS-Input': {
            'isig1': {
                'IOType': 'x',
                'description': 'Torque arbitraion state',
                'init': 0,
                'max': 9,
                'min': 0,
                'offset': 0,
                'type': 'UInt8',
                'unit': '-',
            },
            'isig2': {
                'IOType': 'x',
                'description': 'Torque arbitraion state',
                'init': 0,
                'max': 9,
                'min': 0,
                'offset': 0,
                'type': 'UInt8',
                'unit': '-',
            },
            'isig3': {
                'IOType': 'x',
                'description': 'Torque arbitraion state',
                'init': 0,
                'max': 9,
                'min': 0,
                'offset': 0,
                'type': 'UInt8',
                'unit': '-',
            },
        },
        'LIN-Input': {},
        'Private CAN-Input': {},
        'CAN-Output': {},
        'EMS-Output': {
            'osig1': {
                'IOType': 'x',
                'description': 'Torque arbitraion state',
                'init': 0,
                'max': 9,
                'min': 0,
                'offset': 0,
                'type': 'UInt8',
                'unit': '-',
            },
            'osig2': {
                'IOType': 'x',
                'description': 'Torque arbitraion state',
                'init': 0,
                'max': 9,
                'min': 0,
                'offset': 0,
                'type': 'UInt8',
                'unit': '-',
            },
            'sigI1': {
                'IOType': 'x',
                'description': 'Torque arbitraion state',
                'init': 0,
                'max': 9,
                'min': 0,
                'offset': 0,
                'type': 'UInt8',
                'unit': '-',
            },
            'sigI2': {
                'IOType': 'x',
                'description': 'Torque arbitraion state',
                'init': 0,
                'max': 9,
                'min': 0,
                'offset': 0,
                'type': 'UInt8',
                'unit': '-',
            }
        },
        'LIN-Output': {},
        'Private CAN-Output': {}
    }

    interfaces = copy.deepcopy(_sig_if_cfg_orig)

    @classmethod
    def restore(cls):
        """Restore default cfg."""
        cls.interfaces = copy.deepcopy(cls._sig_if_cfg_orig)


class TotUCfg:
    """Hold a default consistent configuration.

    Instances can be modified to inject inconsistencies.
    """

    tmp_cfg = {
        'inports': {
            'isig1': {
                'VcFnc1': {
                    'class': 'CVC_EXT',
                    'configs': [['CFG', 'CFG1', 'CFG2']],
                    'description': 'Torque arbitraion state',
                    'handle': 'path/to/simulink/blk',
                    'lsb': 1,
                    'max': 9,
                    'min': 0,
                    'name': 'sig1',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-'
                    }
            },
            'isig2': {
                'VcFnc2': {
                    'class': 'CVC_EXT',
                    'configs': [['CFG', 'CFG1', 'CFG2']],
                    'description': 'Torque arbitraion state',
                    'handle': 'path/to/simulink/blk',
                    'lsb': 1,
                    'max': 9,
                    'min': 0,
                    'name': 'sig2',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-'
                    }
            },
            'isig3': {
                'VcFnc1': {
                    'class': 'CVC_EXT',
                    'configs': [['CFG', 'CFG1', 'CFG2']],
                    'description': 'Torque arbitraion state',
                    'handle': 'path/to/simulink/blk',
                    'lsb': 1,
                    'max': 9,
                    'min': 0,
                    'name': 'sig3',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-'
                    }
            },
            'sigI1': {
                'VcFnc1': {
                    'class': 'CVC_EXT',
                    'configs': [['CFG', 'CFG1', 'CFG2']],
                    'description': 'Torque arbitraion state',
                    'handle': 'path/to/simulink/blk',
                    'lsb': 1,
                    'max': 9,
                    'min': 0,
                    'name': 'sig1',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-'
                    }
            },
            'sigI2': {
                'VcFnc1': {
                    'class': 'CVC_EXT',
                    'configs': [['all']],
                    'description': 'Torque arbitraion state',
                    'handle': 'path/to/simulink/blk',
                    'lsb': 1,
                    'max': 9,
                    'min': 0,
                    'name': 'sig2',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-'
                    }
            },
        },
        'outports': {
            'osig1': {
                'VcFnc2': {
                    'class': 'CVC_DISP',
                    'configs': [['all']],
                    'description': 'Torque arbitraion state',
                    'handle': 'path/to/simulink/blk',
                    'lsb': 1,
                    'max': '9',
                    'min': 0,
                    'name': 'sig1',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-'
                    }
            },
            'osig2': {
                'VcFnc2': {
                    'class': 'CVC_DISP',
                    'configs': [['all']],
                    'description': 'Torque arbitraion state',
                    'handle': 'path/to/simulink/blk',
                    'lsb': 1,
                    'max': '9',
                    'min': 0,
                    'name': 'sig2',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-'
                    }
            },
            'sigI1': {
                'VcFnc2': {
                    'class': 'CVC_DISP',
                    'configs': [['all']],
                    'description': 'Torque arbitraion state',
                    'handle': 'path/to/simulink/blk',
                    'lsb': 1,
                    'max': 9,
                    'min': 0,
                    'name': 'sig1',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-'
                    }
            },
            'sigI2': {
                'VcFnc2': {
                    'class': 'CVC_DISP',
                    'configs': [['all']],
                    'description': 'Torque arbitraion state',
                    'handle': 'path/to/simulink/blk',
                    'lsb': 1,
                    'max': 9,
                    'min': 0,
                    'name': 'sig2',
                    'offset': 0,
                    'type': 'UInt8',
                    'unit': '-'
                    }
            },
        }
    }
    _tot_cfg = copy.deepcopy(tmp_cfg)

    def __init__(self):
        self.restore()

    def restore(self):
        """Restore something the tot_cfg."""
        self.tot_cfg = copy.deepcopy(self._tot_cfg)

    def get_tot_ucfg_consistent(self):
        """Generate consistent data of total unit configuration."""
        return self.tot_cfg


def mock_parse_io_cfg(mock_cfg, *_):
    """Does not read config from file, but get conf data from fixed dicts."""
    # Arrrgh! Stupid name-mangling.
    mock_cfg.interfaces = SigIfCfg.interfaces


class BaseSetUp(unittest.TestCase):
    """Inerhitence from this class for all testcases.

    Start the calling this setUpClass method from the setUpClass method in the
    test case, and then modify the base setup in the test case (if needed).
    """

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        super().setUp()
        self.tot_cfg = TotUCfg()
        SigIfCfg.restore()

        self.ucfg = MagicMock(spec_set=UnitConfigs)
        self.ucfg.get_per_cfg_unit_cfg = MagicMock(
            side_effect=self.tot_cfg.get_tot_ucfg_consistent)

        config_dir = Path(Path(__file__).parent, 'cnfg_files')
        build_cfg = MagicMock(spec_set=BuildProjConfig)
        build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        build_cfg.get_prj_cfg_dir = MagicMock(
            return_value=str(config_dir))
        build_cfg.get_if_cfg_dir = MagicMock(
            return_value=str(Path(config_dir, 'ActiveInterfaces')))
        self.build_cfg = build_cfg

        # Patch the CsvSignalInterfaces class to not read the configuration file,
        # but instead use the dicts in this test file.
        patcher_sig_parse = patch.object(CsvSignalInterfaces,
                                         '_parse_io_cnfg',
                                         mock_parse_io_cfg)
        patcher_sig_parse.start()
        self.addCleanup(patcher_sig_parse.stop)
        self.maxDiff = None


class TestSignalIterfacesConsistent(BaseSetUp):
    """Test the CsvSignalInterfaces class with consistent data."""

    def setUp(self):
        super().setUp()
        SigIfCfg.restore()
        self.sigif = CsvSignalInterfaces(self.build_cfg, self.ucfg)

    def test__init__(self):
        """Check that the class can be initialized."""
        self.assertIsInstance(self.sigif, CsvSignalInterfaces)

    def test_get_raw_io_cnfg(self):
        """Check that the class returns correct raw io config."""
        result = self.sigif.get_raw_io_cnfg()
        expected = SigIfCfg.interfaces
        self.assertDictEqual(result, expected)

    def test_get_io_config(self):
        """Check that the class returns correct io config for
        specific project."""
        result = self.sigif.get_io_config()[0]
        expected = {
            'CAN-Input': {},
            'CAN-Output': {},
            'EMS-Input': {'isig1': {'IOType': 'x',
                                    'description': 'Torque arbitraion state',
                                    'init': 0,
                                    'max': 9,
                                    'min': 0,
                                    'offset': 0,
                                    'type': 'UInt8',
                                    'unit': '-'},
                          'isig2': {'IOType': 'x',
                                    'description': 'Torque arbitraion state',
                                    'init': 0,
                                    'max': 9,
                                    'min': 0,
                                    'offset': 0,
                                    'type': 'UInt8',
                                    'unit': '-'},
                          'isig3': {'IOType': 'x',
                                    'description': 'Torque arbitraion state',
                                    'init': 0,
                                    'max': 9,
                                    'min': 0,
                                    'offset': 0,
                                    'type': 'UInt8',
                                    'unit': '-'}},
            'EMS-Output': {'osig1': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'},
                           'osig2': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'},
                           'sigI1': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'},
                           'sigI2': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'}},
            'LIN-Input': {},
            'LIN-Output': {},
            'Private CAN-Input': {},
            'Private CAN-Output': {}}
        self.assertDictEqual(result, expected)

    def test_get_external_io(self):
        """Check that the class returns correct external io config."""
        result = self.sigif.get_io_config()[0]
        expected = {
            'CAN-Input': {},
            'CAN-Output': {},
            'EMS-Input': {'isig1': {'IOType': 'x',
                                    'description': 'Torque arbitraion state',
                                    'init': 0,
                                    'max': 9,
                                    'min': 0,
                                    'offset': 0,
                                    'type': 'UInt8',
                                    'unit': '-'},
                          'isig2': {'IOType': 'x',
                                    'description': 'Torque arbitraion state',
                                    'init': 0,
                                    'max': 9,
                                    'min': 0,
                                    'offset': 0,
                                    'type': 'UInt8',
                                    'unit': '-'},
                          'isig3': {'IOType': 'x',
                                    'description': 'Torque arbitraion state',
                                    'init': 0,
                                    'max': 9,
                                    'min': 0,
                                    'offset': 0,
                                    'type': 'UInt8',
                                    'unit': '-'}},
            'EMS-Output': {'osig1': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'},
                           'osig2': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'},
                           'sigI1': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'},
                           'sigI2': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'}},
            'LIN-Input': {},
            'LIN-Output': {},
            'Private CAN-Input': {},
            'Private CAN-Output': {}}
        self.assertDictEqual(result, expected)

    def test_get_external_inputs(self):
        """Check that the class returns correct external inputs list."""
        result = self.sigif.get_external_inputs()
        expected = {
            'CAN-Input': {},
            'EMS-Input': {'isig1': {'IOType': 'x',
                                    'description': 'Torque arbitraion state',
                                    'init': 0,
                                    'max': 9,
                                    'min': 0,
                                    'offset': 0,
                                    'type': 'UInt8',
                                    'unit': '-'},
                          'isig2': {'IOType': 'x',
                                    'description': 'Torque arbitraion state',
                                    'init': 0,
                                    'max': 9,
                                    'min': 0,
                                    'offset': 0,
                                    'type': 'UInt8',
                                    'unit': '-'},
                          'isig3': {'IOType': 'x',
                                    'description': 'Torque arbitraion state',
                                    'init': 0,
                                    'max': 9,
                                    'min': 0,
                                    'offset': 0,
                                    'type': 'UInt8',
                                    'unit': '-'}},
            'LIN-Input': {},
            'Private CAN-Input': {}}
        self.assertDictEqual(result, expected)

    def test_get_external_outputs(self):
        """Check that the class returns correct external outputs list."""
        result = self.sigif.get_external_outputs()
        expected = {
            'CAN-Output': {},
            'EMS-Output': {'osig1': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'},
                           'osig2': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'},
                           'sigI1': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'},
                           'sigI2': {'IOType': 'x',
                                     'description': 'Torque arbitraion state',
                                     'init': 0,
                                     'max': 9,
                                     'min': 0,
                                     'offset': 0,
                                     'type': 'UInt8',
                                     'unit': '-'}},
            'LIN-Output': {},
            'Private CAN-Output': {}}
        self.assertDictEqual(result, expected)

    def test_check_config(self):
        """Check that the class returns correct configuration check data."""
        result = self.sigif.check_config()
        expected = {
            'sigs': {
                'ext': {},
                'int': {}
            }
        }
        self.assertDictEqual(result, expected)

    def test_check_config_missing(self):
        """Check that the class can handle incorrect indata."""
        self.ucfg.get_per_cfg_unit_cfg = MagicMock(return_value={})
        result = self.sigif.check_config()
        expected = {
            'sigs': {
                'ext': {},
                'int': {}
            }
        }
        self.assertDictEqual(result, expected)


class TestSignalIterfacesExtIncons(BaseSetUp):
    """Test the CsvSignalInterfaces class with external incosistent data."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        BaseSetUp.setUp(self)

    def test_clean(self):
        """Check that the unused external output signals are detected."""
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                },
                'int': {}
            }
        }
        self.assertDictEqual(result, expected)

    def test_missing_ext_inp_vcc(self):
        """Check that the missing external input signals are detected."""
        del self.tot_cfg.tot_cfg['outports']['osig1']
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                    'missing': {
                        'osig1': {}
                    }
                },
                'int': {}
            }
        }
        self.assertDictEqual(result, expected)

    def test_unused_ext_outp_vcc(self):
        """Check that the unused external output signals are detected."""
        del self.tot_cfg.tot_cfg['inports']['isig1']
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                    'unused': {'isig1': {}}
                },
                'int': {}
            }
        }
        self.assertDictEqual(result, expected)

    def test_unused_ext_inp_io(self):
        """Check that the missing input signals in the ext io are detected.

        They should be detected as missing internal input signals.
        """
        del SigIfCfg.interfaces['EMS-Input']['isig1']
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                },
                'int': {
                    'VcFnc1': {
                        'missing': {
                            'isig1': {}
                        }
                    }
                }
            }
        }
        self.assertDictEqual(result, expected)

    def test_unused_ext_outp_io(self):
        """Check that the missing output signals in the ext io are detected.

        They should be detcted as unsued internal input signals.
        """
        del SigIfCfg.interfaces['EMS-Output']['osig1']
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                },
                'int': {
                    'VcFnc2': {
                        'unused': {
                            'osig1': {}
                        }
                    }
                }
            }
        }
        self.assertDictEqual(result, expected)

    def test_incos_ext_inp(self):
        """Check signal definition incosistencies between ext inp & int SW def.

        Faults are injected by chaging the external IO definition.
        """
        SigIfCfg.interfaces['EMS-Input']['isig1']['max'] = 10
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                    'inconsistent_defs': {
                        'VcFnc1': {
                            'isig1': {
                                'max': '10 != 9'
                            }
                        }
                    }
                },
                'int': {}
            }
        }
        self.assertDictEqual(result, expected)

    def test_incos_ext_outp(self):
        """Check signal definition incosistencies between ext outp & int SW def.

        Faults are injected by chaging the external IO definition.
        """
        SigIfCfg.interfaces['EMS-Output']['osig2']['min'] = 1
        SigIfCfg.interfaces['EMS-Output']['osig2']['max'] = 10
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                    'inconsistent_defs': {
                        'VcFnc2': {
                            'osig2': {
                                'min': '1 != 0',
                                'max': '10 != 9'
                            }
                        }
                    }
                },
                'int': {}
            }
        }
        self.assertDictEqual(result, expected)

    def test_incos_int_outp(self):
        """Check signal definition incosistencies between ext outp & int SW def.

        Faults are injected by chaging the VCC SW definition.
        """
        self.tot_cfg.tot_cfg['inports']['isig1']['VcFnc1']['min'] = 1
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                    'inconsistent_defs': {
                        'VcFnc1': {
                            'isig1': {
                                'min': '0 != 1'
                            }
                        }
                    }
                },
                'int': {}
            }
        }
        self.assertDictEqual(result, expected)


class TestSignalIterfacesIntIncons(BaseSetUp):
    """Test the CsvSignalInterfaces class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        BaseSetUp.setUp(self)

    def test_incos_int_incons_def(self):
        """Test inconsistencies between VCC SW units."""
        self.tot_cfg.tot_cfg['inports']['sigI1']['VcFnc1']['min'] = 2
        self.tot_cfg.tot_cfg['inports']['sigI1']['VcFnc1']['max'] = 2
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                },
                'int': {
                    'VcFnc1': {
                        'inconsistent_defs': {
                            'sigI1': {
                                'min': '0 != 2',
                                'max': '9 != 2'
                            }
                        }
                    }
                }
            }
        }
        self.assertDictEqual(result, expected)

    def test_incos_int_missing(self):
        """Test inconsistencies between VCC SW units."""
        del self.tot_cfg.tot_cfg['outports']['sigI1']
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                    'missing': {
                        'sigI1': {}
                    }
                },
                'int': {
                    'VcFnc1': {
                        'missing': {
                            'sigI1': {}
                        }
                    }
                }
            }
        }
        self.assertDictEqual(result, expected)

    def test_incos_int_unused(self):
        """Test inconsistencies between VCC SW units."""
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                },
                'int': {
                }
            }
        }
        self.assertDictEqual(result, expected)

    def test_incos_int_multiple_def(self):
        """Test detection of multiple definitions in VCC SW units."""
        self.tot_cfg.tot_cfg['outports']['sigI2']['VcFnc3'] = \
            {
                'class': 'CVC_DISP',
                'configs': [['all']],
                'description': 'Torque arbitraion state',
                'handle': 'path/to/simulink/blk',
                'lsb': 1,
                'max': 9,
                'min': 0,
                'name': 'sig1',
                'offset': 0,
                'type': 'UInt8',
                'unit': '-'
            }
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        pprint.pprint(csi._unit_cfg.get_per_cfg_unit_cfg())
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                },
                'int': {
                    'VcFnc2': {
                        'multiple_defs': {
                            'sigI2': {}
                        }
                    },
                    'VcFnc3': {
                        'multiple_defs': {
                            'sigI2': {}
                        }
                    }
                }
            }
        }
        self.assertDictEqual(result, expected)

    def test_clean(self):
        """Test detection of multiple definitions in VCC SW units."""
        csi = CsvSignalInterfaces(self.build_cfg, self.ucfg)
        result = csi.check_config()
        expected = {
            'sigs': {
                'ext': {
                },
                'int': {
                }
            }
        }
        self.assertDictEqual(result, expected)
