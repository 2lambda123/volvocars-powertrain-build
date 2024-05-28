# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Module to test the update_model_yaml.py module."""


import unittest
from unittest import mock

from pybuild.interface.update_model_yaml import BadYamlFormat, UpdateYmlFormat


class TestUpdateYamlFormat(unittest.TestCase):
    """Unit tests for the UpdateYmlFormat class."""

    def setUp(self):
        app = mock.MagicMock()
        self.update_yml_format = UpdateYmlFormat(app)
        self.update_yml_format.app_insignals = ["in_signal1", "in_signal2"]
        self.update_yml_format.app_outsignals = ["out_signal1", "out_signal2"]

    def test_check_signals_insignal(self):
        """Test check_signals method with insignal."""
        signals_definition = {"spec1": [{"insignal": "in_signal1", "property": "prop1"}]}
        self.update_yml_format.check_signals(signals_definition)
        self.assertEqual(signals_definition, {"spec1": [{"insignal": "in_signal1", "property": "prop1"}]})

    def test_check_signals_outsignal(self):
        """Test check_signals method with outsignal."""
        signals_definition = {"spec1": [{"outsignal": "out_signal1", "property": "prop1"}]}
        self.update_yml_format.check_signals(signals_definition)
        self.assertEqual(signals_definition, {"spec1": [{"outsignal": "out_signal1", "property": "prop1"}]})

    def test_check_signals_no_insignal(self):
        """Test check_signals method without insignal."""
        signals_definition = {"spec1": [{"signal": "in_signal1", "property": "prop1"}]}
        self.update_yml_format.check_signals(signals_definition)
        self.assertEqual(signals_definition, {"spec1": [{"insignal": "in_signal1", "property": "prop1"}]})

    def test_check_signals_no_outsignal(self):
        """Test check_signals method without outsignal."""
        signals_definition = {"spec1": [{"signal": "out_signal1", "property": "prop1"}]}
        self.update_yml_format.check_signals(signals_definition)
        self.assertEqual(signals_definition, {"spec1": [{"outsignal": "out_signal1", "property": "prop1"}]})

    def test_check_signals_bad_yaml(self):
        """Test check_signals method with wrong signal."""
        signals_definition = {"spec1": [{"signal": "bad_signal", "property": "prop1"}]}
        with self.assertRaises(BadYamlFormat):
            self.update_yml_format.check_signals(signals_definition)
