# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test script for pybuild.zone_controller.calibration."""

from unittest import TestCase
from unittest.mock import MagicMock
from pybuild.zone_controller.calibration import ZoneControllerCalibration


class TestZoneControllerCalibration(TestCase):
    """Test case for testing composition_yaml."""

    maxDiff = None

    def setUp(self):
        """Set-up common data structures for all tests in the test case."""
        build_cfg = MagicMock()
        build_cfg.name = "XVC"
        build_cfg.get_src_code_dst_dir.return_value = None
        build_cfg.get_swc_name.return_value = "testName_SC"
        dummy_calib_data = {
            "class_info": {
                "dummy_signal_one": {
                    "type": "Float32",
                    "width": 1
                },
                "dummy_signal_two": {
                    "type": "UInt8",
                    "width": 1
                },
                "dummy_signal_three": {
                    "type": "UInt8",
                    "width": [1, 2]
                },
                "dummy_signal_four": {
                    "type": "UInt8",
                    "width": [2, 2]
                }
            },
            "data_types": {}
        }
        self.zone_controller_calibation = ZoneControllerCalibration(build_cfg, dummy_calib_data)

    def test_get_header_file_content(self):
        """Test ZoneControllerCalibration.get_header_file_content."""
        result = self.zone_controller_calibation.get_header_file_content()
        expected = [
            "#ifndef CALIBRATION_INTERFACE_H\n",
            "#define CALIBRATION_INTERFACE_H\n",
            "#define CVC_CAL\n",
            '#include <string.h>\n',
            '#include "tl_basetypes.h"\n',
            '#include "Rte_testName_SC.h"\n',
            "\n",
            "#define testName_SC_START_SEC_VCC_CAL\n",
            '#include "testName_SC_MemMap.h"\n',
            "extern CVC_CAL Float32 dummy_signal_one;\n",
            "extern CVC_CAL UInt8 dummy_signal_two;\n",
            "extern CVC_CAL UInt8 dummy_signal_three[2];\n",
            "extern CVC_CAL UInt8 dummy_signal_four[2][2];\n",
            "extern CVC_CAL Float32 ctestName_SC_TriggerReadRteCData;\n",
            "#define testName_SC_STOP_SEC_VCC_CAL\n",
            '#include "testName_SC_MemMap.h"\n',
            "\n",
            "extern Float32 Rte_CData_testName_SC_dummy_signal_one(void);\n",
            "extern UInt8 Rte_CData_testName_SC_dummy_signal_two(void);\n",
            "extern const UInt8* Rte_CData_testName_SC_dummy_signal_three(void);\n",
            "extern const UInt8* Rte_CData_testName_SC_dummy_signal_four(void);\n",
            "extern Float32 Rte_CData_testName_SC_ctestName_SC_TriggerReadRteCData(void);\n",
            "\n",
            "void testName_SC_ZcCalibrationStep(void);\n",
            "\n",
            "#endif /* CALIBRATION_INTERFACE_H */\n"
        ]
        self.assertListEqual(result, expected)

    def test_get_source_file_content(self):
        """Test ZoneControllerCalibration.get_source_file_content."""
        result = self.zone_controller_calibation.get_source_file_content()
        expected = [
            '#include "calibration_interface.h"\n',
            "\n",
            "#define testName_SC_START_SEC_VCC_CAL\n",
            '#include "testName_SC_MemMap.h"\n',
            "CVC_CAL Float32 ctestName_SC_TriggerReadRteCData = 0;\n",
            "#define testName_SC_STOP_SEC_VCC_CAL\n",
            '#include "testName_SC_MemMap.h"\n',
            "\n",
            "#define testName_SC_START_SEC_CODE\n",
            '#include "testName_SC_MemMap.h"\n',
            "void testName_SC_ZcCalibrationStep(void)\n{\n",
            "    if (ctestName_SC_TriggerReadRteCData != Rte_CData_testName_SC_ctestName_SC_TriggerReadRteCData())\n",
            "    {\n",
            "        dummy_signal_one = Rte_CData_testName_SC_dummy_signal_one();\n",
            "        dummy_signal_two = Rte_CData_testName_SC_dummy_signal_two();\n",
            "        memcpy(Rte_CData_testName_SC_dummy_signal_three(), &dummy_signal_three, sizeof(UInt8));\n",
            "        memcpy(Rte_CData_testName_SC_dummy_signal_four(), &dummy_signal_four, sizeof(UInt8));\n",
            "        ctestName_SC_TriggerReadRteCData = Rte_CData_testName_SC_ctestName_SC_TriggerReadRteCData();\n",
            "    }\n",
            "}\n",
            "#define testName_SC_STOP_SEC_CODE\n",
            '#include "testName_SC_MemMap.h"\n'
        ]
        self.assertListEqual(result, expected)
