# Unit definition file

This unit definition file contains all the meta data needed for the build system to include the software unit in the build and to create the necessary files (e.g. A2L-files, NVM allocation). It is also used to perform consistency checks in the system.

For TargetLink models, this unit definition file is created by the source generation scripts.

The unit definition file contains nine major keys - version, outports, inports, nvm, core, dids, pre_procs, local_vars and calib_consts. These are described below.

TODO: Consider changing name from unit configuration to unit definition.

Example config_*.json:

```json
{
    "version": "0.2.1",
    "outports": {
        "sVcPemAlc_D_EngLoadReqEl": {
        "handle": "VcPemAlc/VcPemAlc/Subsystem/VcPemAlc/tlop_VcAc_Tq_AcLoad5",
        "name": "sVcPemAlc_D_EngLoadReqEl",
        "configs": ["all"],
        "description": "Request change in electrical loads controlled by CEM",
        "type": "Int16",
        "unit": "W",
        "offset": 0,
        "lsb": 1,
        "min": -32768,
        "max": 32767,
        "class": "CVC_EXT"}},
    "inports": {
        "sVcEc_n_Eng": {
        "handle": "VcPemAlc/VcPemAlc/Subsystem/VcPemAlc/tlip_VcEc_n_Eng",
        "name": "sVcEc_n_Eng",
        "configs": [
            ["all"],
            ["Vc_Pem_Alc_B_CodegenFastCat == 1"],
            ["Vc_Pem_Alc_B_CodegenDpfRegen == 1"]],
        "description": "Engine speed",
        "type": "Float32",
        "unit": "rpm",
        "offset": 0,
        "lsb": 1,
        "min": 0,
        "max": 10000,
        "class": "CVC_EXT"}},
    "calib_consts": {
        "cVcAesAir_B_ThrCtrlStrtWght": {
            "type": "Bool",
            "unit": "g/s",
            "description": "Switch to weight target cylinder flow during hand-over from start throttle",
            "max": "-",
            "min": "-",
            "lsb": "1",
            "offset": "0",
            "class": "CVC_CAL",
            "handle": "VcAesAir/VcAesAir/Subsystem/VcAesAir/VcAesAir/1_AirTarDyn/11_CylTarStrt/B_ThrCtrlStrtWght",
            "configs": ["all"],
            "width": [1]}},
    "local_vars": {
        "rVcAesAir_m_CylTarAct": {
            "type": "Float32",
            "unit": "mg/stk",
            "description": "Target cylinder charge flow for aircharge control",
            "max": "5000",
            "min": "0",
            "lsb": "1",
            "offset": "0",
            "class": "CVC_DISP",
            "handle": "VcAesAir/VcAesAir/Subsystem/VcAesAir/VcAesAir/1_AirTarDyn/11_CylTarStrt/Switch1",
            "configs": ["all"],
            "width": 1}},
    "core": {
        "Events": {
            "VcEvImmoBCM": {
                "API_blk": [
                {
                    "path": "VcPpmImob/VcPpmImob/Subsystem/VcPpmImob/VcPpmImob/1000_ImobConnectionLayer/1600_Diag/1620_CoreIfNew/Dem_SetEventStatusPF1",
                    "config": [
                    "Vc_NewDiagnosticCoreIF == 1"]},
                {
                    "path": "VcPpmImob/VcPpmImob/Subsystem/VcPpmImob/VcPpmImob/1000_ImobConnectionLayer/1600_Diag/1620_CoreIfNew/Dem_SetEventStatusPP1",
                    "config": [
                    "Vc_NewDiagnosticCoreIF == 1"]}],
                "blk_name": "NamedConstant1",
                "subsystem": "VcPpmImob/VcPpmImob/Subsystem/VcPpmImob/VcPpmImob/1000_ImobConnectionLayer/1600_Diag/1620_CoreIfNew",
                "API_blk_type": "Dem_SetEventStatus Pre-Passed",
                "description": "",
                "type": "",
                "unit": "",
                "offset": "",
                "lsb": "",
                "min": "",
                "max": "",
                "class": ""}
            },
        "IUMPR": {},
        "FIDs": {},
        "Ranking": {},
        "TstId": {}},
    "dids": {
      "yVcPpmPsm_B_DriveCycleActive": {
      "name": "yVcPpmPsm_B_DriveCycleActive",
      "description": "Driver  has entered the driving cycle  1= Active 0 = Not Active",
      "handle": "VcPpmPsm/VcPpmPsm/Subsystem/VcPpmPsm/yVcPsm_B_DriveCycleActive",
      "configs": ["Vc_D_CodegenHev > 0"],
      "type": "Bool",
      "unit": "-",
      "offset": 0,
      "lsb": 1,
      "min": "NaN",
      "max": "NaN",
      "class": "CVC_DISP"}},
    "nvm": { },
    "pre_procs" : [
        "Vc_Aes_TrboM_B_CodeGen2Trbo",
        "Vc_Aes_TrboM_B_CodeGenBstPeak",
        "Vc_Aes_TrboM_B_CodeGenTrbo",
        "Vc_Aes_TrboM_B_CodeGenTrboMode06",
        "Vc_Aes_TrboM_B_CodeGenTrboOverSpd"]
}
```

## Unit definition data

### outports, inports, calib_consts, local_vars and nvm

Outports contains all the signals (variables) which the unit produces.
Inports contains all signals used from other units, to perform the unit's task.
calib_consts holds the definition of all the calibration constants in the unit.
local_vars holds the definition of unit internal variables possible to measure.
nvm blocks defines the units use of non-volatile memory.

The keys outports, inports and nvm have the following keys, which defines them:

### handle

This is a handle to where the variable/parameter is created (outports) or used (inports & nvm)
For TargetLink this is a string identifying the block in the model
e.g. "VcPemAlc/VcPemAlc/Subsystem/VcPemAlc/yVcVmcPmm_B_SsActive9".

### name

The name of the variable or parameter.

### configs

Which codeswitches this variable depends on.
For TargetLink this information is parsed from the model structure,
and depends on the use of pre-processor directives.

Can have the following formats;

* a list of lists of config strings
  * [[cs1 and cs2] or [cs3 and cs4]].
* list of config strings,
  * [cs1 and cs2].
* or a string
  * (cs):

E.g. [["Vc_Pem_Alc_B_CodegenFastCat == 1"],["Vc_Pem_Alc_B_CodegenDpfRegen == 1"]]
means that the signal is active in the configuration if the following
configuration expression evaluates to TRUE
(Vc_Pem_Alc_B_CodegenFastCat == 1) OR (Vc_Pem_Alc_B_CodegenDpfRegen == 1)

### description

A string describing the variable/parameter.

### type

The data type of the signal. Valid types are UInt8, UInt16, UInt32, Int8, Int16, Int32, Bool and Float32.

### unit

The name if the unit of the variable/parameter.

### offset

The offset used to convert the variable value from HEX to Physical.

### lsb

The value of a bit (lsb - least significant bit)
The factor used to convert the variable value from HEX to Physical.

### min

The minimum value of the variable.

### max

The maximum value of the variable.

### class

The storage class of the variable. I.e. which type of memory the variable/parameter is assigned to.

### core

The units core ids have the following different types - Events, IUMPR, FIDs, TestID and Ranking (which is not a part of the core, but is included here for simplicity)

TODO: Remove some of the keys for the Core Identifiers. subsystem, type, unit, offset, lsb, min, max, class is not needed for these blocks.

```json
{
    "Events": {
        "NameOfId": {
            "API_blk": [
            {
                "path": "VcPpmImob/VcPpmImob/Subsystem/VcPpmImob/VcPpmImob/1000_ImobConnectionLayer/1600_Diag/1620_CoreIfNew/Dem_SetEventStatusPF1",
                "config": ["Vc_NewDiagnosticCoreIF == 1"]},
            {
                "path": "VcPpmImob/VcPpmImob/Subsystem/VcPpmImob/VcPpmImob/1000_ImobConnectionLayer/1600_Diag/1620_CoreIfNew/Dem_SetEventStatusPP1",
                "config": ["Vc_NewDiagnosticCoreIF == 1"]}],
            "blk_name": "NamedConstant1",
            "subsystem": "VcPpmImob/VcPpmImob/Subsystem/VcPpmImob/VcPpmImob/1000_ImobConnectionLayer/1600_Diag/1620_CoreIfNew",
            "API_blk_type": "Dem_SetEventStatus Pre-Passed",
            "description": "",
            "type": "",
            "unit": "",
            "offset": "",
            "lsb": "",
            "min": "",
            "max": "",
            "class": ""
        }
    }
}
```

The first key under the ID-type key, is the name of the ID. The value of that
key is a dict with the following keys:

### API_blk

The value of this key is a list of dicts, these dicts defines the path to all
the instances where this ID is used in the model, and in which configurations
the ID is active

### API_blk_type

The value of this key is a string, which defines the type of API block that is
used for this Id

### blk_name

The value of this key is a string, which defines the name of the block in simulink

### dids

The dids defined in the unit

### pre_procs

Contains a list of strings, which defines the preprocessor names used in the
unit for configuration
