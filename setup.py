# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Create a python package for pybuild."""

from setuptools import setup, find_packages

setup(
    setup_requires=['pbr>=5.5.0'],
    pbr=True,
    python_requires='>=3.6, <3.11',
    include_package_data=True,

)
