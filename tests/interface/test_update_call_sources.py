# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Module for testing the update_call_sources.py module."""


import json
import unittest

from pybuild.interface import update_call_sources

# C-Code chunks
CHUNK_0 = (
    '/* Used for running spm without csp, such as silver\n'
    '   This code should be replaced when using csp. */\n'
)
CHUNK_1 = (
    '#include "VcHmiRx_CSPMethodCall.h"\n'
    '\n'
    '#include "CVC_CODE_START.h"\n'
    'Bool VcHmiRx_CSPMethodCall(  Float32 sVcScOut_Tq_WhlMotSysTqReq )\n'
    '{\n'
)
CHUNK_2 = (
    '    /* CSP method call\n'
    '    csp::afw::core::ErrorCode errorCode = ADAPTER->METHOD();\n'
)
CHUNK_3 = (
    '    switch(errorCode) {\n'
    '        case csp::afw::core::ErrorCode::kSuccess :\n'
    '            return 0;\n'
    '        default :\n'
    '            return 1;\n'
    '    }\n'
)
CHUNK_4 = '    CSP method call end*/\n'
CHUNK_5 = (
    '    /* C dummy call*/\n'
    '    return 1;\n'
    '    /* C dummy call end*/\n'
)
CHUNK_6 = '}'


class TestUpdateCallSources(unittest.TestCase):
    """Unit tests for the update_call_sources module."""

    def setUp(self):
        base_path = 'test_data/interface/test_update_call_sources/'
        with open(base_path + 'test_case.json', encoding="utf-8") as test_file:
            self.adapters = json.load(test_file)

    def test_is_method_adapter(self):
        """Test is_method_adapter method."""
        no_methods_adapter = update_call_sources.is_method_adapter(self.adapters[0])
        one_method_adapter = update_call_sources.is_method_adapter(self.adapters[1])
        self.assertTrue(one_method_adapter)
        self.assertFalse(no_methods_adapter)

    def test_generate_src_code(self):
        """Test generate_src_code method."""
        adapter = self.adapters[1]
        method = adapter['methods'][0]
        method_config = {"method_call_wrapper": {"pre": "", "post": ""}}
        c_code = ''.join([CHUNK_0, CHUNK_1, CHUNK_2, CHUNK_3, CHUNK_4, CHUNK_5, CHUNK_6])
        new_c = update_call_sources.generate_src_code(adapter, method, c_code, method_config)
        exp_c2 = (
                '    csp::afw::core::ErrorCode errorCode = '
                'adapterwrapper::Csp_Methods->VcPvcDemo_11_CSPMethodCall2();\n'
        )
        exp_c = ''.join([CHUNK_1, exp_c2, CHUNK_3, CHUNK_6])
        self.assertEqual(exp_c, new_c)

    def test_generate_header_code(self):
        """Test generate_header_code method."""
        old_header = (
            r'#include "not_adapter_wrapper.hh"\n'
            r'#include "adapter_wrapper.hh"'
        )
        method_config = {'adapter_declarations_change': None}
        new_header = update_call_sources.generate_header_code(method_config, old_header)
        self.assertEqual(old_header, new_header)
        method_config = {'adapter_declarations_change': 'changed_adapter_header.h'}
        new_header = update_call_sources.generate_header_code(method_config, old_header)
        expected_header = (
            r'#include "not_adapter_wrapper.hh"\n'
            r'#include "changed_adapter_header.h"'
        )
        self.assertEqual(expected_header, new_header)
