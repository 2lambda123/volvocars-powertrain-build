# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

import unittest
from unittest import mock

from pybuild.interface.base import Signal
from pybuild.interface.device_proxy import DPAL, BadYamlFormat


class TestDPAL(unittest.TestCase):
    def setUp(self):
        self.interface_spec = {
            "default": 3,
            "domain": "test_domain",
            "factor": 2,
            "length": 4,
            "offset": 1,
            "property": "test_property",
            "property_type": "Float32",
            "variable": "test_signal",
            "variable_type": "float32",
            "range": {"min": 0, "max": 5},
            "init": 0,
            "description": "Dummy description",
            "unit": "Nm",
            "group": None,
            "strategy": "Always",
            'debug': False,
            'dependability': False,
            'port_name': None
        }
        self.signal_definition = {
            "insignal": "test_signal",
            "property": "test_property",
            "type": "float32",
            "offset": 1,
            "factor": 2,
            "default": 3,
            "length": 4,
            "min": 0,
            "max": 5,
            "enum": None,
            "init": 0,
            "description": "Dummy description",
            "unit": "Nm",
            "group": None,
            "strategy": "Always",
            'dependability': False,
            'debug': False
        }
        self.dep_signal_definition = {
            "insignal": "test_e2e_signal",
            "property": "test_property",
            "type": "float32",
            "offset": 1,
            "factor": 2,
            "default": 3,
            "length": 4,
            "min": 0,
            "max": 5,
            "enum": None,
            "init": 0,
            "description": "Dummy description",
            "unit": "Nm",
            "group": "test_group",
            "strategy": "Always",
            'dependability': True,
            'debug': False
        }
        self.e2e_sts_signal_definition = {
            "insignal": "sVctest_domain_D_test_groupE2eSts",
            "property": "test_property",
            "type": "float32",
            "offset": 1,
            "factor": 2,
            "default": 3,
            "length": 4,
            "min": 0,
            "max": 5,
            "enum": None,
            "init": 255,
            "description": "Dummy description",
            "unit": "Nm",
            "group": "test_group",
            "strategy": "Always",
            'dependability': True,
            'debug': False
        }
        self.signal_spec = (
            "enum_0",
            "test_domain",
            "test_property",
            "float32",
            "Float32",
            "Float32",
            1,
            2,
            3,
            4,
            0,
            5,
            None,
            0,
            "Dummy description",
            "Nm",
            None,
            "Always",
            False,
            False,
            None
        )
        self.dep_signal_spec = (
            "enum_0",
            "test_domain",
            "test_property",
            "float32",
            "Float32",
            "Float32",
            1,
            2,
            3,
            4,
            0,
            5,
            None,
            0,
            "Dummy description",
            "Nm",
            "test_group",
            "Always",
            False,
            True,
            None
        )
        self.e2e_sts_signal_spec = (
            "enum_0",
            "test_domain",
            "test_groupE2eSts",
            "UInt8",
            "UInt8",
            "UInt8",
            0,
            1,
            None,
            None,
            0,
            255,
            None,
            255,
            "E2E status code for E2E protected signal (group) test_e2e_signal.",
            None,
            "test_group",
            "Always",
            False,
            True,
            None
        )
        self.signal_yaml = {
            "default": 3,
            "length": 4,
            "name": "test_property",
            "type": "Float32",
            "range": {"min": 0, "max": 5},
            "description": "Dummy description",
            "unit": "Nm"
        }
        self.outsignals = [
            {
                "outsignal": "outsignal",
                "property": "test_property",
                "type": "Float32",
                "offset": 1,
                "factor": 2,
                "default": 3,
                "length": 4,
                "min": 0,
                "max": 5,
                "enum": None,
                "init": 0,
                "description": "Dummy description",
                "unit": "Nm",
                "group": None,
                "strategy": "Always",
                "debug": False,
                "dependability": False
            },
            {
                "outsignal": "outsignal_bad_strategy",
                "property": "test_property",
                "type": "Float32",
                "offset": 1,
                "factor": 2,
                "default": 3,
                "length": 4,
                "min": 0,
                "max": 5,
                "enum": None,
                "init": 0,
                "description": "Dummy description",
                "unit": "Nm",
                "group": None,
                "strategy": "OnChanged",
                "debug": False,
                "dependability": False
            },
            {
                "outsignal": "outsignal_nonexistent_strategy",
                "property": "test_property",
                "type": "Float32",
                "offset": 1,
                "factor": 2,
                "default": 3,
                "length": 4,
                "min": 0,
                "max": 5,
                "enum": None,
                "init": 0,
                "description": "Dummy description",
                "unit": "Nm",
                "group": None,
                "strategy": "NonExistent",
                "debug": False,
                "dependability": False
            }
        ]
        app = mock.MagicMock()
        app.get_domain_mapping.return_value = {"test": "test_domain"}
        app.pybuild['build_cfg'].get_ecu_info.return_value = ("HI", None)
        self.dummy_app = app
        self.maxDiff = None

    def test_add_signals(self):
        dpal = DPAL(self.dummy_app)
        insignal1 = Signal("test_name_in1", None)
        insignal2 = Signal("test_name_in2", None)
        outsignal = Signal("test_name_out", None)
        dpal.dp_translations = {"test_name_in1": {self.signal_spec},
                                "test_name_in2": {self.signal_spec},
                                "test_name_in_e2e": {self.dep_signal_spec},
                                "test_name_out": {self.signal_spec}, }
        dpal.e2e_sts_signals.add("test_name_in_e2e")

        dpal.add_signals([insignal1], "insignals")
        expected = {
            "other": {"insignals": {"test_name_in1", "test_name_in_e2e"}, "outsignals": set()},
            "dp": {"insignals": set(), "outsignals": {"test_property"}},
        }
        expected_signal_primitives_list = ["test_domain.test_property.insignals"]
        self.assertDictEqual(expected, dpal.signal_names)
        self.assertListEqual(expected_signal_primitives_list, dpal.signal_primitives_list)

        dpal.add_signals([outsignal], "outsignals")
        expected = {
            "other": {
                "insignals": {"test_name_in1", "test_name_in_e2e"},
                "outsignals": {"test_name_out"},
            },
            "dp": {"insignals": {"test_property"},
                   "outsignals": {"test_property"}},
        }
        expected_signal_primitives_list = ["test_domain.test_property.insignals",
                                           "test_domain.test_property.outsignals"]
        self.assertDictEqual(expected, dpal.signal_names)
        self.assertListEqual(expected_signal_primitives_list, dpal.signal_primitives_list)

        exception_msg = "You can't write test_domain.test_property.insignals"\
            " as insignals since this primitive has been used."\
            " Run model_yaml_verification to identify exact models."
        with self.assertRaises(Exception) as context:
            dpal.add_signals([insignal2], "insignals")
        self.assertEqual(exception_msg, str(context.exception))

    def test_check_group_mixed_signals(self):
        dpal = DPAL(self.dummy_app)
        test_signal = list(self.signal_spec)
        test_signal[16] = "signal_group_a"
        test_signal_1 = tuple(test_signal)
        test_signal[16] = "signal_group_a"
        test_signal_2 = tuple(test_signal)

        dpal.dp_translations = {"test_signal_1": {test_signal_1},
                                "test_signal_2": {test_signal_2}
                                }

        dpal.signal_names["other"]["insignals"] = {
            "test_signal_1",
        }
        dpal.signal_names["other"]["outsignals"] = {
            "test_signal_2",
        }
        expected_message = "Signal group signal_group_a for test_domain contains both consumed and produced signals"

        with self.assertRaises(AssertionError) as context:
            dpal.check_groups()
        self.assertEqual(expected_message, str(context.exception))

    def test_check_group_mixed_signals_mixed_signal_groups(self):
        dpal = DPAL(self.dummy_app)
        test_signal = list(self.signal_spec)
        test_signal[16] = "signal_group_a"
        test_signal_1 = tuple(test_signal)
        test_signal[16] = "signal_group_b"
        test_signal_2 = tuple(test_signal)
        test_signal[16] = "signal_group_b"
        test_signal_1 = tuple(test_signal)

        dpal.dp_translations = {"test_signal_1": {test_signal_1},
                                "test_signal_2": {test_signal_2}
                                }

        dpal.signal_names["other"]["insignals"] = {
            "test_signal_1",
        }
        dpal.signal_names["other"]["outsignals"] = {
            "test_signal_2",
        }
        expected_message = "Signal group signal_group_b for test_domain contains both consumed and produced signals"

        with self.assertRaises(AssertionError) as context:
            dpal.check_groups()
        self.assertEqual(expected_message, str(context.exception))

    def test_clear_signal_names(self):
        dpal = DPAL(self.dummy_app)
        insignal1 = Signal("test_name_in1", None)
        insignal2 = Signal("test_name_in2", None)
        outsignal = Signal("test_name_out", None)

        dpal.add_signals([insignal1, insignal2], "insignals")
        expected = {
            "other": {"insignals": {"test_name_in1"}, "outsignals": set()},
            "dp": {"insignals": set(), "outsignals": set()},
        }

        dpal.add_signals([outsignal], "outsignals")
        dpal.clear_signal_names()
        expected = {
            "other": {"insignals": set(), "outsignals": set()},
            "dp": {"insignals": set(), "outsignals": set()},
        }
        self.assertDictEqual(expected, dpal.signal_names)

    def test_parse_signal_definitions(self):
        signal_definitions = {"test": [self.signal_definition]}
        app = self.dummy_app
        app.insignals = [Signal("test_signal", None)]
        app.get_signal_properties.return_value = {"type": "Float32"}
        dpal = DPAL(app)
        dpal.parse_signal_definitions(signal_definitions)
        expected = {"test_signal": {self.signal_spec}}
        self.assertDictEqual(dpal.dp_translations, expected)

    def test_parse_e2e_group_signal_definitions(self):
        signal_definitions = {"test": [self.dep_signal_definition]}
        app = self.dummy_app
        app.insignals = [Signal("test_e2e_signal", None)]
        app.get_signal_properties.return_value = {"type": "Float32"}
        dpal = DPAL(app)
        dpal.parse_signal_definitions(signal_definitions, 'test_group')
        expected = {
            "test_e2e_signal": {self.dep_signal_spec},
            "sVctest_domain_D_test_groupE2eSts": {self.e2e_sts_signal_spec}
        }
        self.assertDictEqual(dpal.dp_translations, expected)

    def test_parse_bad_signal_definition(self):
        """E2E status signals cannot be in any yaml interface file."""
        signal_definitions = {"test": [self.e2e_sts_signal_definition]}
        app = self.dummy_app
        app.insignals = [Signal("sVctest_domain_D_test_groupE2eSts", None)]
        app.get_signal_properties.return_value = {"type": "Float32"}
        dpal = DPAL(app)
        with self.assertRaises(BadYamlFormat):
            dpal.parse_signal_definitions(signal_definitions, 'test_group')

    def test_parse_signal_definitions_output_strategies(self):
        signal_definitions = {"test": self.outsignals}
        app = self.dummy_app
        outsignal1 = Signal("outsignal", None)
        outsignal2 = Signal("outsignal_bad_strategy", None)
        outsignal3 = Signal("outsignal_nonexistent_strategy", None)
        app.outsignals = [outsignal1, outsignal2, outsignal3]
        app.get_signal_properties.return_value = {"type": "Float32"}
        dpal = DPAL(app)
        dpal.parse_signal_definitions(signal_definitions)
        expected = {
            "outsignal": {(
                "enum_0",
                "test_domain",
                "test_property",
                "Float32",
                "Float32",
                "Float32",
                1,
                2,
                3,
                4,
                0,
                5,
                None,
                0,
                "Dummy description",
                "Nm",
                None,
                "Always",
                False,
                False,
                None
            )},
            "outsignal_bad_strategy": {(
                "enum_0",
                "test_domain",
                "test_property",
                "Float32",
                "Float32",
                "Float32",
                1,
                2,
                3,
                4,
                0,
                5,
                None,
                0,
                "Dummy description",
                "Nm",
                None,
                "Always",
                False,
                False,
                None
            )},
            "outsignal_nonexistent_strategy": {(
                "enum_0",
                "test_domain",
                "test_property",
                "Float32",
                "Float32",
                "Float32",
                1,
                2,
                3,
                4,
                0,
                5,
                None,
                0,
                "Dummy description",
                "Nm",
                None,
                "Always",
                False,
                False,
                None
            )}
        }
        self.assertDictEqual(dpal.dp_translations, expected)

    def test_dp_spec_to_dict(self):
        result = DPAL(self.dummy_app).dp_spec_to_dict(self.signal_spec, "test_signal")
        self.assertDictEqual(result, self.interface_spec)

    def test_insignals_dp_manifest_signals(self):
        dpal = DPAL(self.dummy_app)
        suffix = "unittest"
        dpal.dp_translations = {"test_signal": {self.signal_spec}}
        dpal.signal_names["other"]["insignals"] = {
            "test_signal",
        }
        result = dpal.insignals_dp_manifest(suffix)
        expected = [{"name": "unittest", "signal_groups": [{"name": self.signal_yaml["name"]}]}]
        self.assertListEqual(result, expected)

    def test_insignals_dp_manifest_signal_groups(self):
        dpal = DPAL(self.dummy_app)
        suffix = "unittest"
        test_signal = list(self.signal_spec)
        test_signal[16] = "signal_group_a"
        test_signal_1 = tuple(test_signal)

        dpal.dp_translations = {"test_signal_1": {test_signal_1},
                                }
        dpal.signal_names["other"]["insignals"] = {
            "test_signal_1",
        }
        result = dpal.insignals_dp_manifest(suffix)
        expected = [{"name": "unittest", "signal_groups": [{"name": "signal_group_a"}]}]
        self.assertListEqual(result, expected)

    def test_outsignal_dp_manifest_signals(self):
        dpal = DPAL(self.dummy_app)
        suffix = "unittest"
        dpal.dp_translations = {"test_signal": {self.signal_spec}}
        dpal.signal_names["other"]["outsignals"] = {
            "test_signal",
        }
        result = dpal.outsignals_dp_manifest(suffix)
        expected = [{"name": "unittest", "signals": [self.signal_yaml], "signal_groups": []}]
        self.assertListEqual(result, expected)

    def test_outsignal_dp_manifest_signal_groups(self):
        dpal = DPAL(self.dummy_app)
        suffix = "unittest"
        test_signal = list(self.signal_spec)
        test_signal[16] = "signal_group_a"
        test_signal_1 = tuple(test_signal)

        dpal.dp_translations = {"test_signal_1": {test_signal_1},
                                }
        dpal.signal_names["other"]["outsignals"] = {
            "test_signal_1",
        }
        result = dpal.outsignals_dp_manifest(suffix)
        expected = [{
            "name": "unittest",
            "signals": [],
            "signal_groups": [{"name": "signal_group_a", "signals": [self.signal_yaml]}]}]
        self.assertListEqual(result, expected)

    def test_cleanup_dp_manifest_signal_group(self):
        dpal = DPAL(self.dummy_app)
        dpal.dp_translations = {"test_signal": {self.signal_spec}}
        dpal.signal_names["other"]["outsignals"] = {
            "test_signal",
        }
        client = {
            "name": "unittest",
            "consumes": [{"name": "unittest", "signal_groups": []}],
            "produces": [{"name": "unittest", "signals": [self.signal_yaml], "signal_groups": []}]
        }
        dpal.cleanup_dp_manifest(client)
        expected = {"name": "unittest", "produces": [{"name": "unittest", "signals": [self.signal_yaml]}]}
        self.assertDictEqual(client, expected)

    def test_cleanup_dp_manifest_signals(self):
        dpal = DPAL(self.dummy_app)
        test_signal = list(self.signal_spec)
        test_signal[16] = "signal_group_a"
        test_signal_1 = tuple(test_signal)
        test_signal[16] = "signal_group_b"
        test_signal_2 = tuple(test_signal)

        dpal.dp_translations = {"test_signal_1": {test_signal_1}, "test_signal_2": {test_signal_2}}
        dpal.signal_names["other"]["insignals"] = {
            "test_signal_1",
        }
        dpal.signal_names["other"]["outsignals"] = {
            "test_signal_2",
        }
        client = {
            "name": "unittest",
            "consumes": [{"name": "unittest", "signal_groups": [{"name": "signal_group_a"}]}],
            "produces": [{
                "name": "unittest", "signals": [],
                "signal_groups": [{"name": "signal_group_b", "signals": [self.signal_yaml]}]}]
                }
        dpal.cleanup_dp_manifest(client)
        expected = {"name": "unittest",
                    "consumes": [{"name": "unittest", "signal_groups": [{"name": "signal_group_a"}]}],
                    "produces": [{"name": "unittest", "signal_groups": [{"name": "signal_group_b",
                                                                        "signals": [self.signal_yaml]}]}]
                    }
        self.assertDictEqual(client, expected)

    def test_to_manifest_signal_groups(self):
        dpal = DPAL(self.dummy_app)
        client_name = "unittest"
        test_signal = list(self.signal_spec)
        test_signal[16] = "signal_group_a"
        test_signal_1 = tuple(test_signal)
        test_signal[16] = "signal_group_b"
        test_signal_2 = tuple(test_signal)

        dpal.dp_translations = {"test_signal_1": {test_signal_1}, "test_signal_2": {test_signal_2}}
        dpal.signal_names["other"]["insignals"] = {
            "test_signal_1",
        }
        dpal.signal_names["other"]["outsignals"] = {
            "test_signal_2",
        }
        result = dpal.to_manifest(client_name)
        expected = {
            "signal_info": {
                "clients": [
                    {
                        "name": "unittest",
                        "produces": [{
                            "name": "unittest",
                            "signal_groups": [
                                {
                                    "name": "signal_group_b",
                                    "signals": [
                                        {
                                            "default": 3,
                                            "length": 4,
                                            "name": "test_property",
                                            "type": "Float32",
                                            "range": {"min": 0, "max": 5},
                                            "description": "Dummy description",
                                            "unit": "Nm"
                                        }, ]
                                }],
                        }],
                        "consumes": [{"name": "unittest", "signal_groups": [{"name": "signal_group_a"}, ]}]
                    }
                ],
                "version": 0.2,
            }
        }

        self.assertDictEqual(result, expected)

    def test_to_manifest_signals(self):
        dpal = DPAL(self.dummy_app)
        client_name = "unittest"
        dpal.dp_translations = {"test_signal": {self.signal_spec}}
        dpal.signal_names["other"]["outsignals"] = {
            "test_signal",
        }
        result = dpal.to_manifest(client_name)
        expected = {
            "signal_info": {
                "clients": [
                    {
                        "name": "unittest",
                        "produces": [{
                            "name": "unittest",
                            "signals": [
                                {
                                    "default": 3,
                                    "length": 4,
                                    "name": "test_property",
                                    "type": "Float32",
                                    "range": {"min": 0, "max": 5},
                                    "description": "Dummy description",
                                    "unit": "Nm"
                                }
                            ],
                        }],
                    }
                ],
                "version": 0.2,
            }
        }

        self.assertDictEqual(result, expected)

    def test_domain_filter(self):
        dpal = DPAL(self.dummy_app)
        dpal.domain_filter = ["test_domain"]  # Matches self.signal_spec
        client_name = "unittest"
        # Modify signal_spec to not match filter
        domain_position = dpal.dp_position.domain.value
        property_position = dpal.dp_position.property.value
        signal_spec2 = self.signal_spec[:domain_position] + \
            ("another_domain",) + \
            self.signal_spec[domain_position+1:property_position] + \
            ("another_property",) + \
            self.signal_spec[property_position+1:]
        dpal.dp_translations = {"test_signal1": {self.signal_spec},
                                "test_signal2": {signal_spec2}}
        dpal.signal_names["other"]["outsignals"] = {
            "test_signal1",
            "test_signal2",
        }
        result = dpal.to_manifest(client_name)
        expected = {
            "signal_info": {
                "clients": [
                    {
                        "name": "unittest",
                        "produces": [{
                            "name": "unittest",
                            "signals": [self.signal_yaml]
                        }],
                    }
                ],
                "version": 0.2,
            }
        }
        self.assertDictEqual(result, expected)

    def test_empty_manifest(self):
        # If we have no matching signals, don't create a manifest
        dpal = DPAL(self.dummy_app)
        client_name = "unittest"
        dpal.device_filter = ["no_match"]
        self.assertIsNone(dpal.to_manifest(client_name))
