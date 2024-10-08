# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Module to export information of global variables from pybuild projects."""

import argparse
import os
import sys
from typing import Dict, Tuple

from ruamel.yaml import YAML

from pybuild.build_proj_config import BuildProjConfig
from pybuild.feature_configs import FeatureConfigs
from pybuild.unit_configs import UnitConfigs


def get_global_variables(project_config_path: str) -> Dict:
    """Get global variables connected to PyBuild project.

    Args:
        project_config_path (str): Path to ProjectCfg.json file.
    Returns:
        (Dict): Dict containing project name and its global variables (name, type).
    """
    project_name, project_unit_config = _get_project_data(project_config_path)

    variable_types = ["outports", "local_vars", "calib_consts", "nvm"]
    variables = []
    for variable_type in variable_types:
        if variable_type not in project_unit_config:
            continue

        variables_info = [
            {"name": variable, "type": _get_variable_type(variable_info)}
            for variable, variable_info in project_unit_config[variable_type].items()
        ]
        variables.extend(variables_info)
    return {"name": project_name, "variables": variables}


def _get_variable_type(variable_info: Dict) -> str:
    """Get variable type from variable info.

    Args:
        variable_info (Dict): Dictionary with the variable info.

    Returns:
        str: Variable type.
    """
    unit_name = list(variable_info.keys())[0]  # Getting any unit name, since variable type should be the same
    return variable_info[unit_name]["type"]


def _get_project_data(project_config_path: str) -> Tuple[str, Dict]:
    """Gets data for a pybuild project.

    Args:
        project_config_path (str): Path to ProjectCfg.json file.
    Returns:
        project_name (str): Name of PyBuild project.
        project_unit_config (dict): Dict mapping variable types to variables and their data.
    """
    build_cfg = BuildProjConfig(os.path.normpath(project_config_path))
    feature_cfg = FeatureConfigs(build_cfg)
    unit_cfg = UnitConfigs(build_cfg, feature_cfg)
    project_unit_config = unit_cfg.get_per_cfg_unit_cfg()
    return build_cfg.name, project_unit_config


def _export_yaml(data: Dict, file_path: str) -> None:
    """Exports data from dictionary to a yaml file.

    Args:
        data (Dict): Dictionary with data.
        file_path (str): Path of the file to export data.
    """
    with open(file_path, "w", encoding="utf-8") as yaml_file:
        yaml = YAML()
        yaml.default_flow_style = False
        yaml.dump(data, yaml_file)


def _main():
    args = _parse_args()
    global_variables = get_global_variables(args.project_config)
    _export_yaml(global_variables, args.output_file)


def _parse_args():
    parser = argparse.ArgumentParser(description="Export global variables.")
    parser.add_argument("--project-config", help="Project root configuration file.", required=True)
    parser.add_argument("--output-file", help="Output file to export global variables.", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    sys.exit(_main())
