# powertrain_build

---------------------

[TOC]

## Requirements

powertrain_build is supported on Python versions 3.6 through 3.10.

## Basic Usage

Code generation is done from git bash and the generated code is committed.
The TargetLink GUI is currently lean and all projects are initialized in Matlab
through running:

```bash
Projects/Init_PyBuild.m
```

This works the same way for Embedded coder projects, for example:

```bash
actuation-arbitration-manager-simulink-logic/Projects/Init_PyBuild.m
```

**NOTE:** Examples in upcoming chapters use Python version 3.6.

### Code generate a model

In git bash:

```bash
py -3.6 -m powertrain_build.wrapper --codegen --models Models/ICEAES/VcAesTx/VcAesTx.mdl
```

#### Set Matlab 2017 as Environmental Variable

Add New User Variables
click 'New...' and add if you want to run python from command line

```bash
MatInstl2017 "C:\Program Files\MATLAB\R2017b\bin\matlab.exe"
```

or

```bash
MatInstl2017 "/c/Program\ Files/MATLAB/R2017b/bin/matlab.exe"
```

if you want to generate code from bash.

When a new environment variable has been added you need to restart git
bash/command window.

See picture below for details.

![MatlabEnvVar](MatlabEnvVar.JPG)

#### Code generate with Embedded Coder with Matlab2019b

```python
py -3.6 -m powertrain_build.wrapper --codegen --matlab-bin "C:\MATLAB_2019_b\bin\matlab.exe" --models Models/STEER/VcSteer/VcSteer.mdl
```

### Update a TargeLink model to powertrain_build

In git bash:

```python
py -3.6 -m powertrain_build.wrapper --update --models Models/ICEAES/VcAesTx/VcAesTx.mdl
```

### Update and Code generate a model

In git bash:

```bash
py -3.6 -m powertrain_build.wrapper --update --codegen --models Models/ICEAES/VcAesTx/VcAesTx.mdl
```

### Code generation and build

To code generate and build a complete project *ABC_123*:

```bash
py -3.6 -m powertrain_build.wrapper --codegen --build ABC_123
```

### Build a project

You can either use the wrapper:

```bash
py -3.6 -m powertrain_build.wrapper --build ABC_123
```

### Detailed build options

```bash
py -3.6 -m powertrain_build.wrapper --help
```

The powertrain_build wrapper has many options, we'll explain them in detail here:

`--update` This option uses Matlab scripts to migrate models from the old build
system to powertrain_build. Once powertrain_build is officially in use, all source code should
already have been converted.

`--codegen` Runs TargetLink to generate C source code from the Matlab models.
This should be done before changes are submitted for review. If the generated
code is missing, the build system will reject your changes.

`--build` Reads configuration files and sets up preprocessor flags.

`--models=Models/SSP/MODEL/MODEL.mdl` Allows selective building and code
generation, useful for testing individual changes. Multiple model paths can
be entered, separated by comma signs.

`--dry-run` Dry run mode. No actual changes are done, can be used to test
configuration.

`--matlab-bin MATLAB_BIN` matlab arguments currently path to the matlab
binary to use. Defaults to C:\MATLABR2017b_x64\bin\matlab.exe. If you have
Matlab installed in the wrong place you can use:

```bash
py -3.6 -m powertrain_build.wrapper --codegen --models Models/ICEAES/VcAesTx/VcAesTx.mdl --matlab-bin="C:\Program Files\MATLAB\R2017b\bin\matlab.exe"
```

NOTE: Building a project (--build) does not work if a model requires a
preprocessor directive that does not exist in any configuration file.

### What to commit

Using powertrain_build we need to commit:

- Model file and if needed m-file
- All updated files in `Models/SSPXXX/VcXxxYyy/pybuild_cfg`
- Files like `config_VcXxxYyy.json`
- All updated files in `Models/SSPXXX/VcXxxYyy/pybuild_src`
- Files like `tl_defines_XxxYyy.h`, `VcXxxYyy.h`, `VcXxxYyy.c`, `VcXxxYyy.a2l`,
  `VcXxxYyy_OPortMvd_LocalDefs.h`
- Files in `tests` if needed
- Configuration files, e.g. `ConfigDocuments/SPM_Codeswitch_Setup.csv`,
  see [pre processor directives](./PreProcessorDirectives.md).

```txt
gitrepo/
├── ConfigDocuments/
│   ├── .
│   ├── .
│   ├── .
│   ├── SPM_Codeswitch_Setup.csv
│   ├── SPM_Codeswitch_Setup_ICE.csv
│   ├── SPM_Codeswitch_Setup_PVC.csv
│   ├── .
│   ├── .
│   ├── .
├── Models/
│   └── PVCTM/
│       └── VcPvcDemo/
│           ├── pybuild_cfg/
│           │   ├── config_VcPvcDemo.json
│           │   └── VcPvcDemo.yaml
│           ├── pybuild_src/
│           │   ├── tl_defines_PvcDemo.h
│           │   ├── VcPvcDemo.a2l
│           │   ├── VcPvcDemo.c
│           │   ├── VcPvcDemo.h
│           │   └── VcPvcDemo_OPortMvd_LocalDefs.h
│           ├── tests/
│           │   ├── _cumulated_code_coverage_
│           │   │   ├── ctcpost_merge_options.txt
│           │   │   └── experiment.spec
│           │   ├── VcPvcDemo_UnitTests
│           │   │   ├── 00_test_setup
│           │   │   │   ├── dataset.DCM
│           │   │   │   ├── sut_config.txt
│           │   │   │   ├── sut_interface.py
│           │   │   │   └── twTest.sil
│           │   │   ├── 01_stimulus
│           │   │   │   └── U_VcPvcDemo_ExplorativeStimulus.py
│           │   │   └── 02_watchers
│           │   │       └── U_VcPvcDemo_watcher.py
│           │   ├── ctc_env.bat
│           │   └── project.testweaver
│           ├── VcPvcDemo.mdl
│           ├── VcPvcDemo_par
```

### Summary of signals in powertrain_build

[Signal Summary](./signaling_in_powertrain_build.md)

### Signal Interface Tool

[Signal Interface Tool](./signal_interface_tool.md)

### Signal Interface Inconsistency

[Signal inconsistency in check](./signal_inconsistency_check.md)
