# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test data for powertrain_build.zone_controller.composition_yaml with a2l axis data."""

from test_data.zone_controller.test_composition_yaml import composition_yaml_setup

get_per_cfg_unit_cfg_return_value = {
    "outports": {},
    "calib_consts": {
        "tVcGpaDemo_X_DummyOne_x": {
            "VcGpaDemo": {
                "name": "tVcGpaDemo_X_DummyOne_x",
                "type": "Float32",
                "class": "CVC_CAL",
                "min": 0,
                "max": 10,
                "lsb": 1,
                "offset": 0,
                "width": [1, 5]
            }
        },
        "tVcGpaDemo_X_NotSameAsAxisOne": {
            "VcGpaDemo": {
                "name": "tVcGpaDemo_X_NotSameAsAxisOne",
                "type": "Float32",
                "class": "CVC_CAL",
                "min": -10,
                "max": 10,
                "lsb": 1,
                "offset": 0,
                "width": [1, 5]
            },
        },
        "mVcGpaDemo_X_DummyTwo_r": {
            "VcGpaDemo": {
                "name": "mVcGpaDemo_X_DummyTwo_r",
                "type": "UInt8",
                "class": "CVC_CAL",
                "min": 0,
                "max": 255,
                "lsb": 1,
                "offset": 0,
                "width": [1, 10]
            }
        },
        "mVcGpaDemo_X_DummyTwo_c": {
            "VcGpaDemo": {
                "name": "mVcGpaDemo_X_DummyTwo_c",
                "type": "UInt8",
                "class": "CVC_CAL",
                "min": "-",
                "max": "-",
                "lsb": 1,
                "offset": 0,
                "width": [1, 25]
            }
        },
        "mVcGpaDemo_X_NotSameAsAxisTwo": {
            "VcGpaDemo": {
                "name": "mVcGpaDemo_X_NotSameAsAxisTwo",
                "type": "UInt8",
                "class": "CVC_CAL",
                "min": 5,
                "max": 10,
                "lsb": 1,
                "offset": 0,
                "width": [10, 25]
            }
        }
    },
    "local_vars": {
        "sVcGpaDemo_D_BrkCtrlr": {
            "VcGpaDemo": {
                "name": "sVcGpaDemo_D_BrkCtrlr",
                "type": "UInt8",
                "class": "CVC_DISP",
                "min": "-",
                "max": "-",
                "lsb": 1,
                "offset": 0,
                "width": 1,
            }
        }
    },
    "inports": {},
}

a2l_axis_data = {
    "tVcGpaDemo_X_NotSameAsAxisOne": {
        "axes": ["tVcGpaDemo_X_DummyOne_x"],
    },
    "mVcGpaDemo_X_NotSameAsAxisTwo": {
        "axes": ["mVcGpaDemo_X_DummyTwo_r", "mVcGpaDemo_X_DummyTwo_c"],
    },
}

calibration_definitions = [
    "CVC_CAL Float32 tVcGpaDemo_X_NotSameAsAxisOne[5] = ",
    "{",
    "    0.F, 0.F, 0.F, 0.F, 0.F",
    "};",
    "CVC_CAL UInt8 mVcGpaDemo_X_NotSameAsAxisTwo[10][25] = ",
    "{",
    "   {",
    "       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ",
    "       5, 5, 5, 5, 5 ",
    "   },",
    "   {",
    "       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ",
    "       5, 5, 5, 5, 5 ",
    "   },",
    "   {",
    "       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ",
    "       5, 5, 5, 5, 5 ",
    "   },",
    "   {",
    "       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ",
    "       5, 5, 5, 5, 5 ",
    "   },",
    "   {",
    "       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ",
    "       5, 5, 5, 5, 5 ",
    "   },",
    "   {",
    "       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ",
    "       5, 5, 5, 5, 5 ",
    "   },",
    "   {",
    "       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ",
    "       5, 5, 5, 5, 5 ",
    "   },",
    "   {",
    "       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ",
    "       5, 5, 5, 5, 5 ",
    "   },",
    "   {",
    "       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ",
    "       5, 5, 5, 5, 5 ",
    "   },",
    "   {",
    "       5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, ",
    "       5, 5, 5, 5, 5 ",
    "   }",
    "};"
    "",
]

expected_result = {
    "SoftwareComponents": {
        "testName_SC": {
            "type": "SWC",
            "template": "ARTCSC",
            "runnables": {
                "AR_prefix_VcExtINI": {
                    "type": "INIT",
                    "accesses": [
                        "tVcGpaDemo_X_DummyOne_x",
                        "tVcGpaDemo_X_NotSameAsAxisOne",
                        "mVcGpaDemo_X_DummyTwo_r",
                        "mVcGpaDemo_X_DummyTwo_c",
                        "mVcGpaDemo_X_NotSameAsAxisTwo"
                    ]
                },
                "AR_prefix_testRunnable": {
                    "period": 10,
                    "type": "PERIODIC",
                    "accesses": [
                        "tVcGpaDemo_X_DummyOne_x",
                        "tVcGpaDemo_X_NotSameAsAxisOne",
                        "mVcGpaDemo_X_DummyTwo_r",
                        "mVcGpaDemo_X_DummyTwo_c",
                        "mVcGpaDemo_X_NotSameAsAxisTwo"
                    ]
                }
            },
            "diagnostics": {},
            "static": composition_yaml_setup.base_static,
            "shared": {
                "tVcGpaDemo_X_DummyOne_x": {
                    "access": "READ-WRITE",
                    "type": "dt_tVcGpaDemo_X_DummyOne_x",
                    "init": [0.0, 0.0, 0.0, 0.0, 0.0]
                },
                "tVcGpaDemo_X_NotSameAsAxisOne": {
                    "access": "READ-WRITE",
                    "type": "dt_tVcGpaDemo_X_NotSameAsAxisOne",
                    "init": [0.0, 0.0, 0.0, 0.0, 0.0]
                },
                "mVcGpaDemo_X_DummyTwo_r": {
                    "access": "READ-WRITE",
                    "type": "dt_mVcGpaDemo_X_DummyTwo_r",
                    "init": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                },
                "mVcGpaDemo_X_DummyTwo_c": {
                    "access": "READ-WRITE",
                    "type": "dt_mVcGpaDemo_X_DummyTwo_c",
                    "init": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                },
                "mVcGpaDemo_X_NotSameAsAxisTwo": {
                    "access": "READ-WRITE",
                    "type": "dt_mVcGpaDemo_X_NotSameAsAxisTwo",
                    "init": [
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
                    ]
                }
            },
            "ports": {
                "GlobSignNme": {"direction": "IN", "interface": "PIGlobSignNme"}
            },
        }
    },
    "DataTypes": {
        "Bool": {
            "type": "ENUMERATION",
            "enums": {
                "False": 0,
                "True": 1
            }
        },
        "Float32": {
            "type": "FLOAT",
            "limits": {
                "lower": -3.4e38,
                "upper": 3.4e38
            }
        },
        "Int16": {
            "type": "INTEGER",
            "limits": {
                "lower": -32768,
                "upper": 32767
            }
        },
        "Int32": {
            "type": "INTEGER",
            "limits": {
                "lower": -2147483648,
                "upper": 2147483647
            }
        },
        "Int8": {
            "type": "INTEGER",
            "limits": {
                "lower": -128,
                "upper": 127
            }
        },
        "UInt16": {
            "type": "INTEGER",
            "limits": {
                "lower": 0,
                "upper": 65535
            }
        },
        "UInt32": {
            "type": "INTEGER",
            "limits": {
                "lower": 0,
                "upper": 4294967295
            }
        },
        "UInt8": {
            "type": "INTEGER",
            "limits": {
                "lower": 0,
                "upper": 255
            }
        },
        "ExtraType": {
            "type": "RECORD",
            "elements": {
                "structElem": "UInt8"
            }
        },
        "dt_tVcGpaDemo_X_DummyOne_x": {
            "type": "COM_AXIS",
            "axis-index": 1,
            "size": 5,
            "limits": {"lower": 0, "upper": 10},
            "swrecordlayout": {
                "name": "Distr_tVcGpaDemo_X_DummyOne_x",
                "type": "INDEX_INCR",
                "basetype": "float32",
                "label": "X"
            }
        },
        "dt_tVcGpaDemo_X_NotSameAsAxisOne": {
            "type": "CURVE",
            "axis": "dt_tVcGpaDemo_X_DummyOne_x",
            "limits": {"lower": -10, "upper": 10},
            "swrecordlayout": {
                "name": "Curve_tVcGpaDemo_X_NotSameAsAxisOne",
                "type": "COLUMN_DIR",
                "basetype": "float32",
                "label": "Val"
            }
        },
        "dt_mVcGpaDemo_X_DummyTwo_r": {
            "type": "COM_AXIS",
            "axis-index": 1,
            "size": 10,
            "limits": {"lower": 0, "upper": 255},
            "swrecordlayout": {
                "name": "Distr_mVcGpaDemo_X_DummyTwo_r",
                "type": "INDEX_INCR",
                "basetype": "uint8",
                "label": "X"
            }
        },
        "dt_mVcGpaDemo_X_DummyTwo_c": {
            "type": "COM_AXIS",
            "axis-index": 2,
            "size": 25,
            "limits": {"lower": 0, "upper": 255},
            "swrecordlayout": {
                "name": "Distr_mVcGpaDemo_X_DummyTwo_c",
                "type": "INDEX_INCR",
                "basetype": "uint8",
                "label": "Y"
            }
        },
        "dt_mVcGpaDemo_X_NotSameAsAxisTwo": {
            "type": "MAP",
            "x-axis": "dt_mVcGpaDemo_X_DummyTwo_r",
            "y-axis": "dt_mVcGpaDemo_X_DummyTwo_c",
            "limits": {"lower": 5, "upper": 10},
            "swrecordlayout": {
                "name": "Map_mVcGpaDemo_X_NotSameAsAxisTwo",
                "type": "COLUMN_DIR",
                "basetype": "uint8",
                "label": "Val"
            }
        }
    },
    "PortInterfaces": composition_yaml_setup.base_port_interfaces,
    "ExternalFiles": composition_yaml_setup.base_configuration
}
