# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for SigIfHtmlReport class."""
from copy import deepcopy
import unittest
from unittest.mock import MagicMock
from pathlib import Path
from pybuild.build_proj_config import BuildProjConfig
from pybuild.unit_configs import UnitConfigs
from pybuild.signal_interfaces import CsvSignalInterfaces
from pybuild.signal_if_html_rep import SigIfHtmlReport

UNIT_CFG = {
    'VcAesSupM__gen3': {
        'calib_consts': {
            'cVcAesSupM_B_SupMonrHiBypFiMPerm': {
                'class': 'CVC_CAL',
                'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                'description': 'Switch to bypass FiM permission  '
                               'supercharger high boost monitor',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                          '1_SupMonr/11_SupChrgrSys/112_EnaCond/B_SupMonrHiBypFiMPerm',
                'lsb': '1',
                'max': ' ',
                'min': ' ',
                'offset': '0',
                'width': 1,
                'type': 'Bool',
                'unit': ''}
            },
        'core': {
            'Events': {
                'VcEvSupChrPMdlPlausHi': {
                    'API_blk': [
                        {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                         'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                 '1_SupMonr/11_SupChrgrSys/114_InformationStorage/'
                                 '141_CoreHiBoost/Dem_SetEventStatusPF1'},
                        {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                         'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                 '1_SupMonr/11_SupChrgrSys/114_InformationStorage/'
                                 '141_CoreHiBoost/Dem_SetEventStatusPP1'}],
                    'API_blk_type': 'Dem_SetEventStatus Pre-Passed',
                    'blk_name': 'NamedConstant2',
                    'class': '-',
                    'description': '-',
                    'lsb': '-',
                    'max': '-',
                    'min': '-',
                    'offset': '-',
                    'subsystem': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                                 '1_SupMonr/11_SupChrgrSys/114_InformationStorage/141_CoreHiBoost',
                    'type': '-',
                    'unit': '-'}},
            'FIDs': {
                'VcFiSupChrPMdlPlausHi': {
                    'API_blk': [
                        {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                         'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM'
                                 '/VcAesSupM/1_SupMonr/11_SupChrgrSys/112_EnaCond/'
                                 'FiM_GetFunctionPermission'}],
                    'API_blk_type': 'FiM_GetFunctionPermission',
                    'blk_name': 'NamedConstant2',
                    'class': '-',
                    'description': '-',
                    'lsb': '-',
                    'max': '-',
                    'min': '-',
                    'offset': '-',
                    'subsystem': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                 'VcAesSupM/1_SupMonr/11_SupChrgrSys/112_EnaCond',
                    'type': '-',
                    'unit': '-'}},
            'IUMPR': {},
            'Ranking': {
                'VcRvSupChrPMdlPlausHi': {
                    'API_blk': [
                        {'config': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                         'path': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                 'VcAesSupM/1_SupMonr/11_SupChrgrSys/'
                                 '114_InformationStorage/141_CoreHiBoost/Vc_SetRanking'}],
                    'API_blk_type': 'Vcc_SetRanking',
                    'blk_name': 'NamedConstant1',
                    'class': '-',
                    'description': '-',
                    'lsb': '-',
                    'max': '-',
                    'min': '-',
                    'offset': '-',
                    'subsystem': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                                 'VcAesSupM/1_SupMonr/11_SupChrgrSys/'
                                 '114_InformationStorage/141_CoreHiBoost',
                    'type': '-',
                    'unit': '-'}},
            'TstId': {}
        },
        'dids': {},
        'inports': {
            'sVcEc_p_Amb': {
                'class': 'CVC_EXT',
                'configs': [['Vc_Aes_SupM_B_CodeGenSprChrg']],
                'description': 'Ambient pressure sensor',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/tlop_VcXx_insignal3',
                'lsb': 1,
                'max': 200,
                'min': 0,
                'name': 'sVcEc_p_Amb',
                'offset': 0,
                'type': 'Float32',
                'unit': 'kPa'},
            'yVcEc_B_ObdExe': {
                'class': 'CVC_EXT',
                'configs': [['Vc_Aes_SupM_B_CodeGenSprChrg']],
                'description': 'OBD execution flag',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                          'tlop_VcXx_insignal1',
                'lsb': 1,
                'max': '-',
                'min': '-',
                'name': 'yVcEc_B_ObdExe',
                'offset': 0,
                'type': 'Bool',
                'unit': '-'}},
        'local_vars': {
            'rVcAesSupM_p_SupChrgrPDsAtmDiff': {
                'class': 'CVC_DISP',
                'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                'description': 'Over pressure downstream supercharger',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                          '2_EngProtn/21_SupChrgrPPeak/211_PPeakTest/Sum5',
                'lsb': '1',
                'max': ' ',
                'min': ' ',
                'offset': '0',
                'width': 1,
                'type': 'Float32',
                'unit': 'kPa'},
            'rVcAesSupM_p_SupMonrPDif': {
                'class': 'CVC_DISP',
                'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                'description': 'Supercharger actual  and target pressure difference',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                          '1_SupMonr/11_SupChrgrSys/111_SignalCalc/Sum5',
                'lsb': '1',
                'max': '300',
                'min': ' 300',
                'offset': '0',
                'width': 1,
                'type': 'Float32',
                'unit': 'kPa'},
            'rVcAesSupM_p_SupMonrSCTarDly': {
                'class': 'CVC_DISP',
                'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                'description': 'Low pass filtered supercharger target pressure',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                          '1_SupMonr/11_SupChrgrSys/111_SignalCalc/FirstOrderFilter/Sum2',
                'lsb': '1',
                'max': '300',
                'min': '0',
                'offset': '0',
                'width': 1,
                'type': 'Float32',
                'unit': 'kPa'}},
        'nvm': {},
        'outports': {
            'yVcAesSupM_B_SupChrgrErr': {
                'class': 'CVC_DISP',
                'configs': ['all'],
                'description': 'Supercharger Peak Pressure engine protection activation flag',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/'
                          'tlop_VcAesAct_posn_EgrTar1',
                'lsb': 1,
                'max': '-',
                'min': '-',
                'name': 'yVcAesSupM_B_SupChrgrErr',
                'offset': 0,
                'type': 'Bool',
                'unit': '%'}},
        'pre_procs': ['Vc_Aes_SupM_B_CodeGenSprChrg']
    }
}

PER_CFG_UNIT_CFG = {
    'calib_consts': {
        'cVcAesSupM_B_SupMonrHiBypFiMPerm': {
            'VcAesSupM__gen3': {
                'class': 'CVC_CAL',
                'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                'description': 'Switch to bypass FiM permission  supercharger '
                               'high boost monitor',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                          '1_SupMonr/11_SupChrgrSys/112_EnaCond/B_SupMonrHiBypFiMPerm',
                'lsb': '1',
                'max': ' ',
                'min': ' ',
                'offset': '0',
                'width': 1,
                'type': 'Bool',
                'unit': ''}}},
    'inports': {
        'sVcEc_p_Amb': {
            'VcAesSupM__gen3': {
                'class': 'CVC_EXT',
                'configs': [['Vc_Aes_SupM_B_CodeGenSprChrg']],
                'description': 'Ambient pressure sensor',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/tlop_VcXx_insignal3',
                'lsb': 1,
                'max': 200,
                'min': 0,
                'name': 'sVcEc_p_Amb',
                'offset': 0,
                'type': 'Float32',
                'unit': 'kPa'}},
        'yVcEc_B_ObdExe': {
            'VcAesSupM__gen3': {
                'class': 'CVC_EXT',
                'configs': [['Vc_Aes_SupM_B_CodeGenSprChrg']],
                'description': 'OBD execution flag',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/tlop_VcXx_insignal1',
                'lsb': 1,
                'max': '-',
                'min': '-',
                'name': 'yVcEc_B_ObdExe',
                'offset': 0,
                'type': 'Bool',
                'unit': '-'}}},
    'local_vars': {
        'rVcAesSupM_p_SupChrgrPDsAtmDiff': {
            'VcAesSupM__gen3': {
                'class': 'CVC_DISP',
                'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                'description': 'Over pressure downstream supercharger',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                          '2_EngProtn/21_SupChrgrPPeak/211_PPeakTest/Sum5',
                'lsb': '1',
                'max': ' ',
                'min': ' ',
                'offset': '0',
                'width': 1,
                'type': 'Float32',
                'unit': 'kPa'}},
        'rVcAesSupM_p_SupMonrPDif': {
            'VcAesSupM__gen3': {
                'class': 'CVC_DISP',
                'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                'description': 'Supercharger actual  and target pressure difference',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                          '1_SupMonr/11_SupChrgrSys/111_SignalCalc/Sum5',
                'lsb': '1',
                'max': '300',
                'min': ' 300',
                'offset': '0',
                'width': 1,
                'type': 'Float32',
                'unit': 'kPa'}},
        'rVcAesSupM_p_SupMonrSCTarDly': {
            'VcAesSupM__gen3': {
                'class': 'CVC_DISP',
                'configs': ['Vc_Aes_SupM_B_CodeGenSprChrg'],
                'description': 'Low pass filtered supercharger target pressure',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/VcAesSupM/'
                          '1_SupMonr/11_SupChrgrSys/111_SignalCalc/FirstOrderFilter/Sum2',
                'lsb': '1',
                'max': '300',
                'min': '0',
                'offset': '0',
                'width': 1,
                'type': 'Float32',
                'unit': 'kPa'}}},
    'outports': {
        'yVcAesSupM_B_SupChrgrErr': {
            'VcAesSupM__gen3': {
                'class': 'CVC_DISP',
                'configs': ['all'],
                'description': 'Supercharger Peak Pressure engine protection activation flag',
                'handle': 'VcAesSupM__gen3/VcAesSupM/Subsystem/VcAesSupM/tlop_VcAesAct_posn_EgrTar1',
                'lsb': 1,
                'max': '-',
                'min': '-',
                'name': 'yVcAesSupM_B_SupChrgrErr',
                'offset': 0,
                'type': 'Bool',
                'unit': '%'
            }
        }
    }
}
SRC_DIR = Path(__file__).parent


class TestSigIfHtmlReport(unittest.TestCase):
    """Test case for testing the SigIfHtmlReport class."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        prj_cnf_dir = str(Path(SRC_DIR, 'cnfg_files'))
        self.build_cfg.get_prj_cfg_dir = MagicMock(return_value=prj_cnf_dir)
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        self.unit_cfg = MagicMock(spec_set=UnitConfigs)
        self.unit_cfg.get_per_unit_cfg = MagicMock(return_value=UNIT_CFG)
        self.unit_cfg.get_per_cfg_unit_cfg = MagicMock(return_value=PER_CFG_UNIT_CFG)
        self.sig_if = MagicMock(spec_set=CsvSignalInterfaces)
        self.sig_report = SigIfHtmlReport(self.build_cfg, self.unit_cfg, self.sig_if)

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
<h1>Signal interface report</h1>
'''
        result = self.sig_report._gen_header()
        self.assertTrue(result.startswith(startstr))
        self.assertTrue(result.endswith(endstr))

    def test_gen_signal_toc(self):
        """Check generated toc."""
        result = self.sig_report._gen_signal_toc()
        expected = '''  <h2 id="signal_index">Signal index</h2>
  <div><a href="#yVcAesSupM_B_SupChrgrErr">yVcAesSupM_B_SupChrgrErr</a></div>
'''
        self.assertEqual(result, expected)

    def test_gen_sigs_details(self):
        """Check generated contents."""
        result = self.sig_report._gen_sigs_details()
        expected = """  <h2 id="signal_details">Detailed Signal Information</h2>
  <h3 id="yVcAesSupM_B_SupChrgrErr">yVcAesSupM_B_SupChrgrErr</h3>
  <p>Supercharger Peak Pressure engine protection activation flag</p>
  <table id="sig_desc">
    <thead>
      <tr>
        <th>Unit</th>
        <th>Type</th>
        <th>Class</th>
        <th>Min</th>
        <th>Max</th>
        <th>Lsb</th>
        <th>Offset</th>
        <th>Configs</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>%</td>
        <td>Bool</td>
        <td>CVC_DISP</td>
        <td>-</td>
        <td>-</td>
        <td>1</td>
        <td>0</td>
        <td>['all']</td>
      </tr>
    </tbody>
  </table>
  <p></p>

  <table id="detailed_sig_def">
    <thead>
      <tr>
        <th>Defined in unit</th>
        <th>in projects</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>VcAesSupM__gen3</td>
        <td>['CFG1']</td>
      </tr>
    </tbody>
  </table>
"""
        self.assertEqual(result, expected)

    def test_gen_html_end(self):
        """Check generated document footer."""
        result = self.sig_report._gen_end()
        expected = "</body>\n</html>\n"
        self.assertEqual(result, expected)

    def test_generate_html_file(self):
        """Check generated document file."""
        report_dst = Path(SRC_DIR, 'output', 'SigIf.html')
        self.sig_report.generate_report_file(str(report_dst))
        with report_dst.open(encoding="utf-8") as fhandle:
            result = fhandle.read()
        with Path(SRC_DIR, 'reference_files', 'SigIf.html').open(encoding="utf-8") as fhandle:
            expected = fhandle.read()
        self.maxDiff = None
        self.assertEqual(result, expected)


class TestSigIfHtmlReportIncomplete(unittest.TestCase):
    """Test case for testing the SigIfHtmlReport class wit incomplete data."""

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        self.build_cfg = MagicMock(spec_set=BuildProjConfig)
        prj_cnf_dir = str(Path(SRC_DIR, 'cnfg_files'))
        self.build_cfg.get_prj_cfg_dir = MagicMock(return_value=prj_cnf_dir)
        self.build_cfg.get_prj_config = MagicMock(return_value='CFG1')
        self.unit_cfg = MagicMock(spec_set=UnitConfigs)
        tmp_unit_cfg = deepcopy(UNIT_CFG)
        del tmp_unit_cfg['VcAesSupM__gen3']['outports']['yVcAesSupM_B_SupChrgrErr']['min']
        self.unit_cfg.get_per_unit_cfg = MagicMock(return_value=tmp_unit_cfg)
        tmp_per_cfg = deepcopy(PER_CFG_UNIT_CFG)
        del tmp_per_cfg['outports']['yVcAesSupM_B_SupChrgrErr']['VcAesSupM__gen3']['min']
        self.unit_cfg.get_per_cfg_unit_cfg = MagicMock(return_value=tmp_per_cfg)
        self.sig_if = MagicMock(spec_set=CsvSignalInterfaces)
        self.sig_report = SigIfHtmlReport(self.build_cfg, self.unit_cfg, self.sig_if)

    def test_gen_sigs_details(self):
        """Check generated contents."""
        result = self.sig_report._gen_sigs_details()
        expected = """  <h2 id="signal_details">Detailed Signal Information</h2>
  <h3 id="yVcAesSupM_B_SupChrgrErr">yVcAesSupM_B_SupChrgrErr</h3>
  <p>Supercharger Peak Pressure engine protection activation flag</p>
  <table id="sig_desc">
    <thead>
      <tr>
        <th>Unit</th>
        <th>Type</th>
        <th>Class</th>
        <th>Min</th>
        <th>Max</th>
        <th>Lsb</th>
        <th>Offset</th>
        <th>Configs</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>%</td>
        <td>Bool</td>
        <td>CVC_DISP</td>
        <td>-</td>
        <td>-</td>
        <td>1</td>
        <td>0</td>
        <td>['all']</td>
      </tr>
    </tbody>
  </table>
  <p></p>

  <table id="detailed_sig_def">
    <thead>
      <tr>
        <th>Defined in unit</th>
        <th>in projects</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>VcAesSupM__gen3</td>
        <td>['CFG1']</td>
      </tr>
    </tbody>
  </table>
"""
        self.maxDiff = None
        self.assertEqual(result, expected)
