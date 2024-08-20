/**************************************************************************************************\
 *** 
 *** Simulink model       : VcTestModel2_OPortMvd
 *** TargetLink subsystem : VcTestModel2_OPortMvd/VcTestModel2
 *** Codefile             : udt_VcTestModel2.h
 ***
 *** Generation date: 2020-11-17 14:35:15
 ***
 *** TargetLink version      : 4.3p3 from 16-Oct-2018
 *** Code generator version  : Build Id 4.3.0.27 from 2018-09-24 17:55:03
\**************************************************************************************************/

#ifndef UDT_VcTestModel2_H
#define UDT_VcTestModel2_H

#include "tl_basetypes.h"

struct sVcTestModel_Bus_Dummy {
   Float32 sVcTestModel_D_One;
   UInt8 yVcTestModel_B_One;
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

typedef enum EnumTest_tag {
   ENUMTESTTWO_COOLGREQ = 0, 
   ENUMTESTTWO_HEATGREQ = 1 
} EnumTest; /* Description: Enumeration type derived from Simulink type EnumTest */

typedef enum EnumTestThree_tag {
   ENUMTESTTHREE_DTELECCOOLG = 0, 
   ENUMTESTTHREE_DTELECPASCOOLG = 1, 
   ENUMTESTTHREE_DTELECHEATG = 2, 
   ENUMTESTTHREE_DTELECPASHEATG = 3, 
   ENUMTESTTHREE_DTELECACTVHEATG = 4, 
   ENUMTESTTHREE_DTELECPASACTVHEATG = 5, 
   ENUMTESTTHREE_DTELECPAS = 6, 
   ENUMTESTTHREE_DEGAS = 7, 
   ENUMTESTTHREE_FAILSAFE = 8,
   ENUMTESTTHREE_EXTRAVERSUSUNITONE = 9
} EnumTestThree; /* Description: Enumeration type derived from Simulink type EnumTestThree */

#endif /* UDT_VcTestModel2_H */
/*------------------------------------------------------------------------------------------------*\
  END OF FILE
\*------------------------------------------------------------------------------------------------*/

