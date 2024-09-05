# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Module for testing the reading of core id legacy config files."""

import unittest

from pathlib import Path
from powertrain_build.build_proj_config import BuildProjConfig

CNFG_DIR = Path(Path(__file__).parent, 'cnfg_files')


class TestReadCodeSw(unittest.TestCase):
    """Test case for testing the FeatureConfigs class."""

    @classmethod
    def setUpClass(cls):
        """Set-up common data structures for all tests in the test case."""
        cls.build_prj_cfg = BuildProjConfig(str(Path(CNFG_DIR, 'ProjectCfg.json')))

    def test_get_root_dir(self):
        """Check reading the build project definition files."""
        result = self.build_prj_cfg.get_root_dir()
        expected = str(CNFG_DIR.resolve())
        self.assertEqual(result, expected)

    def test_get_incuded_units(self):
        """Check reading the build project definition files."""
        result = self.build_prj_cfg.get_included_units()
        expected = ['VcScBCoord', 'VcScCVehMtn', 'VcScFeh', 'VcConst']
        self.assertEqual(result, expected)

    def test_get_code_generation_config_default(self):
        """Test build_proj_config._get_code_generation_config with not input."""
        expected = {'CodeGenerationConfig': self.build_prj_cfg._get_default_code_generation_config()}
        self.assertDictEqual(self.build_prj_cfg._get_code_generation_config(), expected)

    def test_get_code_generation_config_project_template_and_custom(self):
        """Test build_proj_config._get_code_generation_config with project template and custom changes."""
        self.build_prj_cfg = BuildProjConfig(str(Path(CNFG_DIR, 'ProjectCfg_CodeGenConfig.json')))
        expected = self.build_prj_cfg._get_default_code_generation_config()
        expected['generalAsilLevelDebug'] = 'D'
        expected['generalAsilLevelDependability'] = 'D'
        expected['generateInterfaceHeaders'] = True
        expected['generateYamlInterfaceFile'] = True
        expected['useSwcNameAsPrefix'] = True
        self.assertDictEqual(self.build_prj_cfg._prj_cfg['CodeGenerationConfig'], expected)
