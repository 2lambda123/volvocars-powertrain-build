# Introduction of powertrain_build for new employee

[TOC]

<!--:powertrain_build:-->

## General powertrain_build Information

[powertrain_build introduction](./powertrain_build.md) introduces installation and basic usage of powertrain_build.

## powertrain_build Code Base

The basic code introduction is placed in [powertrain_build General Code Introduction](./powertrain_build_architecture.md).

## powertrain_build Deployment

Information on how to deploy powertrain_build can be found [here](./powertrain_build_deployment.md).

## powertrain_build Development

If you want to develop powertrain_build, you can run it directly from the Git repositories. You probably need a separate virtual environment, as any installed release versions of powertrain_build would interfere:

```shell
python3 -m venv powertrain_build_venv
source ./powertrain_build_venv/bin/activate
```

Once activated, you can execute it:

```shell
PYTHONPATH=<path_to>//powertrain-build python -m powertrain_build.wrapper build-specific --project-config Projects/CSP/PvcDepDemo/ProjectCfg.json --core-dummy
```
