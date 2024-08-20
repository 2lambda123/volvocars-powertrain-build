# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for Signals class."""

import copy
import unittest
from unittest.mock import MagicMock
from pathlib import Path
from powertrain_build.build_proj_config import BuildProjConfig
from powertrain_build.signal_interfaces import CsvSignalInterfaces
from .io_cnfg import IO_CNFG_DICT, INPUT_CNFG_DICT, OUTPUT_CNFG_DICT, DBG_CNFG_DICT, DEP_IO_CNFG_DICT

CNFG_DIR = Path(Path(__file__).parent, 'cnfg_files')


class TestSignalsInterfaces(unittest.TestCase):
    """Test case for testing the SignalsInterfaces class."""

    loc_defs = {
        'Enable1': '(Vc_AcReg_B_CodegenPHEV == 1)'
                   ' && '
                   '(Vc_Ac_Ctrl_B_CodeGenTorqueEstOff == 1)'
    }

    def setUp(self):
        """Load the definition file used for all tests."""
        self._build_cfg = MagicMock(config_set=BuildProjConfig)
        prj_cnf_dir = str(CNFG_DIR)
        self._build_cfg.get_prj_cfg_dir = MagicMock(return_value=prj_cnf_dir)
        if_cnf_dir = str(Path(CNFG_DIR, 'ActiveInterfaces'))
        self._build_cfg.get_if_cfg_dir = MagicMock(return_value=if_cnf_dir)

        self._build_cfg.get_prj_config = MagicMock(return_value='VEP4_GENIII')
        self.vep = copy.deepcopy(self._build_cfg)

        self._build_cfg.get_prj_config = MagicMock(return_value='VED4_GENIII')
        self.ved = copy.deepcopy(self._build_cfg)

        self._unit_cfg = MagicMock()
        # Fixa unit config nedan!!!
        self._unit_cfg.get_per_cfg_unit_cfg = MagicMock(return_value={})
        self._unit_cfg.get_local_defs = MagicMock(return_value=self.loc_defs)
        self._signal_ifs = CsvSignalInterfaces(self.ved, self._unit_cfg)
        self.maxDiff = None

    def test_get_external_inputs_cfg1(self):
        """Test that the external inputs method work for VED4_GENIII."""
        signal_ifs = CsvSignalInterfaces(self.ved, self._unit_cfg)
        result = signal_ifs.get_external_inputs()
        expected_res = INPUT_CNFG_DICT['VED4_GENIII']
        self.assertDictEqual(result, expected_res)

    def test_get_external_inputs_cfg2(self):
        """Test that the external inputs method work for VEP4_GENIII.

        Furthermore, check that the default project can be overridden with
        the argument to get_external_inputs(conf).
        """
        signal_ifs = CsvSignalInterfaces(self.vep, self._unit_cfg)
        result = signal_ifs.get_external_inputs()
        expected_res = INPUT_CNFG_DICT['VEP4_GENIII']
        self.assertDictEqual(result, expected_res)

    def test_get_external_outputs_cfg1(self):
        """Test that the external outputs method work for VED4_GENIII."""
        signal_ifs = CsvSignalInterfaces(self.ved, self._unit_cfg)
        result = signal_ifs.get_external_outputs()
        expected_res = OUTPUT_CNFG_DICT['VED4_GENIII']
        self.assertDictEqual(result, expected_res)

    def test_get_external_outputs_cfg2(self):
        """Test that the external outputs method work for VEP4_GENIII."""
        signal_ifs = CsvSignalInterfaces(self.vep, self._unit_cfg)
        result = signal_ifs.get_external_outputs()
        expected_res = OUTPUT_CNFG_DICT['VEP4_GENIII']
        self.assertDictEqual(result, expected_res)

    def test_get_external_io(self):
        """Return a tuple with nrm, dep, dbg dicts."""
        signal_ifs = CsvSignalInterfaces(self.ved, self._unit_cfg)
        nrm_dict, dep_dict, _, dbg_dict = signal_ifs.get_external_io()
        self.assertDictEqual(nrm_dict, IO_CNFG_DICT['VED4_GENIII'])
        self.assertDictEqual(dep_dict, DEP_IO_CNFG_DICT['VED4_GENIII'])
        self.assertDictEqual(dbg_dict, DBG_CNFG_DICT['VED4_GENIII'])
        # Test another configuration
        signal_ifs = CsvSignalInterfaces(self.vep, self._unit_cfg)
        nrm_dict, dep_dict, _, dbg_dict = signal_ifs.get_external_io()
        self.assertDictEqual(nrm_dict, IO_CNFG_DICT['VEP4_GENIII'])
        self.assertDictEqual(dep_dict, DEP_IO_CNFG_DICT['VEP4_GENIII'])
        self.assertDictEqual(dbg_dict, DBG_CNFG_DICT['VEP4_GENIII'])
