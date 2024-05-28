# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Run 'pytest' from the 'pytools' sub-directory to discover and launch all tests."""

import unittest
from unittest.mock import patch, Mock

from pybuild import pt_matlab


class TestMatlab(unittest.TestCase):
    """Tests for Matlab Python library."""

    def test_pathcmd_singledir(self):
        """Test generation of path commands."""
        self.assertEqual(pt_matlab.cmd_path(r"C:\foo\bar"), r"addpath('C:\foo\bar')")

    def test_pathcmd_recursive(self):
        """Test generation of path commands."""
        self.assertEqual(
            pt_matlab.cmd_path(r"C:\foo\bar", True), r"addpath(genpath('C:\foo\bar'))"
        )

    def test_cmd_arg_str(self):
        """Test argument conversion for strings."""
        self.assertEqual("'foobar'", pt_matlab.cmd_arg("foobar"))

    def test_cmd_arg_bool_true(self):
        """Test argument conversion for boolean 'True' value."""
        self.assertEqual("true", pt_matlab.cmd_arg(True))

    def test_cmd_arg_bool_false(self):
        """Test argument conversion for boolean 'False' value."""
        self.assertEqual("false", pt_matlab.cmd_arg(False))

    def test_cmd_arg_list(self):
        """Test argument conversion for list values (only strings)."""
        self.assertEqual("{'foo', 'bar'}", pt_matlab.cmd_arg(["foo", "bar"]))

    def test_is_model(self):
        """Test pt_matlab.is_model."""
        self.assertTrue(pt_matlab.is_model("foo.mdl"))
        self.assertTrue(pt_matlab.is_model("foo.slx"))
        self.assertFalse(pt_matlab.is_model("foo.notmdl"))

    def test_extract_model_names(self):
        """Test pt_matlab.extract_model_names."""
        dummy_files = [
            "Somme/Path/To/Model.mdl",
            "Somme/Path/To/Model.slx",
            "Somme/Path/To/Model_par.m",
            "Some/Other/Path/To/ModelTwo.mdl",
        ]
        expected = ["Model", "ModelTwo"]
        self.assertEqual(expected, pt_matlab.extract_model_names(dummy_files, ".mdl"))

    def test_cmd_callfunc(self):
        """Test pt_matlab.cmd_callfunc."""
        self.assertEqual("foo()", pt_matlab.cmd_callfunc("foo"))
        self.assertEqual("foo('bar')", pt_matlab.cmd_callfunc("foo", "bar"))
        self.assertEqual("foo('bar', 'baz')", pt_matlab.cmd_callfunc("foo", "bar", "baz"))


class TestPtMatlab(unittest.TestCase):
    """Test pt_matlab."""

    FAKE_MATLAB_CALLS = ["fake_matlab_call1()", "fake_matlab_call2('fake_arg1')"]

    @patch("os.linesep", "\r\n")
    def test_make_joined_cmds_windows(self):
        """Try making multiline commands separated correct for Windows."""
        self.assertEqual(
            "fake_matlab_call1();\r\nfake_matlab_call2('fake_arg1')",
            pt_matlab.cmds_join(self.FAKE_MATLAB_CALLS),
        )

    @patch("os.linesep", "\n")
    def test_make_joined_cmds_unix(self):
        """Try making multiline commands separated correct for Unices."""
        self.assertEqual(
            "fake_matlab_call1();\nfake_matlab_call2('fake_arg1')",
            pt_matlab.cmds_join(self.FAKE_MATLAB_CALLS),
        )


class TestRunMScript(unittest.TestCase):
    """Test running matlab script."""

    def setUp(self):
        """Set up."""
        pt_matlab.RETRY_TIME = 0
        pt_matlab.POLL_TIME = 0.001
        self.maxDiff = None
        self.matlab = pt_matlab.Matlab(dry_run=True)
        self.matlab.run_m_script = Mock(
            side_effect=self.matlab.run_m_script
        )  # wrap for call_count

    def test_no_attempts(self):
        """Test number of attempts."""
        expected_exitcode = 2
        exitcode = self.matlab.run_m_script("mfile.m", wrap_cmd=True, attempts=0)
        self.assertEqual(exitcode, expected_exitcode)

    def test_exitcode_returned(self):
        """Test correct exitcode."""
        expected_exitcode = 0
        exitcode = self.matlab.run_m_script("mfile.m", wrap_cmd=True, attempts=1)
        self.assertEqual(exitcode, expected_exitcode)

    def test_one_targetlink_error(self):
        """Test number of targetlink errors."""
        self.matlab.targetlink_watcher.targetlink_error = True
        expected_exitcode = 0
        expected_calls = 2  # targetlink_error is reset before the second attempt
        exitcode = self.matlab.run_m_script("mfile.m", wrap_cmd=True, attempts=10)
        self.assertEqual(exitcode, expected_exitcode)
        self.assertEqual(self.matlab.run_m_script.call_count, expected_calls)

    def test_attempts_exceeded(self):
        """Test attempts exceeded."""

        def set_error(__value):
            self.matlab.targetlink_watcher.targetlink_error = True

        self.matlab.sync_log = Mock(side_effect=set_error)
        expected_exitcode = 2
        expected_calls = (
            10 + 1
        )  # 10 attempts, 1 additional call when iteration exceeds attempts (no execution)
        exitcode = self.matlab.run_m_script("mfile.m", wrap_cmd=True, attempts=10)
        self.assertEqual(exitcode, expected_exitcode)
        self.assertEqual(self.matlab.run_m_script.call_count, expected_calls)
