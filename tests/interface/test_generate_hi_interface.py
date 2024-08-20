# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Module for unit testing generate_hi_interface.py."""


import json
import os
from argparse import Namespace
from pathlib import Path
from unittest import TestCase
from ruamel.yaml import YAML
from powertrain_build.interface.generate_hi_interface import generate_hi_interface


class TestHIManifestParser(TestCase):
    """Test cases for HI Manifest Parser."""

    def test_generate_hi_interface(self):
        """Test case for generate_hi_interface."""
        base_path = "test_data/interface/test_generate_hi_interface"

        with open(os.path.join(base_path, "test_case.json"), encoding="utf-8") as json_file:
            hi_interface = json.load(json_file)
        with open(os.path.join(base_path, "expected_result.json"), encoding="utf-8") as json_file:
            expected = json.load(json_file)

        yaml_tmp = Path("yaml_tmp.yaml")
        args = Namespace()
        args.output = yaml_tmp
        generate_hi_interface(args, hi_interface)
        with yaml_tmp.open(encoding="utf-8") as fh:
            yaml = YAML(typ='safe', pure=True)
            result = yaml.load(fh)
        self.assertDictEqual(expected, result)
        yaml_tmp.unlink()
