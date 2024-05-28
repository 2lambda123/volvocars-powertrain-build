# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for GenAllSystemInfo."""
import json
from pathlib import Path
from unittest import TestCase
from unittest.mock import MagicMock
from numpy import ndarray
from pybuild.signal_interfaces import CsvSignalInterfaces
from pybuild.unit_configs import UnitConfigs
from pybuild.gen_allsysteminfo import GenAllSystemInfo

CNFG_DIR = Path(Path(__file__).parent, 'cnfg_files')


class TestGenAllSystemInfo(TestCase):
    """Test case for testing GenAllSystemInfo class."""

    def setUp(self):
        """Set up data structure for all tests."""
        self.mock_signal_if = MagicMock(spec_set=CsvSignalInterfaces)
        self.mock_signal_if.check_config.return_value = {
            "sigs": {
                "ext": {
                    "missing": {
                        "VcDummySignal1": {},
                        "VcDummySignal2": {}
                        },
                    "unused": {
                        "VcDummySignal3": {}
                    },
                    "inconsistent_defs": {
                        "VcDummySignal4": {}
                    }
                },
                "int": {
                    "VcDummyUnit1": {
                        "missing": {
                            "VcDummySignal5": {}
                        },
                        "unused": {
                            "VcDummySignal6": {}
                        },
                        "multiple_defs": {},
                        "inconsistent_defs": {}
                    },
                    "VcDummyUnit2": {
                        "missing": {},
                        "unused": {
                            "VcDummySignal7": {},
                            "VcDummySignal8": {}
                        }
                    }
                }
            }
        }

        self.mock_unit_cfg = MagicMock(spec_set=UnitConfigs)

        json_string = ""
        with Path(CNFG_DIR, 'Mock-unit_configs-get_per_unit_cfg.json').open(encoding="utf-8") as unit_cfg_file:
            json_string = unit_cfg_file.read()

        self.mock_unit_cfg.get_per_unit_cfg.return_value = json.loads(json_string)

        self.gen_allsysteminfo = GenAllSystemInfo(self.mock_signal_if, self.mock_unit_cfg)

    def test_gen_allsysteminfo_init_args(self):
        """Check that constructor arguments are validated."""
        # Call with reversed arguments
        self.assertRaises(TypeError, GenAllSystemInfo, self.mock_unit_cfg, self.mock_signal_if)

    def test_get_signals_without_sources(self):
        """Check that signal interfaces is parsed and filtered correctly."""
        result = self.gen_allsysteminfo.get_signals_without_source()
        expected = {
            "VcDummySignal1": {"VarStatus": "Not Used", "SignalType": "missing"},
            "VcDummySignal2": {"VarStatus": "Not Used", "SignalType": "missing"},
            "VcDummySignal3": {"VarStatus": "Not Used", "SignalType": "unused"},
            "VcDummySignal5": {"VarStatus": "Not Used", "SignalType": "missing"},
            "VcDummySignal6": {"VarStatus": "Not Used", "SignalType": "unused"},
            "VcDummySignal7": {"VarStatus": "Not Used", "SignalType": "unused"},
            "VcDummySignal8": {"VarStatus": "Not Used", "SignalType": "unused"},
        }

        self.assertDictEqual(result, expected)

    def test_get_core_ids(self):
        """Check that unit configs are parsed and filtered correctly."""
        with Path(CNFG_DIR, 'Mock-gen_allsysteminfo-_get_core_ids.json').open(encoding="utf-8") as core_id_json:
            expected = json.loads(core_id_json.read())

        result = self.gen_allsysteminfo.get_core_ids()
        # Convert arrays to lists
        for unit_data in result.values():
            for core_id, core_id_data in unit_data.items():
                for identifier, id_data in core_id_data.items():
                    for tl_field, tl_data in id_data.items():
                        if isinstance(tl_data, ndarray):
                            unit_data[core_id][identifier][tl_field] = list(tl_data)
        self.assertDictEqual(expected, result)

    def test_get_dids(self):
        """Check that unit configs are parsed and filtered correctly."""
        with Path(CNFG_DIR, 'Mock-gen_allsysteminfo-_get_dids.json').open(encoding="utf-8") as did_json:
            expected = json.loads(did_json.read())

        result = self.gen_allsysteminfo.get_dids()
        self.assertDictEqual(expected, result)
