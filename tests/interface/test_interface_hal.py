# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Test cases for the HAL interface."""

import unittest
from unittest import mock

from pybuild.interface.base import Signal
from pybuild.interface.hal import HALA

SIGNAL_SPEC = (
    "enum_0",  # enum padding
    "property1",  # property
    "float",  # property_interface_type
    "Float32",  # variable_type
    0,  # offset
    1,  # factor
    0,  # default
    1,  # length
    -100,  # min
    100,  # max
    False,  # enum
    0,  # init
    "Description",  # description
    "Nm",  # unit
    "API",  # endpoint
    "interface",  # api
    "properties",  # variant
)


class TestHal(unittest.TestCase):
    """Test cases for the HAL interface."""

    def setUp(self):
        dummy_app = mock.MagicMock()
        self.hal = HALA(dummy_app)

    def test_add_signals(self):
        """Test add_signals method."""
        insignal1 = Signal("test_name_in1", None)
        insignal2 = Signal("test_name_in2", None)
        outsignal = Signal("test_name_out", None)
        signal_spec = SIGNAL_SPEC

        test_signal1 = list(signal_spec)
        test_signal1[14] = "endpoint1"
        test_signal_1 = tuple(test_signal1)

        test_signal2 = list(signal_spec)
        test_signal2[14] = "endpoint1"
        test_signal_2 = tuple(test_signal2)

        test_signal3 = list(signal_spec)
        test_signal3[14] = "endpoint3"
        test_signal_3 = tuple(test_signal3)
        self.hal.translations = {
            "test_name_in1": {test_signal_1},
            "test_name_in2": {test_signal_2},
            "test_name_out": {test_signal_3},
        }

        self.hal.add_signals([insignal1], "insignals")
        expected = {
            "app": {"insignals": {"test_name_in1"}, "outsignals": set()},
            "api": {"insignals": set(), "outsignals": {"property1"}},
        }
        expected_signal_primitives_list = ["interface.properties.endpoint1.property1.insignals"]
        self.assertDictEqual(expected, self.hal.signal_names)
        self.assertListEqual(expected_signal_primitives_list, self.hal.signal_primitives_list)

        self.hal.add_signals([outsignal], "outsignals")
        expected = {
            "app": {
                "insignals": {"test_name_in1"},
                "outsignals": {"test_name_out"},
            },
            "api": {"insignals": {"property1"}, "outsignals": {"property1"}},
        }
        self.assertDictEqual(expected, self.hal.signal_names)
        expected_signal_primitives_list = ["interface.properties.endpoint1.property1.insignals",
                                           "interface.properties.endpoint3.property1.outsignals"]
        self.assertDictEqual(expected, self.hal.signal_names)
        self.assertListEqual(expected_signal_primitives_list, self.hal.signal_primitives_list)

        exception_msg = "You can't write interface.properties.endpoint1.property1.insignals"\
            " as insignals since this primitive has been used."\
            " Run model_yaml_verification to identify exact models."
        with self.assertRaises(Exception) as context:
            self.hal.add_signals([insignal2], "insignals")
        self.assertEqual(exception_msg, str(context.exception))

    def test_extract_definition(self):
        """Test extract_definition method."""
        # Old hals
        definition = [{
            'ClutchModeRequest': [
                {
                    'outsignal': 'sVcScOut_D_DftlCluModReqReLe',
                    'property': 'rear_left'
                },
                {
                    'outsignal': 'sVcScOut_D_DftlCluModReqReRi',
                    'property': 'rear_right'
                }
            ],
            'ClutchTorqueCapacityRequest': [
                {
                    'outsignal': 'sVcScOut_Tq_DftlCluTqCpReqReLe',
                    'property': 'rear_left'
                },
                {
                    'outsignal': 'sVcScOut_Tq_DftlCluTqCpReqReRi',
                    'property': 'rear_right'
                }
            ]
        }]
        expected = {'hals': definition}
        result = self.hal.extract_definition(definition)
        self.assertDictEqual(expected, result)

        # New HALs (as of 2021-07-08) supporting methods (and properties)
        definition = {
            'methods': [{
                'RequestClutchMode': [
                    {
                        'outsignal': 'sVcScOut_D_DftlCluModReqReLe',
                        'property': 'rear_left'
                    },
                    {
                        'outsignal': 'sVcScOut_D_DftlCluModReqReRi',
                        'property': 'rear_right'
                    }
                ],
                'RequestClutchTorque': [
                    {
                        'outsignal': 'sVcScOut_Tq_DftlCluTqCpReqReLe',
                        'property': 'rear_left'
                    },
                    {
                        'outsignal': 'sVcScOut_Tq_DftlCluTqCpReqReRi',
                        'property': 'rear_right'
                    }
                ]
            }]
        }
        expected = {
            'properties': [],
            'methods': definition['methods']
        }
        result = self.hal.extract_definition(definition)
        self.assertDictEqual(expected, result)
