# Signal Interface Tool

[TOC]

## Introduction

Please install PyTools to enable the commands below, see [powertrain_build and PyTools instruction](./powertrain_build.md)
Powertrain Build contains scripts for both signal consistency checks and signal interface information.

If you type the following in git bash:

```bash
py -3.6 -m powertrain_build.wrapper --help
```

## Signal Interface report

The signal Interface tool generates html reports. The following example shows how to generate the report:

```bash
py -3.6 -m powertrain_build.wrapper --build ABC_123 --interface
```

A project specific report will be available here: `Projects\ABC_123\output\Reports\SigIf.html`.
This report only displays what signals that exist in that project.

## Signal consistency report

Signal in-consistency displays per model:

* **Missing signals**, Inports whose signals are not generated in the listed configuration(s)
* **Unused signals**, Outports that are generated, but not used in the listed configuration(s).
* **Multiple defined signals**, Outports that are generated more than once in the listed configuration(s).
* **Internal signal inconsistencies**, Inports that have different variable definitions than the producing outport.
* **External signal inconsistencies**, In-/Out-ports that have different variable definitions than in the interface definition file.

After running the generation command above(e.g. for ABC_123) the Signal consistency reports are available in `Projects\ABC_123\output\Reports\`.
