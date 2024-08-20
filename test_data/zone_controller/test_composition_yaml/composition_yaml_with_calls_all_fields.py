# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test data for powertrain_build.zone_controller.composition_yaml with calls using all fields."""

from test_data.zone_controller.test_composition_yaml import composition_yaml_setup

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
                    "calls": {
                        "CallOne": {
                            "operation": "OperationOne",
                            "timeout": 0.1,
                        }
                    }
                },
                "AR_testName_SC_ZcCalibrationStep": {
                    "period": 0.1,
                    "type": "PERIODIC",
                    "accesses": composition_yaml_setup.base_accesses
                }
            },
            "diagnostics": {"events": {}, "dids": {}},
            "static": composition_yaml_setup.base_static,
            "shared":  composition_yaml_setup.base_shared,
            "ports": {
                "GlobSignNme": {"direction": "IN", "interface": "PIGlobSignNme"},
                "CallOne": {"direction": "IN", "interface": "InterfaceOne"}
            }
        }
    },
    "DataTypes": composition_yaml_setup.base_data_types,
    "PortInterfaces": composition_yaml_setup.base_port_interfaces,
    "ExternalFiles": composition_yaml_setup.base_configuration
}
