# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for pybuild.build module."""

import os
import logging
import unittest
from unittest.mock import MagicMock, patch, PropertyMock
from pathlib import Path

from pybuild.lib import helper_functions
from pybuild.problem_logger import ProblemLogger
from pybuild.build_proj_config import BuildProjConfig
from pybuild.unit_configs import UnitConfigs
from pybuild.signal_interfaces import CsvSignalInterfaces
from pybuild.core import Core
from pybuild import build

SRC_DIR = Path(__file__).parent


def remove(*files):
    """Try to remove file."""
    for file_ in files:
        try:
            os.remove(file_)
        except FileNotFoundError:
            pass


def exists(*files):
    """Check if file exists."""
    for file_ in files:
        if not os.path.isfile(file_):
            raise AssertionError(f'File {file_} does not exist.')
    return True


class TestBuild(unittest.TestCase):
    """Test case for testing the build module."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        output_folder = Path(SRC_DIR, 'output')
        cnfg_files_folder = Path(SRC_DIR, 'cnfg_files')
        common_src_dir = str(Path(SRC_DIR, 'common_src_files'))
        prj_cnf_dir = str(cnfg_files_folder)
        prj_out_dir = str(output_folder)
        prj_src_dir = str(Path(SRC_DIR, 'src_files'))
        projdir = cnfg_files_folder.resolve()
        helper_functions.create_dir(Path(SRC_DIR, 'output'))
        helper_functions.create_dir(Path(cnfg_files_folder, 'output'))

        self.build_cfg = MagicMock(spec_set=BuildProjConfig(Path(cnfg_files_folder, 'ProjectCfg.json')))
        self.build_cfg.get_prj_cfg_dir = MagicMock(return_value=prj_cnf_dir)
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        self.build_cfg.get_reports_dst_dir = MagicMock(return_value=prj_out_dir)
        self.build_cfg.get_src_code_dst_dir = MagicMock(return_value=prj_out_dir)
        self.build_cfg.get_unit_cfg_deliv_dir = MagicMock(return_value=prj_out_dir)
        self.build_cfg.get_did_cfg_file_name = MagicMock(return_value='DIDIds_FullRange')
        self.build_cfg.get_car_com_dst = MagicMock(return_value=os.path.join(prj_out_dir, 'CarCom_DIDDefs.csv'))
        self.build_cfg.get_core_dummy_name = MagicMock(return_value=prj_out_dir + '/VcCoreDummy')
        self.build_cfg.get_nvm_defs = MagicMock(return_value={
            'fileName': 'vcc_nvm_struct',
            "baseNvmStructs": "nvm_structs_ref_empty.json"
            })
        self.build_cfg.get_common_src_dir = MagicMock(return_value=common_src_dir)
        self.build_cfg.get_unit_src_dirs = MagicMock(return_value={'mocked': prj_src_dir})
        self.build_cfg.get_unit_cfg_dirs = MagicMock(return_value={'mocked': prj_cnf_dir})
        self.build_cfg.get_a2l_name = MagicMock(return_value='merged.a2l')
        self.build_cfg.get_root_dir = MagicMock(return_value=projdir)
        self.build_cfg.get_ecu_info = MagicMock(return_value=('Denso', 'G2'))
        self.unit_cfg = MagicMock(spec_set=UnitConfigs)
        type(self.unit_cfg).base_types_headers = '#include tl_basetypes.h\n'
        type(self.unit_cfg).code_generators = 'target_link'

    @staticmethod
    def test_setup_logging():
        """Check that init_logger is called."""
        log = logging.getLogger()
        log_dst_dir = str(Path(SRC_DIR, 'output'))
        problem_logger = MagicMock(spec_set=ProblemLogger)
        build.setup_logging(log_dst_dir, problem_logger, debug=True, quiet=True)
        problem_logger.init_logger.assert_called_once_with(log)

    def test_check_interfaces(self):
        """Check that interface check is run."""
        signal_if = MagicMock(spec_set=CsvSignalInterfaces)
        signal_if.check_config = MagicMock(return_value={'sigs': {'ext': {}, 'int': {}}})
        build.check_interfaces(self.build_cfg, signal_if)
        self.build_cfg.get_reports_dst_dir.assert_called_once()
        signal_if.check_config.called_once()

    def test_interface_report(self):
        """Check that interface report is generated."""
        signal_if = MagicMock(spec_set=CsvSignalInterfaces)
        signal_if.check_config = MagicMock(return_value={'sigs': {'ext': {}, 'int': {}}})
        filename = str(Path(SRC_DIR, 'output', 'SigIf.html'))
        remove(filename)
        build.interface_report(self.build_cfg, self.unit_cfg, signal_if)
        self.build_cfg.get_reports_dst_dir.assert_called_once()
        exists(filename)

    def test_generate_did_files(self):
        """Check that interface report is generated."""
        output_folder = Path(SRC_DIR, 'output')
        filename = str(Path(output_folder, 'VcDIDDefinition'))
        cfile = filename + '.c'
        hfile = filename + '.h'
        csvfile = str(Path(output_folder, 'CarCom_DIDDefs.csv'))
        remove(cfile, hfile, csvfile)
        build.generate_did_files(self.build_cfg, self.unit_cfg)
        self.build_cfg.get_src_code_dst_dir.assert_called_once()
        self.build_cfg.get_did_cfg_file_name.assert_called()
        self.build_cfg.get_prj_cfg_dir.assert_called()
        exists(cfile, hfile, csvfile)

    def test_generate_core_dummy_denso(self):
        """Check that core dummy files are generated."""
        self.build_cfg.get_ecu_info = MagicMock(return_value=('Denso', 'G2'))
        core = MagicMock(spec_set=Core)
        core.get_current_core_config = MagicMock()
        filename = str(Path(SRC_DIR, 'output', 'VcCoreDummy'))
        cfile = filename + '.c'
        hfile = filename + '.h'
        remove(cfile, hfile)
        build.generate_core_dummy(self.build_cfg, core, self.unit_cfg)
        core.get_current_core_config.assert_called_once()
        self.build_cfg.get_core_dummy_name.assert_called_once()
        self.build_cfg.get_ecu_info.assert_called_once()
        exists(cfile, hfile)

    def test_generate_core_dummy_rb(self):
        """Check that core dummy files are generated."""
        self.build_cfg.get_ecu_info = MagicMock(return_value=('RB', 'xx'))
        core = MagicMock(spec_set=Core)
        core.get_current_core_config = MagicMock()
        filename = str(Path(SRC_DIR, 'output', 'VcCoreDummy'))
        cfile = filename + '.c'
        hfile = filename + '.h'
        remove(cfile, hfile)
        build.generate_core_dummy(self.build_cfg, core, self.unit_cfg)
        core.get_current_core_config.assert_called_once()
        self.build_cfg.get_core_dummy_name.assert_called_once()
        self.build_cfg.get_ecu_info.assert_called_once()
        exists(cfile, hfile)

    def test_generate_core_dummy_other(self):
        """Check that core dummy files are generated."""
        self.build_cfg.get_ecu_info = MagicMock(return_value=('Other', 'yy'))
        core = MagicMock(spec_set=Core)
        core.get_current_core_config = MagicMock()
        self.assertRaises(ValueError, build.generate_core_dummy, self.build_cfg, core, self.unit_cfg)

    def test_generate_ext_var(self):
        """Check that ExtVar files are generated."""
        self.build_cfg.has_yaml_interface = False
        signal_if = MagicMock(spec_set=CsvSignalInterfaces)
        signal_if.get_external_io = MagicMock(return_value=(
            {
                'EMS-Output': {},
                'EMS-Input': {'DummyIn': {
                    'type': 'Float32',
                    'min': 0,
                    'max': 100,
                    'unit': 'Nm',
                    'description': 'Dummy',
                    'init': 0,
                    'element_index': 5,
                    'IOType': 'x'
                }},
                'LIN-Output': {},
                'LIN-Input': {},
                'CAN-Output': {},
                'CAN-Input': {},
                'Private CAN-Output': {},
                'Private CAN-Input': {}
            }, {
                'EMS-Output': {},
                'EMS-Input': {'DummyInSafe': {
                    'type': 'Float32',
                    'min': 0,
                    'max': 100,
                    'unit': 'Nm',
                    'description': 'Safe dummy',
                    'init': 0,
                    'element_index': 5,
                    'IOType': 's'
                }},
                'LIN-Output': {},
                'LIN-Input': {},
                'CAN-Output': {},
                'CAN-Input': {},
                'Private CAN-Output': {},
                'Private CAN-Input': {}
            }, {}, {}
        ))
        filepath = str(Path(SRC_DIR, 'output'))
        files = [
            filepath + '/VcExtVar.c',
            filepath + '/VcExtVar.a2l',
            filepath + '/VcExtVarSafe.c',
            filepath + '/VcExtVarSafe.a2l',
            filepath + '/VcDebug.c',
            filepath + '/VcDebug.a2l',
            filepath + '/VcDebugOutput.c',
            filepath + '/VcDebugOutput.a2l']
        remove(*files)
        with patch('pybuild.user_defined_types.UserDefinedTypes') as udt_mock:
            udt_mock.return_value.common_header_files = PropertyMock(return_value=[])
            build.generate_ext_var(self.build_cfg, self.unit_cfg, signal_if, udt_mock)
        signal_if.get_external_io.assert_called_once()
        self.build_cfg.get_src_code_dst_dir.assert_called()
        exists(*files)
        self.assertFalse(os.path.isfile(f"{filepath}/VcExtVarSecure.c"))

    def test_generate_nvm_def(self):
        """Check that NVM files are generated."""
        unit_cfg = MagicMock(spec_set=UnitConfigs)
        type(unit_cfg).base_types_headers = ''
        no_nvm_a2l = False
        filepath = str(Path(SRC_DIR, 'output'))
        files = [
            filepath + '/vcc_nvm_struct.c',
            filepath + '/vcc_nvm_struct.h',
            filepath + '/vcc_nvm_struct.a2l']
        remove(*files)
        build.generate_nvm_def(self.build_cfg, unit_cfg, no_nvm_a2l)
        self.build_cfg.get_src_code_dst_dir.assert_called()
        unit_cfg.get_per_cfg_unit_cfg.assert_called()
        exists(*files)

    @unittest.mock.patch('shutil.copy2')
    def test_copy_unit_src_to_src_out(self, mock_copy):
        """Check that source files are copied."""
        build.copy_unit_src_to_src_out(self.build_cfg)
        self.build_cfg.get_unit_src_dirs.assert_called()
        self.build_cfg.get_src_code_dst_dir.assert_called()
        mock_copy.assert_called()

    @unittest.mock.patch('shutil.copy2')
    def test_copy_unit_cfgs_to_output(self, mock_copy):
        """Check that unit-configs are copied."""
        build.copy_unit_cfgs_to_output(self.build_cfg)
        self.build_cfg.get_unit_cfg_deliv_dir.assert_called()
        self.build_cfg.get_unit_cfg_dirs.assert_called()
        mock_copy.assert_called()

    def test_merge_a2l_files(self):
        """Check that a2l-files are merged."""
        unit_cfg = MagicMock(spec_set=UnitConfigs)
        filepath = str(Path(SRC_DIR, 'output'))
        remove(filepath + '/merged.a2l')
        build.merge_a2l_files(self.build_cfg, unit_cfg)
        self.build_cfg.get_unit_src_dirs.assert_called()
        self.build_cfg.get_src_code_dst_dir.assert_called()
        self.build_cfg.get_a2l_name.assert_called()
        unit_cfg.get_per_unit_cfg.assert_called()
        exists(filepath + '/merged.a2l')

    def test_build_no_cfg(self):
        """Check that main entrypoint raises exception for missing config."""
        prj_root = str(Path(SRC_DIR, 'cnfg_files', 'NonexistentProjectCfg.json'))
        with unittest.mock.patch('pybuild.build.find_all_project_configs') as mock:
            mock.return_value = [prj_root]
            self.assertRaises(FileNotFoundError, build.build, prj_root, quiet=True)

    @staticmethod
    @unittest.mock.patch('pybuild.unit_configs.UnitConfigs.get_per_unit_cfg')
    @unittest.mock.patch('pybuild.build.find_all_project_configs')
    def test_build(mock_find_all_project_configs, mock_get_per_unit_cfg):
        """Check that main entrypoint can be run without exceptions."""
        prj_root = str(Path(SRC_DIR, 'cnfg_files', 'ProjectCfg.json'))
        output = str(Path(SRC_DIR, 'output', 'logs', 'build.log'))
        remove(output)
        mock_find_all_project_configs.return_value = [prj_root]
        mock_get_per_unit_cfg.return_value = {'VcScBCoord': {}, 'VcScCVehMtn': {}, 'VcScFeh': {}}
        build.build(prj_root,
                    interface=True,
                    core_dummy=True,
                    no_abort=False,
                    debug=True,
                    quiet=True)
        exists(output)

    @staticmethod
    @unittest.mock.patch('pybuild.unit_configs.UnitConfigs.get_per_unit_cfg')
    @unittest.mock.patch('pybuild.build.find_all_project_configs')
    def test_build_ec(mock_find_all_project_configs, mock_get_per_unit_cfg):
        """Check that main entrypoint can be run without exceptions."""
        prj_root = str(Path(SRC_DIR, 'cnfg_files', 'ProjectCfg.json'))
        output = str(Path(SRC_DIR, 'output', 'logs', 'build.log'))
        remove(output)
        mock_find_all_project_configs.return_value = [prj_root]
        mock_get_per_unit_cfg.return_value = {
            'VcScBCoord': {'code_generator': 'embedded_coder'},
            'VcScCVehMtn': {'code_generator': 'embedded_coder'},
            'VcScFeh': {'code_generator': 'embedded_coder'}}
        build.build(prj_root,
                    interface=True,
                    core_dummy=True,
                    no_abort=False,
                    debug=True,
                    quiet=True)
        exists(output)

    @staticmethod
    @unittest.mock.patch('pybuild.unit_configs.UnitConfigs.get_per_unit_cfg')
    @unittest.mock.patch('pybuild.build.find_all_project_configs')
    def test_build_mixed_ec_tl(mock_find_all_project_configs, mock_get_per_unit_cfg):
        """Check that main entrypoint can be run without exceptions."""
        prj_root = str(Path(SRC_DIR, 'cnfg_files', 'ProjectCfg.json'))
        output = str(Path(SRC_DIR, 'output', 'logs', 'build.log'))
        remove(output)
        mock_find_all_project_configs.return_value = [prj_root]
        mock_get_per_unit_cfg.return_value = {
            'VcScBCoord': {'code_generator': 'embedded_coder'},
            'VcScCVehMtn': {'code_generator': 'target_link'},
            'VcScFeh': {}}
        build.build(prj_root,
                    interface=True,
                    core_dummy=True,
                    no_abort=False,
                    debug=True,
                    quiet=True)
        exists(output)

    @staticmethod
    @unittest.mock.patch('pybuild.unit_configs.UnitConfigs.get_per_unit_cfg')
    @unittest.mock.patch('pybuild.build.find_all_project_configs')
    def test_build_no_abort(mock_find_all_project_configs, mock_get_per_unit_cfg):
        """Check that main entrypoint can be run without exceptions with no abort set to True."""
        prj_root = str(Path(SRC_DIR, 'cnfg_files', 'ProjectCfg.json'))
        output = str(Path(SRC_DIR, 'output', 'logs', 'build.log'))
        remove(output)
        mock_find_all_project_configs.return_value = [prj_root]
        mock_get_per_unit_cfg.return_value = {'VcScBCoord': {}, 'VcScCVehMtn': {}, 'VcScFeh': {}}
        build.build(prj_root,
                    interface=True,
                    core_dummy=True,
                    no_abort=True,
                    debug=True,
                    quiet=True)
        exists(output)
