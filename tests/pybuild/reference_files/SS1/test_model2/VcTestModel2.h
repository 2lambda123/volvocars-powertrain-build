/**************************************************************************************************\
 *** 
 *** Simulink model       : VcTestModel2_OPortMvd
 *** TargetLink subsystem : VcTestModel2_OPortMvd/VcTestModel2
 *** Codefile             : VcTestModel2.h
 ***
 *** Generated by TargetLink, the dSPACE production quality code generator
 ***
 *** TargetLink version      : 4.3p3 from 16-Oct-2018
 *** Code generator version  : Build Id 4.3.0.27 from 2018-09-24 17:55:03
\**************************************************************************************************/

#ifndef VCTESTMODEL2_H
#define VCTESTMODEL2_H

/*------------------------------------------------------------------------------------------------*\
  DEFINES (OPT)
\*------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------------------------------------------*\
  INCLUDES
\*------------------------------------------------------------------------------------------------*/

#include "tl_defines_TestModel2.h"
#include "tl_basetypes.h"
#include "udt_VcTestModel2.h"

/*------------------------------------------------------------------------------------------------*\
  ENUMS
\*------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------------------------------------------*\
  DEFINES
\*------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------------------------------------------*\
  TYPEDEFS
\*------------------------------------------------------------------------------------------------*/

struct sVcTestModel2_Bus_Dummy {
   Float32 sVcTestModel2_D_One;
   Bool yVcTestModel2_B_One;
}; /* Description: bus outport struct */

struct sVcTestModel2_Bus_Dummy {
   Float32 sVcTestModel2_D_One;
   UInt8 yVcTestModel2_B_One;
}; /* Description: bus outport struct */

/*------------------------------------------------------------------------------------------------*\
  VARIABLES
\*------------------------------------------------------------------------------------------------*/

#include "PREDECL_CAL_START.h"
/**************************************************************************************************\
   CVC_CAL: CVC calibration constants in FLASH | Width: 32
\**************************************************************************************************/
extern CVC_CAL UInt8 cVcDummy_D_CalDummyOne32; /* 
   Unit: -
   LSB: 2^0 OFF: 0 MIN/MAX: 0 .. 255
   Description: Debug switch for profile manager value for rear  air flow. */
#include "PREDECL_CAL_END.h"

#include "PREDECL_DISP_START.h"
/**************************************************************************************************\
   CVC_DISP: CVC global observable variables in RAM | Width: 32
\**************************************************************************************************/
extern CVC_DISP Float32 sVcDummy_D_DispDummyOne32;

/**************************************************************************************************\
   CVC_DISP: CVC global observable variables in RAM | Width: 8
\**************************************************************************************************/
extern CVC_DISP Int8 sVcDummy_D_DispDummyOne8;

/**************************************************************************************************\
   CVC_DISP: CVC global observable variables in RAM | Width: N.A.
\**************************************************************************************************/
extern CVC_DISP struct sVcTestModel2_Bus_Dummy
    sVcTestModel2_Bus_Dummy;
#include "PREDECL_DISP_END.h"

#include "PREDECL_START.h"
/**************************************************************************************************\
   CVC_EXT: CVC external interface input variables | Width: 32
\**************************************************************************************************/
CVC_EXT Float32 sVcDummy_D_DummyOne; /* Description: Nvram temp stored Driver Temp setting.
   */
CVC_EXT Float32 sVcDummy_D_DummyTwo; /* 
   Unit: -
   Description: Driver Temperature Value Request */

/**************************************************************************************************\
   CVC_EXT: CVC external interface input variables | Width: N.A.
\**************************************************************************************************/
CVC_EXT struct sVc_Bus_Dummy sVc_Bus_Dummy; /* Description: Profil
   e manager settings */

#include "PREDECL_END.h"

/*------------------------------------------------------------------------------------------------*\
  PARAMETERIZED MACROS
\*------------------------------------------------------------------------------------------------*/
/*------------------------------------------------------------------------------------------------*\
  FUNCTION PROTOTYPES
\*------------------------------------------------------------------------------------------------*/

/**************************************************************************************************\
   GLOBAL_FCN: global function(s) (exported to other modules)
\**************************************************************************************************/
extern void RESTART_VcTestModel2(void);
extern void VcTestModel2(void);

#endif /* VCTESTMODEL2_H */
/*------------------------------------------------------------------------------------------------*\
  END OF FILE
\*------------------------------------------------------------------------------------------------*/

