# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Test the config module."""
import json
import os
import unittest
from unittest.mock import patch
from pathlib import Path

from powertrain_build.config import ProcessHandler
from powertrain_build.config import CConfigParser
from powertrain_build.config import HeaderConfigParser
from powertrain_build.config import JsonConfigHandler

SRC_DIR = Path(__file__).parent
SKIP_WHILE_DEVELOPING = False
# SKIP_WHILE_DEVELOPING = True


class TestConfig(unittest.TestCase):
    """Test the config module."""

    def setUp(self):
        """Set up the test."""
        # Set create_new to True to update the files in reference map
        # And disable the skip statement where you want tests
        # self.create_new = SKIP_WHILE_DEVELOPING
        # self.create_new = True
        self.create_new = False
        basename_patch = patch('os.path.basename',
                               return_value='VcVmcPmm__HEP7')
        self.addCleanup(basename_patch.stop)
        self.basename_patch = basename_patch.start()
        cnfg_dir = str(Path(SRC_DIR, 'cnfg_files'))
        self.files = {
            'c_file': os.path.join(cnfg_dir, 'VcVmcPmm.c'),
            'c_sedded': os.path.join(cnfg_dir, 'VcVmcPmm.e'),
            'aux_file': os.path.join(cnfg_dir, 'tl_aux_defines_VmcPmm__HE.h'),
            'oport_file': os.path.join(cnfg_dir, 'VcVmcPmm__HEP7_OPortMvd_LocalDefs.h'),
            'json_file': os.path.join(cnfg_dir, 'config_VcVmcPmm__HEP7.json'),
            'ref_dir': str(Path(SRC_DIR, 'reference_files'))}

    def test_create_new(self):
        """Make sure this test is testing."""
        self.assertFalse(self.create_new)
        self.assertFalse(SKIP_WHILE_DEVELOPING)

    @unittest.skipIf(SKIP_WHILE_DEVELOPING, 'Updating other tests')
    def test_sed(self):
        """Test updating VcVmcPmm."""
        c_code = CConfigParser.read_file(self.files['c_file'])
        ref_e = self.files['c_sedded']
        if self.create_new:
            # Hack to update correct answers
            with open(ref_e, 'w') as ref_file:
                for line in c_code:
                    ref_file.write(line + '\n')
        with open(ref_e) as ref_file:
            sedded_ref = [line.rstrip('\n') for line in ref_file.readlines()]
        # assertListEqual is too slow to run regularly
        # self.assertTrue(c_code == sedded_ref)
        self.assertListEqual(c_code, sedded_ref)

    @unittest.skipIf(SKIP_WHILE_DEVELOPING, 'Updating other tests')
    def test_read_aux(self):
        """Test reading OPort file."""
        local_defines = HeaderConfigParser.read_file(self.files['aux_file'])
        header = HeaderConfigParser()
        header.parse_file_content(local_defines)
        local_defs = header.get_config()
        json_ref = self.files['ref_dir'] + '/config_local_defs.json'
        if self.create_new:
            # Hack to update correct answers
            with open(json_ref, 'w') as ref_file:
                ref_file.write(json.dumps(local_defs, indent=4))
        with open(json_ref) as ref_config_file:
            local_defs_ref = json.load(ref_config_file)
        self.assertDictEqual(local_defs, local_defs_ref)

    @unittest.skipIf(SKIP_WHILE_DEVELOPING, 'Updating other tests')
    def test_read_aux_after_oport(self):
        """Test reading OPort file."""
        oport_defines = HeaderConfigParser.read_file(self.files['oport_file'])
        header = HeaderConfigParser()
        header.parse_file_content(oport_defines)
        oport_defs = header.get_config()
        local_defines = HeaderConfigParser.read_file(self.files['aux_file'])
        header = HeaderConfigParser()
        header.set_defines(oport_defs)
        header.parse_file_content(local_defines)
        local_defs = header.get_config()
        json_ref = self.files['ref_dir'] + '/config_combined_header.json'
        if self.create_new:
            # Hack to update correct answers
            with open(json_ref, 'w') as ref_file:
                ref_file.write(json.dumps(local_defs, indent=4))
        with open(json_ref) as ref_config_file:
            local_defs_ref = json.load(ref_config_file)
        self.assertDictEqual(local_defs, local_defs_ref)

    @unittest.skipIf(SKIP_WHILE_DEVELOPING, 'Updating other tests')
    def test_read_oport(self):
        """Test reading OPort file."""
        local_defines = HeaderConfigParser.read_file(self.files['oport_file'])
        header = HeaderConfigParser()
        header.parse_file_content(local_defines)
        local_defs = header.get_config()
        json_ref = self.files['ref_dir'] + '/config_OPort_defs.json'
        if self.create_new:
            # Hack to update correct answers
            with open(json_ref, 'w') as ref_file:
                ref_file.write(json.dumps(local_defs, indent=4))
        with open(json_ref) as ref_config_file:
            local_defs_ref = json.load(ref_config_file)
        self.assertDictEqual(local_defs, local_defs_ref)

    @unittest.skipIf(SKIP_WHILE_DEVELOPING, 'Updating other tests')
    def test_get_files(self):
        """Test that we get the correct file names.

        A current model is used, but it does not have to actually exist.
        """
        model_dir = os.path.join('Models', 'SSPTM', 'VcVmcPmm__HEP7')
        model_src_dir = os.path.join(model_dir, 'pybuild_src')
        model_cfg_dir = os.path.join(model_dir, 'pybuild_cfg')
        files = ProcessHandler.get_files(os.path.join(model_dir, 'VcVmcPmm__HEP7.mdl'))
        config_dir = str(Path(SRC_DIR, 'cnfg_files'))
        expected_files = (
            self.files['oport_file'].replace(config_dir, model_src_dir),
            self.files['aux_file'].replace(config_dir, model_src_dir),
            self.files['c_file'].replace(config_dir, model_src_dir),
            self.files['json_file'].replace(config_dir, model_cfg_dir),
            )
        self.assertTupleEqual(files, expected_files)

    @unittest.skipIf(SKIP_WHILE_DEVELOPING, 'Updating other tests')
    def test_update_complete(self):
        """Test a complete config generation for a nasty model."""
        local_defs = ProcessHandler.get_header_config(self.files['oport_file'], {})
        aux_defs = ProcessHandler.get_header_config(self.files['aux_file'], local_defs)
        cparser = CConfigParser()
        c_code = cparser.read_file(self.files['c_file'])
        json_handler = JsonConfigHandler(cparser, aux_defs)
        unit_config = json_handler.read_config(self.files['json_file'])
        json_handler.update_config(unit_config, c_code, aux_defs)
        json_ref = self.files['ref_dir'] + '/config_combined.json'
        if self.create_new:
            # Hack to update correct answers
            json_handler.write_config(json_ref, unit_config)
        with open(json_ref) as ref_config_file:
            unit_ref_json = json.load(ref_config_file)
        self.assertDictEqual(unit_config, unit_ref_json)
