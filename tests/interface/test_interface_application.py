# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

import pathlib
import unittest
from unittest import mock

from pybuild.interface.application import Application, Raster, Model
from pybuild.interface.base import Signal


class TestApplication(unittest.TestCase):
    def test_parse_definition(self):
        # Tested in pybuild.
        pass

    def test_parse_ports(self):
        app = Application()
        app._insignals = set()
        app._outsignals = set()
        defined_ports = {'inports': set(), 'outports': set()}
        port_data = {
            'inports': {
                'signal_1': {
                    'configs': 'dummy'
                }
            },
            'outports': {
                'signal_2': {
                    'configs': 'dummy'
                }
            }
        }
        feature_cfg = mock.MagicMock()
        feature_cfg.check_if_active_in_config.return_value = True
        app.parse_ports(port_data, defined_ports, feature_cfg, 'model_1')
        expected_data = {
            'inports': {'signal_1'},
            'outports': {'signal_2'}
        }
        self.assertDictEqual(defined_ports, expected_data)
        self.assertSetEqual({s.name for s in app.insignals}, expected_data['inports'])
        self.assertSetEqual({s.name for s in app.outsignals}, expected_data['outports'])

    @mock.patch.object(Raster, 'parse_definition')
    def test_get_rasters(self, raster_parser):
        pybuild_raster_definition = {
            'SampleTimes': {'raster1': '0.01', 'raster2': '0.02'},
            'Scheduled': {
                'raster1': ['model_1', 'model_2'],
                'raster2': ['model_3', 'model_4']
            }
        }
        app = Application()
        app.pybuild['build_cfg'] = mock.MagicMock()
        app.pybuild['build_cfg'].get_units_raster_cfg.return_value = pybuild_raster_definition
        app._insignals = {'signal1'}
        app._outsignals = set()
        app._signals = {'signal1': {}}
        app.pybuild['unit_vars'] = {
            'model_1': {
            },
            'model_2': {
            }
        }
        rasters = app.get_rasters()
        raster_parser.assert_any_call(('raster1', ['model_1', 'model_2'], {'signal1': {}}))
        raster_parser.assert_any_call(('raster2', ['model_3', 'model_4'], {'signal1': {}}))
        self.assertEqual(len(rasters), 2)

    def test_signals(self):
        app = Application()
        app.pybuild['unit_vars'] = {
            'model_1': {
                'outports': {
                    'signal_1_1': {
                        'configs': 'dummy'
                    },
                    'signal_1_2': {
                        'configs': 'dummy'
                    },
                },
                'inports': {
                    'signal_2_1': {
                        'configs': 'dummy'
                    },
                    'extern_1': {
                        'configs': 'dummy'
                    },
                    'extern_2': {
                        'configs': 'dummy'
                    },
                }
            },
            'model_2': {
                'outports': {
                    'signal_2_1': {
                        'configs': 'dummy'
                    },
                    'signal_2_2': {
                        'configs': 'dummy'
                    },
                },
                'inports': {
                    'signal_1_1': {
                        'configs': 'dummy'
                    },
                    'extern_2': {
                        'configs': 'dummy'
                    },
                    'extern_3': {
                        'configs': 'dummy'
                    },
                }
            }
        }
        app.pybuild['feature_cfg'] = mock.MagicMock()
        app.pybuild['feature_cfg'].check_if_active_in_config.return_value = True
        self.assertSetEqual({s.name for s in app.insignals}, {'extern_1', 'extern_2', 'extern_3'})
        self.assertSetEqual({s.name for s in app.outsignals}, {'signal_1_1', 'signal_1_2', 'signal_2_1', 'signal_2_2'})

    def test_signal_properties(self):
        app = Application()
        app.pybuild['build_cfg'] = mock.MagicMock()
        app._insignals = set()
        app._outsignals = {'signal1'}
        signal_def = Signal('signal1', app)
        signal_def.producer = 'model_1'
        app._signals = {'signal1': signal_def}
        app.pybuild['unit_vars'] = {
            'model_1': {
                'outports': {
                    'signal1': {
                        'configs': 'dummy',
                    },
                }
            }
        }
        self.assertEqual(app.outsignals[0].properties['configs'], 'dummy')

    def test_get_name(self):
        app = Application()
        app.name = 'test'
        self.assertEqual(app.get_name('dummy_path'), 'test')


class TestRaster(unittest.TestCase):
    def test_parse_definition(self):
        raster = Raster(None)
        raster.parse_definition(('raster_name', ['model1', 'model2'], {}))
        self.assertSetEqual(raster.models, {'model1', 'model2'})

    def test_signals(self):
        signals = {'signal1': Signal('signal1', None),
                   'signal2': Signal('signal2', None),
                   'signal3': Signal('signal3', None)}
        signals['signal1'].producer = 'model1'
        signals['signal2'].producer = 'model2'
        signals['signal2'].consumers = 'model1'
        signals['signal3'].consumers = 'model2'
        raster = Raster(None)
        raster.parse_definition(('raster_name', ['model1', 'model2'], signals))
        self.assertSetEqual(raster.models, {'model1', 'model2'})
        self.assertSetEqual({s.name for s in raster.insignals}, {'signal3'})
        self.assertSetEqual({s.name for s in raster.outsignals}, {'signal1', 'signal2'})


class TestModel(unittest.TestCase):
    def test_parse_definition(self):
        model = Model(None)
        dummy_model_config = {'inports': {'mdl_signal': {'name': 'mdl_signal'}}, 'outports': {}}
        model._load_json = mock.MagicMock()
        model._load_json.side_effect = [dummy_model_config]
        model.parse_definition(('test', pathlib.Path('path', 'to', 'a', 'file')))
        self.assertSetEqual(model._insignals, set(['mdl_signal']))
        self.assertSetEqual(model._outsignals, set())

        dummy_model_config_mdl = {'inports': {'mdl_signal': {'name': 'mdl_signal'}},
                                  'outports': {},
                                  'includes': ['dummy_model_c']}
        dummy_model_config_c = {'inports': {'c_isignal': {'name': 'c_isignal'}},
                                'outports': {'c_osignal': {'name': 'c_osignal'}}}
        model._load_json = mock.MagicMock()
        model._load_json.side_effect = [dummy_model_config_mdl, dummy_model_config_c]
        model.parse_definition(('test', pathlib.Path('path', 'to', 'a', 'file')))
        self.assertSetEqual(model._insignals, set(['mdl_signal', 'c_isignal']))
        self.assertSetEqual(model._outsignals, set(['c_osignal']))

    def test_get_signal_properties(self):
        model = Model(None)
        signal_properties = {'a': 1, 'b': 2}
        model._signal_specs = {'test': signal_properties}
        signal = Signal('test', model)
        self.assertDictEqual(signal.properties, signal_properties)
