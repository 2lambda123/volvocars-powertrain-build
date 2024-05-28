# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

import unittest
from pybuild.create_conversion_table import get_vtab_text


class TestGetVtabText(unittest.TestCase):
    """Unit test class for testing the get_vtab_text function."""

    def setUp(self):
        """Set up method for the test cases. Initializes a vtab dictionary
        to be used in the test cases.
        """
        self.vtab = {
            'name': 'VTab1',
            'disp_values': ['Value1', 'Value2', 'Value3'],
            'start_value': 10
        }

    def test_get_vtab_text(self):
        """Test case for the get_vtab_text function. Checks if the function
        returns the expected output when provided with a vtab dictionary
        containing display values.
        """
        expected_output = (
            '    /begin COMPU_VTAB\n'
            '        CONV_TAB_VTab1             /* Name */\n'
            '        "Conversion table"          /* LongIdentifier */\n'
            '        TAB_VERB            /* ConversionType */\n'
            '        3          /* NumberValuePairs */\n'
            '        10          /* InVal */\n'
            '        "Value1"          /* OutVal */\n'
            '        11          /* InVal */\n'
            '        "Value2"          /* OutVal */\n'
            '        12          /* InVal */\n'
            '        "Value3"          /* OutVal */\n'
            '    /end COMPU_VTAB\n\n'
        )

        result = get_vtab_text(self.vtab)
        self.assertEqual(result, expected_output)

    def test_get_vtab_text_empty_disp_values(self):
        """Test case for the get_vtab_text function. Checks if the function
        returns the expected output when provided with a vtab dictionary
        with an empty list of display values.
        """
        self.vtab['disp_values'] = []
        expected_output = (
            '    /begin COMPU_VTAB\n'
            '        CONV_TAB_VTab1             /* Name */\n'
            '        "Conversion table"          /* LongIdentifier */\n'
            '        TAB_VERB            /* ConversionType */\n'
            '        0          /* NumberValuePairs */\n'
            '    /end COMPU_VTAB\n\n'
        )

        result = get_vtab_text(self.vtab)
        self.assertEqual(result, expected_output)
