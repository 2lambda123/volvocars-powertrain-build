# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Module to test the ModelYmlVerification class."""


import unittest
from unittest import mock

from powertrain_build.interface.model_yaml_verification import ModelYmlVerification


class TestModelYamlVerification(unittest.TestCase):
    """Unit tests for the ModelYmlVerification class."""

    def test_verify_outsignals(self):
        """Test the verify_signals method with outsignals."""
        app = mock.MagicMock()
        modelyamlver = ModelYmlVerification(app)
        modelyamlver.model_name = "dummy_model"
        modelyamlver.signal_properties = {"dummy_model": []}
        modelyamlver.app_outsignals = {}
        modelyamlver.raw = {"dummy_dp": [{"property": "test_outsignal", "outsignal": "test_outsignal"}]}
        exception_msg = "ERROR:root:test_outsignal is not defined as an outsignal in json file\n"
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(warn_info.output, [exception_msg])

        # Different properties connected to the same outsignal in the same device proxy.
        modelyamlver.app_outsignals = ["test_outsignal"]
        modelyamlver.signal_properties = {"dummy_model": []}
        modelyamlver.raw = {
            "dummy_dp": [
                {"property": "test_property", "outsignal": "test_outsignal"},
                {"property": "test_property2", "outsignal": "test_outsignal"},
            ]
        }

        exception_msg = (
            "ERROR:root:You can't connect a signal test_outsignal in dummy_model model to the same "
            "interface (dummy_dp) twice. It's already connected as "
            "dummy_dp.test_property.test_outsignal in model dummy_model.\n"
        )

        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(warn_info.output, [exception_msg])

        # Different properties connected to the same outsignal in different device proxies.
        modelyamlver.app_outsignals = ["test_outsignal"]
        modelyamlver.signal_properties = {"dummy_model": []}
        modelyamlver.raw = {
            "dummy_dp": [
                {"property": "test_property", "outsignal": "test_outsignal"},
            ],
            "dummy_dp2": [{"property": "test_property2", "outsignal": "test_outsignal"}],
        }

        expected_signal_properties = {
            "dummy_model": ["dummy_dp.test_property.test_outsignal", "dummy_dp2.test_property2.test_outsignal"],
        }
        modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(expected_signal_properties, modelyamlver.signal_properties)

        # Different properties connected to the same outsignal in different device proxies.
        modelyamlver.app_outsignals = ["test_outsignal2", "test_outsignal"]
        modelyamlver.signal_properties = {"dummy_model": []}
        modelyamlver.raw = {
            "dummy_dp": [
                {"property": "test_property2", "outsignal": "test_outsignal2"},
                {"property": "test_property", "outsignal": "test_outsignal"},
            ]
        }

        expected_signal_properties = {
            "dummy_model": ["dummy_dp.test_property2.test_outsignal2", "dummy_dp.test_property.test_outsignal"],
        }
        modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(expected_signal_properties, modelyamlver.signal_properties)

        # Different outsignals connected to the same property
        modelyamlver.app_outsignals = ["test_outsignal", "test_outsignal2"]
        modelyamlver.signal_properties = {"dummy_model": []}
        modelyamlver.raw = {
            "dummy_dp": [
                {"property": "test_property", "outsignal": "test_outsignal"},
                {"property": "test_property", "outsignal": "test_outsignal2"},
            ]
        }
        exception_msg = (
            "ERROR:root:You can't connect another signal to the existing property "
            "dummy_dp.test_property.test_outsignal2"
            " in dummy_model model, because it is already defined in dummy_model model.\n"
        )
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(warn_info.output, [exception_msg])

        # Same outsignal connected to the same property several times
        modelyamlver.app_outsignals = ["test_outsignal", "test_outsignal2"]
        modelyamlver.signal_properties = {"dummy_model": []}
        modelyamlver.raw = {
            "dummy_dp": [
                {"property": "test_property", "outsignal": "test_outsignal"},
                {"property": "test_property", "outsignal": "test_outsignal"},
            ]
        }
        exception_msg = "ERROR:root:You can't connect signal test_outsignal in dummy_model model twice.\n"
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(warn_info.output, [exception_msg])

    def test_verify_insignals(self):
        """Test the verify_signals method with insignals."""
        app = mock.MagicMock()
        modelyamlver = ModelYmlVerification(app)
        modelyamlver.model_name = "dummy_model"
        modelyamlver.app_insignals = {}
        modelyamlver.raw = {"dummy_dp": [{"property": "test_property", "insignal": "test_insignal"}]}
        exception_msg = "ERROR:root:test_insignal is not defined as an insignal in json file\n"
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(warn_info.output, [exception_msg])

        # Different properties connected to the same insignal
        modelyamlver.app_insignals = ["test_insignal"]
        modelyamlver.signal_properties = {"dummy_model": []}
        modelyamlver.raw = {
            "dummy_dp": [
                {"property": "test_property", "insignal": "test_insignal"},
                {"property": "test_property2", "insignal": "test_insignal"},
            ]
        }
        exception_msg = (
            "ERROR:root:You can't connect a signal test_insignal in dummy_model model to two"
            " different primitives. It's already connected in dummy_model model\n"
        )

        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(warn_info.output, [exception_msg])

        # Different insignals connected to the same property
        modelyamlver.app_insignals = ["test_insignal", "test_insignal2"]
        modelyamlver.signal_properties = {"dummy_model": []}
        modelyamlver.raw = {
            "dummy_dp": [
                {"property": "test_property", "insignal": "test_insignal"},
                {"property": "test_property", "insignal": "test_insignal2"},
            ]
        }
        exception_msg = (
            "ERROR:root:You can't connect another signal to the existing property "
            "dummy_dp.test_property.test_insignal2"
            " in dummy_model model, because it is already defined in dummy_model model.\n"
        )
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(warn_info.output, [exception_msg])

        # Different insignals connected to the same property in different models, should give an error message
        modelyamlver.signal_properties = {"dummy_model": [], "dummy_model2": []}
        modelyamlver.app_insignals = ["test_insignal", "test_insignal2"]
        model_signal = {"dummy_model": "test_insignal", "dummy_model2": "test_insignal2"}
        for model in ["dummy_model", "dummy_model2"]:
            modelyamlver.model_name = model
            modelyamlver.raw = {"dummy_dp": [{"property": "test_property", "insignal": model_signal[model]}]}
            exception_msg = (
                "ERROR:root:You can't connect another signal to the existing property "
                "dummy_dp.test_property.test_insignal2"
                " in dummy_model2 model, because it is already defined in dummy_model model.\n"
            )
            try:
                with self.assertLogs(level="INFO") as warn_info:
                    modelyamlver.verify_signals(modelyamlver.raw)
            except AssertionError:
                warn_info = None
        if not hasattr(warn_info, "output"):
            raise AssertionError("no logs of level INFO or higher triggered on root")
        self.assertEqual(warn_info.output, [exception_msg])

        # Same insignal connected to the same property several times
        modelyamlver.app_insignals = ["test_insignal", "test_insignal2"]
        modelyamlver.signal_properties = {"dummy_model": []}
        modelyamlver.model_name = "dummy_model"
        modelyamlver.raw = {
            "dummy_dp": [
                {"property": "test_property", "insignal": "test_insignal"},
                {"property": "test_property", "insignal": "test_insignal"},
            ]
        }
        exception_msg = "ERROR:root:You can't connect signal test_insignal in dummy_model model twice.\n"
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(warn_info.output, [exception_msg])

        # Same insignal connected to the same property in different models, this should not give an error message
        modelyamlver.signal_properties = {"dummy_model": [], "dummy_model2": []}
        modelyamlver.app_insignals = ["test_insignal"]
        for model in ["dummy_model", "dummy_model2"]:
            modelyamlver.model_name = model
            modelyamlver.raw = {"dummy_dp": [{"property": "test_property", "insignal": "test_insignal"}]}
            exception_msg = (
                "ERROR:root:You can't write dummy_dp.test_property in dummy_model2 model."
                " It already exists in dummy_model model\n"
            )
            try:
                with self.assertLogs(level="INFO") as warn_info:
                    modelyamlver.verify_signals(modelyamlver.raw)
            except AssertionError:
                continue
            raise AssertionError(f"Error raised: {warn_info.output}")

    def test_verify_hal_struct(self):
        """Test the verify_signals method for hal struct."""
        app = mock.MagicMock()
        modelyamlver = ModelYmlVerification(app)
        modelyamlver.model_name = "dummy_model"
        modelyamlver.app_insignals = {}
        modelyamlver.raw = {
            "insignal_struct": [
                {"insignal": "test_insignal", "property": "test_insignal"},
                {"property": "test_insignal2", "insignal": "test_insignal2"},
            ]
        }
        exception_msg = [
            "ERROR:root:test_insignal is not defined as an insignal in json file\n",
            "ERROR:root:test_insignal2 is not defined as an insignal in json file\n",
        ]
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.verify_signals(modelyamlver.raw)
        self.assertEqual(warn_info.output, exception_msg)

    def test_verify_hal_signals(self):
        """Test the verify_signals method for hal signals."""
        app = mock.MagicMock()
        modelyamlver = ModelYmlVerification(app)
        modelyamlver.model_name = "dummy_model"
        modelyamlver.app_insignals = {}
        modelyamlver.raw = {"insignal_property": [{"insignal": "test_insignal"}]}
        exception_msg = "ERROR:root:test_insignal is not defined as an insignal in json file\n"
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.verify_signals(modelyamlver.raw, is_hal=True, is_service=False, group="dummy_grp")
        self.assertEqual(warn_info.output, [exception_msg])

        app = mock.MagicMock()
        modelyamlver = ModelYmlVerification(app)
        modelyamlver.model_name = "dummy_model"
        modelyamlver.app_insignals = ["test_insignal"]
        modelyamlver.raw = {"insignal_property": [{"insignal": "test_insignal"}]}
        modelyamlver.signal_properties = {"dummy_model": ["dummy_dp.property_outsignal"]}
        modelyamlver.verify_signals(modelyamlver.raw, is_hal=True, is_service=False, group="dummy_grp")
        expected_signal_properties = {
            "dummy_model": ["dummy_dp.property_outsignal", "insignal_property.dummy_grp.test_insignal"]
        }
        self.assertEqual(modelyamlver.signal_properties, expected_signal_properties)

    def test_parse_service_definitions(self):
        """Test the parse_service_definitions method."""
        app = mock.MagicMock()
        modelyamlver = ModelYmlVerification(app)
        modelyamlver.model_name = "dummy_model"
        modelyamlver.app_insignals = ["test_insignal"]
        modelyamlver.signal_properties = {"dummy_model": []}
        modelyamlver.raw = {
            "dummy_service": {
                "methods": [
                    {
                        "dummy_endpoint1": [{"insignal": "test_insignal"}],
                        "dummy_endpoint2": [{"insignal": "test_insignal"}],
                    }
                ]
            }
        }
        exception_msg = [
            "ERROR:root:You can't connect a signal test_insignal in dummy_model model to two "
            "different primitives. It's already connected in dummy_model model\n"
        ]
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.parse_service_definitions(modelyamlver.raw)
        self.assertEqual(warn_info.output, exception_msg)

    def test_validate_dp_signal_schema(self):
        """Test the validate_signal_schema method."""
        app = mock.MagicMock()
        modelyamlver = ModelYmlVerification(app)
        modelyamlver.model_name = "dummy_model"
        signal_spec = {"insignal": "test_insignal"}
        exception_msg = "ERROR:root:required key not provided @ data['property'] in dummy_model\n"
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.validate_signal_schema(signal_spec, "insignal", is_hal=False, is_service=False)
        self.assertEqual(warn_info.output, [exception_msg])

    def test_check_dp_property(self):
        """Test the verify_primitive method."""
        app = mock.MagicMock()
        modelyamlver = ModelYmlVerification(app)
        modelyamlver.model_name = "dummy_model2"
        modelyamlver.signal_properties = {"dummy_model1": ["dummy_dp.property_outsignal.signal"], "dummy_model2": []}
        exception_msg = (
            "ERROR:root:You can't connect another signal to the existing property "
            "dummy_dp.property_outsignal.signal2"
            " in dummy_model2 model, because it is already defined in dummy_model1 model.\n"
        )
        with self.assertLogs(level="INFO") as warn_info:
            modelyamlver.check_property("dummy_dp.property_outsignal.signal2")
        self.assertEqual(warn_info.output, [exception_msg])

        app = mock.MagicMock()
        modelyamlver = ModelYmlVerification(app)
        modelyamlver.model_name = "dummy_model2"
        modelyamlver.signal_properties = {"dummy_model1": ["dummy_dp.property_outsignal"], "dummy_model2": []}
        expected_signal_properties = {
            "dummy_model1": ["dummy_dp.property_outsignal"],
            "dummy_model2": ["dummy_dp.property_insignal.signal"],
        }
        modelyamlver.verify_primitive("dummy_dp.property_insignal.signal", "outsignal")
        self.assertEqual(expected_signal_properties, modelyamlver.signal_properties)
