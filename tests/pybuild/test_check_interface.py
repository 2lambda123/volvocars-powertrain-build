"""Tests for the check_interface module."""

from unittest import TestCase, mock

from powertrain_build.interface.base import BaseApplication, Signal, LOGGER as bl
from powertrain_build.interface.application import Model
import powertrain_build.check_interface as checker

checker.LOGGER.setLevel(10)
bl.setLevel(10)


class TestChecker(TestCase):
    """Test the check_interface module."""

    @mock.patch("powertrain_build.interface.application.Application.parse_definition")
    def test_process_app(self, app_parser):
        """Test the process_app function."""
        app = checker.process_app("test")
        self.assertTrue(isinstance(app, BaseApplication))

    @staticmethod
    def test_check_models_generic():
        """Test the check_models_generic function."""
        model1 = Model(None)
        model1.name = "model1"
        model1._load_json = mock.MagicMock()
        model2 = Model(None)
        model2.name = "model2"
        model2._load_json = mock.MagicMock()

        checker.check_models_generic([model1, model2], ["model1", "model2"], [])

    def test_get_active_signals(self):
        """Test the get_active_signals function."""
        model = Model(None)
        model.get_signal_properties = mock.MagicMock()
        model.get_signal_properties.return_value = {"configs": "whatever"}
        model._load_json = mock.MagicMock()
        signal1 = Signal("test1", model)
        signal2 = Signal("test2", model)

        feature_cfg = mock.MagicMock()
        feature_cfg.check_if_active_in_config.side_effect = [True, False]
        result = checker.get_active_signals([signal1, signal2], feature_cfg)
        expected = [signal1]
        self.assertListEqual(result, expected)

    def test_correct_type(self):
        """Test the correct_type function."""
        spec1 = {"type": "Float32"}
        spec2 = {"type": "Float32"}
        spec3 = {"type": "Bool"}
        self.assertTrue(checker.correct_type(spec1, spec2))
        self.assertFalse(checker.correct_type(spec1, spec3))

    def test_correct_attribute(self):
        """Test the correct_attribute function."""
        spec1 = {"type": "Float32", "test": 1, "another": 1}
        spec2 = {"type": "Float32", "test": 1}
        spec3 = {"type": "Bool", "test": 2}
        self.assertTrue(checker.correct_attribute(spec1, spec2, "test"))
        self.assertFalse(
            checker.correct_attribute(spec1, spec3, "test", check_bool=True)
        )
        self.assertFalse(
            checker.correct_attribute(spec1, spec3, "test", check_bool=False)
        )
        self.assertTrue(
            checker.correct_attribute(spec3, spec1, "test", check_bool=False)
        )
        self.assertFalse(
            checker.correct_attribute(spec3, spec1, "test", check_bool=True)
        )
        self.assertTrue(checker.correct_attribute(spec1, spec2, "another", default=1))
        self.assertFalse(checker.correct_attribute(spec1, spec2, "another", default=2))

    @staticmethod
    def test_check_signals():
        """Test the check_signals function."""
        owner = BaseApplication()
        owner.name = "test"
        owner.get_signal_properties = mock.MagicMock()
        owner.get_signal_properties.side_effect = [
            {"type": "Bool", "min": 0, "max": 1000, "unit": "s", "width": 1},
            {"type": "Bool", "min": 0, "max": 1000, "unit": "s", "width": 1},
        ]
        signal1 = Signal("signal1", owner)
        owner._insignals = {"signal1"}
        owner._outsignals = {"signal1"}
        owner._signals = {"signal1": signal1}
        errors = {"type": 0, "range": 0, "unit": 0, "width": 0}
        checker.check_signals([signal1], [signal1], errors)

    def test_signal_match(self):
        """Test the signal_match function."""
        matches = {}
        signals = [Signal(f"signal{i}", None) for i in range(10)]
        checker.signal_match(signals[:-1], signals[1:], matches)
        expected = {signal.name: True for signal in signals[1:-1]}
        expected[signals[0].name] = False
        self.assertDictEqual(expected, matches)

        matches = {}
        signals = [Signal(f"signal{i}", None) for i in range(10)]
        checker.signal_match(signals[:-1], signals[1:-5], matches)
        checker.signal_match(signals[:-1], signals[-5:], matches)
        self.assertDictEqual(expected, matches)
