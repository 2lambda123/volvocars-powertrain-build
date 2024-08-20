# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Module to test the interface module"""


import unittest
from unittest import mock

from powertrain_build.interface.base import Domain, Interface, MultipleProducersError, Signal


class DummyApp:
    """Dummy application class"""

    def __init__(self, name, properties=None):
        self.name = name
        self._insignals = []
        self._outsignals = []
        self._properties = properties if properties is not None else {}

    @property
    def insignals(self):
        """Get insignals"""
        return self._insignals

    @property
    def outsignals(self):
        """Get outsignals"""
        return self._outsignals

    def get_signal_properties(self, *args):
        """Dummy properties"""
        return self._properties


def create_dummies():
    """Create dummy applications and signals"""
    dummy_apps = []
    signals = []
    for i in range(0, 3):
        dummy_app_name = "dummy" + str(i)
        signal_properties = {"prop_from_" + str(i): dummy_app_name}
        dummy_app = DummyApp("dummy" + str(i), signal_properties)
        dummy_apps.append(dummy_app)
        signals.append(Signal("signal_" + str(i * 2), dummy_app))
        signals.append(Signal("signal_" + str(i * 2 + 1), dummy_app))
    dummy_apps[0]._outsignals = [signals[0], signals[1]]
    dummy_apps[0]._insignals = [signals[2], signals[4]]  # 1 from dummy1, 1 from elsewhere
    dummy_apps[1]._outsignals = [signals[2], signals[3]]
    dummy_apps[1]._insignals = [signals[0], signals[5]]  # 1 from dummy0, 1 from elsewhere
    return signals, dummy_apps


class TestSignal(unittest.TestCase):
    """Unit tests for the Signal class."""

    def test_init(self):
        """Test the initialization of a Signal instance."""
        signal = Signal("test_name", None)
        self.assertEqual(signal.name, "test_name")
        self.assertDictEqual(signal.applications, {})

    def test_consumers(self):
        """Test the consumers property of a Signal instance."""
        signal = Signal("test_name", None)
        signal.consumers = "Consumer_1"
        signal.consumers = "Consumer_2"
        self.assertSetEqual(signal.consumers, set(["Consumer_1", "Consumer_2"]))

    def test_producer(self):
        """Test the producer property of a Signal instance."""
        signal = Signal("test_name", None)
        signal.producer = "Producer_1"
        self.assertSetEqual(signal.producer, {"Producer_1"})

    def test_multiple_producer(self):
        """Test the behavior of a Signal instance when multiple producers are set."""
        signal = Signal("test_name", None)
        signal.producer = "Producer_1"
        signal.producer = "Producer_1"
        with self.assertRaises(MultipleProducersError):
            signal.set_producer("Producer_2")

    def test_force_producers(self):
        """Test the force_producer method of a Signal instance."""
        signal = Signal("test_name", None)
        signal.producer = "Producer_1"
        signal.force_producer("Producer_2")
        self.assertSetEqual(signal.producer, set(["Producer_1", "Producer_2"]))

    def test_properties(self):
        """Test the properties property of a Signal instance."""
        dummy = mock.MagicMock()
        properties = {"type": "dummy", "description": "DUMMY"}
        dummy.get_signal_properties.return_value = properties
        signal = Signal("test_name", dummy)
        self.assertDictEqual(signal.properties, properties)


class TestInterface(unittest.TestCase):
    """Unit tests for the Interface class."""

    def setUp(self):
        """Set up the test case by creating dummy signals and apps."""
        signals, apps = create_dummies()
        self.signals = signals
        self.apps = apps

    def test_init(self):
        """Test the initialization of the Interface class."""
        interface = Interface(self.apps[0], self.apps[1])
        self.assertEqual(interface.name, "dummy0_dummy1")

    def test_signals_current_to_corresponding(self):
        """Test the get_produced_signals, get_consumed_signals, and get_directional_signals methods."""
        interface = Interface(self.apps[0], self.apps[1])
        self.assertListEqual(interface.get_produced_signals(self.apps[0].name), [self.signals[0]])
        self.assertListEqual(interface.get_consumed_signals(self.apps[1].name), [self.signals[0]])
        self.assertListEqual(
            interface.get_directional_signals(consumer=self.apps[1], producer=self.apps[0]), [self.signals[0]]
        )

    def test_signals_corresponding_to_current(self):
        """Test the get_produced_signals, get_consumed_signals, and get_directional_signals methods."""
        interface = Interface(self.apps[0], self.apps[1])
        self.assertListEqual(interface.get_produced_signals(self.apps[1].name), [self.signals[2]])
        self.assertListEqual(interface.get_consumed_signals(self.apps[0].name), [self.signals[2]])
        self.assertListEqual(
            interface.get_directional_signals(consumer=self.apps[0], producer=self.apps[1]), [self.signals[2]]
        )

    def test_properties(self):
        """Test the properties of the signals."""
        properties = {"prop_from_0": "dummy0"}
        self.assertDictEqual(self.signals[0].properties, properties)
        interface = Interface(self.apps[0], self.apps[1])
        properties.update({"prop_from_1": "dummy1"})
        for signal in interface.get_directional_signals(self.apps[0], self.apps[1]):
            self.assertDictEqual(signal.properties, properties)
        self.assertDictEqual(self.signals[0].properties, properties)


class TestDomain(unittest.TestCase):
    """Unit tests for the Domain class."""

    def setUp(self):
        """Set up the test case by creating dummy signals and apps, and initializing interfaces."""
        signals, apps = create_dummies()
        self.signals = signals
        self.apps = apps
        self.interfaces = [
            Interface(self.apps[0], self.apps[1]),
            Interface(self.apps[0], self.apps[2]),
            Interface(self.apps[1], self.apps[2]),
        ]

    def test_add_interface(self):
        """Test the add_interface method of the Domain class."""
        domain = Domain()
        domain.set_name("test")
        domain.add_interface(self.interfaces[0])
        self.assertSetEqual(domain.clients, set(["dummy0", "dummy1"]))
        self.assertSetEqual(set(domain.signals.keys()), set(["signal_0", "signal_2"]))
        self.assertSetEqual(domain.signals["signal_0"].consumers, set(["dummy1"]))
        self.assertSetEqual(domain.signals["signal_2"].consumers, set(["dummy0"]))

    def test_create_groups(self):
        """Test the create_groups method of the Domain class."""
        domain = Domain()
        domain.set_name("test")
        domain.add_interface(self.interfaces[0])
        groups = domain.create_groups()
        expected_signals = {"dummy0": ["signal_0"], "dummy1": ["signal_2"]}
        for group_name, group in groups.items():
            self.assertCountEqual([s.name for s in group], expected_signals[group_name])
