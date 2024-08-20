# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for a2l.py."""

from copy import deepcopy
import unittest
from unittest.mock import MagicMock
from powertrain_build.a2l import A2l
from powertrain_build.build_proj_config import BuildProjConfig

A2L_DATA = {
    "function": "rVcAesSupM",
    "vars": {
        "rVcAesSupM_p_SupMonrSCTarDly": {
            "var": {
                "type": "Float32",
                "cvc_type": "CVC_DISP"
            },
            "a2l_data": {
                "unit": "kPa",
                "description": "Low pass filtered supercharger target pressure",
                "max": "300",
                "min": "0",
                "lsb": "1",
                "offset": "0",
                "bitmask": None,
                "x_axis": None,
                "y_axis": None,
            },
            "array": None
        },
        "cVcAesSupM_B_SupMonrHiBypFiMPerm": {
            "var": {
                "type": "Bool",
                "cvc_type": "CVC_CAL"
            },
            "a2l_data": {
                "unit": "",
                "description": "Switch to bypass FiM permission  supercharger high boost monitor",
                "max": 1,
                "min": 0,
                "lsb": 1,
                "offset": 0
            }
        },
        "tVcAesSupM_tc_SupMonrSCTarDly": {
            "var": {
                "type": "Float32",
                "cvc_type": "CVC_CAL",
            },
            "a2l_data": {
                "unit": "s",
                "description": "Supercharger boost pressure monitor target pressure "
                               "lowpass filter time constant engine speed support points",
                "max": "100",
                "min": "0",
                "lsb": "1",
                "offset": "0",
                "x_axis": None
            },
            "array": [6]
        },
        "tVcAesSupM_tc_SupMonrSCTarDly_x": {
            "var": {
                "type": "Float32",
                "cvc_type": "CVC_CAL"
            },
            "a2l_data": {
                "unit": "rpm",
                "description": "Supercharger boost pressure monitor target pressure "
                               "lowpass filter time constant engine speed support points",
                "max": "10000",
                "min": "0",
                "lsb": "1",
                "offset": "0"
            },
            "array": [6]
        },
        "mVcAesSupM_m_SupChrgrStuckMaxLoadLim_y": {
            "var": {
                "type": "UInt16",
                "cvc_type": "CVC_CAL"
            },
            "a2l_data": {
                "unit": "rpm",
                "description": "Engine speed breakpoint data for supercharger stuck load limit",
                "max": "10000",
                "min": "0",
                "lsb": "0.25",
                "offset": "0",
            },
            "array": [4]
        },
        "mVcAesSupM_m_SupChrgrStuckMaxLoadLim_x": {
            "var": {
                "type": "UInt16",
                "cvc_type": "CVC_CAL"
            },
            "a2l_data": {
                "unit": "kPa",
                "description": "Ambient Pressure breakpoint data for supercharger stuck load limit",
                "max": "200",
                "min": "0",
                "lsb": "0.0039063",
                "offset": "0",
            },
            "array": [3]
        },
        "mVcAesSupM_m_SupChrgrStuckMaxLoadLim": {
            "var": {
                "type": "UInt16",
                "cvc_type": "CVC_CAL"
            },
            "a2l_data": {
                "unit": "g/rev",
                "description": "Supercharger stuck load limit",
                "max": "5",
                "min": "0",
                "lsb": "0.00024414",
                "offset": "0",
                "x_axis": None,
                "y_axis": None
            },
            "array": [3, 4]
        },
        "not_a2l_var": {
            "var": None,
            "a2l_data": None
        }
    }
}

A2L_OUTPUT = ("\n"
              "    /begin CHARACTERISTIC\n"
              "        cVcAesSupM_B_SupMonrHiBypFiMPerm /* Name */\n"
              "        \"Switch to bypass FiM permission  supercharger high boost monitor\" /* LongIdentifier */\n"
              "        VALUE   /* Datatype */\n"
              "        0x00000000    /* address: cVcAesSupM_B_SupMonrHiBypFiMPerm */\n"
              "        UBYTE_COL_DIRECT   /* Deposit */\n"
              "        0   /* MaxDiff */\n"
              "        rVcAesSupM_1_0_0_   /* Conversion */\n"
              "        0   /* LowerLimit */\n"
              "        1   /* UpperLimit */\n"
              "    /end CHARACTERISTIC\n"
              "\n"
              "    /begin CHARACTERISTIC\n"
              "        tVcAesSupM_tc_SupMonrSCTarDly /* Name */\n"
              "        \"Supercharger boost pressure monitor target pressure lowpass filter time constant engine"
              " speed support points\" /* LongIdentifier */\n"
              "        CURVE   /* Datatype */\n"
              "        0x00000000    /* address: tVcAesSupM_tc_SupMonrSCTarDly */\n"
              "        FLOAT32_IEEE_COL_DIRECT   /* Deposit */\n"
              "        0   /* MaxDiff */\n"
              "        rVcAesSupM_1_0_0_0_s   /* Conversion */\n"
              "        0   /* LowerLimit */\n"
              "        100   /* UpperLimit */\n"
              "        /begin AXIS_DESCR\n"
              "            COM_AXIS    /* Attribute */\n"
              "            NO_INPUT_QUANTITY   /* InputQuantity */\n"
              "            rVcAesSupM_1_0_0_0_rpm  /* Conversion */\n"
              "            6  /* MaxAxisPoints */\n"
              "            0  /* LowerLimit */\n"
              "            10000   /* UpperLimit */\n"
              "            AXIS_PTS_REF tVcAesSupM_tc_SupMonrSCTarDly_x\n"
              "            DEPOSIT ABSOLUTE\n"
              "        /end AXIS_DESCR\n"
              "    /end CHARACTERISTIC\n"
              "\n"
              "    /begin CHARACTERISTIC\n"
              "        mVcAesSupM_m_SupChrgrStuckMaxLoadLim /* Name */\n"
              "        \"Supercharger stuck load limit\" /* LongIdentifier */\n"
              "        MAP   /* Datatype */\n"
              "        0x00000000    /* address: mVcAesSupM_m_SupChrgrStuckMaxLoadLim */\n"
              "        UWORD_COL_DIRECT   /* Deposit */\n"
              "        0   /* MaxDiff */\n"
              "        rVcAesSupM_0_00024414_0_0_g_rev   /* Conversion */\n"
              "        0   /* LowerLimit */\n"
              "        5   /* UpperLimit */\n"
              "        /begin AXIS_DESCR\n"
              "            COM_AXIS    /* Attribute */\n"
              "            NO_INPUT_QUANTITY   /* InputQuantity */\n"
              "            rVcAesSupM_0_0039063_0_0_kPa  /* Conversion */\n"
              "            3  /* MaxAxisPoints */\n"
              "            0  /* LowerLimit */\n"
              "            200   /* UpperLimit */\n"
              "            AXIS_PTS_REF mVcAesSupM_m_SupChrgrStuckMaxLoadLim_x\n"
              "            DEPOSIT ABSOLUTE\n"
              "        /end AXIS_DESCR\n"
              "        /begin AXIS_DESCR\n"
              "            COM_AXIS    /* Attribute */\n"
              "            NO_INPUT_QUANTITY   /* InputQuantity */\n"
              "            rVcAesSupM_0_25_0_0_rpm  /* Conversion */\n"
              "            4  /* MaxAxisPoints */\n"
              "            0  /* LowerLimit */\n"
              "            10000   /* UpperLimit */\n"
              "            AXIS_PTS_REF mVcAesSupM_m_SupChrgrStuckMaxLoadLim_y\n"
              "            DEPOSIT ABSOLUTE\n"
              "        /end AXIS_DESCR\n"
              "    /end CHARACTERISTIC\n"
              "\n"
              "    /begin AXIS_PTS\n"
              "        tVcAesSupM_tc_SupMonrSCTarDly_x   /* Name */\n"
              "        \"Supercharger boost pressure monitor target pressure lowpass filter time constant engine"
              " speed support points\"   /* LongIdentifier */\n"
              "        0x00000000\n"
              "        NO_INPUT_QUANTITY   /* InputQuantity */\n"
              "        FLOAT32_IEEE_X_INCR_DIRECT  /* Deposit */\n"
              "        0   /* MaxDiff */\n"
              "        rVcAesSupM_1_0_0_0_rpm  /* Conversion */\n"
              "        6  /* MaxAxisPoints */\n"
              "        0   /* LowerLimit */\n"
              "        10000   /* UpperLimit */\n"
              "        DEPOSIT ABSOLUTE\n"
              "    /end AXIS_PTS\n"
              "\n"
              "    /begin AXIS_PTS\n"
              "        mVcAesSupM_m_SupChrgrStuckMaxLoadLim_y   /* Name */\n"
              "        \"Engine speed breakpoint data for supercharger stuck load limit\"   /* LongIdentifier */\n"
              "        0x00000000\n"
              "        NO_INPUT_QUANTITY   /* InputQuantity */\n"
              "        UWORD_X_INCR_DIRECT  /* Deposit */\n"
              "        0   /* MaxDiff */\n"
              "        rVcAesSupM_0_25_0_0_rpm  /* Conversion */\n"
              "        4  /* MaxAxisPoints */\n"
              "        0   /* LowerLimit */\n"
              "        10000   /* UpperLimit */\n"
              "        DEPOSIT ABSOLUTE\n"
              "    /end AXIS_PTS\n"
              "\n"
              "    /begin AXIS_PTS\n"
              "        mVcAesSupM_m_SupChrgrStuckMaxLoadLim_x   /* Name */\n"
              "        \"Ambient Pressure breakpoint data for supercharger stuck load limit\"   /* LongIdentifier */\n"
              "        0x00000000\n"
              "        NO_INPUT_QUANTITY   /* InputQuantity */\n"
              "        UWORD_X_INCR_DIRECT  /* Deposit */\n"
              "        0   /* MaxDiff */\n"
              "        rVcAesSupM_0_0039063_0_0_kPa  /* Conversion */\n"
              "        3  /* MaxAxisPoints */\n"
              "        0   /* LowerLimit */\n"
              "        200   /* UpperLimit */\n"
              "        DEPOSIT ABSOLUTE\n"
              "    /end AXIS_PTS\n"
              "\n"
              "    /begin MEASUREMENT\n"
              "        rVcAesSupM_p_SupMonrSCTarDly /* Name */\n"
              "        \"Low pass filtered supercharger target pressure\" /* LongIdentifier */\n"
              "        FLOAT32_IEEE   /* Datatype */\n"
              "        rVcAesSupM_1_0_0_0_kPa   /* Conversion */\n"
              "        1   /* Resolution */\n"
              "        0   /* Accuracy */\n"
              "        0   /* LowerLimit */\n"
              "        300   /* UpperLimit */\n"
              "        READ_WRITE\n"
              "        ECU_ADDRESS 0x00000000\n"
              "    /end MEASUREMENT\n"
              "\n"
              "    /begin COMPU_METHOD\n"
              "        rVcAesSupM_1_0_0_0_kPa   /* Name */\n"
              "        \"\"    /* LongIdentifier */\n"
              "        RAT_FUNC    /* ConversionType */\n"
              "        \"%11.3\"   /* Format */\n"
              "        \"kPa\" /* Unit */\n"
              "        COEFFS 0 1 0.0 0 0 1.0\n"
              "    /end COMPU_METHOD\n"
              "\n"
              "    /begin COMPU_METHOD\n"
              "        rVcAesSupM_1_0_0_   /* Name */\n"
              "        \"\"    /* LongIdentifier */\n"
              "        RAT_FUNC    /* ConversionType */\n"
              "        \"%11.3\"   /* Format */\n"
              "        \"\" /* Unit */\n"
              "        COEFFS 0 1 0.0 0 0 1\n"
              "    /end COMPU_METHOD\n"
              "\n"
              "    /begin COMPU_METHOD\n"
              "        rVcAesSupM_1_0_0_0_s   /* Name */\n"
              "        \"\"    /* LongIdentifier */\n"
              "        RAT_FUNC    /* ConversionType */\n"
              "        \"%11.3\"   /* Format */\n"
              "        \"s\" /* Unit */\n"
              "        COEFFS 0 1 0.0 0 0 1.0\n"
              "    /end COMPU_METHOD\n"
              "\n"
              "    /begin COMPU_METHOD\n"
              "        rVcAesSupM_1_0_0_0_rpm   /* Name */\n"
              "        \"\"    /* LongIdentifier */\n"
              "        RAT_FUNC    /* ConversionType */\n"
              "        \"%11.3\"   /* Format */\n"
              "        \"rpm\" /* Unit */\n"
              "        COEFFS 0 1 0.0 0 0 1.0\n"
              "    /end COMPU_METHOD\n"
              "\n"
              "    /begin COMPU_METHOD\n"
              "        rVcAesSupM_0_25_0_0_rpm   /* Name */\n"
              "        \"\"    /* LongIdentifier */\n"
              "        RAT_FUNC    /* ConversionType */\n"
              "        \"%11.3\"   /* Format */\n"
              "        \"rpm\" /* Unit */\n"
              "        COEFFS 0 1 0.0 0 0 0.25\n"
              "    /end COMPU_METHOD\n"
              "\n"
              "    /begin COMPU_METHOD\n"
              "        rVcAesSupM_0_0039063_0_0_kPa   /* Name */\n"
              "        \"\"    /* LongIdentifier */\n"
              "        RAT_FUNC    /* ConversionType */\n"
              "        \"%11.3\"   /* Format */\n"
              "        \"kPa\" /* Unit */\n"
              "        COEFFS 0 1 0.0 0 0 0.0039063\n"
              "    /end COMPU_METHOD\n"
              "\n"
              "    /begin COMPU_METHOD\n"
              "        rVcAesSupM_0_00024414_0_0_g_rev   /* Name */\n"
              "        \"\"    /* LongIdentifier */\n"
              "        RAT_FUNC    /* ConversionType */\n"
              "        \"%11.3\"   /* Format */\n"
              "        \"g/rev\" /* Unit */\n"
              "        COEFFS 0 1 0.0 0 0 0.00024414\n"
              "    /end COMPU_METHOD\n"
              "\n"
              "    /begin FUNCTION\n"
              "        rVcAesSupM /* Name */\n"
              "        \"\"  /* LongIdentifier */\n"
              "        /begin DEF_CHARACTERISTIC\n"
              "            cVcAesSupM_B_SupMonrHiBypFiMPerm /* Identifier */\n"
              "            tVcAesSupM_tc_SupMonrSCTarDly /* Identifier */\n"
              "            tVcAesSupM_tc_SupMonrSCTarDly_x /* Identifier */\n"
              "            mVcAesSupM_m_SupChrgrStuckMaxLoadLim_y /* Identifier */\n"
              "            mVcAesSupM_m_SupChrgrStuckMaxLoadLim_x /* Identifier */\n"
              "            mVcAesSupM_m_SupChrgrStuckMaxLoadLim /* Identifier */\n"
              "        /end DEF_CHARACTERISTIC\n"
              "        /begin LOC_MEASUREMENT\n"
              "            rVcAesSupM_p_SupMonrSCTarDly /* Identifier */\n"
              "        /end LOC_MEASUREMENT\n"
              "    /end FUNCTION\n"
              "\n"
              "    /begin RECORD_LAYOUT\n"
              "        FLOAT32_IEEE_COL_DIRECT /* Name */\n"
              "        FNC_VALUES 1 FLOAT32_IEEE COLUMN_DIR DIRECT\n"
              "    /end RECORD_LAYOUT\n"
              "\n"
              "    /begin RECORD_LAYOUT\n"
              "        UBYTE_COL_DIRECT /* Name */\n"
              "        FNC_VALUES 1 UBYTE COLUMN_DIR DIRECT\n"
              "    /end RECORD_LAYOUT\n"
              "\n"
              "    /begin RECORD_LAYOUT\n"
              "        FLOAT32_IEEE_X_INCR_DIRECT /* Name */\n"
              "        AXIS_PTS_X 1 FLOAT32_IEEE INDEX_INCR DIRECT\n"
              "    /end RECORD_LAYOUT\n"
              "\n"
              "    /begin RECORD_LAYOUT\n"
              "        UWORD_X_INCR_DIRECT /* Name */\n"
              "        AXIS_PTS_X 1 UWORD INDEX_INCR DIRECT\n"
              "    /end RECORD_LAYOUT\n"
              "\n"
              "    /begin RECORD_LAYOUT\n"
              "        UWORD_COL_DIRECT /* Name */\n"
              "        FNC_VALUES 1 UWORD COLUMN_DIR DIRECT\n"
              "    /end RECORD_LAYOUT\n")


class TestA2l(unittest.TestCase):
    """Test case for testing the A2l class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        self.build_cfg.get_ecu_info = MagicMock(return_value=('Denso', 'G2'))
        self.a2l = A2l(A2L_DATA, self.build_cfg)

    def test_init_a2l(self):
        """Test generation of a2l string from given dict."""
        self.assertEqual(self.a2l._a2lstr, A2L_OUTPUT)

    def test_init_a2l_invalid(self):
        """Test generation of a2l string from invalid dict."""
        invalid = deepcopy(A2L_DATA)
        del invalid['vars']['rVcAesSupM_p_SupMonrSCTarDly']['var']['cvc_type']
        self.assertRaises(KeyError, A2l, invalid, self.build_cfg)

    def test_find_axis_data(self):
        """Test parsing of all variables to identify axis points."""
        self.a2l._find_axis_data()
        result = self.a2l._axis_data
        expected = {
            'mVcAesSupM_m_SupChrgrStuckMaxLoadLim': ('mVcAesSupM_m_SupChrgrStuckMaxLoadLim_x',
                                                     'mVcAesSupM_m_SupChrgrStuckMaxLoadLim_x'),
            'tVcAesSupM_tc_SupMonrSCTarDly': ('tVcAesSupM_tc_SupMonrSCTarDly_x', None)}
        self.assertEqual(result, expected)

    def test_find_axis_ref(self):
        """Test parsing of all variables to identify which are defined as axis points."""
        self.a2l._find_axis_ref()
        result = self.a2l._axis_ref
        expected = {}
        self.assertEqual(result, expected)

    def test_get_a2d_minmax(self):
        """Test getting min max limits from a2l data."""
        minlim, maxlim = self.a2l._get_a2d_minmax({'min': '0', 'max': '100'})
        self.assertEqual(minlim, '0')
        self.assertEqual(maxlim, '100')
        minlim, maxlim = self.a2l._get_a2d_minmax({})
        self.assertEqual(minlim, '-1e38')
        self.assertEqual(maxlim, '1e38')

    def test_check_axis_ref(self):
        """Test check of axis definitions."""
        self.a2l.clear_log()
        self.a2l._check_axis_ref()
        self.assertEqual(self.a2l.get_nbr_problems(), {'critical': 0, 'warning': 0})

    def test_check_axis_ref_invalid(self):
        """Test check of axis definitions."""
        invalid = deepcopy(A2L_DATA)
        invalid['vars']['rVcAesSupM_p_SupMonrSCTarDly']['a2l_data']['x_axis'] = 'undefined_variable'
        invalid['vars']['rVcAesSupM_p_SupMonrSCTarDly']['a2l_data']['y_axis'] = 'undefined_variable2'
        invalid['vars']['cVcAesSupM_B_SupMonrHiBypFiMPerm']['a2l_data']['x_axis'] = 'undefined_variable'
        invalid['vars']['cVcAesSupM_B_SupMonrHiBypFiMPerm']['a2l_data']['y_axis'] = 'undefined_variable2'
        a2l = A2l(invalid, self.build_cfg)
        a2l.clear_log()
        a2l._check_axis_ref()
        self.assertEqual(a2l.get_nbr_problems(), {'critical': 0, 'warning': 1})

    def test_gen_compu_methods(self):
        """Test generation of COMPU_METHOD data."""
        self.a2l._gen_compu_methods()
        result = self.a2l._compu_meths
        expected = {
            (0.00024414, 0.0, 'g/rev'): {
                'coeffs': 'COEFFS 0 1 0.0 0 0 0.00024414',
                'name': 'rVcAesSupM_0_00024414_0_0_g_rev',
                'vars': ['mVcAesSupM_m_SupChrgrStuckMaxLoadLim']},
            (0.0039063, 0.0, 'kPa'): {
                'coeffs': 'COEFFS 0 1 0.0 0 0 0.0039063',
                'name': 'rVcAesSupM_0_0039063_0_0_kPa',
                'vars': ['mVcAesSupM_m_SupChrgrStuckMaxLoadLim_x']},
            (0.25, 0.0, 'rpm'): {
                'coeffs': 'COEFFS 0 1 0.0 0 0 0.25',
                'name': 'rVcAesSupM_0_25_0_0_rpm',
                'vars': ['mVcAesSupM_m_SupChrgrStuckMaxLoadLim_y']},
            (1, 0.0, ''): {
                'coeffs': 'COEFFS 0 1 0.0 0 0 1',
                'name': 'rVcAesSupM_1_0_0_',
                'vars': ['cVcAesSupM_B_SupMonrHiBypFiMPerm']},
            (1.0, 0.0, 'kPa'): {
                'coeffs': 'COEFFS 0 1 0.0 0 0 1.0',
                'name': 'rVcAesSupM_1_0_0_0_kPa',
                'vars': ['rVcAesSupM_p_SupMonrSCTarDly']},
            (1.0, 0.0, 'rpm'): {
                'coeffs': 'COEFFS 0 1 0.0 0 0 1.0',
                'name': 'rVcAesSupM_1_0_0_0_rpm',
                'vars': ['tVcAesSupM_tc_SupMonrSCTarDly_x']},
            (1.0, 0.0, 's'): {
                'coeffs': 'COEFFS 0 1 0.0 0 0 1.0',
                'name': 'rVcAesSupM_1_0_0_0_s',
                'vars': ['tVcAesSupM_tc_SupMonrSCTarDly']}}
        self.assertEqual(result, expected)

    def test_compu_key_2_name(self):
        """Test generation of COMPU_METHOD name from the keys in the name."""
        result = self.a2l._compu_key_2_name((1, 0, 'km/h'))
        expected = 'rVcAesSupM_1_0_km_h'
        self.assertEqual(result, expected)

    def test_array_to_a2l_string(self):
        """Test conversion of c-style array definitions to A2L MATRIX_DIM style."""
        result = self.a2l._array_to_a2l_string([1, 2, 3])
        expected = 'MATRIX_DIM 1 2 3'
        self.assertEqual(result, expected)

    def test_get_coefs_str(self):
        """Test calculation of a2l-coeffs from the lsb and offs fields."""
        result = self.a2l._get_coefs_str(2, 3)
        expected = 'COEFFS 0 1 3 0 0 2'
        self.assertEqual(result, expected)

    def test_calc_lsb(self):
        """Test conversion of 2^-2, style lsbs to numericals."""
        result = self.a2l._calc_lsb(1)
        expected = 1
        self.assertEqual(result, expected)
        result = self.a2l._calc_lsb('2')
        expected = 2
        self.assertEqual(result, expected)
        result = self.a2l._calc_lsb('2^-2')
        expected = 0.25
        self.assertEqual(result, expected)

    def test_gen_record_layouts_data(self):
        """Test generation of record layouts."""
        self.a2l._gen_record_layouts_data()
        result = self.a2l._rec_layouts
        expected = {
            'FLOAT32_IEEE_COL_DIRECT': 'FNC_VALUES 1 FLOAT32_IEEE COLUMN_DIR DIRECT',
            'FLOAT32_IEEE_X_INCR_DIRECT': 'AXIS_PTS_X 1 FLOAT32_IEEE INDEX_INCR DIRECT',
            'UBYTE_COL_DIRECT': 'FNC_VALUES 1 UBYTE COLUMN_DIR DIRECT',
            'UWORD_COL_DIRECT': 'FNC_VALUES 1 UWORD COLUMN_DIR DIRECT',
            'UWORD_X_INCR_DIRECT': 'AXIS_PTS_X 1 UWORD INDEX_INCR DIRECT'}
        self.assertEqual(result, expected)

    def test_get_inpq_data(self):
        """Test InputQuantity parameters. Valid data."""
        result = self.a2l._get_inpq_data('tVcAesSupM_tc_SupMonrSCTarDly_x')
        expected = 'tVcAesSupM_tc_SupMonrSCTarDly_x'
        self.assertEqual(result, expected)

    def test_get_inpq_data_invalid(self):
        """Test InputQuantity parameters. Invalid data."""
        result = self.a2l._get_inpq_data('other_name')
        expected = 'NO_INPUT_QUANTITY'
        self.assertEqual(result, expected)
        result = self.a2l._get_inpq_data(None)
        expected = 'NO_INPUT_QUANTITY'
        self.assertEqual(result, expected)

    def test_gen_a2l_measurement_blk(self):
        """Test generation of a2l MEASUREMENT block. Valid data."""
        var_name = 'rVcAesSupM_p_SupMonrSCTarDly'
        data = A2L_DATA['vars'][var_name]
        result = self.a2l._gen_a2l_measurement_blk(var_name, data)
        expected = '''
    /begin MEASUREMENT
        rVcAesSupM_p_SupMonrSCTarDly /* Name */
        "Low pass filtered supercharger target pressure" /* LongIdentifier */
        FLOAT32_IEEE   /* Datatype */
        rVcAesSupM_1_0_0_0_kPa   /* Conversion */
        1   /* Resolution */
        0   /* Accuracy */
        0   /* LowerLimit */
        300   /* UpperLimit */
        READ_WRITE
        ECU_ADDRESS 0x00000000
    /end MEASUREMENT
'''
        self.assertEqual(result, expected)

    def test_gen_a2l_measurement_blk_invalid(self):
        """Test generation of a2l MEASUREMENT block. Invalid data"""
        var_name = 'rVcAesSupM_p_SupMonrSCTarDly'
        data = {}
        result = self.a2l._gen_a2l_measurement_blk(var_name, data)
        expected = None
        self.assertEqual(result, expected)

    def test_gen_a2l_characteristic_blk(self):
        """Test generation of a2l CHARACTERISTIC block. Valid data."""
        var_name = 'cVcAesSupM_B_SupMonrHiBypFiMPerm'
        data = A2L_DATA['vars'][var_name]
        result = self.a2l._gen_a2l_characteristic_blk(var_name, data)
        expected = '''
    /begin CHARACTERISTIC
        cVcAesSupM_B_SupMonrHiBypFiMPerm /* Name */
        "Switch to bypass FiM permission  supercharger high boost monitor" /* LongIdentifier */
        VALUE   /* Datatype */
        0x00000000    /* address: cVcAesSupM_B_SupMonrHiBypFiMPerm */
        UBYTE_COL_DIRECT   /* Deposit */
        0   /* MaxDiff */
        rVcAesSupM_1_0_0_   /* Conversion */
        0   /* LowerLimit */
        1   /* UpperLimit */
    /end CHARACTERISTIC
'''
        self.assertEqual(result, expected)

    def test_gen_a2l_characteristic_blk_invalid(self):
        """Test generation of a2l CHARACTERISTIC block. Invalid data."""
        var_name = 'cVcAesSupM_B_SupMonrHiBypFiMPerm'
        data = {}
        result = self.a2l._gen_a2l_characteristic_blk(var_name, data)
        expected = None
        self.assertEqual(result, expected)

    def test_gen_a2l_axis_desc_blk(self):
        """Test generation of a2l AXIS_DESCR block."""
        inp_quant = None
        axis_pts_ref = 'tVcAesSupM_tc_SupMonrSCTarDly_x'
        result = self.a2l._gen_a2l_axis_desc_blk(inp_quant, axis_pts_ref)
        expected = '''
        /begin AXIS_DESCR
            COM_AXIS    /* Attribute */
            NO_INPUT_QUANTITY   /* InputQuantity */
            rVcAesSupM_1_0_0_0_rpm  /* Conversion */
            6  /* MaxAxisPoints */
            0  /* LowerLimit */
            10000   /* UpperLimit */
            AXIS_PTS_REF tVcAesSupM_tc_SupMonrSCTarDly_x
            DEPOSIT ABSOLUTE
        /end AXIS_DESCR'''
        self.assertEqual(result, expected)

    def test_gen_a2l_compu_metod_blk(self):
        """Test generation of a2l COMPU_METHOD block."""
        key = (1.0, 0.0, 'kPa')
        result = self.a2l._gen_a2l_compu_metod_blk(key)
        expected = '''
    /begin COMPU_METHOD
        rVcAesSupM_1_0_0_0_kPa   /* Name */
        ""    /* LongIdentifier */
        RAT_FUNC    /* ConversionType */
        "%11.3"   /* Format */
        "kPa" /* Unit */
        COEFFS 0 1 0.0 0 0 1.0
    /end COMPU_METHOD
'''
        self.assertEqual(result, expected)

    def test_gen_a2l_axis_pts_blk(self):
        """Test generation of a2l AXIS_PTS block."""
        var = 'tVcAesSupM_tc_SupMonrSCTarDly_x'
        data = A2L_DATA['vars'][var]
        result = self.a2l._gen_a2l_axis_pts_blk(var, data)
        expected = ('\n'
                    '    /begin AXIS_PTS\n'
                    '        tVcAesSupM_tc_SupMonrSCTarDly_x   /* Name */\n'
                    '        "Supercharger boost pressure monitor target pressure lowpass filter time constant engine'
                    ' speed support points"   /* LongIdentifier */\n'
                    '        0x00000000\n'
                    '        NO_INPUT_QUANTITY   /* InputQuantity */\n'
                    '        FLOAT32_IEEE_X_INCR_DIRECT  /* Deposit */\n'
                    '        0   /* MaxDiff */\n'
                    '        rVcAesSupM_1_0_0_0_rpm  /* Conversion */\n'
                    '        6  /* MaxAxisPoints */\n'
                    '        0   /* LowerLimit */\n'
                    '        10000   /* UpperLimit */\n'
                    '        DEPOSIT ABSOLUTE\n'
                    '    /end AXIS_PTS\n')
        self.assertEqual(result, expected)

    def test_gen_a2l_rec_layout_blk(self):
        """Test generation of a2l AXIS_PTS block."""
        key = 'FLOAT32_IEEE_COL_DIRECT'
        result = self.a2l._gen_a2l_rec_layout_blk(key)
        expected = '''
    /begin RECORD_LAYOUT
        FLOAT32_IEEE_COL_DIRECT /* Name */
        FNC_VALUES 1 FLOAT32_IEEE COLUMN_DIR DIRECT
    /end RECORD_LAYOUT
'''
        self.assertEqual(result, expected)

    def test_gen_a2l_function_blk(self):
        """Test generation of a2l FUNCTION block."""
        result = self.a2l._gen_a2l_function_blk()
        expected = '''
    /begin FUNCTION
        rVcAesSupM /* Name */
        ""  /* LongIdentifier */
        /begin DEF_CHARACTERISTIC
            cVcAesSupM_B_SupMonrHiBypFiMPerm /* Identifier */
            tVcAesSupM_tc_SupMonrSCTarDly /* Identifier */
            tVcAesSupM_tc_SupMonrSCTarDly_x /* Identifier */
            mVcAesSupM_m_SupChrgrStuckMaxLoadLim_y /* Identifier */
            mVcAesSupM_m_SupChrgrStuckMaxLoadLim_x /* Identifier */
            mVcAesSupM_m_SupChrgrStuckMaxLoadLim /* Identifier */
        /end DEF_CHARACTERISTIC
        /begin LOC_MEASUREMENT
            rVcAesSupM_p_SupMonrSCTarDly /* Identifier */
        /end LOC_MEASUREMENT
    /end FUNCTION
'''
        self.assertEqual(result, expected)
