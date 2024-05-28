# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

import os
import unittest

from pathlib import Path

from pybuild.signal_interfaces import YamlSignalInterfaces

BASEDIR = Path(__file__).parent / "cnfg_files/test-repo"
CSP_PROJECT_ROOT = BASEDIR / "Projects/CSP/CATC"

EXTERNAL_INPUT_SIGNAL = "sVcFioc_Te_AmbTMecRimSnsr"
EXTERNAL_OUTPUT_SIGNAL = "yVcTestTx_B_CircCnctVlvReq"
EXTERNAL_INPUT_MODEL = "VcTestRx"
EXTERNAL_OUTPUT_MODEL = "VcTestTx"


class TestYamlSignalInterface(unittest.TestCase):

    def setUp(self):

        project_cfg_file = CSP_PROJECT_ROOT / "ProjectCfg.json"
        os.chdir(project_cfg_file.parents[3])
        self.yaml_signal_interface = YamlSignalInterfaces.from_config_file(project_cfg_file)

    def test_get_external_io(self):
        normal = self.yaml_signal_interface.get_external_io()[0]
        ext_input = normal["input"]
        ext_output = normal["output"]
        self.assertIn(EXTERNAL_INPUT_SIGNAL, ext_input)
        self.assertIn(EXTERNAL_OUTPUT_SIGNAL, ext_output)

    def test_get_external_inputs(self):
        external_inputs = self.yaml_signal_interface.get_external_inputs()
        ext_output = external_inputs["input"]
        self.assertIn(EXTERNAL_INPUT_SIGNAL, ext_output)

    def test_get_external_outputs(self):
        external_outputs = self.yaml_signal_interface.get_external_outputs()
        ext_output = external_outputs["output"]
        self.assertIn(EXTERNAL_OUTPUT_SIGNAL, ext_output)

    def test_check_external_outp(self):
        self.yaml_signal_interface._check_external_outp()
        result = self.yaml_signal_interface._result
        model_inconsistencies = result["sigs"]["ext"]["inconsistent_defs"][EXTERNAL_OUTPUT_MODEL]
        self.assertNotIn(EXTERNAL_INPUT_SIGNAL, model_inconsistencies)

    def test_check_external_inp(self):
        self.yaml_signal_interface._check_external_inp()
        result = self.yaml_signal_interface._result
        model_inconsistencies = result["sigs"]["ext"]["inconsistent_defs"][EXTERNAL_INPUT_MODEL]
        self.assertNotIn(EXTERNAL_OUTPUT_SIGNAL, model_inconsistencies)


if __name__ == '__main__':
    unittest.main()
