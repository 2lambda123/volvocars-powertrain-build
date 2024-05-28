# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Tests for pybuild environment check module.

Run from project: py -3 -m pytest ./pybuild/test/test_environmentcheck.py
"""


import unittest
from unittest.mock import patch

from pybuild import environmentcheck


class TestpybuildEnvironmentCheck(unittest.TestCase):
    """Unit tests for environmentcheck module."""

    @patch('sys.version_info', (3, 5))
    def test_check_python_string_too_low_version_major_only(self):
        """Test for version 3.5, requiring a version higher than or equal to 3.6."""
        with self.assertRaises(RuntimeError):
            environmentcheck.check_python_string('3.6')

    @patch('sys.version_info', (3, 5))
    def test_check_python_string_too_low_version_major_minor(self):
        """Test for version 3.5, requiring exactly version 3.6."""
        with self.assertRaises(RuntimeError):
            environmentcheck.check_python_string('3.6', '3.6')

    @staticmethod
    @patch('sys.version_info', (3, 8))
    def test_check_python_string_higher_version_major_only():
        """Test for version 3.8, requiring a version higher than or equal to 3.6."""
        environmentcheck.check_python_string('3.6')

    @staticmethod
    @patch('sys.version_info', (3, 7))
    def test_check_python_string_version_between_limits_major_only():
        """Test for version 3.7, requiring a version higher than or equal to 3.6 and lower or equal to 3.8."""
        environmentcheck.check_python_string('3.6', '3.8')

    @patch('sys.version_info', (3, 8))
    def test_check_python_string_too_high_version_major_minor_identical(self):
        """Test for version 3.8, requiring exactly version 3.6."""
        with self.assertRaises(RuntimeError):
            environmentcheck.check_python_string('3.6', '3.6')

    @patch('sys.version_info', (3, 8))
    def test_check_python_string_too_high_version_major_minor(self):
        """Test for version 3.8, requiring a version between 3.6 to 3.7."""
        with self.assertRaises(RuntimeError):
            environmentcheck.check_python_string('3.6', '3.7')

    @staticmethod
    @patch('sys.version_info', (3, 6))
    def test_check_python_string_version_upper_lower_identical():
        """Test for version 3.6, requiring exactly version 3.6."""
        environmentcheck.check_python_string('3.6', '3.6')
