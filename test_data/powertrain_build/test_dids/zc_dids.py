# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test data for powertrain_build.dids.ZCDIDs."""

dummy_project_dids = {
    'dummy_did_one': {
        'handle': 'VcDummy/VcDummy/Subsystem/VcDummy/VcDummy/1_VcDummy/Rel',
        'name': 'dummy_did_one',
        'configs': '((ALWAYS_ACTIVE))',
        'description': 'Dummy DID',
        'type': 'UInt8',
        'unit': '',
        'offset': '',
        'lsb': '',
        'min': '-',
        'max': '-',
        'class': 'ASIL_D/CVC_DISP_ASIL_D'
    },
    'dummy_did_two': {
        'handle': 'VcDummyTwo/VcDummyTwo/Subsystem/VcDummyTwo/VcDummyTwo/1_VcDummyTwo/Rel',
        'name': 'dummy_did_two',
        'configs': '((ALWAYS_ACTIVE))',
        'description': 'Dummy DID number 2',
        'type': 'UInt8',
        'unit': '',
        'offset': '',
        'lsb': '',
        'min': '-',
        'max': '-',
        'class': 'ASIL_D/CVC_DISP_ASIL_D'
    }
}

bad_dummy_project_dids = {
    'dummy_did_one': {
        'handle': 'VcDummy/VcDummy/Subsystem/VcDummy/VcDummy/1_VcDummy/Rel',
        'name': 'dummy_did_one',
        'configs': '((ALWAYS_ACTIVE))',
        'description': 'Dummy DID',
        'type': 'Float32',
        'unit': '',
        'offset': '',
        'lsb': '',
        'min': '-',
        'max': '-',
        'class': 'ASIL_D/CVC_DISP_ASIL_D'
    },
    'dummy_did_two': {
        'handle': 'VcDummy/VcDummy/Subsystem/VcDummy/VcDummy/1_VcDummyTwo/Rel',
        'name': 'dummy_did_two',
        'configs': '((ALWAYS_ACTIVE))',
        'description': 'Dummy DID',
        'type': 'Int8',
        'unit': '',
        'offset': '',
        'lsb': '',
        'min': '-',
        'max': '-',
        'class': 'ASIL_D/CVC_DISP_ASIL_D'
    },
}

valid_dids = {
    'dummy_did_one': {
        'operations': {
            'ReadData': {},
        },
    },
    'dummy_did_two': {
        'operations': {
            'ReadData': {},
        },
    }
}

bad_valid_dids = {
    'dummy_did_one': {
        'identifier': 0xAAAA,
        'numberOfParameters': 2,
        'totalNumberOfBytes': 2,
        'operations': {
            'ReadData': {'random_data': {}},
            'WriteData': {'random_data': {}},
            'ShortTermAdjustment': {'random_data': {}},
            'ReturnControlToECU': {'random_data': {}},
        },
    },
    'dummy_did_two': {
        'identifier': 0xAAAB,
        'numberOfParameters': 2,
        'totalNumberOfBytes': 2,
        'operations': {
            'ReadData': {'random_data': {}},
            'WriteData': {'random_data': {}},
            'ShortTermAdjustment': {'random_data': {}},
            'ReturnControlToECU': {'random_data': {}},
        },
    },
    'dummy_did_three': {
        'identifier': 0xAAAC,
        'numberOfParameters': 2,
        'totalNumberOfBytes': 2,
        'operations': {
            'ReadData': {'random_data': {}},
            'WriteData': {'random_data': {}},
            'ShortTermAdjustment': {'random_data': {}},
            'ReturnControlToECU': {'random_data': {}},
        },
    },
}

test_valid_dids_setter_expected = {
    'dummy_did_one': {
        'identifier': 0xAAAA,
        'numberOfParameters': 2,
        'totalNumberOfBytes': 2,
        'operations': {
            'ReadData': {'random_data': {}},
            'WriteData': {'random_data': {}},
            'ShortTermAdjustment': {'random_data': {}},
            'ReturnControlToECU': {'random_data': {}},
        },
    },
    'dummy_did_two': {
        'identifier': 0xAAAB,
        'numberOfParameters': 2,
        'totalNumberOfBytes': 2,
        'operations': {
            'ReadData': {'random_data': {}},
            'WriteData': {'random_data': {}},
            'ShortTermAdjustment': {'random_data': {}},
            'ReturnControlToECU': {'random_data': {}},
        },
    },
}

test_get_operation_data_did_data = {
    'dummy_did_one': {
        'name': 'dummy_did_one',
        'type': 'UInt8',
    },
    'dummy_did_two': {
        'name': 'dummy_did_two',
        'type': 'UInt32',
    }
}

test_get_operation_data_expected = {
    'dummy_did_one': {
        'ReadData': {
            'declaration': 'UInt8 Run_dummy_did_one_ReadData(UInt8 *Data)',
            'body': (
                '{\n'
                '  *Data = dummy_did_one;\n'
                '  return 0U;\n'
                '}\n'
            ),
        },
    },
    'dummy_did_two': {
        'ReadData': {
            'declaration': 'UInt8 Run_dummy_did_two_ReadData(UInt8 Data[4])',
            'body': (
                '{\n'
                '  for (UInt8 i = 0U; i < 4; i++) {\n'
                '    Data[i] = (dummy_did_two >> (8 * i)) & 0xFF;\n'
                '  }\n'
                '  return 0U;\n'
                '}\n'
            ),
        },
    },
}

TEST_GET_HEADER_FILE_CONTENT_EXPECTED = (
    '#ifndef VCDIDAPI_H\n'
    '#define VCDIDAPI_H\n'
    '\n'
    '#include "tl_basetypes.h"\n'
    '#include "Rte_DUMMY.h"\n'
    '\n'
    '#include "PREDECL_DISP_ASIL_D_START.h"\n'
    'extern CVC_DISP_ASIL_D UInt8 dummy_did_one;\n'
    'extern CVC_DISP_ASIL_D UInt8 dummy_did_two;\n'
    '#include "PREDECL_DISP_ASIL_D_END.h"\n'
    '\n#include "PREDECL_CODE_ASIL_D_START.h"\n'
    'UInt8 Run_dummy_did_one_ReadData(UInt8 *Data);\n'
    'UInt8 Run_dummy_did_two_ReadData(UInt8 *Data);\n'
    '#include "PREDECL_CODE_ASIL_D_END.h"\n'
    '\n#endif /* VCDIDAPI_H */\n'
)

TEST_GET_SOURCE_FILE_CONTENT_EXPECTED = (
    '#include "VcDIDAPI.h"\n'
    '\n'
    '#include "CVC_CODE_ASIL_D_START.h"\n'
    'UInt8 Run_dummy_did_one_ReadData(UInt8 *Data)\n'
    '{\n'
    '  *Data = dummy_did_one;\n'
    '  return 0U;\n'
    '}\n'
    'UInt8 Run_dummy_did_two_ReadData(UInt8 *Data)\n'
    '{\n'
    '  *Data = dummy_did_two;\n'
    '  return 0U;\n'
    '}\n'
    '#include "CVC_CODE_ASIL_D_END.h"\n'
)
