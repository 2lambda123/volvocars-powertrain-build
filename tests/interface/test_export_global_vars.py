# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for export_global_vars.py."""

from unittest import TestCase, mock

from powertrain_build.interface.export_global_vars import get_global_variables


class TestGlobalVarsExport(TestCase):
    """Test the `export_global_vars.py` script."""

    def test_get_global_variables(self):
        """Test export_global_variables.get_global_variables."""
        dummy_project_name = "dummy_project"
        dummy_pybuild_return = (
            dummy_project_name,
            {
                "version": "0.2.1",
                "includes": [],
                "integrity_level": "QM",
                "outports": {"sVcOut_D_One": {"unit": {"type": "dummy_type"}}},
                "inports": {"not_interesting": {"dummy": "data"}},
                "core": {"not_interesting": {"dummy": "data"}},
                "dids": {"not_interesting": {"dummy": "data"}},
                "nvm": {"sVcNvm_D_One": {"unit": {"type": "dummy_type"}}},
                "pre_procs": {"not_interesting": {"dummy": "data"}},
                "local_vars": {"sVcLocal_D_One": {"unit": {"type": "dummy_type"}}},
                "calib_consts": {
                    "sVcCalib_D_One": {"unit": {"type": "dummy_type"}},
                    "sVcCalib_D_Two": {"unit": {"type": "dummy_type"}},
                },
            },
        )
        with mock.patch("powertrain_build.interface.export_global_vars._get_project_data", return_value=dummy_pybuild_return):
            result = get_global_variables("Dummy")
        expected_variables = [
            {"name": "sVcOut_D_One", "type": "dummy_type"},
            {"name": "sVcNvm_D_One", "type": "dummy_type"},
            {"name": "sVcLocal_D_One", "type": "dummy_type"},
            {"name": "sVcCalib_D_One", "type": "dummy_type"},
            {"name": "sVcCalib_D_Two", "type": "dummy_type"},
        ]
        self.assertEqual(dummy_project_name, result["name"])
        self.assertCountEqual(expected_variables, result["variables"])
