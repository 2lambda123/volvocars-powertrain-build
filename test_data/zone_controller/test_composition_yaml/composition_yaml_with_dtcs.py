# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test data for powertrain_build.zone_controller.composition_yaml with DTCs."""

from test_data.zone_controller.test_composition_yaml import composition_yaml_setup

diagnostics = {
    "events": {
        "DTC1": {
            "operations": ["SetEventStatus", "SomethingElse"],
            "runnable": ["dummy"],
            "identifier": "34EA",
            "ThresholdUnconfirmed": 1,
            "StepDown": 0,
            "JumpDown": True,
            "JumpDownInit": 1,
            "StepUp": 1,
            "JumpUp": True,
            "JumpUpInit": 127,
            "TestFailedLimit": 0,
            "TestPassedLimit": 0,
            "AgedDTCLimit": 0,
            "ConfirmedDTCLimit": 1,
            "DTCEventPriority": 1,
            "OperationCycle":  "Battery",
        },
    },
}

expected_result = {
    "SoftwareComponents": {
        "testName_SC": {
            "type": "SWC",
            "template": "ARTCSC",
            "runnables": {
                "AR_prefix_VcExtINI": {
                    "type": "INIT",
                    "accesses": composition_yaml_setup.base_accesses
                },
                "AR_prefix_testRunnable": {
                    "period": 10,
                    "type": "PERIODIC",
                    "accesses": composition_yaml_setup.base_accesses,
                }
            },
            "diagnostics": {
                "events": {
                    "DTC1": {
                        "operations": ["SetEventStatus"],
                        "runnable": ["dummy"],
                        "identifier": "34EA",
                        "ThresholdUnconfirmed": 1,
                        "StepDown": 0,
                        "JumpDown": True,
                        "JumpDownInit": 1,
                        "StepUp": 1,
                        "JumpUp": True,
                        "JumpUpInit": 127,
                        "TestFailedLimit": 0,
                        "TestPassedLimit": 0,
                        "AgedDTCLimit": 0,
                        "ConfirmedDTCLimit": 1,
                        "DTCEventPriority": 1,
                        "OperationCycle":  "Battery",
                    },
                },
            },
            "static": composition_yaml_setup.base_static,
            "shared":  composition_yaml_setup.base_shared,
            "ports": {
                "GlobSignNme": {"direction": "IN", "interface": "PIGlobSignNme"},
            }
        }
    },
    "DataTypes": composition_yaml_setup.base_data_types,
    "PortInterfaces": composition_yaml_setup.base_port_interfaces,
    "ExternalFiles": composition_yaml_setup.base_configuration
}
