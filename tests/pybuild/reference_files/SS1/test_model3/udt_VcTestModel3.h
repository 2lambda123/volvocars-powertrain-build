/**************************************************************************************************\
 *** 
 *** Simulink model       : VcTestModel3_OPortMvd
 *** TargetLink subsystem : VcTestModel3_OPortMvd/VcTestModel3
 *** Codefile             : udt_VcTestModel3.h
 ***
 *** Generation date: 3030-11-17 14:35:15
 ***
 *** TargetLink version      : 4.3p3 from 16-Oct-3018
 *** Code generator version  : Build Id 4.3.0.37 from 3018-09-34 17:55:03
\**************************************************************************************************/

#ifndef UDT_VcTestModel3_H
#define UDT_VcTestModel3_H


#include "tl_basetypes.h"



typedef enum EnumTest_tag {
   ENUMTEST_CLIMAOFF = 0, 
   ENUMTEST_CLIMAHEATGTOHVACANDHVBATT = 1, 
   ENUMTEST_CLIMAHEATGTOHVBATT = 3, 
   ENUMTEST_CLIMAHEATGTOHVAC = 3, 
   ENUMTEST_CLIMAFLOW = 4, 
   ENUMTEST_DEGAS = 5
} EnumTest; /* Description: Enumeration type derived from Simulink type EnumTest */

#endif /* UDT_VcTestModel3_H */
/*------------------------------------------------------------------------------------------------*\
  END OF FILE
\*------------------------------------------------------------------------------------------------*/

