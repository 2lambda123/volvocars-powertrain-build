# Project configuration files

Configuration files needed by the build system. The "entry point" is the project configuration file given as a command line argument to build.py. This file can contain references to other configuration files and to the software [unit definition files](unit_config.md).

## Project config

The project config file contains project specific configuration settings and references to other configuration files. It is a json file that should be located in the project root. The project configuration file can override keys/values in the base configuration file.

Example ProjectCfg.json:

```json
{
  "ConfigFileVersion": "0.2.1",
  "BaseConfig" : "../../ConfigDocuments/BaseConfig.json",
  "UnitCfgs": "conf.local/rasters.json",
  "ProjectInfo" : {
    "projConfig" : "VED4_GENIII",
    "a2LFileName": "VEA_VED4_SPA.a2l",
    "ecuSupplier" : "Denso",
    "ecuType" : "G2",
    "unitCfgDeliveryDir": "./output/UnitCfgs"
  }
}
```

## Base config

The base config file shares the same structure as the project config file and can be used for non project-specific configuration settings and default values.

Example BaseConfig.json:

```json
{
  "BaseConfigFileVersion": "0.2.1",
  "ProjectInfo" : {
    "didDefFile": "DIDIds_FullRange",
    "srcCodeDstDir": "./output/SourceCode",
    "reportDstDir": "./output/Reports",
    "logDstDir": "./output/logs",
    "configDir": "../../ConfigDocuments",
    "interfaceCfgDir": "./Config/ActiveInterfaces",
    "prjUnitSrcDir": "../../Models/*/Vc*/pybuild_src",
    "prjUnitCfgDir": "../../Models/*/Vc*/pybuild_cfg",
    "prjUnitMdlDir": "../../Models/*/Vc*",
    "prjLocalDefs": "*_LocalDefs.h",
    "prjCodeswitches": "SPM_Codeswitch_Setup*.csv",
    "coreDummyFileName" : "VcCoreDummy",
    "featureHeaderName": "VcCodeSwDefines.h",
    "tsHeaderName": "VcUnitTsDefines.h",
    "useGlobalConst" : "VcConst"
  },
  "NvmConfig": {
    "fileName" : "vcc_nvm_struct",
    "baseNvmStructs" : "conf.local/nvm_structs.json"
  }
}
```

## Units config

The units config file contains information about included software units and scheduling rasters. The software units are executed in the order they are defined within each time raster definition.

```json
{
  "UnitsConfigFileVersion": "0.2.1",
  "Projects": {
    "GEP3_HEP7": {
      "Rasters": {
        "2ms": [],
        "10ms": [
          "VcScBCoord",
          "VcScCVehMtn",
          "VcScAAccPed"
        ],
        "100ms": [
          "VcTmEdMon",
          "VcAcCtrl"
        ]
      },
      "SampleTimes": {
        "2ms": "0.002",
        "10ms": "0.010",
        "100ms": "0.100"
      }
    }
  }
}
```

## Configuration settings

### File versioning

The build system compares the version information in the configuration files with the application version to make sure a consistent configuration is used.

- "ConfigFileVersion": "0.2.1"
  - Project configuration file version.
- "BaseConfigFileVersion": "0.2.1"
  - Base configuration file version.
- "UnitsConfigFileVersion": "0.2.1"
  - Units configuration file version.

## ProjectInfo

### projConfig

The name of the project. This name is used in all the configuration files to identify the project.

### ecuSupplier

Ecu supplier name. This is used to choose supplier dependent code generation (possibly in combination with ECU Type), e.g. the core dummy file generation.

### ecuType

Ecu type name. This is used to choose supplier dependent code generation (possibly in combination with ECU Supplier), e.g. the core dummy file generation.

### unitCfgDeliveryDir

If this key is defined, the build system will deliver all the unit configuration files into the directory specified.

### didDefFile

The name of the file defining all DIDs of the project.

### srcCodeDstDir

The source code destination directory.

### logDstDir

The log files destination directory.

### configDir

The path to a folder containing all the configuration files of the project. Used to find codeswitches, core-id and DID definition files.

### interfaceCfgDir

The path to a folder with csv-files defining the supplier interface configuration. The files shall be comma separated files, with the delimiter ';'

The following files shall exists in the folder: CAN-Input.csv, CAN-Output.csv, EMS-Input.csv, EMS-Output.csv, LIN-Input.csv, LIN-Output.csv, Private CAN-Input.csv and Private CAN-Output.csv.

### prjUnitSrcDir

A file path where the superset of the source code files are found. This path can/shall use wildcards. E.g. "./Models/SSP*/Beta/Vc*/src", will match all folders under the Models folder which start with SSP, and then all folders in Beta starting with Vc, which have a src folder. The build system only includes files from software units referenced by the units config file.

### prjUnitCfgDir

A file path to the unit definition files. This file is a json file containing all the relevant meta data for the function. E.g. input parameters, output parameters, calibration labels, local measurement variables, etc... The unit definition file must match the filename pattern "config_*.json"

### coreDummyFileName

Defines the file names of the dummy Core Identifier c code, which is generated by the build environment.

### useGlobalConst

If declared, this module is included in the build. If the string is empty no module is included

### NvmConfig

This key configures the NVM area sizes, and the filename of the c-files generated to defined the NVM. The NVM is defined by six structs. The reason for using c-structs is to guarantee the order the variables are declared in memory. The c-standard does not specify in which order global variables are allocated in memory. However, the standard says that struct members should be placed in memory in the order they are declared.

```json
{
  "NvmConfig": {
    "fileName" : "vcc_nvm_struct",
    "baseNvmStructs" : "conf.local/nvm_structs.json"
  }
}
```

### baseNvmStructs

This json file holds the order for NVM signals in the structs, it also holds area size and allowed signals. We want to preserve the order for signals. So signals should never be removed from this list. If a signal is not used anymore it should not be removed, it should instead be marked with 'Position_*' eg. Position_16Bit_195 the signal position will then be filled in by buildscript with signal found in model that's not found in the json.

```json
{
  "signals": [
    {
      "x_size": 1,
      "type": "Float32",
      "name": "sVcDtcIsc_Tq_NvmAdpnNC",
      "y_size": 1
    }
  ],
  "name": "NVM_LIST_32_PER",
  "default_datatype": "UInt32",
  "instanceName": "nvm_list_32_per",
  "includeStart": "MemMap_SDA_START.h",
  "includeStop": "MemMap_SDA_STOP.h",
  "size": 190,
  "persistent": true,
  "allowed_datatypes": ["Float32", "UInt32", "Int32"]
}
```

### fileName

This key defines the name of the c-files generated, which defines the NVM areas.

### SampleTimes

The key "SampleTimes" defines the names of the available time rasters, and the value defines the scheduling time in seconds.

### Rasters

The key "Rasters", defines which units that are scheduled in that raster, and the order of the list defines the order the units are executed within the raster.
