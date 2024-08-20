# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for powertrain_build.zone_controller.generate_yaml."""

import copy
import os
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from powertrain_build.build_proj_config import BuildProjConfig
from powertrain_build.core import ZCCore
from powertrain_build.dids import ZCDIDs
from powertrain_build.unit_configs import UnitConfigs
from powertrain_build.zone_controller.composition_yaml import CompositionYaml
from test_data.zone_controller.test_composition_yaml import (
    composition_yaml_setup,
    composition_yaml,
    composition_yaml_with_a2l_axis_data,
    composition_yaml_with_calls_all_fields,
    composition_yaml_with_calls_no_optional_fields,
    composition_yaml_with_dids,
    composition_yaml_with_dtcs,
)

SRC_DIR = Path(__file__).parent


class BuildProjConfigMock(BuildProjConfig):
    """Class mocking BuildProjConfig"""
    name = ""


class TestCompositionYaml(unittest.TestCase):
    """Test case for testing composition_yaml."""

    maxDiff = None

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfigMock)
        self.build_cfg.name = "XVC"
        self.build_cfg.get_scheduler_prefix = MagicMock(return_value="prefix_")
        self.build_cfg.get_src_code_dst_dir = MagicMock(
            return_value=os.path.abspath("output")
        )
        self.build_cfg.get_composition_arxml = MagicMock(return_value="some_arxml.arxml")
        self.build_cfg.get_units_raster_cfg = MagicMock(
            return_value=({"SampleTimes": {"testRunnable": 10}})
        )
        self.build_cfg.get_composition_name = MagicMock(return_value="compositionName")
        self.build_cfg.get_swc_name = MagicMock(return_value="testName_SC")
        self.build_cfg.get_gen_ext_impl_type = MagicMock(return_value=True)

        self.unit_cfg = MagicMock(spec_set=UnitConfigs)
        self.unit_cfg.get_per_cfg_unit_cfg.return_value = copy.deepcopy(
            composition_yaml_setup.get_per_cfg_unit_cfg_return_value
        )

        with patch.object(ZCCore, "_get_project_dtcs", return_value=set()):
            self.zc_core = ZCCore(self.build_cfg, self.unit_cfg)

        with patch.object(ZCDIDs, "_get_project_dids", return_value={}):
            self.zc_dids = ZCDIDs(self.build_cfg, self.unit_cfg)

        self.zc_spec = copy.deepcopy(composition_yaml_setup.zc_spec)

        self.calibration_definitions = copy.deepcopy(composition_yaml_setup.calibration_definitions)

        with patch.object(
            CompositionYaml,
            "_get_all_calibration_definitions",
            return_value=self.calibration_definitions
        ):
            self.composition_yaml = CompositionYaml(
                self.build_cfg, self.zc_spec, self.unit_cfg, self.zc_core, self.zc_dids, {}
            )

        # Common expected results variables
        self.base_configuration = copy.deepcopy(composition_yaml_setup.base_configuration)
        self.base_port_interfaces = copy.deepcopy(composition_yaml_setup.base_port_interfaces)
        self.base_accesses = copy.deepcopy(composition_yaml_setup.base_accesses)
        self.base_shared = copy.deepcopy(composition_yaml_setup.base_shared)
        self.base_static = copy.deepcopy(composition_yaml_setup.base_static)
        self.base_data_types = copy.deepcopy(composition_yaml_setup.base_data_types)

    def test_check_unsupported_fields(self):
        """Test CompositionYaml.check_unsupported_fields."""
        self.composition_yaml.warning = MagicMock()
        test_data = {
            "name": "sVcGpaDemo_D_BrkCtrlr",
            "type": "UInt8",
            "class": "CVC_DISP",
            "lsb": 1,
            "offset": "-",
            "width": 1,
        }
        self.composition_yaml.check_unsupported_fields("dummy", test_data)
        self.composition_yaml.warning.assert_not_called()
        test_data["lsb"] = 10
        self.composition_yaml.check_unsupported_fields("dummy", test_data)
        self.composition_yaml.warning.assert_called_once()

    def test_composition_yaml(self):
        """Checking that the dict is generated correctly"""
        result = self.composition_yaml.gather_yaml_info()
        self.assertDictEqual(composition_yaml.expected_result, result)

    def test_composition_yaml_with_a2l_axis_data(self):
        """Checking that the dict is generated correctly, including a2l axis data."""
        self.unit_cfg.get_per_cfg_unit_cfg.return_value = \
            composition_yaml_with_a2l_axis_data.get_per_cfg_unit_cfg_return_value
        a2l_axis_data = composition_yaml_with_a2l_axis_data.a2l_axis_data
        calibration_definitions = \
            self.calibration_definitions + composition_yaml_with_a2l_axis_data.calibration_definitions
        with patch.object(CompositionYaml, "_get_all_calibration_definitions", return_value=calibration_definitions):
            self.composition_yaml = CompositionYaml(
                self.build_cfg, self.zc_spec, self.unit_cfg, self.zc_core, self.zc_dids, a2l_axis_data
            )

        result = self.composition_yaml.gather_yaml_info()
        self.assertDictEqual(composition_yaml_with_a2l_axis_data.expected_result, result)

    def test_composition_yaml_with_calls_all_fields(self):
        """Checking that the dict is generated correctly, with calls including all fields."""
        self.zc_spec["calls"] = {
            "CallOne": {
                "interface": "InterfaceOne",
                "direction": "IN",
                "operation": "OperationOne",
                "timeout": 0.1,
            }
        }
        with patch.object(
            CompositionYaml,
            "_get_all_calibration_definitions",
            return_value=self.calibration_definitions
        ):
            self.composition_yaml = CompositionYaml(
                self.build_cfg, self.zc_spec, self.unit_cfg, self.zc_core, self.zc_dids, {}
            )
        result = self.composition_yaml.gather_yaml_info()
        self.assertDictEqual(composition_yaml_with_calls_all_fields.expected_result, result)

    def test_composition_yaml_with_calls_no_optional_fields(self):
        """Checking that the dict is generated correctly, with calls without optional fields."""
        self.zc_spec["calls"] = {
            "CallOne": {
                "direction": "IN",
                "operation": "OperationOne",
            }
        }
        with patch.object(
            CompositionYaml,
            "_get_all_calibration_definitions",
            return_value=self.calibration_definitions
        ):
            self.composition_yaml = CompositionYaml(
                self.build_cfg, self.zc_spec, self.unit_cfg, self.zc_core, self.zc_dids, {}
            )
        result = self.composition_yaml.gather_yaml_info()
        self.assertDictEqual(composition_yaml_with_calls_no_optional_fields.expected_result, result)

    def test_composition_yaml_with_dids(self):
        """Checking that the dict is generated correctly, with DIDs."""
        self.zc_dids.project_dids = {"DID1": {"type": "UInt8"}}
        self.zc_spec["Diagnostics"] = composition_yaml_with_dids.diagnostics
        with patch.object(
            CompositionYaml,
            "_get_all_calibration_definitions",
            return_value=self.calibration_definitions
        ):
            self.composition_yaml = CompositionYaml(
                self.build_cfg, self.zc_spec, self.unit_cfg, self.zc_core, self.zc_dids, {}
            )
        result = self.composition_yaml.gather_yaml_info()
        self.assertDictEqual(composition_yaml_with_dids.expected_result, result)

    def test_composition_yaml_with_dtcs(self):
        """Checking that the dict is generated correctly, with DTCs."""
        self.zc_core.project_dtcs = {"DTC1"}
        self.zc_spec["Diagnostics"] = composition_yaml_with_dtcs.diagnostics
        with patch.object(
            CompositionYaml,
            "_get_all_calibration_definitions",
            return_value=self.calibration_definitions
        ):
            self.composition_yaml = CompositionYaml(
                self.build_cfg, self.zc_spec, self.unit_cfg, self.zc_core, self.zc_dids, {}
            )
        result = self.composition_yaml.gather_yaml_info()
        self.assertDictEqual(composition_yaml_with_dtcs.expected_result, result)

    def test_get_init_values_expecting_failure(self):
        """Test CompositionYaml.get_init_values with a non-existing calibration definition."""
        self.composition_yaml.clear_log()
        json_variables = {"signal_name": "dummy"}
        c_definitions = ["CVC_CAL Float32 signal_name_other = 1.F; "]
        with patch.object(CompositionYaml, "_get_all_calibration_definitions", return_value=c_definitions):
            init_values = self.composition_yaml.get_init_values(json_variables)
        logged_problems = self.composition_yaml.get_problems()
        self.assertEqual(init_values, {})
        self.assertEqual(logged_problems["warning"], [])
        self.assertEqual(logged_problems["critical"], ["Missing init values for calibration variables:\nsignal_name"])
