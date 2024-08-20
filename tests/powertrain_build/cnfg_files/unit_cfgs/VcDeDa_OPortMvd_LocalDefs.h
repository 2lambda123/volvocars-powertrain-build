#include "VcCodeSwDefines.h"

#if (((Vc_Pvc_Hw_B_Erad==0)&&(Vc_Pvc_Hw_B_Efad==0)&&((Vc_Pvc_Hw_B_VeaGen1==1)||(Vc_Pvc_Hw_B_VeaGen2==1)||(Vc_Pvc_Hw_B_VeaGen3==1)||(Vc_Pvc_Hw_B_Gep3Gen1==1))))
   #define VcDeDa_111_EcoIndcn_1
#endif

#if (((Vc_Pvc_Hw_B_Bev==1)||((Vc_Pvc_Hw_B_Erad==0)&&(Vc_Pvc_Hw_B_Efad==0)&&(Vc_Pvc_Hw_B_VeaGen1==0)&&(Vc_Pvc_Hw_B_VeaGen2==0)&&(Vc_Pvc_Hw_B_Gep3Gen1==0))))
   #define VcDeDa_112_PwrIndcn_2
#endif

#define Vc_Pvc_Hw_B_Efad_CN (Vc_Pvc_Hw_B_Efad)
#define Vc_Pvc_Hw_B_Erad_CN (Vc_Pvc_Hw_B_Erad)
#define Vc_Pvc_Hw_B_Isg_CN (Vc_Pvc_Hw_B_Isg)
