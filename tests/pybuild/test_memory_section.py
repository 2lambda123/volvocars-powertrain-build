# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for memory_section module."""

from pathlib import Path
from unittest import mock, TestCase
from powertrain_build.build_proj_config import BuildProjConfig
from powertrain_build.memory_section import MemorySection
from powertrain_build.lib import helper_functions
from .test_build import remove

SRC_DIR = Path(__file__).parent


class TestMemorySection(TestCase):
    """Test class for testing the memory_section module."""

    def setUp(self):
        """Set up."""
        self.src_code_dir = Path(SRC_DIR, 'mem_out')
        helper_functions.create_dir(self.src_code_dir)

        cnfg_files_folder = Path(SRC_DIR, 'cnfg_files')
        build_cfg = mock.MagicMock(spec_set=BuildProjConfig(Path(cnfg_files_folder, 'ProjectCfg.json')))
        build_cfg.get_a2l_cfg = mock.MagicMock(return_value={'name': 'MOCK_HI'})
        build_cfg.get_ecu_info = mock.MagicMock(return_value=('HI', 'dummy'))
        build_cfg.get_swc_name = mock.MagicMock(return_value='MOCK_HI_SC')
        build_cfg.get_src_code_dst_dir = mock.MagicMock(return_value=self.src_code_dir)
        build_cfg.get_use_volatile_globals = mock.MagicMock(return_value=False)
        self.memory_section = MemorySection(build_cfg)

    def test_generate_cvc_header_cal(self):
        """Test MemorySection.generate_cvc_header() with CAL type file."""
        test_file_name = 'CVC_CAL_DUMMY.h'
        expected_start = [
            '#ifndef CVC_CAL_DUMMY_H\n',
            '#define CVC_CAL_DUMMY_H\n\n',
            '#undef CVC_CAL\n',
            '#undef CVC_CAL_ASIL_A\n',
            '#undef CVC_CAL_ASIL_B\n',
            '#undef CVC_CAL_ASIL_C\n',
            '#undef CVC_CAL_ASIL_D\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_A\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_B\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_C\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_D\n',
            '#define CVC_CAL \n',
            '#define CVC_CAL_ASIL_A \n',
            '#define CVC_CAL_ASIL_B \n',
            '#define CVC_CAL_ASIL_C \n',
            '#define CVC_CAL_ASIL_D \n',
            '#define CVC_CAL_MERGEABLE_ASIL_A \n',
            '#define CVC_CAL_MERGEABLE_ASIL_B \n',
            '#define CVC_CAL_MERGEABLE_ASIL_C \n',
            '#define CVC_CAL_MERGEABLE_ASIL_D \n',
            '#pragma section ".XcpCalibrationSection"\n',
            '\n#endif /* CVC_CAL_DUMMY_H */\n'
        ]
        expected_stop = [
            '#ifndef CVC_CAL_DUMMY_H\n',
            '#define CVC_CAL_DUMMY_H\n\n',
            '#undef CVC_CAL\n',
            '#undef CVC_CAL_ASIL_A\n',
            '#undef CVC_CAL_ASIL_B\n',
            '#undef CVC_CAL_ASIL_C\n',
            '#undef CVC_CAL_ASIL_D\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_A\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_B\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_C\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_D\n',
            '#pragma section\n',
            '\n#endif /* CVC_CAL_DUMMY_H */\n'
        ]
        result_start = self.memory_section.generate_cvc_header('START', test_file_name)
        result_stop = self.memory_section.generate_cvc_header('END', test_file_name)
        self.assertListEqual(expected_start, result_start)
        self.assertListEqual(expected_stop, result_stop)

    def test_generate_cvc_header_disp(self):
        """Test MemorySection.generate_cvc_header() with DISP type file."""
        test_file_name = 'CVC_DISP_DUMMY.h'
        expected_start = [
            '#ifndef CVC_DISP_DUMMY_H\n',
            '#define CVC_DISP_DUMMY_H\n\n',
            '#undef CVC_DISP\n',
            '#undef CVC_DISP_ASIL_A\n',
            '#undef CVC_DISP_ASIL_B\n',
            '#undef CVC_DISP_ASIL_C\n',
            '#undef CVC_DISP_ASIL_D\n',
            '#define CVC_DISP \n',
            '#define CVC_DISP_ASIL_A \n',
            '#define CVC_DISP_ASIL_B \n',
            '#define CVC_DISP_ASIL_C \n',
            '#define CVC_DISP_ASIL_D \n',
            '#define MOCK_HI_START_SEC_VAR_INIT_UNSPECIFIED\n',
            '#include "MOCK_HI_MemMap.h"\n',
            '\n#endif /* CVC_DISP_DUMMY_H */\n'
        ]
        expected_stop = [
            '#ifndef CVC_DISP_DUMMY_H\n',
            '#define CVC_DISP_DUMMY_H\n\n',
            '#undef CVC_DISP\n',
            '#undef CVC_DISP_ASIL_A\n',
            '#undef CVC_DISP_ASIL_B\n',
            '#undef CVC_DISP_ASIL_C\n',
            '#undef CVC_DISP_ASIL_D\n',
            '#define MOCK_HI_STOP_SEC_VAR_INIT_UNSPECIFIED\n',
            '#include "MOCK_HI_MemMap.h"\n',
            '\n#endif /* CVC_DISP_DUMMY_H */\n'
        ]
        result_start = self.memory_section.generate_cvc_header('START', test_file_name)
        result_stop = self.memory_section.generate_cvc_header('END', test_file_name)
        self.assertListEqual(expected_start, result_start)
        self.assertListEqual(expected_stop, result_stop)

    def test_generate_cvc_header_cal_with_volatile_globals(self):
        """Test MemorySection.generate_cvc_header() with CAL type file and volatile globals."""
        self.memory_section.use_volatile_globals = True
        test_file_name = 'CVC_CAL_DUMMY.h'
        expected_start = [
            '#ifndef CVC_CAL_DUMMY_H\n',
            '#define CVC_CAL_DUMMY_H\n\n',
            '#undef CVC_CAL\n',
            '#undef CVC_CAL_ASIL_A\n',
            '#undef CVC_CAL_ASIL_B\n',
            '#undef CVC_CAL_ASIL_C\n',
            '#undef CVC_CAL_ASIL_D\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_A\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_B\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_C\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_D\n',
            '#define CVC_CAL volatile\n',
            '#define CVC_CAL_ASIL_A volatile\n',
            '#define CVC_CAL_ASIL_B volatile\n',
            '#define CVC_CAL_ASIL_C volatile\n',
            '#define CVC_CAL_ASIL_D volatile\n',
            '#define CVC_CAL_MERGEABLE_ASIL_A volatile\n',
            '#define CVC_CAL_MERGEABLE_ASIL_B volatile\n',
            '#define CVC_CAL_MERGEABLE_ASIL_C volatile\n',
            '#define CVC_CAL_MERGEABLE_ASIL_D volatile\n',
            '#pragma section ".XcpCalibrationSection"\n',
            '\n#endif /* CVC_CAL_DUMMY_H */\n'
        ]
        expected_stop = [
            '#ifndef CVC_CAL_DUMMY_H\n',
            '#define CVC_CAL_DUMMY_H\n\n',
            '#undef CVC_CAL\n',
            '#undef CVC_CAL_ASIL_A\n',
            '#undef CVC_CAL_ASIL_B\n',
            '#undef CVC_CAL_ASIL_C\n',
            '#undef CVC_CAL_ASIL_D\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_A\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_B\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_C\n',
            '#undef CVC_CAL_MERGEABLE_ASIL_D\n',
            '#pragma section\n',
            '\n#endif /* CVC_CAL_DUMMY_H */\n'
        ]
        result_start = self.memory_section.generate_cvc_header('START', test_file_name)
        result_stop = self.memory_section.generate_cvc_header('END', test_file_name)
        self.assertListEqual(expected_start, result_start)
        self.assertListEqual(expected_stop, result_stop)

    def test_generate_cvc_header_disp_with_volatile_globals(self):
        """Test MemorySection.generate_cvc_header() with DISP type file and volatile globals."""
        self.memory_section.use_volatile_globals = True
        test_file_name = 'CVC_DISP_DUMMY.h'
        expected_start = [
            '#ifndef CVC_DISP_DUMMY_H\n',
            '#define CVC_DISP_DUMMY_H\n\n',
            '#undef CVC_DISP\n',
            '#undef CVC_DISP_ASIL_A\n',
            '#undef CVC_DISP_ASIL_B\n',
            '#undef CVC_DISP_ASIL_C\n',
            '#undef CVC_DISP_ASIL_D\n',
            '#define CVC_DISP volatile\n',
            '#define CVC_DISP_ASIL_A volatile\n',
            '#define CVC_DISP_ASIL_B volatile\n',
            '#define CVC_DISP_ASIL_C volatile\n',
            '#define CVC_DISP_ASIL_D volatile\n',
            '#define MOCK_HI_START_SEC_VAR_INIT_UNSPECIFIED\n',
            '#include "MOCK_HI_MemMap.h"\n',
            '\n#endif /* CVC_DISP_DUMMY_H */\n'
        ]
        expected_stop = [
            '#ifndef CVC_DISP_DUMMY_H\n',
            '#define CVC_DISP_DUMMY_H\n\n',
            '#undef CVC_DISP\n',
            '#undef CVC_DISP_ASIL_A\n',
            '#undef CVC_DISP_ASIL_B\n',
            '#undef CVC_DISP_ASIL_C\n',
            '#undef CVC_DISP_ASIL_D\n',
            '#define MOCK_HI_STOP_SEC_VAR_INIT_UNSPECIFIED\n',
            '#include "MOCK_HI_MemMap.h"\n',
            '\n#endif /* CVC_DISP_DUMMY_H */\n'
        ]
        result_start = self.memory_section.generate_cvc_header('START', test_file_name)
        result_stop = self.memory_section.generate_cvc_header('END', test_file_name)
        self.assertListEqual(expected_start, result_start)
        self.assertListEqual(expected_stop, result_stop)

    def test_generate_cvc_header_code(self):
        """Test MemorySection.generate_cvc_header() with CODE type file."""
        test_file_name = 'CVC_CODE_DUMMY.h'
        expected_start = [
            '#ifndef CVC_CODE_DUMMY_H\n',
            '#define CVC_CODE_DUMMY_H\n\n',
            '#define MOCK_HI_START_SEC_CODE\n',
            '#include "MOCK_HI_MemMap.h"\n',
            '\n#endif /* CVC_CODE_DUMMY_H */\n'
        ]
        expected_stop = [
            '#ifndef CVC_CODE_DUMMY_H\n',
            '#define CVC_CODE_DUMMY_H\n\n',
            '#define MOCK_HI_STOP_SEC_CODE\n',
            '#include "MOCK_HI_MemMap.h"\n',
            '\n#endif /* CVC_CODE_DUMMY_H */\n'
        ]
        result_start = self.memory_section.generate_cvc_header('START', test_file_name)
        result_stop = self.memory_section.generate_cvc_header('END', test_file_name)
        self.assertListEqual(expected_start, result_start)
        self.assertListEqual(expected_stop, result_stop)

    def test_generate_cvc_header_const(self):
        """Test MemorySection.generate_cvc_header() with CONST type file."""
        test_file_name = 'CVC_CONST_DUMMY.h'
        expected_start = [
            '#ifndef CVC_CONST_DUMMY_H\n',
            '#define CVC_CONST_DUMMY_H\n\n',
            '#define MOCK_HI_START_SEC_CONST_UNSPECIFIED\n',
            '#include "MOCK_HI_MemMap.h"\n',
            '\n#endif /* CVC_CONST_DUMMY_H */\n'
        ]
        expected_stop = [
            '#ifndef CVC_CONST_DUMMY_H\n',
            '#define CVC_CONST_DUMMY_H\n\n',
            '#define MOCK_HI_STOP_SEC_CONST_UNSPECIFIED\n',
            '#include "MOCK_HI_MemMap.h"\n',
            '\n#endif /* CVC_CONST_DUMMY_H */\n'
        ]
        result_start = self.memory_section.generate_cvc_header('START', test_file_name)
        result_stop = self.memory_section.generate_cvc_header('END', test_file_name)
        self.assertListEqual(expected_start, result_start)
        self.assertListEqual(expected_stop, result_stop)

    def test_generate_cvc_header_pre_declare(self):
        """Test MemorySection.generate_cvc_header() with PREDECL type file."""
        test_file_name = 'PREDECL_DUMMY.h'
        expected_start = [
            '#ifndef PREDECL_DUMMY_H\n',
            '#define PREDECL_DUMMY_H\n\n',
            '#include "MOCK_HI_MemMap.h"\n',
            '\n#endif /* PREDECL_DUMMY_H */\n'
        ]
        expected_stop = [
            '#ifndef PREDECL_DUMMY_H\n',
            '#define PREDECL_DUMMY_H\n\n',
            '#include "MOCK_HI_MemMap.h"\n',
            '\n#endif /* PREDECL_DUMMY_H */\n'
        ]
        result_start = self.memory_section.generate_cvc_header('START', test_file_name)
        result_stop = self.memory_section.generate_cvc_header('END', test_file_name)
        self.assertListEqual(expected_start, result_start)
        self.assertListEqual(expected_stop, result_stop)

    def test_generate_required_header_files(self):
        """Test MemorySection.generate_required_header_files()"""
        expected_file_names = [
            'CVC_CAL_START.h',
            'CVC_CAL_ASIL_A_START.h',
            'CVC_CAL_ASIL_B_START.h',
            'CVC_CAL_ASIL_C_START.h',
            'CVC_CAL_ASIL_D_START.h',
            'CVC_CAL_END.h',
            'CVC_CAL_ASIL_A_END.h',
            'CVC_CAL_ASIL_B_END.h',
            'CVC_CAL_ASIL_C_END.h',
            'CVC_CAL_ASIL_D_END.h',
            'CVC_DISP_START.h',
            'CVC_DISP_ASIL_A_START.h',
            'CVC_DISP_ASIL_B_START.h',
            'CVC_DISP_ASIL_C_START.h',
            'CVC_DISP_ASIL_D_START.h',
            'CVC_DISP_END.h',
            'CVC_DISP_ASIL_A_END.h',
            'CVC_DISP_ASIL_B_END.h',
            'CVC_DISP_ASIL_C_END.h',
            'CVC_DISP_ASIL_D_END.h',
            'CVC_CODE_START.h',
            'CVC_CODE_ASIL_A_START.h',
            'CVC_CODE_ASIL_B_START.h',
            'CVC_CODE_ASIL_C_START.h',
            'CVC_CODE_ASIL_D_START.h',
            'CVC_CODE_END.h',
            'CVC_CODE_ASIL_A_END.h',
            'CVC_CODE_ASIL_B_END.h',
            'CVC_CODE_ASIL_C_END.h',
            'CVC_CODE_ASIL_D_END.h',
            'CVC_CONST_START.h',
            'CVC_CONST_ASIL_A_START.h',
            'CVC_CONST_ASIL_B_START.h',
            'CVC_CONST_ASIL_C_START.h',
            'CVC_CONST_ASIL_D_START.h',
            'CVC_CONST_END.h',
            'CVC_CONST_ASIL_A_END.h',
            'CVC_CONST_ASIL_B_END.h',
            'CVC_CONST_ASIL_C_END.h',
            'CVC_CONST_ASIL_D_END.h',
            'CVC_NVM_START.h',
            'CVC_NVM_END.h',
            'CVC_NVM_P_START.h',
            'CVC_NVM_P_END.h',
            'PREDECL_START.h',
            'PREDECL_END.h',
            'PREDECL_CAL_START.h',
            'PREDECL_CAL_ASIL_A_START.h',
            'PREDECL_CAL_ASIL_B_START.h',
            'PREDECL_CAL_ASIL_C_START.h',
            'PREDECL_CAL_ASIL_D_START.h',
            'PREDECL_CAL_END.h',
            'PREDECL_CAL_ASIL_A_END.h',
            'PREDECL_CAL_ASIL_B_END.h',
            'PREDECL_CAL_ASIL_C_END.h',
            'PREDECL_CAL_ASIL_D_END.h',
            'PREDECL_CAL_EXT_START.h',
            'PREDECL_CAL_EXT_END.h',
            'PREDECL_CAL_MERG_START.h',
            'PREDECL_CAL_MERG_END.h',
            'PREDECL_DISP_START.h',
            'PREDECL_CONST_EXT_START.h',
            'PREDECL_CONST_EXT_END.h',
            'PREDECL_CONST_MERG_END.h',
            'PREDECL_CONST_MERG_START.h',
            'PREDECL_DISP_ASIL_A_START.h',
            'PREDECL_DISP_ASIL_B_START.h',
            'PREDECL_DISP_ASIL_C_START.h',
            'PREDECL_DISP_ASIL_D_START.h',
            'PREDECL_DISP_END.h',
            'PREDECL_DISP_ASIL_A_END.h',
            'PREDECL_DISP_ASIL_B_END.h',
            'PREDECL_DISP_ASIL_C_END.h',
            'PREDECL_DISP_ASIL_D_END.h',
            'PREDECL_CODE_START.h',
            'PREDECL_CODE_ASIL_A_START.h',
            'PREDECL_CODE_ASIL_B_START.h',
            'PREDECL_CODE_ASIL_C_START.h',
            'PREDECL_CODE_ASIL_D_START.h',
            'PREDECL_CODE_END.h',
            'PREDECL_CODE_ASIL_A_END.h',
            'PREDECL_CODE_ASIL_B_END.h',
            'PREDECL_CODE_ASIL_C_END.h',
            'PREDECL_CODE_ASIL_D_END.h',
            'PREDECL_CONST_START.h',
            'PREDECL_CONST_ASIL_A_START.h',
            'PREDECL_CONST_ASIL_B_START.h',
            'PREDECL_CONST_ASIL_C_START.h',
            'PREDECL_CONST_ASIL_D_START.h',
            'PREDECL_CONST_END.h',
            'PREDECL_CONST_ASIL_A_END.h',
            'PREDECL_CONST_ASIL_B_END.h',
            'PREDECL_CONST_ASIL_C_END.h',
            'PREDECL_CONST_ASIL_D_END.h',
            'PREDECL_NVM_START.h',
            'PREDECL_NVM_END.h',
            'PREDECL_NVM_P_START.h',
            'PREDECL_NVM_P_END.h'
        ]
        expected_file_paths = [Path(self.src_code_dir, f) for f in expected_file_names]
        self.memory_section.generate_required_header_files()
        generated_files = list(self.src_code_dir.glob('*'))
        self.assertCountEqual(generated_files, expected_file_paths)
        remove(*generated_files)
        self.src_code_dir.rmdir()
