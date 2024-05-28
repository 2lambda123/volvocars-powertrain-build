# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for SchedFuncs class."""

import unittest
from unittest.mock import MagicMock
from os.path import exists
from os import remove
from pathlib import Path
from pybuild.build_proj_config import BuildProjConfig
from pybuild.sched_funcs import SchedFuncs
from pybuild.unit_configs import UnitConfigs

SRC_DIR = Path(__file__).parent


class TestSchedFuncs(unittest.TestCase):
    """Test case for testing the FeatureConfigs class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        prj_cnf_dir = Path(SRC_DIR, 'cnfg_files')
        prj_out_dir = Path(SRC_DIR, 'output')
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        self.build_cfg.get_prj_cfg_dir = MagicMock(return_value=str(prj_cnf_dir))
        self.build_cfg.get_src_code_dst_dir = MagicMock(return_value=str(prj_out_dir))
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        self.build_cfg.get_scheduler_prefix = MagicMock(return_value='PROJ_')

        self.unit_cfg = MagicMock(spec_set=UnitConfigs)

        self.init_file = str(Path(prj_out_dir, 'VcExtINI.c'))
        if exists(self.init_file):
            remove(self.init_file)

        self.ts_file = str(Path(prj_out_dir, 'ts_test.h'))
        if exists(self.ts_file):
            remove(self.ts_file)

        self.sched_funcs = SchedFuncs(self.build_cfg, self.unit_cfg)

    def test_init_failure(self):
        """Check class init."""
        self.assertRaisesRegex(
            TypeError,
            'Input arguments should be an instance of:'
            f'BuildProjConfig, not {type(None)}'
            f'AND/OR UnitConfigs, not {type(None)}',
            SchedFuncs, None, None
        )

    def test_generate_sched_c_fncs(self):
        """Check generated scheduling raster functions."""
        self.sched_funcs.generate_sched_c_fncs(False)
        with open(self.init_file, encoding="utf-8") as fhandle:
            result = fhandle.read()
        with Path(SRC_DIR, 'reference_files', 'VcExtINI.c').open(encoding="utf-8") as fhandle:
            expected = fhandle.read()
        self.assertEqual(result, expected)

    def test_generate_ts_defines(self):
        """Check the ts defines generated for all units."""
        self.sched_funcs.generate_ts_defines(self.ts_file)
        with open(self.ts_file, encoding="utf-8") as fhandle:
            result = fhandle.read()
        with Path(SRC_DIR, 'reference_files', 'ts_test.h').open(encoding="utf-8") as fhandle:
            expected = fhandle.read()
        self.assertEqual(result, expected)
