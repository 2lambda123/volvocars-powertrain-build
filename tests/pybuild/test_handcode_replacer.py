# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for pybuild.handcode_replacer module."""

import unittest
from pybuild import handcode_replacer


class TestPragmaRegexStart(unittest.TestCase):
    """Unit tests for pybuild.handcode_replacer regexes."""

    def setUp(self):
        self.pragma_replacer = handcode_replacer.PragmaReplacer()

    def tearDown(self):
        self.assertTrue(self.pragma_replacer.cvc_started)
        self.assertIsNotNone(self.pragma_replacer.cvc)

    def test_cvc(self):
        """Test the line found in original_line below"""
        original_line = '#pragma section CVC\n'
        resulting_line = self.pragma_replacer.replace_line(original_line)
        expected_line = '#include "CVC_CODE_START.h"\n'
        self.assertEqual(resulting_line, expected_line)

    def test_cal(self):
        """Test the line found in original_line below"""
        original_line = '#pragma section CVCCAL\n'
        resulting_line = self.pragma_replacer.replace_line(original_line)
        expected_line = '#include "CVC_CAL_START.h"\n'
        self.assertEqual(resulting_line, expected_line)

    def test_disp(self):
        """Test the line found in original_line below"""
        original_line = '#pragma section CVCDISP\n'
        resulting_line = self.pragma_replacer.replace_line(original_line)
        expected_line = '#include "CVC_DISP_START.h"\n'
        self.assertEqual(resulting_line, expected_line)

    def test_nvm(self):
        """Test the line found in original_line below"""
        original_line = '#pragma section CVCNVM\n'
        resulting_line = self.pragma_replacer.replace_line(original_line)
        expected_line = '#include "CVC_NVM_START.h"\n'
        self.assertEqual(resulting_line, expected_line)

    def test_nvm_persistent(self):
        """Test the line found in original_line below"""
        original_line = '#pragma section CVCNVM_P\n'
        resulting_line = self.pragma_replacer.replace_line(original_line)
        expected_line = '#include "CVC_NVM_P_START.h"\n'
        self.assertEqual(resulting_line, expected_line)


class TestPragmaRegexStop(unittest.TestCase):
    """Unit tests for setting the stop lines."""
    def setUp(self):
        self.pragma_replacer = handcode_replacer.PragmaReplacer()
        self.pragma_replacer.cvc_started = True

    def tearDown(self):
        self.assertFalse(self.pragma_replacer.cvc_started)
        self.assertIsNone(self.pragma_replacer.cvc)

    def test_cvc(self):
        """Test the line found in original_line below"""
        self.pragma_replacer.cvc = 'CODE'
        original_line = '#pragma section\n'
        resulting_line = self.pragma_replacer.replace_line(original_line)
        expected_line = '#include "CVC_CODE_END.h"\n'
        self.assertEqual(resulting_line, expected_line)


class TestCodeSwitchReplacer(unittest.TestCase):
    """Unit tests for setting the stop lines."""
    def setUp(self):
        self.codesw_replacer = handcode_replacer.CodeSwitchReplacer()

    def test_cvc(self):
        """Test the line found in original_line below"""
        original_line = '#include "SPM_Codeswitch_Setup.h"\n'
        resulting_line = self.codesw_replacer.replace_line(original_line)
        expected_line = '#include "VcCodeSwDefines.h"\n'
        self.assertEqual(resulting_line, expected_line)
