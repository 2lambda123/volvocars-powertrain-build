# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit test data for pybuild.dids.ZCDIDs."""

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
        'operations': {
            'ReadData': {'random_data': {}},
            'WriteData': {'random_data': {}},
            'ShortTermAdjustment': {'random_data': {}},
            'ReturnControlToECU': {'random_data': {}},
        },
    },
    'dummy_did_two': {
        'operations': {
            'ReadData': {'random_data': {}},
            'WriteData': {'random_data': {}},
            'ShortTermAdjustment': {'random_data': {}},
            'ReturnControlToECU': {'random_data': {}},
        },
    },
    'dummy_did_three': {
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
        'class': 'ASIL_D/CVC_DISP_ASIL_D',
        'operations': {
            'ReadData': {},
        },
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
        'class': 'ASIL_D/CVC_DISP_ASIL_D',
        'operations': {
            'ReadData': {},
        },
    },
}

test_get_operation_data_expected = {
    'ReadData': {
        'declaration': 'UInt8 Run_{did_name}_ReadData({data_type} *Data)',
        'body': (
            '{{\n'
            '  *Data = {did_name};\n'
            '  return 0U;\n'
            '}}\n'
        ),
    }
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
