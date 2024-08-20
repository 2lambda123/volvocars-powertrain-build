# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unittests for helper_functions."""
import unittest
from powertrain_build.lib import helper_functions as HF


class TestHelperFunctions(unittest.TestCase):
    """Test cases for helper functions."""

    def setUp(self):
        """Set up common data structures."""
        self.basic_dict1 = {
                "Bananas": 2,
                "Oranges": {
                    "String": "test"
                },
                "Apples": 4,
        }
        self.basic_dict2 = {
                "Pears": 1,
                "Apples": 2,
                "Balls": 2,
                "Oranges": {}
        }

        self.nested_dict1 = {
            "Bananas": {
                "Type": "Blue",
                "Size": 3,
                "Countries": ["Denmark"]
            },
            "Apples": {
                "Type": "Granny Smith",
                "Colour": "Green",
                "Size": 9
            },
            "Cheese": {
                "Comment": "I love cheese!"
            }
        }
        self.nested_dict2 = {
            "Bananas": {
                "Destination": "Unknown",
                "Size": 7,
                "Countries": ["Sweden", "Norway"]
            },
            "Pears": {
                "Type": "Green ones",
                "Size": "Regular"
            },
            "Apples": {
                "Size": 51
            },
            "Cheese": {
                "Comment": "!!"
            }
        }

    def test_merge_dicts(self):
        """Test basic dict merging."""
        expected = {
                "Bananas": 2,
                "Oranges": {
                    "String": "test"
                },
                "Apples": 4,
                "Pears": 1,
                "Balls": 2
        }
        result = HF.merge_dicts(self.basic_dict1, self.basic_dict2)
        self.assertDictEqual(result, expected)

    def test_merge_dicts_handle_collision(self):
        """Test dict merging with custom collision handling."""
        expected = {
                "Bananas": 2,
                "Oranges": "COLLISION",
                "Apples": "COLLISION",
                "Pears": 1,
                "Balls": 2
        }
        result = HF.merge_dicts(self.basic_dict1, self.basic_dict2, lambda a, b: "COLLISION")
        self.assertDictEqual(result, expected)

    def test_merge_dicts_recursively(self):
        """Test nested dict merging recursively."""
        expected = {
            "Bananas": {
                "Type": "Blue",
                "Size": 3,
                "Destination": "Unknown",
                "Countries": ["Denmark"]
            },
            "Apples": {
                "Type": "Granny Smith",
                "Colour": "Green",
                "Size": 9
            },
            "Cheese": {
                "Comment": "I love cheese!"
            },
            "Pears": {
                "Type": "Green ones",
                "Size": "Regular"
            }
        }

        result = HF.merge_dicts(self.nested_dict1, self.nested_dict2, merge_recursively=True)
        self.assertDictEqual(result, expected)

    def test_merge_dicts_handle_collision_recursively(self):
        """Test nested dict merging with custom collision handling."""
        expected = {
            "Bananas": {
                "Type": "Blue",
                "Size": 10,
                "Destination": "Unknown",
                "Countries": ["Denmark", "Sweden", "Norway"]
            },
            "Apples": {
                "Type": "Granny Smith",
                "Colour": "Green",
                "Size": 60
            },
            "Cheese": {
                "Comment": "I love cheese!!!"
            },
            "Pears": {
                "Type": "Green ones",
                "Size": "Regular"
            },
        }
        result = HF.merge_dicts(self.nested_dict1, self.nested_dict2, lambda a, b: a + b, True)
        self.assertDictEqual(result, expected)
