# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Tests for pybuild version compatibility check module."""

import unittest
from pybuild import __config_version__
from pybuild.versioncheck import Version


class TestVersionCheck(unittest.TestCase):
    """Unit tests for pybuild version compatibility check module."""

    def test_float_version(self):
        version = Version(1.04)
        self.assertTupleEqual((version[0], version[1], version[2]), (1, 4, 0))
        version = Version(0.3)
        self.assertTupleEqual((version[0], version[1], version[2]), (0, 3, 0))

        self.assertRaises(ValueError, Version, -1.1)

    def test_int_version(self):
        version = Version(10)
        self.assertTupleEqual((version[0], version[1], version[2]), (10, 0, 0))

        self.assertRaises(ValueError, Version, -1)

    def test_string_version(self):
        version = Version('1.0.0')
        self.assertTupleEqual((version[0], version[1], version[2]), (1, 0, 0))

        self.assertRaises(ValueError, Version, '1')
        self.assertRaises(ValueError, Version, '1.0')
        self.assertRaises(ValueError, Version, '1.0.0.0')
        self.assertRaises(ValueError, Version, '1,0.0')
        self.assertRaises(ValueError, Version, 'wrong')

    def test_is_compatible(self):
        current_version = Version(__config_version__)

        self.assertTrue(Version.is_compatible(__config_version__))

        higher_major = '{0}.{1}.{2}'.format(current_version[0] + 1, current_version[1], current_version[2])
        self.assertFalse(Version.is_compatible(higher_major))

        if current_version[0] - 1 >= 0:
            lower_major = '{0}.{1}.{2}'.format(current_version[0] - 1, current_version[1], current_version[2])
            self.assertFalse(Version.is_compatible(lower_major))

        if current_version[1] - 1 >= 0:
            same_major_lower_minor = '{0}.{1}.{2}'.format(
                    current_version[0],
                    current_version[1] - 1,
                    current_version[2])
            self.assertTrue(Version.is_compatible(same_major_lower_minor))

        same_major_higher_minor = '{0}.{1}.{2}'.format(current_version[0], current_version[1] + 1, current_version[2])
        self.assertFalse(Version.is_compatible(same_major_higher_minor))

        if current_version[2] - 1 >= 0:
            same_major_lower_patch = '{0}.{1}.{2}'.format(
                    current_version[0],
                    current_version[1],
                    current_version[2] - 1)
            self.assertTrue(Version.is_compatible(same_major_lower_patch))

        same_major_higher_patch = '{0}.{1}.{2}'.format(current_version[0], current_version[1], current_version[2] + 1)
        self.assertFalse(Version.is_compatible(same_major_higher_patch))
