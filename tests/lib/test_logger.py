# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Unit tests for logger module."""
from pybuild.lib import logger


def test_parse_log_level_default_on_error():
    """Invalid log level string should result in DEBUG level."""
    assert logger.parse_log_level('COOL_LOG_LEVEL_BRO') == logger.LEVELS[logger.LEVEL_DEBUG]
