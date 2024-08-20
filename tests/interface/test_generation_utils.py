# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Test cases for the generation utils."""

import unittest
from unittest import mock

from powertrain_build.interface import generation_utils
from powertrain_build.interface.application import Application, Raster
from powertrain_build.interface.base import Signal
from powertrain_build.interface.hal import HALA


class TestGenerationUtils(unittest.TestCase):
    """Test cases for the generation utils."""

    @mock.patch('powertrain_build.interface.application.Raster.insignals', new_callable=mock.PropertyMock)
    @mock.patch('powertrain_build.interface.application.Raster.outsignals', new_callable=mock.PropertyMock)
    @mock.patch('powertrain_build.interface.csp_api.CspApi.read_translation')
    @mock.patch('powertrain_build.interface.hal.HALA.get_map_file')
    @mock.patch('powertrain_build.interface.hal.HALA._get_hal_translation')
    def test_get_interface(self, mock_hal_translation, mock_hal_file, mock_read_file, raster_out, raster_in):
        """Test get_interface method."""
        # Setup signals
        mocked_app_1 = mock.MagicMock()
        mocked_app_2 = mock.MagicMock()
        mocked_app_1.get_signal_properties.return_value = {
                        'configs': 'dummy',
                        'type': 'Bool',
                        'description': 'Dummy description',
                        'min': 0,
                        'max': 5,
                        'init': 0,
                        'unit': 'Nm',
                        'offset': 1,
                        'factor': 2,
                        'lsb': 1
        }
        mocked_app_2.get_signal_properties.return_value = {
                        'configs': 'dummy',
                        'type': 'Float32',
                        'description': 'Dummy description',
                        'min': 0,
                        'max': 5,
                        'init': 0,
                        'unit': 'Nm',
                        'offset': 1,
                        'factor': 2,
                        'lsb': 1
        }
        hal_to_app = Signal('hal_to_app', mocked_app_1)
        app_to_hal = Signal('app_to_hal', mocked_app_2)
        unrelated_signal_1 = Signal('unrelated_signal_1', None)
        unrelated_signal_2 = Signal('unrelated_signal_2', None)

        # Setup dummy project
        app = Application()
        app.name = 'DummyApp'
        app.pybuild['unit_vars'] = {}
        app.pybuild['feature_cfg'] = mock.MagicMock()
        app.pybuild['build_cfg'] = mock.MagicMock()
        app.pybuild['user_defined_types'] = mock.MagicMock()
        app.pybuild['unit_vars'] = {
            'dummy_model': {
                'inports': {
                    'hal_to_app': {
                        'configs': 'dummy',
                        'type': 'Bool',
                        'description': 'Dummy description',
                        'min': 0,
                        "max": 5,
                        'init': 0,
                        'unit': 'Nm',
                        'offset': 1,
                        'factor': 2
                    }
                },
                'outports': {
                    'app_to_hal': {
                        'type': 'Float32',
                        'configs': 'dummy',
                        'description': 'Dummy description',
                        'min': 0,
                        "max": 5,
                        'init': 0,
                        'unit': 'Nm',
                        'offset': 1,
                        'factor': 2
                    }
                }
            }
        }
        app.get_map_file = mock.MagicMock()
        app.get_translation_files = mock.MagicMock(return_value=['dummy_file'])
        raster_in.return_value = [hal_to_app, unrelated_signal_1]
        raster_out.return_value = [app_to_hal, unrelated_signal_2]
        dummy_raster = Raster(app)
        dummy_raster.name = 'DummyRaster'
        app.get_rasters = mock.MagicMock(return_value=[dummy_raster])

        # Setup dummy hal
        mock_read_file.return_value = {
            'hal': {
                'dummy_hal1': [{
                    'hal_set':
                        [{
                            'outsignal': 'app_to_hal',
                        }],
                    'hal_get':
                        [{
                            'insignal': 'hal_to_app'
                        }]
                }],
                'dummy2': [{
                    'HalGroup1': [
                        {
                            'property': 'hal_set',
                            'outsignal': 'app_to_hal'
                        },
                        {
                            'property': 'hal_get',
                            'insignal': 'hal_to_app'
                        }
                    ]
                }]
            }
        }
        mock_hal_translation.return_value = {
            'dummy1': 'DummyHal1',
            'dummy2': 'DummyHal2'
        }
        # Verify results
        hala = HALA(app)
        result = generation_utils.get_interface(app, hala)
        expected_result = {
            'relocatable_language': 'C',
            'DummyRaster': {
                'consumer': [
                    {
                        'variable': 'hal_to_app',
                        'variable_type': 'Bool',
                        'property': None,
                        'property_type': 'Bool',
                        'default': None,
                        'length': None,
                        'offset': 1,
                        'factor': 1,
                        'range': {'min': 0, 'max': 5},
                        'init': 0,
                        'description': 'Dummy description',
                        'unit': 'Nm',
                        'endpoint': 'hal_get',
                        'api': 'DummyHal1',
                        'variant': 'hals',
                        'strategy': 'Always',
                        'debug': False,
                        'dependability': False
                    },
                    {
                        'variable': 'hal_to_app',
                        'variable_type': 'Bool',
                        'property': 'hal_get',
                        'property_type': 'Bool',
                        'default': None,
                        'length': None,
                        'offset': 1,
                        'factor': 1,
                        'range': {'min': 0, 'max': 5},
                        'init': 0,
                        'description': 'Dummy description',
                        'unit': 'Nm',
                        'endpoint': 'HalGroup1',
                        'api': 'DummyHal2',
                        'variant': 'hals',
                        'strategy': 'Always',
                        'debug': False,
                        'dependability': False
                    }
                ],
                'producer': [
                    {
                        'variable': 'app_to_hal',
                        'variable_type': 'Float32',
                        'property': 'hal_set',
                        'property_type': 'Float32',
                        'default': None,
                        'length': None,
                        'offset': 1,
                        'factor': 1,
                        'range': {'min': 0, 'max': 5},
                        'init': 0,
                        'description': 'Dummy description',
                        'unit': 'Nm',
                        'endpoint': 'HalGroup1',
                        'api': 'DummyHal2',
                        'variant': 'hals',
                        'strategy': 'Always',
                        'debug': False,
                        'dependability': False
                    },
                    {
                        'variable': 'app_to_hal',
                        'variable_type': 'Float32',
                        'property': None,
                        'property_type': 'Float32',
                        'default': None,
                        'length': None,
                        'offset': 1,
                        'factor': 1,
                        'range': {'min': 0, 'max': 5},
                        'init': 0,
                        'description': 'Dummy description',
                        'unit': 'Nm',
                        'endpoint': 'hal_set',
                        'api': 'DummyHal1',
                        'variant': 'hals',
                        'strategy': 'Always',
                        'debug': False,
                        'dependability': False
                    }
                ]
            }
        }
        self.assertCountEqual(result['DummyRaster']['consumer'], expected_result['DummyRaster']['consumer'])
        self.assertCountEqual(result['DummyRaster']['producer'], expected_result['DummyRaster']['producer'])
