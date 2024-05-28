# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for the html report generated from the signal consistency check."""
import os
import os.path
import unittest
from pathlib import Path
from pybuild.signal_incons_html_rep_all import SigConsHtmlReportAll

INDATA = {
    "CFG1": {
        "sigs": {
            "ext": {
                "missing": {
                    "sVcAcCtrl_D_ElacDiagcFb": ["GEP3_BEV"]
                },
                "unused": {},
                "inconsistent_defs": {
                    "MDL1": {
                        "sVcAc_D_AirCondCmpsrStats": {"max": "15 != 7"}
                    },
                    "MDL2": {
                        "sVcAc_D_AirCondCmpsrStats": {"max": "15 != 7"}
                    }
                }
            },
            "int": {
                "MDL2": {
                    "missing": {
                        "sVcBec_Pw_HvBattClimaPwr": ["VED4_GENIII"]
                    },
                    "unused": {
                        "sVcAcCtrl_D_ElacDiagcFb": ["VED4_GENIII"]
                    },
                    "multiple_defs": {
                        "yVcAesEch_B_EChrgrActv": ["VEP4_GENIII"]
                    },
                    "inconsistent_defs": {
                        "sVcAcOvr_p_AirCondHiSide_bar": {
                            "max": "100 != 5000",
                            "unit": "bar != kPa"
                        }
                    }
                }
            }
        },
        "never_active_signals": {
            "MDL2": ["sVcNeverActiveOne_B_SomethingFalse", "sVcNeverActiveTwo_B_SomethingFalse"]
        }
    }
}

REPORT_UNIT_TOC = None

REPORT_EXT_TOC = '''  <p><a href="#ext_missing"> Missing external signals</a></p>
  <p><a href="#ext_unused"> Unused external signals</a></p>
'''

REPORT_MISSING = '''
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
        <td>  VED4_GENIII</td>
      </tr>
    </tbody>
  </table>
'''

REPORT_UNUSED = '''
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
        <td>  VED4_GENIII</td>
      </tr>
    </tbody>
  </table>
'''

REPORT_NEVER_ACTIVE = '''
  <table id="unused">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Configurations</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>sVcNeverActiveOne_B_SomethingFalse</td>
        <td></td>
      </tr>
  <tr>
        <td>sVcNeverActiveTwo_B_SomethingFalse</td>
        <td></td>
      </tr>
    </tbody>
  </table>
'''

REPORT_MULTI = '''
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
        <td>  VEP4_GENIII</td>
      </tr>
    </tbody>
  </table>
'''

REPORT_INT_INCONS = """  <table id="inconsistent">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Variable parameter</th>
        <th>Difference</th>
        <th>Configurations</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>sVcAcOvr_p_AirCondHiSide_bar</td>
        <td>max</td>
        <td>100 != 5000</td>
        <td>  CFG1</td>
      </tr>
      <tr>
      <td></td>
        <td>unit</td>
        <td>bar != kPa</td>
        <td>  CFG1</td>
      </tr>
    </tbody>
  </table>
"""

REPORT_EXT_INCONS = """  <table id="inconsistent">
    <thead>
      <tr>
        <th>Variable</th>
        <th>Variable parameter</th>
        <th>Difference</th>
        <th>Configurations</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>sVcAc_D_AirCondCmpsrStats</td>
        <td>max</td>
        <td>15 != 7</td>
        <td>CFG1</td>
      </tr>
    </tbody>
  </table>
"""
REPORT_EXT_UNIT = ('''  <h3 id="MDL1">MDL1</h3>\n''' +
                   '''  <h4>External signal inconsistencies</h4>\n''' +
                   '''  <p>In-/Out-ports that have different variable definitions ''' +
                   '''than in the interface definition file.</p>''' +
                   REPORT_EXT_INCONS)

REPORT_UNIT = ('  <h3 id="MDL2">MDL2</h3>\n' +
               '  <h4>Missing signals</h4>\n' +
               '  <p>Inports whose signals are not generated in the listed configuration(s).</p>' +
               REPORT_MISSING +
               '  <h4>Unused signals</h4>\n' +
               '  <p>Outports that are generated, but not used in the listed configuration(s).</p>' +
               REPORT_UNUSED +
               '  <h4>Multiple defined signals</h4>\n' +
               '  <p>Outports that are generated more than once in the listed configuration(s).</p>' +
               REPORT_MULTI +
               '  <h4>Internal signal inconsistencies</h4>\n' +
               '  <p>Inports that have different variable definitions than the producing outport.</p>' +
               REPORT_INT_INCONS +
               '  <h4>External signal inconsistencies</h4>\n'
               '  <p>In-/Out-ports that have different variable definitions'
               ' than in the interface definition file.</p>' +
               REPORT_EXT_INCONS +
               '  <h4>Never active signals</h4>\n'
               '  <p>Never active signals will not appear in generated .c file, '
               'signals probablty lead to terminators in Simulink model.</p>' +
               REPORT_NEVER_ACTIVE)

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
        <td>  GEP3_BEV</td>
      </tr>
    </tbody>
  </table>
'''

REPORT_END = '''</body>
</html>
'''


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


class TestSigConsHtmlReportAll(unittest.TestCase):
    """Test case for the html report generated from the signal consistency check."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.maxDiff = None
        self.sig_cons = SigConsHtmlReportAll(INDATA)

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
        result_int = self.sig_cons._gen_units()
        results = ''
        for prj, result in result_int.items():
            results += result
        self.assertEqual(results, REPORT_UNITS)

    def test_set_to_str(self):
        """Test conversion of a set to a sorted string."""
        set_ = set()
        result = self.sig_cons._set_to_str(set_)
        self.assertEqual(result, '')
        set_ = {"1", "2", "3"}
        result = self.sig_cons._set_to_str(set_)
        self.assertEqual(result, '1, 2, 3')

    def test_gen_unit1(self):
        """Test generation of report for the unit specific information."""
        self.sig_cons._prj = 'CFG1'
        result = self.sig_cons._gen_unit('CFG1', 'MDL1')
        self.assertEqual(result, REPORT_EXT_UNIT)

    def test_gen_unit2(self):
        """Test generation of report for the unit specific information."""
        self.sig_cons._prj = 'CFG1'
        result = self.sig_cons._gen_unit('CFG1', 'MDL2')
        self.assertEqual(result, REPORT_UNIT)

    def test_gen_missing_sigs(self):
        """Test generation of unit specific information for missing signal."""
        unit_data = INDATA['CFG1']['sigs']['int']['MDL2']
        self.sig_cons._unit_data_all = {}
        self.sig_cons._unit_data_all.update({'CFG1': unit_data})
        result = self.sig_cons._gen_missing_sigs(unit_data, self.sig_cons._unit_data_all)
        self.assertEqual(result, REPORT_MISSING)

    def test_gen_unused_sigs(self):
        """Test generation of unit specific information for unused signals."""
        unit_data = INDATA['CFG1']['sigs']['int']['MDL2']
        self.sig_cons._unit_data_all = {}
        self.sig_cons._unit_data_all.update({'CFG1': unit_data})
        result = self.sig_cons._gen_unused_sigs(unit_data, self.sig_cons._unit_data_all)
        self.assertEqual(result, REPORT_UNUSED)

    def test_gen_multiple_def_sigs(self):
        """Test generation of unit specific information for signals generated more than once."""
        unit_data = INDATA['CFG1']['sigs']['int']['MDL2']
        self.sig_cons._unit_data_all = {}
        self.sig_cons._unit_data_all.update({'CFG1': unit_data})
        result = self.sig_cons._gen_multiple_def_sigs(unit_data, self.sig_cons._unit_data_all)
        self.assertEqual(result, REPORT_MULTI)

    def test_gen_ext_inconsistent_defs(self):
        """Test generation of report of inconsistent variable definition parameters."""
        result = self.sig_cons._gen_ext_inconsistent_defs('CFG1', 'MDL1')
        self.assertEqual(result, REPORT_EXT_INCONS)

    def test_gen_int_inconsistent_defs(self):
        """Test generation of report of inconsistent variable definition parameters."""
        unit_data = INDATA['CFG1']['sigs']['int']['MDL2']
        self.sig_cons._unit_data_all = {}
        self.sig_cons._unit_data_all.update({'CFG1': unit_data})
        result = self.sig_cons._gen_int_inconsistent_defs(unit_data, self.sig_cons._unit_data_all)
        self.assertEqual(result, REPORT_INT_INCONS)

    def test_gen_ext_signals_report(self):
        """Test generation of report for external signals."""
        self.sig_cons._prj = "CFG1"
        result = self.sig_cons._gen_ext_signals_report('missing', 'comment')
        self.assertEqual(result, REPORT_EXT_SIGNALS)

    def test_gen_html_end(self):
        """Test generation of end of the body and html document."""
        result = self.sig_cons._gen_end()
        self.assertEqual(result, REPORT_END)

    def test_generate_html_file(self):
        """Test that write to file generates output."""
        filename = str(Path(Path(__file__).parent, 'output', 'SigCheck.html'))
        remove(filename)
        self.sig_cons.generate_report_file(filename)
        exists(filename)

    def test_generate_html_file_empty(self):
        """Test that write to file with minimal indata generates output."""
        filename = str(Path(Path(__file__).parent, 'output', 'SigCheck.html'))
        remove(filename)
        sig_cons = SigConsHtmlReportAll({'sigs': {'ext': {}, 'int': {}}})
        sig_cons.generate_report_file(filename)
        exists(filename)
