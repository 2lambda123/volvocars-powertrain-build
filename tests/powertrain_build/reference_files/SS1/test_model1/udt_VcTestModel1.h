/**************************************************************************************************\
 *** 
 *** Simulink model       : VcTestModel1_OPortMvd
 *** TargetLink subsystem : VcTestModel1_OPortMvd/VcTestModel1
 *** Codefile             : udt_VcTestModel1.h
 ***
 *** Generation date: 2020-11-17 14:35:15
 ***
 *** TargetLink version      : 4.3p3 from 16-Oct-2018
 *** Code generator version  : Build Id 4.3.0.27 from 2018-09-24 17:55:03
\**************************************************************************************************/

#ifndef UDT_VcTestModel1_H
#define UDT_VcTestModel1_H

#include "tl_basetypes.h"


struct sVcTestModel_Bus_Dummy {
   Float32 sVcTestModel_D_One;
   Bool yVcTestModel_B_One;
}; /* Description: bus inport struct */

typedef enum EnumTest_tag {
   ENUMTEST_CLIMAOFF = 0, 
   ENUMTEST_CLIMAHEATGTOHVACANDHVBATT = 1, 
   ENUMTEST_CLIMAHEATGTOHVBATT = 2, 
   ENUMTEST_CLIMAHEATGTOHVAC = 3, 
   ENUMTEST_CLIMAFLOW = 4, 
   ENUMTEST_DEGAS = 5, 
   ENUMTEST_FAILSAFE = 6 
} EnumTest; /* Description: Enumeration type derived from Simulink type EnumTest */

typedef enum EnumTestTwo_tag {
   ENUMTESTTWO_COOLGREQ = 0, 
   ENUMTESTTWO_HEATGREQ = 1 
} EnumTestTwo; /* Description: Enumeration type derived from Simulink type EnumTestTwo */

#endif /* UDT_VcTestModel1_H */
/*------------------------------------------------------------------------------------------------*\
  END OF FILE
\*------------------------------------------------------------------------------------------------*/

