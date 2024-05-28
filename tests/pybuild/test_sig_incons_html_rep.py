# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for the html report generated from the signal consistency check."""

import os
import os.path
import unittest
from pathlib import Path
from pybuild.signal_incons_html_rep import SigConsHtmlReport

INDATA = {
    "sigs": {
        "ext": {
            "missing": {
                "sVcAcCtrl_D_ElacDiagcFb": {"GEP3_BEV"}
            },
            "unused": {},
            "inconsistent_defs": {
                "EXT_UNIT_NAME": {
                    "sVcAc_D_AirCondCmpsrStats": {"max": "15 != 7"}
                }
            }
        },
        "int": {
            "INT_UNIT_NAME": {
                "missing": {
                    "sVcBec_Pw_HvBattClimaPwr": {"VED4_GENIII"}
                },
                "unused": {
                    "sVcAcCtrl_D_ElacDiagcFb": {"VED4_GENIII"}
                },
                "multiple_defs": {
                    "yVcAesEch_B_EChrgrActv": {"VEP4_GENIII"}
                },
                "inconsistent_defs": {
                    "sVcAcOvr_p_AirCondHiSide_bar": {
                        "max": "100 != 5000",
                        "unit": "bar != kPa"
                    }
                }
            }
        }
    }
}

REPORT_UNIT_TOC = '''  <h2 id="unit_index">Unit index</h2>
  <div><a href="#EXT_UNIT_NAME">EXT_UNIT_NAME</a></div>
  <div><a href="#INT_UNIT_NAME">INT_UNIT_NAME</a></div>
'''

REPORT_EXT_TOC = '''  <p><a href="#ext_missing"> Missing external signals</a></p>
  <p><a href="#ext_unused"> Unused external signals</a></p>
'''

REPORT_MISSING = '''  <h4>Missing signals</h4>
  <p>Inports whose signals are not generated in the listed configuration(s).</p>
  <table id="unused">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Configurations</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>sVcBec_Pw_HvBattClimaPwr</td>
        <td>VED4_GENIII</td>
      </tr>
    </tbody>
  </table>
'''

REPORT_UNUSED = '''  <h4>Unused signals</h4>
  <p>Outports that are generated, but not used in the listed configuration(s).</p>
  <table id="unused">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Configurations</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>sVcAcCtrl_D_ElacDiagcFb</td>
        <td>VED4_GENIII</td>
      </tr>
    </tbody>
  </table>
'''

REPORT_MULTI = '''  <h4>Multiple defined signals</h4>
  <p>Outports that are generated more than once in the listed configuration(s).</p>
  <table id="unused">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Configurations</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>yVcAesEch_B_EChrgrActv</td>
        <td>VEP4_GENIII</td>
      </tr>
    </tbody>
  </table>
'''

REPORT_INT_INCONS = '''  <h4>Internal signal inconsistencies</h4>
  <p>Inports that have different variable definitions than the producing outport.</p>
  <table id="inconsistent">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Variable parameter</th>
        <th>Difference</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>sVcAcOvr_p_AirCondHiSide_bar</td>
        <td>max</td>
        <td>100 != 5000</td>
      </tr>
      <tr>
      <td></td>
        <td>unit</td>
        <td>bar != kPa</td>
      </tr>
    </tbody>
  </table>
'''

REPORT_EXT_INCONS = '''  <h4>External signal inconsistencies</h4>
  <p>In-/Out-ports that have different variable definitions than in the interface definition file.</p>
  <table id="inconsistent">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Variable parameter</th>
        <th>Difference</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>sVcAc_D_AirCondCmpsrStats</td>
        <td>max</td>
        <td>15 != 7</td>
      </tr>
    </tbody>
  </table>
'''

REPORT_UNIT = ('''  <h3 id="INT_UNIT_NAME">INT_UNIT_NAME</h3>\n''' +
               REPORT_MISSING +
               REPORT_UNUSED +
               REPORT_MULTI +
               REPORT_INT_INCONS)

REPORT_EXT_UNIT = ('''  <h3 id="EXT_UNIT_NAME">EXT_UNIT_NAME</h3>\n''' +
                   REPORT_EXT_INCONS)

REPORT_UNITS = ('''  <h2 id="unit_details">Detailed Unit Information</h2>\n''' +
                REPORT_EXT_UNIT +
                REPORT_UNIT)

REPORT_EXT_SIGNALS = '''  <h3 id="ext_missing">Missing external signals</h3>
<p>comment</p>
  <table id="unused">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Configurations</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>sVcAcCtrl_D_ElacDiagcFb</td>
        <td>GEP3_BEV</td>
      </tr>
    </tbody>
  </table>
'''

REPORT_END = '''</body>
</html>
'''

OUTPUT_DIR = Path(Path(__file__).parent, 'output')


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
            raise AssertionError('File {} does not exist.'.format(file_))
    return True


class TestSigConsHtmlReport(unittest.TestCase):
    """Test case for the html report generated from the signal consistency check."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.maxDiff = None
        self.sig_cons = SigConsHtmlReport(INDATA)

    def test_gen_header(self):
        """Test generation of html header."""
        startstr = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
'''
        endstr = '''
</head>
<body>
<h1>Signal consistency report</h1>
'''
        result = self.sig_cons._gen_header()
        self.assertTrue(result.startswith(startstr))
        self.assertTrue(result.endswith(endstr))

    def test_gen_unit_toc(self):
        """Test generation of a unit TOC."""
        result = self.sig_cons._gen_unit_toc()
        self.assertEqual(result, REPORT_UNIT_TOC)

    def test_gen_units(self):
        """Test generation of the information regarding all the units."""
        result = self.sig_cons._gen_units()
        self.assertEqual(result, REPORT_UNITS)

    def test_set_to_str(self):
        """Test conversion of a set to a sorted string."""
        set_ = set()
        result = self.sig_cons._set_to_str(set_)
        self.assertEqual(result, '')
        set_ = {"1", "2", "3"}
        result = self.sig_cons._set_to_str(set_)
        self.assertEqual(result, '1, 2, 3')

    def test_gen_unit(self):
        """Test generation of report for the unit specific information."""
        result = self.sig_cons._gen_unit('EXT_UNIT_NAME')
        self.assertEqual(result, REPORT_EXT_UNIT)
        result = self.sig_cons._gen_unit('INT_UNIT_NAME')
        self.assertEqual(result, REPORT_UNIT)

    def test_gen_missing_sigs(self):
        """Test generation of unit specific information for missing signal."""
        unit_data = INDATA['sigs']['int']['INT_UNIT_NAME']
        result = self.sig_cons._gen_missing_sigs(unit_data)
        self.assertEqual(result, REPORT_MISSING)

    def test_gen_unused_sigs(self):
        """Test generation of unit specific information for unused signals."""
        unit_data = INDATA['sigs']['int']['INT_UNIT_NAME']
        result = self.sig_cons._gen_unused_sigs(unit_data)
        self.assertEqual(result, REPORT_UNUSED)

    def test_gen_multiple_def_sigs(self):
        """Test generation of unit specific information for signals generated more than once."""
        unit_data = INDATA['sigs']['int']['INT_UNIT_NAME']
        result = self.sig_cons._gen_multiple_def_sigs(unit_data)
        self.assertEqual(result, REPORT_MULTI)

    def test_gen_ext_inconsistent_defs(self):
        """Test generation of report of inconsistent variable definition parameters."""
        result = self.sig_cons._gen_ext_inconsistent_defs('EXT_UNIT_NAME')
        self.assertEqual(result, REPORT_EXT_INCONS)

    def test_gen_int_inconsistent_defs(self):
        """Test generation of report of inconsistent variable definition parameters."""
        unit_data = INDATA['sigs']['int']['INT_UNIT_NAME']
        result = self.sig_cons._gen_int_inconsistent_defs(unit_data)
        self.assertEqual(result, REPORT_INT_INCONS)

    def test_gen_ext_signals_report(self):
        """Test generation of report for external signals."""
        result = self.sig_cons._gen_ext_signals_report('missing', 'comment')
        self.assertEqual(result, REPORT_EXT_SIGNALS)

    def test_gen_html_end(self):
        """Test generation of end of the body and html document."""
        result = self.sig_cons._gen_end()
        self.assertEqual(result, REPORT_END)

    def test_generate_html_file(self):
        """Test that write to file generates output."""
        filename = str(Path(OUTPUT_DIR, 'SigCheck.html'))
        remove(filename)
        self.sig_cons.generate_report_file(filename)
        exists(filename)

    def test_generate_html_file_empty(self):
        """Test that write to file with minimal indata generates output."""
        filename = str(Path(OUTPUT_DIR, 'SigCheck.html'))
        remove(filename)
        sig_cons = SigConsHtmlReport({'sigs': {'ext': {}, 'int': {}}})
        sig_cons.generate_report_file(filename)
        exists(filename)
