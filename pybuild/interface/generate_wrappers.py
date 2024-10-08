# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

# -*- coding: utf-8 -*-
"""Python module used for calculating interfaces for CSP"""
from pathlib import Path
from pybuild.interface.hal import HALA, get_hal_list
from pybuild.interface.device_proxy import DPAL
from pybuild.interface.service import ServiceFramework, get_service_list
from pybuild.lib import logger
from pybuild.interface import generation_utils

LOGGER = logger.create_logger("CSP wrappers")


def get_manifest(app, domain, client_name):
    """Get signal manifest for application

    The model yaml files are parsed for the models included in the application.
    If there are no signals to interact with,
    this function returns None to indicate that there should not be a manifest.

    Args:
        app (Application): Pybuild project
        domain (str): Domain that the signals should not be part of
        client_name (str): Client name in the signal database
    Returns:
        spec (dict/None): signal manifest, None if no manifest should be written
    """
    rasters = app.get_rasters()
    LOGGER.debug("Rasters: %s", rasters)
    translation_files = app.get_translation_files()

    dpal = DPAL(app)
    dpal.domain_filter = [domain]
    dpal.parse_definition(translation_files)
    dpal.clear_signal_names()
    dpal.add_signals(app.insignals, "insignals")
    dpal.add_signals(app.outsignals, "outsignals")
    return dpal.to_manifest(client_name)


def parse_args():
    """Parse command line arguments

    Returns:
        Namespace: Arguments from command line
    """
    parser = generation_utils.base_parser()
    parser.add_argument(
        "--client-name",
        help="Name of the context object in CSP. Defaults to project name."
    )
    parser.add_argument(
        "--dp-interface",
        help="Output file with DP interface specifications",
        type=Path
    )
    parser.add_argument(
        "--dp-manifest-dir",
        help="Output directory for signal manifests",
        type=Path
    )
    parser.add_argument(
        "--hal-interface",
        help="Output file with HAL interface specifications",
        type=Path,
    )
    parser.add_argument(
        "--service-interface",
        help="Output file with service interface specifications",
        type=Path
    )
    return parser.parse_args()


def main():
    """ Main function for stand alone execution.
    Mostly useful for testing and generation of dummy hal specifications
    """
    args = parse_args()
    app = generation_utils.process_app(args.config)
    client_name = generation_utils.get_client_name(args, app)
    wrappers(args, app, client_name)


def wrappers(args, app, client_name):
    """ Generate specifications for pt-scheduler wrappers.

    Args:
        args (Namespace): Arguments from command line
        app (Application): Application to generate specifications for
        client_name (str): Signal client name
    """
    if args.hal_interface:
        hala = HALA(app)
        interface = generation_utils.get_interface(app, hala)
        interface["relocatable_language"] = "C"
        generation_utils.write_to_file(interface, args.hal_interface, is_yaml=True)
        hals = get_hal_list(app)
        cmake = Path(args.hal_interface.parent, 'hal.cmake')
        generation_utils.write_to_file(hals, cmake)
    if args.dp_interface:
        dp = DPAL(app)
        interface = generation_utils.get_interface(app, dp)
        interface["relocatable_language"] = "C"
        generation_utils.write_to_file(interface, args.dp_interface, is_yaml=True)
    if args.service_interface:
        service = ServiceFramework(app)
        interface = generation_utils.get_interface(app, service)
        interface["relocatable_language"] = "C"
        generation_utils.write_to_file(interface, args.service_interface, is_yaml=True)
        proxies = get_service_list(app)
        cmake = Path(args.service_interface.parent, 'service-proxies.cmake')
        generation_utils.write_to_file(proxies, cmake)
    if args.dp_manifest_dir:
        if not args.dp_manifest_dir.is_dir():
            args.dp_manifest_dir.mkdir()

        # Enable changing client name in generation
        for domain in app.get_domain_names():
            manifest = get_manifest(app, domain, client_name)
            if manifest is None:
                # Manifests without produced or consumed signals are not allowed
                # Therefore get_manifests returned None to tell us to skip this domain
                continue
            domain_file = Path(
                args.dp_manifest_dir,
                f"{domain}_{app.name}.yaml")
            generation_utils.write_to_file(manifest, domain_file, is_yaml=True)


if __name__ == "__main__":
    main()
