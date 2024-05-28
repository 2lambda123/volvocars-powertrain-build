# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for the pt_win32 module."""

import unittest
try:
    import win32job
    import win32api
except ImportError as import_error:
    raise unittest.SkipTest("Failed to import win32api, probably wrong platform") from import_error

from pybuild import pt_win32


class TestPtWin32Process(unittest.TestCase):
    """Tests for the pt_win32 module."""

    def test_kill_on_job_close(self):
        """Test that the process is killed when the job object is closed."""
        pt_process = pt_win32.PtWin32Process(kill_on_job_close=True)
        limit_flags = pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags']
        self.assertEqual(limit_flags, win32job.JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE)

        pt_process.run(command='cmd')
        self.assertEqual(pt_process.poll(), pt_win32.STILL_ACTIVE)
        win32api.CloseHandle(pt_process.job_handle)
        self.assertNotEqual(pt_process.poll(), pt_win32.STILL_ACTIVE)

    def test_add_limit_flags(self):
        """Test adding limit flags."""
        limit_a = 8
        limit_b = 32
        limit_ab = limit_a | limit_b
        pt_process = pt_win32.PtWin32Process(kill_on_job_close=False)
        pt_process.add_limit_flags(limit_a)
        self.assertEqual(pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'], limit_a)
        pt_process.add_limit_flags(limit_b)
        self.assertEqual(pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'], limit_ab)

    def test_remove_limit_flags(self):
        """Test removing limit flags."""
        limit_a = 8
        limit_b = 32
        limit_ab = limit_a | limit_b
        pt_process = pt_win32.PtWin32Process(kill_on_job_close=False)
        pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'] = limit_ab
        pt_process.remove_limit_flags(limit_a)
        self.assertEqual(pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'], limit_b)
        pt_process.remove_limit_flags(limit_b)
        self.assertEqual(pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'], 0)

    def test_set_limit_flags(self):
        """Test setting limit flags."""
        limit_a = 8
        limit_b = 32
        limit_ab = limit_a | limit_b
        pt_process = pt_win32.PtWin32Process(kill_on_job_close=False)
        pt_process.set_limit_flags(limit_a)
        self.assertEqual(pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'], limit_a)
        pt_process.set_limit_flags(limit_b)
        self.assertEqual(pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'], limit_b)
        pt_process.set_limit_flags(limit_ab)
        self.assertEqual(pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'], limit_ab)

    def test_get_limit_flags(self):
        """Test getting limit flags."""
        limit_a = 8
        limit_b = 32
        limit_ab = limit_a | limit_b
        pt_process = pt_win32.PtWin32Process(kill_on_job_close=False)
        pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'] = limit_ab
        self.assertEqual(pt_process.get_limit_flags(), limit_ab)
        pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'] = limit_a
        self.assertEqual(pt_process.get_limit_flags(), limit_a)
        pt_process.limit_info_dict['BasicLimitInformation']['LimitFlags'] = limit_b
        self.assertEqual(pt_process.get_limit_flags(), limit_b)
