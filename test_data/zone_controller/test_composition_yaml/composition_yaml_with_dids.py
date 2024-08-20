# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test data for powertrain_build.zone_controller.composition_yaml with DIDs."""

from test_data.zone_controller.test_composition_yaml import composition_yaml_setup

diagnostics = {
    "dids": {
        "DID1": {
            "identifier": "34EE",
            "numberOfParameters": 1,
            "totalNumberOfBytes": 2,
            "operations": {
                "ReadData": {
                    "securityAccess": "",
                    "readLocalVariables": ["MyIRV"],
                    "writtenLocalVariables": ["MyIRV"],
                },
                "WriteData": {
                    "securityAccess": "",
                    "readLocalVariables": ["MyIRV3"],
                    "writtenLocalVariables": ["MyIRV3"],
                },
                "ShortTermAdjustment": {
                    "securityAccess": "",
                    "readLocalVariables": ["MyIRV4"],
                    "writtenLocalVariables": ["MyIRV4"],
                },
                "ReturnControlToECU": {
                    "securityAccess": "",
                    "readLocalVariables": ["MyIRV5"],
                    "writtenLocalVariables": ["MyIRV6"],
                },
            },
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
                },
                "AR_testName_SC_ZcCalibrationStep": {
                    "period": 0.1,
                    "type": "PERIODIC",
                    "accesses": composition_yaml_setup.base_accesses
                }
            },
            "diagnostics": {
                "dids": {
                    "DID1": {
                        "identifier": "34EE",
                        "numberOfParameters": 1,
                        "totalNumberOfBytes": 2,
                        "operations": {
                            "ReadData": {
                                "securityAccess": "",
                                "readLocalVariables": ["MyIRV"],
                                "writtenLocalVariables": ["MyIRV"],
                            },
                            "WriteData": {
                                "securityAccess": "",
                                "readLocalVariables": ["MyIRV3"],
                                "writtenLocalVariables": ["MyIRV3"],
                            },
                            "ShortTermAdjustment": {
                                "securityAccess": "",
                                "readLocalVariables": ["MyIRV4"],
                                "writtenLocalVariables": ["MyIRV4"],
                            },
                            "ReturnControlToECU": {
                                "securityAccess": "",
                                "readLocalVariables": ["MyIRV5"],
                                "writtenLocalVariables": ["MyIRV6"],
                            },
                        },
                    },
                }
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
