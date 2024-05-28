# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

import unittest
from unittest import mock
from pathlib import Path

from pybuild.interface.base import Signal
from pybuild.interface.service import ServiceFramework, get_service_list
from pybuild.interface.csp_api import MissingApi


SIGNAL_SPEC = (
    "enum_0",  # enum padding
    "property1",  # property
    "Float32",  # property_interface_type
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
    "Always",  # strategy
    False,  # debug
    False,  # dependability
)


class TestFunctions(unittest.TestCase):
    def test_get_service_list(self):
        dummy_app = mock.MagicMock()
        dummy_app.get_service_mapping = mock.MagicMock(
            return_value={'interface': 'service'}
        )
        service_list = get_service_list(dummy_app)
        expected_services = ("LIST(APPEND extra_libraries"
                             " ${SERVICE_LIBINTERFACE_SERVICE_PROXY})\n"
                             "LIST(APPEND EXTRA_INCLUDE_DIRS"
                             " ${SERVICE_INCLUDE_DIR})\n")

        self.assertEqual(expected_services, service_list)


class TestSfw(unittest.TestCase):
    def test_parse_definition(self):
        spec = {
            'services': {}
        }
        dummy_app = mock.MagicMock()
        sfw = ServiceFramework(dummy_app)
        sfw.read_translation = mock.MagicMock(return_value=spec)
        sfw.parse_definition('no_file')
        self.assertDictEqual(sfw.translations, {})

    def test_add_signals(self):
        dummy_app = mock.MagicMock()
        sfw = ServiceFramework(dummy_app)
        insignal1 = Signal("test_name_in1", None)
        insignal2 = Signal("test_name_in2", None)
        outsignal = Signal("test_name_out", None)
        signal_spec = SIGNAL_SPEC

        test_signal1 = list(signal_spec)
        test_signal1[14] = "endpoint1"
        test_signal_1 = tuple(test_signal1)

        test_signal2 = list(signal_spec)
        test_signal2[14] = "endpoint2"
        test_signal_2 = tuple(test_signal2)

        test_signal3 = list(signal_spec)
        test_signal3[14] = "endpoint3"
        test_signal_3 = tuple(test_signal3)
        sfw.translations = {
            "test_name_in1": {test_signal_1},
            "test_name_in2": {test_signal_2},
            "test_name_out": {test_signal_3},
        }

        sfw.add_signals([insignal1], "insignals")
        expected = {
            "app": {"insignals": {"test_name_in1"}, "outsignals": set()},
            "api": {"insignals": set(), "outsignals": {"property1"}},
        }
        expected_signal_primitives_list = ["interface.properties.endpoint1.property1.insignals"]
        self.assertDictEqual(expected, sfw.signal_names)
        self.assertListEqual(expected_signal_primitives_list, sfw.signal_primitives_list)

        sfw.add_signals([insignal2], "insignals")
        expected = {
            "app": {
                "insignals": {"test_name_in1", "test_name_in2"},
                "outsignals": set(),
            },
            "api": {"insignals": set(), "outsignals": {"property1"}},
        }
        self.assertDictEqual(expected, sfw.signal_names)
        expected_signal_primitives_list = ["interface.properties.endpoint1.property1.insignals",
                                           "interface.properties.endpoint2.property1.insignals"]
        self.assertDictEqual(expected, sfw.signal_names)
        self.assertListEqual(expected_signal_primitives_list, sfw.signal_primitives_list)

        sfw.add_signals([outsignal], "outsignals")
        expected = {
            "app": {
                "insignals": {"test_name_in1", "test_name_in2"},
                "outsignals": {"test_name_out"},
            },
            "api": {"insignals": {"property1"}, "outsignals": {"property1"}},
        }
        self.assertDictEqual(expected, sfw.signal_names)
        expected_signal_primitives_list = ["interface.properties.endpoint1.property1.insignals",
                                           "interface.properties.endpoint2.property1.insignals",
                                           "interface.properties.endpoint3.property1.outsignals"]
        self.assertDictEqual(expected, sfw.signal_names)
        self.assertListEqual(expected_signal_primitives_list, sfw.signal_primitives_list)

    def test_check_group_mixed_signals(self):
        dummy_app = mock.MagicMock()
        sfw = ServiceFramework(dummy_app)
        signal_spec = SIGNAL_SPEC
        test_signal = list(signal_spec)
        test_signal_1 = tuple(test_signal)
        test_signal_2 = tuple(test_signal)

        sfw.translations = {
            "test_signal_1": {test_signal_1},
            "test_signal_2": {test_signal_2}
        }

        sfw.signal_names["app"]["insignals"] = {
            "test_signal_1",
        }
        sfw.signal_names["app"]["outsignals"] = {
            "test_signal_2",
        }
        expected_message = "Signal endpoint API for interface contains both consumed and produced signals"

        with self.assertRaises(AssertionError) as context:
            sfw.check_endpoints()
        self.assertEqual(expected_message, str(context.exception))

    def test_missing_service(self):
        dummy_app = mock.MagicMock()
        dummy_app.get_service_mapping = mock.MagicMock(return_value={'other_interface': 'service'})
        dummy_app.get_services_file = mock.MagicMock(return_value=Path('file'))
        insignal1 = Signal("signal1", dummy_app)
        insignal2 = Signal("signal2", dummy_app)
        dummy_app.insignals = [insignal1, insignal2]
        dummy_app.get_signal_properties = mock.MagicMock(
            side_effect=[
                {'type': 'Float32'},
                {'type': 'Float32'}
            ]
        )
        sfw = ServiceFramework(dummy_app)
        service_definitions = {
            "interface": {
                "properties": [
                    {
                        "API": [
                            {
                                "insignal": "signal1",
                                "property": "property1"
                            },
                            {
                                "insignal": "signal2",
                                "property": "property2"
                            },
                        ]
                    }
                ]
            }
        }
        expected_message = "Api interface missing from file"
        with self.assertRaises(MissingApi) as context:
            sfw.parse_api_definitions(service_definitions)
        self.assertEqual(expected_message, context.exception.message)

    def test_parse_api_definitions(self):
        dummy_app = mock.MagicMock()
        dummy_app.get_service_mapping = mock.MagicMock(return_value={'interface': 'service'})
        dummy_app.insignals = [
            Signal("signal1", None),
            Signal("signal2", None),
            Signal("signal3", None),
            Signal("signal4", None),
            Signal("signal5", None)
        ]
        dummy_app.get_signal_properties = mock.MagicMock(
            side_effect=[
                {'type': 'Float32'},
                {'type': 'Float32'},
                {'type': 'Float32'},
                {'type': 'Float32'},
                {'type': 'Float32'}
            ]
        )
        sfw = ServiceFramework(dummy_app)
        service_definitions = {
            "interface": {
                "properties": [
                    {
                        "API": [
                            {
                                "insignal": "signal1",
                                "property": "property1"
                            },
                            {
                                "insignal": "signal2",
                                "property": "property2"
                            },
                        ],
                        "RAW_0": [
                            {
                                "insignal": "signal3",
                            }
                        ],
                        "RAW_1": [
                            {
                                "insignal": "signal4",
                                "property": None
                            }
                        ],
                        "RAW_2": [
                            {
                                "insignal": "signal5",
                                "property": ""
                            }
                        ],
                    }
                ]
            }
        }
        sfw.parse_api_definitions(service_definitions)
        expected = {
            'signal1': {('enum_0', 'property1', 'Float32', None, None, None, None, None, None, None,
                         None, 0, None, None, 'API', 'interface', 'properties', 'Always', False, False)},
            'signal2': {('enum_0', 'property2', 'Float32', None, None, None, None, None, None, None,
                         None, 0, None, None, 'API', 'interface', 'properties', 'Always', False, False)},
            'signal3': {('enum_0', None, 'Float32', None, None, None, None, None, None, None,
                         None, 0, None, None, 'RAW_0', 'interface', 'properties', 'Always', False, False)},
            'signal4': {('enum_0', None, 'Float32', None, None, None, None, None, None, None,
                         None, 0, None, None, 'RAW_1', 'interface', 'properties', 'Always', False, False)},
            'signal5': {('enum_0', None, 'Float32', None, None, None, None, None, None, None,
                         None, 0, None, None, 'RAW_2', 'interface', 'properties', 'Always', False, False)}
        }
        self.assertDictEqual(sfw.translations, expected)

    def test_parse_property_definitions_output_strategies(self):
        dummy_app = mock.MagicMock()
        dummy_app.get_service_mapping = mock.MagicMock(return_value={'interface': 'service'})
        outsignal1 = Signal("signal1", None)
        outsignal2 = Signal("signal2", None)
        outsignal3 = Signal("signal3", None)
        dummy_app.get_signal_properties = mock.MagicMock(
            side_effect=[
                {'type': 'Float32'},
                {'type': 'Float32'},
                {'type': 'Float32'}
            ]
        )
        dummy_app.outsignals = [outsignal1, outsignal2, outsignal3]
        sfw = ServiceFramework(dummy_app)
        signal_definitions = {
            "interface": [
                {
                    "outsignal": "signal1",
                    "strategy": "Always"  # Correct
                },
                {
                    "outsignal": "signal2",
                    "strategy": "OnChanged"  # Not allowed for outsignals
                },
                {
                    "outsignal": "signal3",
                    "strategy": "NonExistent"  # Invalid strategy
                }
            ]
        }

        sfw.parse_property_definitions(signal_definitions, 'API', 'properties')
        expected = {
            'signal1': {(
                'enum_0',
                None,
                'Float32',
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                0,
                None,
                None,
                'API',
                'interface',
                'properties',
                'Always',
                False,
                False
            )},
            'signal2': {(
                'enum_0',
                None,
                'Float32',
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                0,
                None,
                None,
                'API',
                'interface',
                'properties',
                'Always',
                False,
                False
            )},
            'signal3': {(
                'enum_0',
                None,
                'Float32',
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                0,
                None,
                None,
                'API',
                'interface',
                'properties',
                'Always',
                False,
                False
            )}
        }
        self.assertEqual(sfw.translations, expected)

    def test_parse_property_definitions_level_0(self):
        dummy_app = mock.MagicMock()
        dummy_app.get_service_mapping = mock.MagicMock(return_value={'interface': 'service'})
        insignal1 = Signal("signal1", None)
        dummy_app.get_signal_properties = mock.MagicMock(
            side_effect=[
                {'type': 'Float32'},
            ]
        )
        dummy_app.insignals = [insignal1]
        sfw = ServiceFramework(dummy_app)
        signal_definitions = {
            "interface": [
                {
                    "insignal": "signal1",
                },
            ]
        }

        sfw.parse_property_definitions(signal_definitions, 'API', 'properties')
        expected = {
            'signal1': {(
                'enum_0',
                None,
                'Float32',
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                0,
                None,
                None,
                'API',
                'interface',
                'properties',
                'Always',
                False,
                False
            )}
        }
        self.assertEqual(sfw.translations, expected)

    def test_parse_property_definitions_level_1(self):
        dummy_app = mock.MagicMock()
        insignal1 = Signal("signal1", None)
        insignal2 = Signal("signal2", None)
        dummy_app.get_signal_properties = mock.MagicMock(
            side_effect=[
                {'type': 'Float32'},
                {'type': 'Float32'}
            ]
        )
        dummy_app.insignals = [insignal1, insignal2]
        dummy_app.get_service_mapping = mock.MagicMock(return_value={'interface': 'service'})
        sfw = ServiceFramework(dummy_app)
        signal_definitions = {
            "interface": [
                {
                    "insignal": "signal1",
                    "property": "property1"
                },
                {
                    "insignal": "signal2",
                    "property": "property2"
                }
            ]
        }

        sfw.parse_property_definitions(signal_definitions, 'API', 'properties')
        expected = {
            'signal1': {(
                'enum_0',
                'property1',
                'Float32',
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                0,
                None,
                None,
                'API',
                'interface',
                'properties',
                'Always',
                False,
                False
            )},
            'signal2': {(
                'enum_0',
                'property2',
                'Float32',
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                0,
                None,
                None,
                'API',
                'interface',
                'properties',
                'Always',
                False,
                False
            )}
        }
        self.assertEqual(sfw.translations, expected)

    def test_parse_property_definitions_level_x(self):
        dummy_app = mock.MagicMock()
        dummy_app.get_service_mapping = mock.MagicMock(return_value={'interface': 'service'})
        dummy_app.get_signal_properties = mock.MagicMock(
            return_value={'type': 'Float32'}
        )
        dummy_app.insignals = [
            Signal("signal1", dummy_app),
            Signal("signal2", dummy_app),
            Signal("signal3", dummy_app),
            Signal("signal4", dummy_app),
        ]
        sfw = ServiceFramework(dummy_app)
        signal_definitions = {
            "interface": [
                {
                    "insignal": "signal1",
                    "property": "property0.member0"
                },
                {
                    "insignal": "signal2",
                    "property": "property0.member1"
                },
                {
                    "insignal": "signal3",
                    "property": "property1.member0.member0"
                },
                {
                    "insignal": "signal4",
                    "property": "property1.member1.member0.member0"
                },
            ]
        }

        sfw.parse_property_definitions(signal_definitions, 'API', 'properties')
        expected = {
            'signal1': {
                (
                    'enum_0',
                    'property0.member0',
                    'Float32',
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    0,
                    None,
                    None,
                    'API',
                    'interface',
                    'properties',
                    'Always',
                    False,
                    False
                )
            },
            'signal2': {(
                'enum_0', 'property0.member1', 'Float32', None, None, None, None, None, None, None,
                None, 0, None, None, 'API', 'interface', 'properties', 'Always', False, False
            )},
            'signal3': {(
                'enum_0', 'property1.member0.member0', 'Float32', None, None, None, None, None, None,
                None, None, 0, None, None, 'API', 'interface', 'properties', 'Always', False, False
            )},
            'signal4': {(
                'enum_0', 'property1.member1.member0.member0', 'Float32', None, None, None, None, None, None,
                None, None, 0, None, None, 'API', 'interface', 'properties', 'Always', False, False
            )}
        }
        self.assertEqual(sfw.translations, expected)

    def test_spec_to_dict(self):
        dummy_app = mock.MagicMock()
        dummy_app.get_service_mapping = mock.MagicMock(return_value={'interface': 'service'})
        sfw = ServiceFramework(dummy_app)
        result = sfw.spec_to_dict(
            SIGNAL_SPEC,
            'signal1'
        )
        expected = {
            'api': 'interface',
            'property_type': 'Float32',
            'endpoint': 'API',
            'default': 0,
            'description': 'Description',
            'factor': 1,
            'init': 0,
            'length': 1,
            'offset': 0,
            'property': 'property1',
            'range': {'max': 100, 'min': -100},
            'unit': 'Nm',
            'variable': 'signal1',
            'variable_type': 'Float32',
            'variant': 'properties',
            'strategy': 'Always',
            'debug': False,
            'dependability': False
        }
        self.assertDictEqual(result, expected)

    def test_to_dict(self):
        dummy_app = mock.MagicMock()
        dummy_app.get_service_mapping = mock.MagicMock(return_value={'interface': 'service'})
        dummy_app.get_signal_properties = mock.MagicMock(
            return_value={'type': 'Float32'}
        )
        insignal1 = Signal("signal1", dummy_app)
        insignal2 = Signal("signal2", dummy_app)
        dummy_app.insignals = [insignal1, insignal2]
        sfw = ServiceFramework(dummy_app)
        service_definitions = {
            "interface": {
                "properties": [
                    {
                        "API": [
                            {
                                "insignal": "signal1",
                                "property": "property1"
                            },
                            {
                                "insignal": "signal2",
                                "property": "property2"
                            },
                        ]
                    }
                ]
            }
        }
        sfw.parse_api_definitions(service_definitions)
        sfw.add_signals([insignal1, insignal2], 'insignals')
        result = sfw.to_dict()
        expected = {
            'consumer': [
                {
                    'api': 'interface',
                    'property_type': 'Float32',
                    'endpoint': 'API',
                    'default': None,
                    'description': None,
                    'factor': None,
                    'init': 0,
                    'length': None,
                    'offset': None,
                    'property': 'property1',
                    'range': {'max': None, 'min': None},
                    'unit': None,
                    'variable': 'signal1',
                    'variable_type': None,
                    'variant': 'properties',
                    'strategy': 'Always',
                    'debug': False,
                    'dependability': False
                },
                {
                    'api': 'interface',
                    'property_type': 'Float32',
                    'endpoint': 'API',
                    'default': None,
                    'description': None,
                    'factor': None,
                    'init': 0,
                    'length': None,
                    'offset': None,
                    'property': 'property2',
                    'range': {'max': None, 'min': None},
                    'unit': None,
                    'variable': 'signal2',
                    'variable_type': None,
                    'variant': 'properties',
                    'strategy': 'Always',
                    'debug': False,
                    'dependability': False
                }
            ],
            'producer': []
        }
        self.assertDictEqual(expected, result)

    def test_to_model(self):
        dummy_app = mock.MagicMock()
        dummy_app.get_service_mapping = mock.MagicMock(return_value={'interface': 'service'})
        insignal1 = Signal("signal1", dummy_app)
        insignal2 = Signal("signal2", dummy_app)
        dummy_app.insignals = [insignal1, insignal2]
        dummy_app.get_signal_properties = mock.MagicMock(
            return_value={
                'type': 'Float32',
                'description': 'test description',
                'unit': 'test unit'
            }
        )

        dummy_app.insignals = [insignal1, insignal2]
        sfw = ServiceFramework(dummy_app)
        inherit_properties = [
            {"destination": "description", "source": "description"},
            {"destination": "unit", "source": "unit"},
        ]

        service_definitions = {
            "interface": {
                "properties": [
                    {
                        "API": [
                            {
                                "insignal": "signal1",
                                "property": "property1"
                            },
                            {
                                "insignal": "signal2",
                                "property": "property2"
                            },
                        ],
                        "API2": [
                            {
                                "insignal": "signal1",
                            }
                        ]
                    }
                ]
            }
        }
        sfw.parse_api_definitions(service_definitions)
        sfw.add_signals([insignal1, insignal2], 'insignals', inherit_properties)
        expected = {
            'description': {
                'brief': 'Internal interface for associated application.',
                'full': 'This interface should only be used by the associated application.'
            },
            'name': '',
            'properties': [
                {
                    'accessors': 'r-',
                    'description': {
                        'brief': 'API2',
                        'full': 'test description'},
                    'name': 'API2',
                    'type': 'Float32',
                    'unit': 'test unit'
                },
                {
                    'accessors': 'r-',
                    'description': {
                        'brief': 'API',
                        'full': 'Generated from project without custom '
                                'description'},
                    'name': 'API',
                    'type': 'API',
                    'unit': 'struct'
                },
            ],
            'types': [
                {
                    'description': {
                        'brief': 'API',
                        'full': 'Generated from project without custom '
                                'description'},
                    'kind': 'struct',
                    'members': [{'name': 'property1', 'type': 'Float32'},
                                {'name': 'property2', 'type': 'Float32'}],
                    'name': 'API'}],
            'version': '${SERVICE_VERSION}'
        }
        result = sfw.to_model('internal')
        self.assertDictEqual(result, expected)

    def test_properties_service_model(self):
        dummy_app = mock.MagicMock()
        dummy_app.get_signal_properties = mock.MagicMock(
            return_value={'type': 'Float32'}
        )
        dummy_app.get_service_mapping = mock.MagicMock(return_value={'interface': 'service'})
        insignal1 = Signal("signal1", dummy_app)
        dummy_app.insignals = [insignal1]
        sfw = ServiceFramework(dummy_app)
        sfw.signal_names["app"]["insignals"] = {'signal1'}
        sfw.translations = {
            "signal1": {SIGNAL_SPEC},
        }
        properties, types = sfw.properties_service_model('internal')
        expected_properties = [{
            'name': 'API',
            'type': 'API',
            'unit': 'struct',
            'accessors': 'r-',
            'description': {
                'brief': 'API',
                'full': 'Generated from project without custom description'
            }
        }]
        expected_types = [{
            'name': 'API',
            'kind': 'struct',
            'description': {
                'brief': 'API',
                'full': 'Generated from project without custom description'},
            'members': [{'name': 'property1', 'type': 'Float32'}]
        }]
        self.assertCountEqual(properties, expected_properties)
        self.assertCountEqual(types, expected_types)
