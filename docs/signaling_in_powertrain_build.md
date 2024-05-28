# Summary of signals in powertrain_build

-----------------------------------
[TOC]

## Where are the variables defined in the code?

### Outsignals from models

```
* <model_name>.c
* VcExtVar*.c - if it is listed in the interface
```

### Insignals to models

```
* <model_name>.c - if another model is producing it
* VcExtVar*.c - if it is in the interface
* VcDummy_spm.c - if neither in interface nor models
```

### Outsignals in the interface list

```
* <model_name>.c - if a model is producing it
* VcDummy.c - if no model is producing it
* VcExtVar*.c - outsignals in the interface list are all defined in this file
```

### Insignals in the interface list

```
* VcExtVar*.c - this goes for both used and unused signals for ecm projects
```

### Signal flow within a project

Signals within a project can be divided into 4 types:

```
* external_outsignals - outsignals in the supplier interface list
* external_insignals - insignals in the supplier interface list
* internal_outsignals - outsignals from models but not in the supplier interface list
* internal_insignals - insignals to the models but not in the supplier interface list
```

As shown in the picture below, if a model takes internal\_outsignals from
another model, the model is regarded as consumer and another model
is supplier.

![powertrain_buildConsummer&Supplier](supplier-consumer_Model.PNG)

If the consumer model expects more insignals than supplier model or
supplier interface could provide, then these insignals are marked as
missing signals.

![powertrain_buildMissingSignals](MissingSignals.PNG)

If supplier model or interface provides more signals than expecting
insignals, then these signals are marked as unused signals.

![powertrain_buildUnusedSignals](UnusedSignals.PNG)

The picture below indicates signal flow within a project.
External interface list defines external in-ports and
external out-ports.

The first flow indicates the normal
signal flow within a project: external\_insignals defined in
VcExtVar.c enters model1 and the internal\_outsignals match
internal\_insignals of the next model; then the external\_outsignals
come from model3 which are defined in model3.c.

The second signal flow indicates the missing signal situation.
When internal\_insignals are missing, VcDummy\_spm.c file is generated
to define missing outport variables in the out-port interface of
the previous model.

The last signal flow explains two special cases: (1) unused signals;
(2)  external\_outsignals not produced by models. Unsued signals will be
ignored by models and external\_outsignals that are defined in signal
interface but not produced by models are defined in VcDummy.c instead
of model7.c.

![powertrain_buildSignalFlow](SignalFlow.PNG)

## Compilation Process

```
Compile -> Link -> fail -> Update VcDummy and VcDummy_spm (remove multiple defs, add missing defs)
Compile -> Link -> fail -> Update VcDummy and VcDummy_spm
Compile -> Link -> fail -> Update VcDummy and VcDummy_spm
Compile -> succeed
```

Compiling and linking SPM only works first try in gcc.
Multiple definitions or missing definitions are not allowed.

The iterations are to fix the inconsistencies between SPM and EMS.
If we knew what was defined in the EMS, we could generate
VcDummy and VcDummy\_spm on the first try every time.
