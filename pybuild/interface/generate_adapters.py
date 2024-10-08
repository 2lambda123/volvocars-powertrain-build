# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

# -*- coding: utf-8 -*-
"""Python module used for calculating interfaces for CSP"""
from pathlib import Path
from os import path
from pybuild.interface.hal import HALA
from pybuild.interface.device_proxy import DPAL
from pybuild.interface.service import ServiceFramework
from pybuild.interface import simulink
from pybuild.lib import logger
from pybuild.interface import generation_utils
from pybuild.lib.helper_functions import deep_json_update

LOGGER = logger.create_logger("CSP adapters")


def parse_args():
    """Parse arguments

    Returns:
        Namespace: the parsed arguments
    """
    parser = generation_utils.base_parser()
    parser.add_argument(
        "--dp-interface",
        help="Add dp interface to adapter specification",
        action="store_true"
    )
    parser.add_argument(
        "--hal-interface",
        help="Add dp interface to adapter specification",
        action="store_true"
    )
    parser.add_argument(
        "--service-interface",
        help="Add sfw interface to adapter specification",
        action="store_true"
    )
    parser.add_argument(
        "output",
        help="Output file with interface specifications",
        type=Path
    )
    parser.add_argument(
        "--update-config",
        help="Update project config file with path to adapter specifications",
        action="store_true"
    )
    return parser.parse_args()


def main():
    """ Main function for stand alone execution.
    Mostly useful for testing and generation of dummy hal specifications
    """
    args = parse_args()
    app = generation_utils.process_app(args.config)
    adapters(args, app)


def update_project_config(args):
    """ Update project config file with relative location to adapter specification file, linux styled path.

    Args:
        args (Namespace): Arguments from command line
    """
    config_dir = Path(args.config).resolve().parents[0]
    output_dir = Path(args.output).resolve().parents[0]
    rel_dir = Path(path.relpath(output_dir, config_dir))
    rel_path = rel_dir / Path(args.output).name
    rel_path_linux = rel_path.as_posix()
    deep_json_update(
        args.config,
        {'ProjectInfo': {'adapterSpec': rel_path_linux}}
    )


def adapters(args, app):
    """ Generate specification for adapter generation.

    Args:
        args (Namespace): Arguments from command line
        app (Application): Application to generate specification for
    """

    if args.dp_interface:
        dp = DPAL(app)
        dp_interface = generation_utils.get_interface(app, dp)
    else:
        dp_interface = {}

    if args.hal_interface:
        hala = HALA(app)
        hal_interface = generation_utils.get_interface(app, hala)
    else:
        hal_interface = {}

    if args.service_interface:
        sfw = ServiceFramework(app)
        sfw_interface = generation_utils.get_interface(app, sfw)
        method_interface = generation_utils.get_method_interface(app)
    else:
        sfw_interface = {}
        method_interface = {}

    interface_data_types = app.pybuild['user_defined_types'].get_interface_data_types()

    adapters = simulink.get_interface(
        interface_data_types,
        dp_interface,
        hal_interface,
        sfw_interface,
        method_interface
    )

    generation_utils.write_to_file(adapters, args.output, is_yaml=True)

    if args.update_config:
        update_project_config(args)


if __name__ == "__main__":
    main()
