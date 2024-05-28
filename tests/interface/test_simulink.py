# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Test cases for the Simulink interface module."""


import json
import os
import unittest

from pybuild.interface import simulink


class TestSimulink(unittest.TestCase):
    """Unit tests for the Simulink interface module."""

    def setUp(self):
        self.base_path = "test_data/interface/test_simulink/"
        with open(self.base_path + "test_case.json", encoding="utf-8") as test_file:
            data = json.load(test_file)
            self.dp = data.get("DP", {})
            self.dp_enum = data.get("DP_ENUM", {})
            self.api = data.get("API", {})
            self.api_enum = data.get("API_ENUM", {})
            self.api_enums = data.get("API_ENUMS", {})
            self.api_double_enum = data.get("API_DOUBLE_ENUM", {})
            self.interface_data_types = data.get("INTERFACE_DATA_TYPES", {})
            self.methods = data.get("METHODS", {})

    def test_split_interface(self):
        """Test split_interface method."""
        result = simulink.split_interface(self.dp)
        with open(os.path.join(self.base_path, "split_interface_expected_result.json"), encoding="utf-8") as json_file:
            expected = json.load(json_file)
        self.assertDictEqual(result, expected)

    def test_get_interface_dp(self):
        """Test get_interface method with DP."""
        output = simulink.get_interface({}, self.dp, {}, {}, {})
        with open(os.path.join(self.base_path, "get_interface_dp_expected_result.json"), encoding="utf-8") as json_file:
            expected = json.load(json_file)
        self.assertCountEqual(output, expected)

    def test_add_dp(self):
        """Test add_dp method."""
        output = []
        result = simulink.add_dp(output, {}, self.dp)
        with open(os.path.join(self.base_path, "add_dp_expected_result.json"), encoding="utf-8") as json_file:
            expected = json.load(json_file)
        self.assertListEqual(result, expected)

    def test_get_interface_hal(self):
        """Test get_interface method with HAL."""
        output = simulink.get_interface({}, {}, self.api, {}, {})
        with open(
            os.path.join(self.base_path, "get_interface_hal_expected_result.json"), encoding="utf-8"
        ) as json_file:
            expected = json.load(json_file)
        self.assertCountEqual(output, expected)

    def test_add_api(self):
        """Test add_api method."""
        output = []
        result = simulink.add_api(output, {}, self.api)
        with open(os.path.join(self.base_path, "add_api_expected_result.json"), encoding="utf-8") as json_file:
            expected = json.load(json_file)
        self.assertListEqual(result, expected)

    def test_extend_adapter(self):
        """Test add_api method with adapter."""
        with open(os.path.join(self.base_path, "extend_adapters_interface.json"), encoding="utf-8") as json_file:
            interface = json.load(json_file)
        result = simulink.add_api(interface, {}, self.api)
        with open(os.path.join(self.base_path, "extend_adapters_expected_result.json"), encoding="utf-8") as json_file:
            expected = json.load(json_file)
        self.assertListEqual(result, expected)

    def test_get_interface_sfw(self):
        """Test get_interface method with SFW."""
        output = simulink.get_interface({}, {}, {}, self.api, {})
        with open(
            os.path.join(self.base_path, "get_interface_sfw_expected_result.json"), encoding="utf-8"
        ) as json_file:
            expected = json.load(json_file)
        self.assertCountEqual(output, expected)

    def test_add_method(self):
        """Test that add_method adds new adapters."""
        with open(os.path.join(self.base_path, "add_method_output.json"), encoding="utf-8") as json_file:
            output = json.load(json_file)
        result = simulink.add_methods(output, {}, self.methods)
        with open(os.path.join(self.base_path, "add_method_expected_methods.json"), encoding="utf-8") as json_file:
            expected_methods = json.load(json_file)
        with open(os.path.join(self.base_path, "add_method_expected_result.json"), encoding="utf-8") as json_file:
            expected = json.load(json_file)
            expected[1]["methods"] = expected_methods
        self.assertCountEqual(result, expected)

    def test_get_interface_with_data_types(self):
        """Test get_interface method adding interface_data_types."""
        output = simulink.get_interface(self.interface_data_types, {}, {}, self.api_enums, {})
        with open(
            os.path.join(self.base_path, "get_interface_with_data_types_expected_result.json"), encoding="utf-8"
        ) as json_file:
            expected = json.load(json_file)
        self.assertCountEqual(output, expected)

    def test_get_interface_with_double_enum(self):
        """Test get_interface method adding interface data types and double enum."""
        output = simulink.get_interface(self.interface_data_types, {}, {}, self.api_double_enum, {})
        with open(
            os.path.join(self.base_path, "get_interface_with_double_enum_expected_result.json"), encoding="utf-8"
        ) as json_file:
            expected = json.load(json_file)
        self.assertCountEqual(output, expected)

    def test_add_api_with_data_types(self):
        """Test add_api method adding interface_data_types."""
        output = []
        result = simulink.add_api(output, self.interface_data_types, self.api_enum)
        with open(
            os.path.join(self.base_path, "add_api_with_data_types_expected_result.json"), encoding="utf-8"
        ) as json_file:
            expected = json.load(json_file)
        self.assertListEqual(result, expected)

    def test_add_dp_with_data_types(self):
        """Test add_dp method adding interface_data_types."""
        output = []
        result = simulink.add_dp(output, self.interface_data_types, self.dp_enum)
        with open(
            os.path.join(self.base_path, "add_dp_with_data_types_expected_result.json"), encoding="utf-8"
        ) as json_file:
            expected = json.load(json_file)
        self.assertListEqual(result, expected)

    def test_ensure_raster(self):
        """Test ensure_raster method."""
        raster = "Vc10ms"
        output = []
        result = simulink.ensure_raster(output, raster)
        expected = [{"name": "Vc10ms", "ports": {"in": {}, "out": {}}}]
        self.assertListEqual(result, expected)

    def test_get_adapter(self):
        """Test get_adapter method."""
        interface = [{"name": "Vc10ms", "ports": {"in": {}, "out": {}}}]
        result = simulink.get_adapter(interface, "Vc10ms")
        expected = {"name": "Vc10ms", "ports": {"in": {}, "out": {}}}
        self.assertDictEqual(result, expected)
