# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Constant defining the expected result from reading the unit config files.

Reads from a test configuration file, and checks the if the output is
accorfing to expectioans.
"""

IO_CNFG_DICT = {
    'VED4_GENIII': {
        'CAN-Input': {
            'sVcAc_D_EngRunReqClim': {
                'IOType': 'd',
                'description': 'Engine running request (inhibit stop) from climate',
                'element_index': 5,
                'init': 0,
                'max': 3,
                'min': 0,
                'type': 'UInt8',
                'unit': '-'
            }
        },
        'CAN-Output': {
            'sVcAc_D_AirCondCmpsrStats': {
                'IOType': 'd',
                'description': 'Aircond compressor status',
                'element_index': 5,
                'init': 0,
                'max': 7,
                'min': 0,
                'type': 'UInt8',
                'unit': '-'
            }
        },
        'LIN-Input': {},
        'LIN-Output': {},
        'EMS-Input': {},
        'EMS-Output': {},
        'Private CAN-Input': {
            'sVcTc_p_LockUp': {
                'IOType': 'x',
                'description': 'AW Pressure request to LU',
                'element_index': 5,
                'init': 0,
                'max': 16383,
                'min': 0,
                'type': 'Float32',
                'unit': 'gf/cm2'
            }
        },
        'Private CAN-Output': {}
        },
    'VEP4_GENIII': {
        'CAN-Input': {},
        'CAN-Output': {
            'sVcAc_D_AirCondCmpsrStats': {
                'IOType': 'd',
                'description': 'Aircond compressor status',
                'element_index': 5,
                'init': 0,
                'max': 7,
                'min': 0,
                'type': 'UInt8',
                'unit': '-'
            }
        },
        'LIN-Input': {},
        'LIN-Output': {},
        'EMS-Input': {},
        'EMS-Output': {},
        'Private CAN-Input': {},
        'Private CAN-Output': {}
    }
}

INPUT_CNFG_DICT = {
    'VED4_GENIII': {
        'CAN-Input': {
            'sVcAc_D_EngRunReqClim': {
                'IOType': 'd',
                'description': 'Engine running request (inhibit stop) from climate',
                'element_index': 5,
                'init': 0,
                'max': 3,
                'min': 0,
                'type': 'UInt8',
                'unit': '-'
            },
            'sVcAcc_a_Max': {
                'IOType': 's',
                'description': 'Max acceleration request from ACC',
                'element_index': 6,
                'init': 0,
                'max': 5,
                'min': -5,
                'type': 'Float32',
                'unit': 'm/s2'
            }
        },
        'EMS-Input': {},
        'LIN-Input': {},
        'Private CAN-Input': {
            'sVcTc_p_LockUp': {
                'IOType': 'x',
                'description': 'AW Pressure request to LU',
                'element_index': 5,
                'init': 0,
                'max': 16383,
                'min': 0,
                'type': 'Float32',
                'unit': 'gf/cm2'
            }
        }
    },
    'VEP4_GENIII': {
        'CAN-Input': {},
        'EMS-Input': {},
        'LIN-Input': {},
        'Private CAN-Input': {},
    }
}

OUTPUT_CNFG_DICT = {
    'VED4_GENIII': {
        'CAN-Output': {
            'sVcAc_D_AirCondCmpsrStats': {
                'IOType': 'd',
                'description': 'Aircond compressor status',
                'element_index': 5,
                'init': 0,
                'max': 7,
                'min': 0,
                'type': 'UInt8',
                'unit': '-'
            }
        },
        'EMS-Output': {},
        'LIN-Output': {},
        'Private CAN-Output': {}
        },
    'VEP4_GENIII': {
        'CAN-Output': {
            'sVcAc_D_AirCondCmpsrStats': {
                'IOType': 'd',
                'description': 'Aircond compressor status',
                'element_index': 5,
                'init': 0,
                'max': 7,
                'min': 0,
                'type': 'UInt8',
                'unit': '-'
            }
        },
        'EMS-Output': {},
        'LIN-Output': {},
        'Private CAN-Output': {}
    }
}

DEP_IO_CNFG_DICT = {
    'VED4_GENIII': {
        'CAN-Input': {
            'sVcAcc_a_Max': {
                'IOType': 's',
                'description': 'Max acceleration request from ACC',
                'element_index': 6,
                'init': 0,
                'max': 5,
                'min': -5,
                'type': 'Float32',
                'unit': 'm/s2'}},
        'CAN-Output': {},
        'EMS-Input': {},
        'EMS-Output': {},
        'LIN-Input': {},
        'LIN-Output': {},
        'Private CAN-Input': {},
        'Private CAN-Output': {}
    },
    'VEP4_GENIII': {
        'CAN-Input': {},
        'CAN-Output': {},
        'EMS-Input': {},
        'EMS-Output': {},
        'LIN-Input': {},
        'LIN-Output': {},
        'Private CAN-Input': {},
        'Private CAN-Output': {}
    }
}

DBG_CNFG_DICT = {
    'VED4_GENIII': {
        'CAN-Input': {
            'sVcAc_D_EngRunReqClim': {
                'IOType': 'd',
                'description': 'Engine running '
                               'request (inhibit '
                               'stop) from climate',
                'element_index': 5,
                'init': 0,
                'max': 3,
                'min': 0,
                'type': 'UInt8',
                'unit': '-'}},
        'CAN-Output': {
            'sVcAc_D_AirCondCmpsrStats': {
                'IOType': 'd',
                'description': 'Aircond compressor status',
                'element_index': 5,
                'init': 0,
                'max': 7,
                'min': 0,
                'type': 'UInt8',
                'unit': '-'
            }
        },
        'EMS-Input': {},
        'EMS-Output': {},
        'LIN-Input': {},
        'LIN-Output': {},
        'Private CAN-Input': {},
        'Private CAN-Output': {}
    },
    'VEP4_GENIII': {
        'CAN-Input': {},
        'CAN-Output': {
            'sVcAc_D_AirCondCmpsrStats': {
                'IOType': 'd',
                'description': 'Aircond compressor status',
                'element_index': 5,
                'init': 0,
                'max': 7,
                'min': 0,
                'type': 'UInt8',
                'unit': '-'
            }
        },
        'EMS-Input': {},
        'EMS-Output': {},
        'LIN-Input': {},
        'LIN-Output': {},
        'Private CAN-Input': {},
        'Private CAN-Output': {}
    }
}

EC_CNFG_DICT = {
    'ADAS': {
        'CAN-Input': {
            'sVcAc_D_EngRunReqClim': {
                'IOType': 'd',
                'description': 'Engine running request (inhibit stop) from climate',
                'element_index': 5,
                'init': 0,
                'max': 3,
                'min': 0,
                'type': 'ulong_T',
                'unit': '-'
            }
        },
        'CAN-Output': {
            'sVcAc_D_AirCondCmpsrStats': {
                'IOType': 'd',
                'description': 'Aircond compressor status',
                'element_index': 5,
                'init': 0,
                'max': 7,
                'min': 0,
                'type': 'real32_T',
                'unit': '-'
            }
        },
        'LIN-Input': {},
        'LIN-Output': {},
        'EMS-Input': {},
        'EMS-Output': {},
        'Private CAN-Input': {},
        'Private CAN-Output': {}
    }
}
