

#ifndef VCVMCPMM_C
#define VCVMCPMM_C




#include "tl_aux_defines_VmcPmm__HE.h"
#include "VcVmcPmm__HEP7_OPortMvd_LocalDefs.h"
#include "VcVmcPmm.h"
#include "VcUnitTsDefines.h"
#include "TabIdxS18T6.h"
#include "TabIdxS18T390.h"
#include "Tab2DIntpI1T6.h"
#include "Tab1DIntpI1T6.h"
#include "Tab1DIntpI1T54.h"






#include "CVC_CODE_START.h"

static Float32 X_SVmcPmm__HE161_UnitDelay = 0.F;
static Float32 X_SVmcPmm__HE163_UnitDelay = 0.F;
static Float32 X_SVmcPmm__HE164_UnitDelay = 0.F;
static Float32 X_SVmcPmm__HE165_UnitDelay = 0.F;


static Bool X_SVmcPmm__HE159_UnitDelay1 = 0;
static Bool X_SVmcPmm__HE160_UnitDelay1 = 0;
#include "CVC_CODE_END.h"

#include "PREDECL_CAL_EXT_START.h"

CVC_CAL_EXT Bool cVc_B_SeriesHev; 
#include "PREDECL_CAL_EXT_END.h"

#include "CVC_CAL_START.h"


#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Float32 cVcVmcPmm_Pw_IsgStrtAllow = 4.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_Te_AbrtStallEngClntL = -10.F; 


#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_Te_AmbHighH = 25.F; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_Te_AmbHighL = 20.F; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_Te_AmbLowH = 2.F; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_Te_AmbLowL = 0.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_Te_EngClntEngOffReq = 10.F; 
CVC_CAL Float32 cVcVmcPmm_Te_EngClntEngRunReq = -4.5F; 
CVC_CAL Float32 cVcVmcPmm_Te_FCAdaptEngClntRst = 40.F; 
CVC_CAL Float32 cVcVmcPmm_Te_FCAdaptEngClntSet = 50.F; 


#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Float32 cVcVmcPmm_Te_IsgStartPossible = 0.F; 
#endif




#ifdef SVmcPmm__HE512_Switch_AUX
CVC_CAL Float32 cVcVmcPmm_Te_TrnMdeC3OilPresMax = 20.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Te_TrnOil = 0.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_Tq_CrShRampDown = 20.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_Tq_CrShRampUp = -20.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_Tq_DrCrShRampDown = 20.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_Tq_DrCrShRampUp = -20.F; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_ERADRampDown = 20.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_EfadBrkOKIsgBrk = 1000.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_EfadIsgStrtDi = 2.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_EfadIsgStrtDiFlt = 8.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_EfadIsgStrtEna = 1.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_EfadIsgStrtEnaFlt = 6.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_Tq_FastEngmtIsgStrtBrkTqMax = 1.F; 


#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_IsgRampDown = 10.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_IsgStandStillBrkTqOK = 1000.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_IsgStandStillBslTqOK = 1.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_IsgStopCoastDrReqMax = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_IsgStopCoastDrReqMin = 0.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_Tq_PropFrntRampDown = 100.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_Tq_PropFrntRampUp = -100.F; 
#endif




#ifdef SVmcPmm__HE821__ransHeatReq_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_TransHeatReqOffset = 10.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_Wait4CluStrtDi = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_Tq_Wait4CluStrtEna = 500.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_X_AccPedFastEngmtMin = 0.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_X_EfadAccPedOKIsgBrk = 1.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_X_FanAfterrunLimHi = 0.F; 
CVC_CAL Float32 cVcVmcPmm_X_FanAfterrunLimLo = 0.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_X_IsgStopRoadGradMax = 100.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_X_IsgStopRoadGradMaxHyst = 0.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_X_StallRcvClNtrl = 30.F; 
CVC_CAL Float32 cVcVmcPmm_X_StallRcvClOnly = 60.F; 
CVC_CAL Float32 cVcVmcPmm_X_StrtAbrtAcc = 10.F; 
CVC_CAL Float32 cVcVmcPmm_X_StrtAbrtCl = 50.F; 
CVC_CAL Float32 cVcVmcPmm_X_StrtMdeAcc = 110.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_X_Wait4CluStrtDi = 2.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_X_Wait4CluStrtEna = 5.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_Xd_AccPedFastEngmtMin = 30.F; 


#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Float32 cVcVmcPmm_Z_BrkHGSkipParkDownH = -16.F; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Float32 cVcVmcPmm_Z_BrkHGSkipParkDownL = -15.F; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Float32 cVcVmcPmm_Z_BrkHGSkipParkUpH = 16.F; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Float32 cVcVmcPmm_Z_BrkHGSkipParkUpL = 15.F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_Z_ResetLimDownHill = -7.F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_Z_ResetLimUpHill = 6.F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_Z_SetLimDownHill = -8.5F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_Z_SetLimUpHill = 9.F; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_Z_SsActTrailerUpHillH = -100.F; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_Z_SsActTrailerUpHillL = -100.F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_a_HillGradientFault = 0.F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_a_HillGradientMax = 4.F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_a_HillGradientMin = -4.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_a_Wait4CluStrtDi = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_a_Wait4CluStrtEna = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_n_12VStrtAllwdEngSpdMax = -10000.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_n_CFTStop = 300.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_n_CluStrtAllwdEngSpdMax = -10000.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_n_EngOnDelayOff = 10000.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_n_FCAdaptEngRst = 800.F; 
CVC_CAL Float32 cVcVmcPmm_n_FCAdaptEngSet = 1000.F; 
CVC_CAL Float32 cVcVmcPmm_n_IceStallMax = 10000.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_n_IsgStrtAllwdEngSpdMax = -10000.F; 
#endif




#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Float32 cVcVmcPmm_n_PwdRpmOnly = 100.F; 
#endif
CVC_CAL Float32 cVcVmcPmm_n_StallEmiMinEngSpd = 100.F; 
CVC_CAL Float32 cVcVmcPmm_n_StallRcv = 10000.F; 


#ifdef SVmcPmm__HE477_MinMax_AUX
CVC_CAL Float32 cVcVmcPmm_n_TrnEngBlockMin = 1000.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_n_Wait4Eng2StopLim = 450.F; 
CVC_CAL Float32 cVcVmcPmm_n_Wait4Eng2StopLimHigh = 500.F; 
CVC_CAL Float32 cVcVmcPmm_n_Wait4Eng2StopLimHighTest = -10000.F; 


#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_p_AmbH = 85.F; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_p_AmbL = 84.F; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Float32 cVcVmcPmm_p_BrVacuum = -4.5F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_rt_EfadLowAvailTrq = -1000.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_rt_EfadStrtAllow = 0.5F; 
#endif


CVC_CAL Float32 cVcVmcPmm_rt_FCLvlRunning = 0.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_12VStrtActrRdyDly = 0.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_ATComStrt = 0.1F; 
CVC_CAL Float32 cVcVmcPmm_t_AbrtFrstDrCycle = 5.F; 
CVC_CAL Float32 cVcVmcPmm_t_AbrtStall = 10.F; 
CVC_CAL Float32 cVcVmcPmm_t_AbsStrt = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_BlockAbrtFrstDrCycle = 0.F; 


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Float32 cVcVmcPmm_t_BlockPsmPwd = 0.F; 
#endif


#if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
CVC_CAL Float32 cVcVmcPmm_t_BrakeRunReqOnDelayHmi = 20.F; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Float32 cVcVmcPmm_t_BrkAbs = 4.F; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Float32 cVcVmcPmm_t_BrkEngRunReqAlive = 0.F; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Float32 cVcVmcPmm_t_BrkHillGrad = 10.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_BrkLimIsgStrtGearLvrDR = 0.5F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_BrkStrt = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_CTFStop = 0.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_CatHeatVehSpdOKIsgDrv = 5.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_ChrgReqDly = 0.06F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_CluStrtActrRdyDly = 0.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_ComInhbtIceStatus = 0.F; 


#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_t_CrShPahDiTiOut = 5.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_DrLeaveAutoParkReq = 30.F; 
CVC_CAL Float32 cVcVmcPmm_t_DrLeaveDCADly = 1.F; 
CVC_CAL Float32 cVcVmcPmm_t_DrLeavePwrDwnDly = 4800.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_DrvCycActvFirstStrt = 2.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadAccPedOKIsgBrk = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadBrkOKIsgBrk = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadDrvCycTiOut = 2.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadGearLvrPNDetn = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadIceStsDlyIsgDrv = 5.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadLowAvailTrqDly = 0.25F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadRunReqDelay = 2.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadShftProgsOffDly = 0.3F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadShftProgsTimeOut = 3.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadTrqAllowTiOut = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EfadVehSpdOKIsgBrk = 0.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_EngEngmtFastRstDelay = 1.F; 
CVC_CAL Float32 cVcVmcPmm_t_EngOff = 0.2F; 
CVC_CAL Float32 cVcVmcPmm_t_EngOffFcAdapt = 0.01F; 
CVC_CAL Float32 cVcVmcPmm_t_EngOffMax = 1000.F; 


#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_t_EngOnDelayOff = 2.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_EngOnOff = 4.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EngOnReqDly = 0.05F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EngRunReqIsgStopMax = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_EngRunReqIsgStopMin = 0.F; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Float32 cVcVmcPmm_t_EradDisable = 2.F; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Float32 cVcVmcPmm_t_EradNtrlGlitch = 0.5F; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Float32 cVcVmcPmm_t_EradOffGlitch = 0.F; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Float32 cVcVmcPmm_t_EradOnGlitch = 0.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_FCAdaptIdleDelayOff = 0.F; 


#if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
CVC_CAL Float32 cVcVmcPmm_t_FCAdaptRunReqOnDelayHmi = 0.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_FanAfterrunDelay = 0.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_FirstStrtDlyOff = 2.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_GearLevDRDly = 2.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_GearLevNDly = 2.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_t_GearLevPNDlyOn = 0.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_GlitchEngOnTrans = 0.5F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IceRunng12VStrt = 0.5F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IceRunngCluStrt = 0.5F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IceRunngIsgStrt = 0.5F; 
#endif




#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgAdapt = 0.1F; 
#endif




#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgDisable = 0.5F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgDrCycStop = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgDrCycStopMax = 0.F; 
#endif




#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgICEStop = 0.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_t_IsgIceStopACCTimeout = 1.5F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_t_IsgIceStopTimeout = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgPahDiTiOut = 5.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgStandStillBrkTqOK = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgStandStillBslTqOK = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgStandStillVehSpdOK = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgStrtActrRdyDly = 0.F; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgStrtOkDelay = 0.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_IsgStrtPahReqTiOut = 2.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_IsgStrtWhlTrqOK = 1.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_MinStopCEC = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_MinStopChas = 3.F; 
CVC_CAL Float32 cVcVmcPmm_t_MinStopClim = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_MinStopEMS = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_MinStopEmLv = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_MinStopTime = 0.2F; 
CVC_CAL Float32 cVcVmcPmm_t_MinStopTm = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_MinStopTrans = 0.F; 


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Float32 cVcVmcPmm_t_PwdRcShutOff = 0.F; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Float32 cVcVmcPmm_t_PwdRpm = 0.04F; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Float32 cVcVmcPmm_t_PwdSeatBeltAT = 100000.F; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Float32 cVcVmcPmm_t_PwdTcmModeFail = 4.F; 
#endif


#if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
CVC_CAL Float32 cVcVmcPmm_t_RunReqObdDelayHmi = 5.F; 
#endif




#if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
CVC_CAL Float32 cVcVmcPmm_t_RunReqOnDelayHmi = 2.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_Running = 0.5F; 


#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_t_SsActAbs = 4.F; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_t_SsActBrk = 0.F; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_t_SsActSeatBelt = 100000.F; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Float32 cVcVmcPmm_t_SsActTcmModeFail = 2.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_StallEmiMinEngSpd = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_StallIceStrt = 2.F; 
CVC_CAL Float32 cVcVmcPmm_t_StallIceStrtActrFinishd = 0.5F; 
CVC_CAL Float32 cVcVmcPmm_t_StallIceStrtEmi = 40.F; 
CVC_CAL Float32 cVcVmcPmm_t_StallIceStrtEmiExtra = 2.F; 
CVC_CAL Float32 cVcVmcPmm_t_StallIceStrtIsgDrv = 4.F; 
CVC_CAL Float32 cVcVmcPmm_t_StallRcvClDelay = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_StallRcvNeutral = 0.1F; 
CVC_CAL Float32 cVcVmcPmm_t_StallRun = 0.5F; 
CVC_CAL Float32 cVcVmcPmm_t_StallRunComInhbt = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_StallRunUnintd = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_StallStrtM = 1.5F; 


#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_t_StandStill = 0.7F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_Started = 0.04F; 
CVC_CAL Float32 cVcVmcPmm_t_StrtAbrt = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_StrtMdeAccRst = 1.F; 
CVC_CAL Float32 cVcVmcPmm_t_StrtMdeAccRun = 0.F; 
CVC_CAL Float32 cVcVmcPmm_t_StrtMdeRunning = 0.F; 


#ifdef SVmcPmm__HE821__ransHeatReq_AUX
CVC_CAL Float32 cVcVmcPmm_t_TransHeatDelayOn = 2.F; 
#endif




#if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
CVC_CAL Float32 cVcVmcPmm_t_TransRunReqOnDelayHmi = 1.F; 
#endif




#ifdef SVmcPmm__HE477_MinMax_AUX
CVC_CAL Float32 cVcVmcPmm_t_TrnEngBlockMax = 1.F; 
#endif




#ifdef SVmcPmm__HE477_MinMax_AUX
CVC_CAL Float32 cVcVmcPmm_t_TrnEngCatHeatDly = 5.F; 
#endif




#ifdef SVmcPmm__HE477_MinMax_AUX
CVC_CAL Float32 cVcVmcPmm_t_TrnEngRpmDly = 0.F; 
#endif




#ifdef SVmcPmm__HE512_Switch_AUX
CVC_CAL Float32 cVcVmcPmm_t_TrnMdeC3OilPresMax = 25.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_VehSpdLimIsgStrtGearLvrDR = 0.5F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_VehSpdOKIsgDrv = 0.5F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_t_Wait4CluStrtTiOut = 10.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_t_Wait4Eng2StopTiOut = 2.F; 
CVC_CAL Float32 cVcVmcPmm_t_Wait4EngRunReqTot = 0.02F; 
CVC_CAL Float32 cVcVmcPmm_t_WaitToReset = 2.F; 
CVC_CAL Float32 cVcVmcPmm_tc_AccPedDer = 0.1F; 


#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_tc_BcmLongAccFilt = 0.5F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_tc_BrkTrqFilt = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_tc_LatAccFilt = 0.F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_tc_StandStill = 0.1F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_tc_VdmAccFilt = 0.F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_tc_VehAccFilt = 0.3F; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Float32 cVcVmcPmm_v_12VStrtMax = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_CluStrtSpdAllw = 70.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_v_DrLeaveLim = 5.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadCluStrtDi = 8.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadCluStrtEna = 10.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadGearLvrPNDiseng = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadVehSpdNOKIsgBrk = 1.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadVehSpdNOKIsgDrv = 5.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadVehSpdNOKIsgDrvHybridEco = 5.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadVehSpdNOKPrioIsgDrv = 8.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadVehSpdNOKPrioIsgDrvHybridEco = 8.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadVehSpdOKIsgBrk = 0.1F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadVehSpdOKIsgDrv = 0.1F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadVehSpdOKIsgDrvHybridEco = 0.1F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadVehSpdOKPrioIsgDrv = 4.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_EfadVehSpdOKPrioIsgDrvHybridEco = 4.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_v_EngStopReqAT = 350.F; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Float32 cVcVmcPmm_v_EradOffSpdLim = 140.F; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Float32 cVcVmcPmm_v_EradOnSpdLim = 130.F; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Float32 cVcVmcPmm_v_EradSpdCtrl = 255.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_v_FCAdaptVehRst = 35.F; 
CVC_CAL Float32 cVcVmcPmm_v_FCAdaptVehSet = 40.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_IsgStandStillVehSpdOK = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_IsgStopCoastSpdMax = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_IsgStopCoastSpdMinOff = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_IsgStopCoastSpdMinOn = 0.F; 
#endif




#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Float32 cVcVmcPmm_v_PwdSpeedLimit = 10.F; 
#endif


#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_v_ReqEngDrDir = -1.F; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_v_SpeedLimitHG = 2.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_v_StallRcvStart = 5.F; 
CVC_CAL Float32 cVcVmcPmm_v_StallReset = -2.F; 


#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 cVcVmcPmm_v_StandStillLoLim = 2.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_v_TotNtrlReset = 18.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_v_TotNtrlSet = 25.F; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Float32 cVcVmcPmm_v_TotNtrlVehDrDir = -1.F; 
#endif




#if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
CVC_CAL Float32 cVcVmcPmm_v_TransRunRqDlyMaxHmi = 125.F; 
#endif




#ifdef SVmcPmm__HE477_MinMax_AUX
CVC_CAL Float32 cVcVmcPmm_v_TrnEngBlockMax = 5.F; 
#endif




#ifdef SVmcPmm__HE512_Switch_AUX
CVC_CAL Float32 cVcVmcPmm_v_TrnMdeC3OilPresMax = 20.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_v_VehMaxStallRcv = 10.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 cVcVmcPmm_v_VehSpdLimIsgStrtGearLvrDR = -1000.F; 
#endif


CVC_CAL Float32 cVcVmcPmm_v_WaitToReset = 350.F; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 mVcVmcPmm_Z_BrkRoadIncline_c[8] = 
{
    1.F, 2.F, 3.F, 4.F, 5.F, 6.F, 7.F, 8.F
   
}; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Float32 mVcVmcPmm_Z_BrkRoadIncline_r[8] = 
{
    1.F, 2.F, 3.F, 4.F, 5.F, 6.F, 7.F, 8.F
   
}; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 mVcVmcPmm_tc_HillGradient[6][4] = 
{
   {
       1.F, 2.F, 4.F, 4.F
      
   },
   {
       1.F, 2.F, 4.F, 4.F
      
   },
   {
       1.F, 2.F, 4.F, 4.F
      
   },
   {
       1.F, 2.F, 4.F, 4.F
      
   },
   {
       1.F, 2.F, 4.F, 4.F
      
   },
   {
       1.F, 2.F, 4.F, 4.F
      
   }
}; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 mVcVmcPmm_tc_HillGradient_c[4] = 
{
    0.F, 500.F, 1000.F, 2000.F
   
}; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 mVcVmcPmm_tc_HillGradient_r[6] = 
{
    0.F, 2.F, 5.F, 10.F, 50.F, 100.F
   
}; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Float32 tVcVmcPmm_Tq_IsgStrtAllow[6] = 
{
    50.F, 50.F, 50.F, 0.F, 0.F, 0.F
   
}; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Float32 tVcVmcPmm_Tq_IsgStrtAllow_x[6] = 
{
    500.F, 1000.F, 1500.F, 2500.F, 3500.F, 5000.F
   
}; 
#endif




#ifdef SVmcPmm__HE821__ransHeatReq_AUX
CVC_CAL Float32 tVcVmcPmm_Tq_TransHeatReq[6] = 
{
    600.F, 600.F, 500.F, 325.F, 250.F, 200.F
   
}; 
#endif




#ifdef SVmcPmm__HE821__ransHeatReq_AUX
CVC_CAL Float32 tVcVmcPmm_Tq_TransHeatReq_x[6] = 
{
    0.F, 50.F, 55.F, 80.F, 110.F, 140.F
   
}; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 tVcVmcPmm_Z_HillGradAcc2deg[5] = 
{
    -90.F, -45.F, 0.F, 45.F, 90.F
   
}; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Float32 tVcVmcPmm_Z_HillGradAcc2deg_x[5] = 
{
    -9.81F, -4.9F, 0.F, 4.9F, 9.81F
   
}; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Float32 tVcVmcPmm_p_BrVacuumVeh[7] = 
{
    -45.F, -50.F, -55.F, -60.F, -65.F, -70.F, -90.F
   
}; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Float32 tVcVmcPmm_p_BrVacuumVeh_x[7] = 
{
    0.F, 15.F, 30.F, 45.F, 60.F, 75.F, 300.F
   
}; 
#endif





#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Bool cVcVmcPmm_B_12VStartEnable_dbi = 0; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Bool cVcVmcPmm_B_12VStartEnable_swi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_12VStrtBlk_dbi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_12VStrtBlk_swi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_12VStrtReq_dbi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_12VStrtReq_swi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_12VStrtTrigNewPos = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_ATComStrt = 1; 
CVC_CAL Bool cVcVmcPmm_B_AbrtFrstStrtStall = 0; 
CVC_CAL Bool cVcVmcPmm_B_AbrtNtrlAdapt = 1; 
CVC_CAL Bool cVcVmcPmm_B_AbrtStallAbortHard = 1; 
CVC_CAL Bool cVcVmcPmm_B_AbrtStallEngClntL = 0; 
CVC_CAL Bool cVcVmcPmm_B_AbrtStallGp = 0; 
CVC_CAL Bool cVcVmcPmm_B_AbrtStallMicHev = 1; 
CVC_CAL Bool cVcVmcPmm_B_AbrtStallRcShutOff = 0; 
CVC_CAL Bool cVcVmcPmm_B_AbrtStallRcvInSpd = 1; 
CVC_CAL Bool cVcVmcPmm_B_AbrtStallSeatBelt = 1; 
CVC_CAL Bool cVcVmcPmm_B_AbrtStallSsRcfSet = 1; 
CVC_CAL Bool cVcVmcPmm_B_AbrtStallTime = 1; 
CVC_CAL Bool cVcVmcPmm_B_AbsStrt = 0; 


#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Bool cVcVmcPmm_B_BrkAbs = 1; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Bool cVcVmcPmm_B_BrkEngRunReq = 0; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Bool cVcVmcPmm_B_BrkEngRunReqAlive = 0; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Bool cVcVmcPmm_B_BrkHGSkipPark = 0; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Bool cVcVmcPmm_B_BrkHillGrad = 0; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Bool cVcVmcPmm_B_BrkHillGradStart = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_BrkStrt = 0; 


#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Bool cVcVmcPmm_B_BrkUseNegVacuum = 0; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Bool cVcVmcPmm_B_BrkVacuum = 1; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL Bool cVcVmcPmm_B_BrkVacuumVeh = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_CTFStart = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_CluStrtBlk_dbi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_CluStrtBlk_swi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_CluStrtInDeplBlk = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_CluStrtReq_dbi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_CluStrtReq_swi = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_CrShPathEnable_dbi = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_CrShPathEnable_swi = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_CrShaftRampDownIgnore = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_DepStop = 1; 


#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_DepStopAT = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_DepStrt = 1; 
CVC_CAL Bool cVcVmcPmm_B_DrLeaveEnable = 0; 
CVC_CAL Bool cVcVmcPmm_B_DrLeaveKeepRunReq = 1; 
CVC_CAL Bool cVcVmcPmm_B_DrLeavePowerDown = 1; 


#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Bool cVcVmcPmm_B_ERADTqAllw = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_Efad12VStrtEnblIngoreDep = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_EfadGearLvrPNDisengEna = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_EfadPathEnaParkEngd = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_EfadPathEnable_dbi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_EfadPathEnable_swi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_EfadUse12VStrt = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_EfadUseCluStrt = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_EfadUseIsgStrt = 1; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_EngOnDelayIgnore = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_EngOnReq_dbi = 0; 
CVC_CAL Bool cVcVmcPmm_B_EngOnReq_swi = 0; 
CVC_CAL Bool cVcVmcPmm_B_EngRunReqTot_dbi = 0; 
CVC_CAL Bool cVcVmcPmm_B_EngRunReqTot_swi = 0; 
CVC_CAL Bool cVcVmcPmm_B_EngStoppedUseHiRes = 0; 
CVC_CAL Bool cVcVmcPmm_B_EngineArchitecture = 1; 


#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Bool cVcVmcPmm_B_EradIgnrPathDisable = 1; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Bool cVcVmcPmm_B_EradPathEnable_dbi = 0; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Bool cVcVmcPmm_B_EradPathEnable_swi = 0; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Bool cVcVmcPmm_B_EradRmpDwnTqSignal = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_FCAdaptEnable = 0; 
CVC_CAL Bool cVcVmcPmm_B_FCAdaptIdle = 1; 
CVC_CAL Bool cVcVmcPmm_B_FastEngmtIsgStrtUseStartReq = 0; 
CVC_CAL Bool cVcVmcPmm_B_GlitchEngOnTrans = 0; 


#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_CAL Bool cVcVmcPmm_B_ISGTqAllw = 1; 
#endif




#if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
CVC_CAL Bool cVcVmcPmm_B_IgnoreGearLevRespStrt = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_IgnrCcActive = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IgnrDepl = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IgnrPropAlwdEfad = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IgnrPropAlwdIsg = 1; 
#endif




#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgIgnrPathDisable = 1; 
#endif




#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgRmpDwnTqSignal = 0; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStartEnable_dbi = 0; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStartEnable_swi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStopRunReqCluStrtBlkEna = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStopRunReqIgnrEfadPathAct = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtBlk_dbi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtBlk_swi = 0; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtFirstStartOverride = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtGearLvrDRAbortEna = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtInDUseEfadPathAct = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtPahReq_dbi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtPahReq_swi = 0; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtPcrOverride = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtReq_dbi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtReq_swi = 0; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtRunDryOverride = 0; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtSpdCtrlOverride = 0; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtTempOverride = 0; 
#endif




#ifdef SVmcPmm__HE818_Switch_AUX
CVC_CAL Bool cVcVmcPmm_B_IsgStrtUseSpdCtrl = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_LosStop = 0; 
CVC_CAL Bool cVcVmcPmm_B_LosStrt = 0; 
CVC_CAL Bool cVcVmcPmm_B_MinStopCEC = 0; 
CVC_CAL Bool cVcVmcPmm_B_MinStopChas = 1; 
CVC_CAL Bool cVcVmcPmm_B_MinStopClim = 0; 
CVC_CAL Bool cVcVmcPmm_B_MinStopEMS = 0; 
CVC_CAL Bool cVcVmcPmm_B_MinStopEmLv = 0; 
CVC_CAL Bool cVcVmcPmm_B_MinStopTm = 0; 
CVC_CAL Bool cVcVmcPmm_B_MinStopTrans = 0; 
CVC_CAL Bool cVcVmcPmm_B_PTDGearLevAT = 1; 
CVC_CAL Bool cVcVmcPmm_B_PTDStrt = 0; 


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdAbortHard = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdAbrtStall = 1; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdDrReadyAbortHard = 1; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdIgnoreQfDrDoor = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdRcShutOff = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdRcShutOffDCA = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdRcfDep = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdRpmOnly = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdSeatBelt = 1; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdSeatBeltDoor = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdSeatBeltN = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdSeatBeltP = 1; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdSpeedLimit = 1; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdTCMModeFail = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdTCMNodeAlive = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdTransFailure = 0; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_PwdUseSeatBeltAT = 1; 
#endif
CVC_CAL Bool cVcVmcPmm_B_RcShutOff = 0; 


#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_CAL Bool cVcVmcPmm_B_SerialModeSafeBISG = 0; 
#endif




#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_CAL Bool cVcVmcPmm_B_SkipIsgCalibration = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActAbs = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActAmbPres = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActBrk = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActDoorBeltD = 1; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActDoorBeltN = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActDoorBeltP = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActDoorBeltR = 1; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActDoorNoBelt = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActDrMdInv = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActDriverLeaving = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActEcoMde = 1; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActGpSs = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActHood = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActNtrl = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActRcfSet = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActRcfSetAlt = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActSeatBelt = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActSeatBeltNoSeq = 1; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActSeatBeltPrkBlock = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActTCMModeFail = 1; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActTCMNodeAlive = 1; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActTemp = 1; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActTempStrt = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActTipSport = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActTrailer = 1; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_SsActTransFailure = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_StallEmiExtraCond = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallIceStrt = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallIceStrtActrFinishd = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallIceStrtEmi = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallRcShutOff = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallRcvAT = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallRcvAccFtOnPed = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallRcvClOnly = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallRcvCrnk = 1; 
CVC_CAL Bool cVcVmcPmm_B_StallRcvFootOnBrPed = 1; 
CVC_CAL Bool cVcVmcPmm_B_StallRcvFrcd = 1; 
CVC_CAL Bool cVcVmcPmm_B_StallRun = 1; 
CVC_CAL Bool cVcVmcPmm_B_StallRunComInhbt = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallRunHiRes = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallRunStartM = 1; 
CVC_CAL Bool cVcVmcPmm_B_StallRunUnintd = 0; 
CVC_CAL Bool cVcVmcPmm_B_StallStartM = 1; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbortClu = 0; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbortHard = 1; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbortIsg = 0; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbortSoft = 0; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbrt = 0; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbrtAcc = 1; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbrtCl = 1; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbrtDrReady = 1; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbrtIce = 1; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbrtNtrl = 1; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbrtNtrlValid = 1; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbrtRpm = 1; 
CVC_CAL Bool cVcVmcPmm_B_StrtAbrtStrtM = 1; 
CVC_CAL Bool cVcVmcPmm_B_StrtMdeSet = 0; 


#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_CAL Bool cVcVmcPmm_B_StrtMdeSkipTrnMde = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_StrtMdeStopTrig = 0; 


#ifdef SVmcPmm__HE477_MinMax_AUX
CVC_CAL Bool cVcVmcPmm_B_TrnEngBlockSkipEngUseReq = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_TrnMdeHev = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_TrnMdeHevUseNIC = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_TrnMdeIC = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_TrnMdeReqBrk = 0; 
#endif




#ifdef SVmcPmm__HE477_MinMax_AUX
CVC_CAL Bool cVcVmcPmm_B_TrnMdeUseAwd = 1; 
#endif




#ifdef SVmcPmm__HE477_MinMax_AUX
CVC_CAL Bool cVcVmcPmm_B_TrnMdeUseBrake = 1; 
#endif




#ifdef SVmcPmm__HE512_Switch_AUX
CVC_CAL Bool cVcVmcPmm_B_TrnMdeUseC3OilPres = 0; 
#endif




#ifdef SVmcPmm__HE477_MinMax_AUX
CVC_CAL Bool cVcVmcPmm_B_TrnMdeUsePcr = 1; 
#endif




#ifdef SVmcPmm__HE477_MinMax_AUX
CVC_CAL Bool cVcVmcPmm_B_TrnMdeUseTrans = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_TrnModIsgReq = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UnintdStallRcShOff = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_Use12vStrtPsblInCluStrtAbort = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseAgedFuel = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseAwdRoadGrad = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseBrake = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseCEC = 1; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseChargeInIsgReq = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseChas = 1; 
CVC_CAL Bool cVcVmcPmm_B_UseClPedAdaptStrtAbrt = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseClim = 1; 
CVC_CAL Bool cVcVmcPmm_B_UseComInhbtIceStatus = 0; 


#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Bool cVcVmcPmm_B_UseDefHGDynoMd = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseDep = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseDesDrvDir = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseDly12VStrtVehPwrUp = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseDrLeave = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseDriver = 1; 
CVC_CAL Bool cVcVmcPmm_B_UseEMS = 1; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseEfadCode = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseEm = 1; 
CVC_CAL Bool cVcVmcPmm_B_UseEmLv = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseEmiGpfFC = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseEngClntRunReq = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseEngOffMaxTime = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseEngOnOff = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseEngOnReqDly = 0; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Bool cVcVmcPmm_B_UseEradCode = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_UseEradHybrid = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseFCAdapt = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseFanAfterrun = 1; 


#if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
CVC_CAL Bool cVcVmcPmm_B_UseFirstStartMode = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseIceEnable = 1; 
CVC_CAL Bool cVcVmcPmm_B_UseIceStall = 1; 
CVC_CAL Bool cVcVmcPmm_B_UseIscActvnEMS = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseIsg = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseIsgBrk = 0; 
#endif




#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_CAL Bool cVcVmcPmm_B_UseIsgCode = 0; 
#endif




#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_CAL Bool cVcVmcPmm_B_UseIsgSpdCtrlStrt = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseIsgStandStill = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseIsgStopCoast = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseIsgStopPostRunReqStandstill = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseIsgStopPwrDwn = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseIsgStopRunReqCoast = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseIsgStopRunReqStandstill = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseIsgStrtAtStndStill = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseLOS = 0; 


#if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
CVC_CAL Bool cVcVmcPmm_B_UseLastStrtMod = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseObd = 0; 


#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_CAL Bool cVcVmcPmm_B_UseOilTemp = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseOld12VStrtAllwd = 1; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_UseOldEngRevStgy = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseOldEngStrtAllwd = 1; 


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_CAL Bool cVcVmcPmm_B_UsePowerDownReq = 0; 
#endif


#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_B_UsePropFrntRampDown = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UsePsm = 1; 
CVC_CAL Bool cVcVmcPmm_B_UseRc = 1; 
CVC_CAL Bool cVcVmcPmm_B_UseRemoteStart = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseRespStartReqFromDeDmm = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseRespStartreqFromVmcEm = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseRespStrtReqInCluStrtAllw = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseRunDryInhb = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseRunDryInhbOnly = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseSapp = 0; 


#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_UseSsActTemp = 1; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL Bool cVcVmcPmm_B_UseSsActive = 1; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseStabCtrl = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseStallRcvBlock = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseStartAllowedPath = 0; 


#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_CAL Bool cVcVmcPmm_B_UseStartModeHybrid = 0; 
#endif




#if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
CVC_CAL Bool cVcVmcPmm_B_UseStartModeHybrid12V = 0; 
#endif




#if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
CVC_CAL Bool cVcVmcPmm_B_UseStrtMde3All12vStrt = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseTm = 0; 
CVC_CAL Bool cVcVmcPmm_B_UseTotEngRunReq = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseTqOffsForCluStrtEval = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseTqSPM = 1; 
CVC_CAL Bool cVcVmcPmm_B_UseTrans = 1; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_B_UseWait4CluStrt = 0; 
#endif


CVC_CAL Bool cVcVmcPmm_B_UseWait4Eng2Stop = 0; 


#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL Bool cVcVmcPmm_B_UseWhlSpdDirection = 1; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_CAL UInt8 cVcVmcPmm_D_BrkHillVal = 1; 
#endif


CVC_CAL UInt8 cVcVmcPmm_D_DrDoorOpen = 1; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_Efad12VStrtMax = 2; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EfadCluStrtMax = 2; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EfadIsgStrLoosenLim = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EfadIsgStrtMax = 2; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EfadModReq_dbi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_D_EfadModReq_swi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EfadPathAllwd1 = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EfadPathAllwd2 = 5; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EfadPathReq_dbi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL Bool cVcVmcPmm_D_EfadPathReq_swi = 0; 
#endif


CVC_CAL UInt8 cVcVmcPmm_D_EngmtModSmooth = 1; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EpbCoding1 = 6; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EpbCoding2 = 12; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EpbCoding3 = 3; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 cVcVmcPmm_D_EpbCoding4 = 10; 
#endif


CVC_CAL Int8 cVcVmcPmm_D_FCAdaptGearRst = 2; 
CVC_CAL Int8 cVcVmcPmm_D_FCAdaptGearSet = 3; 
CVC_CAL UInt8 cVcVmcPmm_D_FCAdaptLockUpRst = 1; 
CVC_CAL UInt8 cVcVmcPmm_D_FCAdaptLockUpSet = 1; 


#if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
CVC_CAL UInt8 cVcVmcPmm_D_GearLevRespStrtOK1 = 0; 
#endif




#if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
CVC_CAL UInt8 cVcVmcPmm_D_GearLevRespStrtOK2 = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Int8 cVcVmcPmm_D_GearTotNtrl = 0; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL UInt8 cVcVmcPmm_D_QfEpbLongAccInit = 0; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_CAL UInt8 cVcVmcPmm_D_QfEpbLongAccOK = 3; 
#endif




#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_CAL UInt8 cVcVmcPmm_D_SafeBISG = 0; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL UInt8 cVcVmcPmm_D_SsActDrMd1 = 100; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL UInt8 cVcVmcPmm_D_SsActDrMd2 = 100; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CAL UInt8 cVcVmcPmm_D_SsActDrMd3 = 100; 
#endif


CVC_CAL UInt8 cVcVmcPmm_D_StartMode_dbi = 0; 
CVC_CAL Bool cVcVmcPmm_D_StartMode_swi = 0; 


#if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
CVC_CAL UInt8 cVcVmcPmm_D_StrtModDft = 4; 
#endif


CVC_CAL UInt8 cVcVmcPmm_D_StrtModLongIceStsDetn = 1; 


#if Vc_Pvc_Hw_B_AT
CVC_CAL UInt8 cVcVmcPmm_D_TransModeReq_dbi = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL Bool cVcVmcPmm_D_TransModeReq_swi = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL UInt8 cVcVmcPmm_D_TrnMdeHevReqEngNIC = 2; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL UInt8 cVcVmcPmm_D_TrnMdeReqEng = 2; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL UInt8 cVcVmcPmm_D_TrnMdeReqNtrl = 3; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL UInt8 cVcVmcPmm_D_TrnMdeReqTotNtrl = 4; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Int8 cVcVmcPmm_D_WhlMotSysCluOperTypReq_dbi = 0; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_CAL Bool cVcVmcPmm_D_WhlMotSysCluOperTypReq_swi = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL UInt8 mVcVmcPmm_Z_BrkRoadIncline[8][8] = 
{
   {
       0, 0, 0, 0, 0, 0, 0, 0
      
   },
   {
       0, 0, 0, 0, 0, 0, 0, 0
      
   },
   {
       0, 0, 0, 0, 0, 0, 0, 0
      
   },
   {
       0, 0, 0, 0, 0, 0, 0, 0
      
   },
   {
       0, 0, 0, 0, 0, 0, 0, 0
      
   },
   {
       0, 0, 0, 0, 0, 0, 0, 0
      
   },
   {
       0, 0, 0, 0, 0, 0, 0, 0
      
   },
   {
       0, 0, 0, 0, 0, 0, 0, 0
      
   }
}; 
#endif





#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_Te_Efad12VStrtEngClntMin = -5.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_Tq_IsgStopCoastDrReqHyst = 0.F; 
#endif


CVC_CAL_MERGEABLE Float32 cVcVmcPmm_n_EngRunning = 700.F; 
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_n_EngStalled = 10.F; 
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_n_EngStarted = 500.F; 
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_n_EngStopped = 100.F; 
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_n_StrtAbrtRpm = 400.F; 


#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_n_StrtDiffFast = 0.F; 
#endif




#ifdef SVmcPmm__HE785__sgStrtAllow_AUX
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_rt_IsgStrtAllow = 0.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_t_EfadPahDiTiOut = 5.F; 
#endif


CVC_CAL_MERGEABLE Float32 cVcVmcPmm_t_EngRunStall = 30.F; 


#ifdef SVmcPmm__HE785__sgStrtAllow_AUX
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_t_IsgRunReqDelay = 2.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_v_Efad12VStartMax = 10.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_v_Efad12VStartMin = -100.F; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL_MERGEABLE Float32 cVcVmcPmm_v_IsgStopCoastSpdHyst = 0.F; 
#endif





#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL_MERGEABLE Bool cVcVmcPmm_B_EfadUseFactory12VStrt = 1; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_CAL_MERGEABLE Bool cVcVmcPmm_B_IgnrPropAlwdCrSh = 1; 
#endif




#ifdef SVmcPmm__HE637__hEnable_dbi_AUX
CVC_CAL_MERGEABLE Bool cVcVmcPmm_B_IsgPathEnable_dbi = 0; 
#endif




#ifdef SVmcPmm__HE637__hEnable_dbi_AUX
CVC_CAL_MERGEABLE Bool cVcVmcPmm_B_IsgPathEnable_swi = 0; 
#endif




#ifdef SVmcPmm__HE389__ReqUseTrans_AUX
CVC_CAL_MERGEABLE Bool cVcVmcPmm_B_PwrUpIceStrtReqUseTrans = 1; 
#endif




#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_CAL_MERGEABLE Bool cVcVmcPmm_B_StrtMdeEscCond = 0; 
#endif


CVC_CAL_MERGEABLE Bool cVcVmcPmm_B_Use7DCT = 0; 
CVC_CAL_MERGEABLE Bool cVcVmcPmm_B_UseClPedAdaptStallRecovery = 0; 
CVC_CAL_MERGEABLE UInt8 cVcVmcPmm_D_AbortStart = 4; 
CVC_CAL_MERGEABLE UInt8 cVcVmcPmm_D_CTF = 0; 
CVC_CAL_MERGEABLE UInt8 cVcVmcPmm_D_EngmtModFast = 2; 


#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_CAL_MERGEABLE UInt8 cVcVmcPmm_D_FastBISG = 1; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_CAL_MERGEABLE UInt8 cVcVmcPmm_D_IceStsStarting = 1; 
#endif




#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_CAL_MERGEABLE UInt8 cVcVmcPmm_D_NormalBISG = 1; 
#endif


#include "CVC_CAL_END.h"

#include "PREDECL_CONST_START.h"

CVC_CONST_EXT UInt8 cVc_D_GearLevATDrive; 
CVC_CONST_EXT UInt8 cVc_D_GearLevATNeutral; 
CVC_CONST_EXT UInt8 cVc_D_GearLevATPark; 
CVC_CONST_EXT UInt8 cVc_D_GearLevATReverse; 


#if Vc_Pvc_Sw_B_StopStart
CVC_CONST_EXT UInt8 cVc_D_GearLevAT2nd; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CONST_EXT UInt8 cVc_D_GearLevAT3rd; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_CONST_EXT UInt8 cVc_D_GearLevAT4th; 
#endif


#include "PREDECL_CONST_END.h"

#include "CVC_DISP_START.h"

CVC_DISP UInt32 rVcVmcPmm_D_EngRunReqLogg; 


#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Float32 rVcVmcPmm_Tq_BrkTrqFilt; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_DISP Float32 rVcVmcPmm_Tq_EradMaxLimNoLim; 
#endif


CVC_DISP Float32 rVcVmcPmm_Xd_AccPedalPos; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Float32 rVcVmcPmm_Z_RoadGradient; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Float32 rVcVmcPmm_a_BcmLongAccFilt; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Float32 rVcVmcPmm_a_MergedAcc; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Float32 rVcVmcPmm_a_MergedAccFilt; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Float32 rVcVmcPmm_a_MergedAccSaturated; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Float32 rVcVmcPmm_a_SignedHGVehFilt; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Float32 rVcVmcPmm_a_Veh; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Float32 rVcVmcPmm_a_VehAccFilt; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_DISP Float32 rVcVmcPmm_p_BrVacuumVeh; 
#endif


CVC_DISP Float32 rVcVmcPmm_rt_FCLvl; 
CVC_DISP Float32 rVcVmcPmm_t_EngOff; 


#ifdef SVmcPmm__HE512_Switch_AUX
CVC_DISP Float32 rVcVmcPmm_t_TrnC3OilPres; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Float32 rVcVmcPmm_tc_HillGadient; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Float32 rVcVmcPmm_tc_HillGradient; 
#endif


CVC_DISP UInt32 sVcVmcPmm_D_EngRunReqLogg; 
CVC_DISP Float32 sVcVmcPmm_Z_HillGradientDeg; 



#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP UInt8 rVcVmcPmm_D_12VStrtCnt; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP UInt8 rVcVmcPmm_D_CluStrtCnt; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP UInt8 rVcVmcPmm_D_EfadModReq; 
#endif


CVC_DISP UInt8 rVcVmcPmm_D_EngRunReqBrake = 0; 
CVC_DISP UInt8 rVcVmcPmm_D_EngRunReqChas; 
CVC_DISP UInt8 rVcVmcPmm_D_EngRunReqDrLeave = 0; 
CVC_DISP UInt8 rVcVmcPmm_D_EngRunReqFCAdapt = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP UInt8 rVcVmcPmm_D_IsgStrtCnt; 
#endif


CVC_DISP UInt8 rVcVmcPmm_D_StallAbortNum; 
CVC_DISP UInt8 rVcVmcPmm_D_TransModeReq = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP UInt8 rVcVmcPmm_Z_BrkRoadIncline; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP UInt8 sVcVmcPmm_D_EfadPathReq; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_DISP UInt8 sVcVmcPmm_D_EngRunReqBrkVac; 
#endif


CVC_DISP UInt8 sVcVmcPmm_D_EngRunReqClim; 
CVC_DISP UInt8 sVcVmcPmm_D_EngRunReqEmLv; 


#if VcVmcPmm__HEP7_1140_Brake_1
CVC_DISP UInt8 sVcVmcPmm_D_EngRunReqHG; 
#endif


CVC_DISP UInt8 sVcVmcPmm_D_EngagementMode; 
CVC_DISP UInt8 sVcVmcPmm_D_IceStatus; 


#if VcVmcPmm__HEP7_1240_Hybrid_Mode_Control_9
CVC_DISP UInt8 sVcVmcPmm_D_IsgModReq; 
#endif


CVC_DISP UInt8 sVcVmcPmm_D_StartMode; 
CVC_DISP UInt8 sVcVmcPmm_D_TransModeReq; 


#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_DISP Int8 sVcVmcPmm_D_WhlMotSysCluOperTypReq; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_DISP UInt8 sVcVmcPmm_D_WhlMotSysModReq; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_12VStrtActrRdy; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_12VStrtAllwd; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_12VStrtBlk; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_DISP Bool xVcVmcPmm_B_12VStrtOk; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_12VStrtPsbl; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_12VStrtReq = 0; 
#endif


CVC_DISP Bool xVcVmcPmm_B_AbrtFrstStrtStall; 
CVC_DISP Bool xVcVmcPmm_B_AbrtNtrlAdapt; 
CVC_DISP Bool xVcVmcPmm_B_AbrtStallAbortHard; 
CVC_DISP Bool xVcVmcPmm_B_AbrtStallEngClntL; 
CVC_DISP Bool xVcVmcPmm_B_AbrtStallGp; 
CVC_DISP Bool xVcVmcPmm_B_AbrtStallMicHev; 
CVC_DISP Bool xVcVmcPmm_B_AbrtStallRcShutOff; 
CVC_DISP Bool xVcVmcPmm_B_AbrtStallSeatBelt; 
CVC_DISP Bool xVcVmcPmm_B_AbrtStallSsRcfSet; 
CVC_DISP Bool xVcVmcPmm_B_AbrtStallTime; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_AccPedOKIsgBrk; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool xVcVmcPmm_B_AmbPresLow; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool xVcVmcPmm_B_AmbTempH; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool xVcVmcPmm_B_AmbTempL; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_DISP Bool xVcVmcPmm_B_BrkHGSkipPark; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_DISP Bool xVcVmcPmm_B_BrkHGSkipParkPre; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Bool xVcVmcPmm_B_BrkHGStart; 
#endif




#ifdef SVmcPmm__HE148_Switch_AUX
CVC_DISP Bool xVcVmcPmm_B_BrkHillGradStart = 0; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_BrkOKIsgBrk; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_BrkRoadIncline; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_DISP Bool xVcVmcPmm_B_BrkVacuumStart; 
#endif




#if VcVmcPmm__HEP7_1140_Brake_1
CVC_DISP Bool xVcVmcPmm_B_BrkVacuumVeh; 
#endif


CVC_DISP Bool xVcVmcPmm_B_CECBlock; 
CVC_DISP Bool xVcVmcPmm_B_CECBlocked; 
CVC_DISP Bool xVcVmcPmm_B_ChasBlocked; 
CVC_DISP Bool xVcVmcPmm_B_ClimBlocked; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_CluStrtActrRdy; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_CluStrtAllwd; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_CluStrtBlk; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_CluStrtPsbl; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_CluStrtTqRsvBlk; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_CluStrtVehSpdOK; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_DISP Bool xVcVmcPmm_B_CrShPathDisabled; 
#endif


CVC_DISP Bool xVcVmcPmm_B_CrnkStallRecov; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Dly12VStrtVehPwrUp; 
#endif


CVC_DISP Bool xVcVmcPmm_B_DrDoorOpen; 
CVC_DISP Bool xVcVmcPmm_B_DrLeaveKeepRun; 
CVC_DISP Bool xVcVmcPmm_B_DrLeavePowerDownReq = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_DrvCycActvFirstStrt; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_DrvCycActvFirstStrtTiOut; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_DrvCycTiOut; 
#endif


CVC_DISP Bool xVcVmcPmm_B_EMSBlock; 
CVC_DISP Bool xVcVmcPmm_B_EMSBlocked; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Efad2IcePahReq; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Efad2IceReq; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Efad2IceReqRst; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Efad2IceUnavl; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Efad2WhlPahReq; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Efad2WhlUnavl; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_EfadDisengdReq; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_EfadUnavl; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_ElecMotLowAvailTrq; 
#endif


CVC_DISP Bool xVcVmcPmm_B_EmLvBlocked; 


#if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
CVC_DISP Bool xVcVmcPmm_B_EmiStrt; 
#endif


CVC_DISP Bool xVcVmcPmm_B_EngOnOff; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_EngOnReqDly; 
#endif


CVC_DISP Bool xVcVmcPmm_B_EngOnReqEng; 
CVC_DISP Bool xVcVmcPmm_B_EngOnReqPre; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_EngOnReqTiOut; 
#endif


CVC_DISP Bool xVcVmcPmm_B_EngOnReqTrans = 0; 


#if Vc_Pvc_Hw_B_AT
CVC_DISP Bool xVcVmcPmm_B_EngOnReqTransPre; 
#endif


CVC_DISP Bool xVcVmcPmm_B_EngRunReqCEC; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqChas; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqDep; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqDrLeave; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqDriver; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqEm; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqEngClnt; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqFCAdapt; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqIceStall; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqIsg; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqIsgStop = 0; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqMaxTime; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqPcr; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqPsm; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqRemote; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqStabCtrl; 
CVC_DISP Bool xVcVmcPmm_B_EngRunReqTotPre; 
CVC_DISP Bool xVcVmcPmm_B_EngRunning; 
CVC_DISP Bool xVcVmcPmm_B_EngRunningRpm; 
CVC_DISP Bool xVcVmcPmm_B_EngRunningRpmDly; 
CVC_DISP Bool xVcVmcPmm_B_EngStart; 
CVC_DISP Bool xVcVmcPmm_B_EngStop; 
CVC_DISP Bool xVcVmcPmm_B_EngStopFast; 


#if Vc_Pvc_Hw_B_AT
CVC_DISP Bool xVcVmcPmm_B_EngStopReqAT; 
#endif


CVC_DISP Bool xVcVmcPmm_B_EngStopped; 
CVC_DISP Bool xVcVmcPmm_B_EngmtModFast; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_EpbActive; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_DISP Bool xVcVmcPmm_B_EradAllow; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_DISP Bool xVcVmcPmm_B_EradEngageReq; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_DISP Bool xVcVmcPmm_B_EradSpdCtrl; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_EvenGearShiftAct; 
#endif


CVC_DISP Bool xVcVmcPmm_B_FCAdaptAct; 
CVC_DISP Bool xVcVmcPmm_B_FanAfterrun; 
CVC_DISP Bool xVcVmcPmm_B_FastEngmtIsgStrt; 
CVC_DISP Bool xVcVmcPmm_B_FastEngmtPwrDemand; 
CVC_DISP Bool xVcVmcPmm_B_FastEngmtTrqDemand; 


#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_DISP Bool xVcVmcPmm_B_FastStart; 
#endif


CVC_DISP Bool xVcVmcPmm_B_ForcedStallStart; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_GarageShiftEfadPahDiOK; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_GearLvrNotDRDetn; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Bool xVcVmcPmm_B_GradOutOfLim; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Bool xVcVmcPmm_B_HGSpdOK; 
#endif




#if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
CVC_DISP Bool xVcVmcPmm_B_HeatUpEOP; 
#endif


CVC_DISP Bool xVcVmcPmm_B_IceStartRun; 


#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgActrTqRampDwn; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgChrgReq; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgChrgReqBrk; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgChrgReqDrv; 
#endif




#ifdef SVmcPmm__HE784__lOperator19_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgEnable; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgReq; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStandStillBrkTqOK; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStandStillBslTqOK; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStandStillVehSpdOK; 
#endif


CVC_DISP Bool xVcVmcPmm_B_IsgStopCoast = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStopPostRunReqStandstill; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStopPwrDwn; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStopRoadGradOK; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStopRunReqCoast; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStopRunReqStandstill; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStopStandstill; 
#endif


CVC_DISP Bool xVcVmcPmm_B_IsgStopStandstillPre = 0; 
CVC_DISP Bool xVcVmcPmm_B_IsgStrtAbort; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtActrRdy; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtAllwd; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtBlk; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtGearLvrDEfadIsgAct; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtGearLvrDR; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtGearLvrDRAbort; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtGearLvrDRBraking; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtLimLoosen; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtLowAvailTrq; 
#endif




#ifdef SVmcPmm__HE808__calOperator_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtOk; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtPsbl; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_IsgStrtWhlTrqOK; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_NonSysStrt; 
#endif


CVC_DISP Bool xVcVmcPmm_B_PTDisengagedAT; 


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_DISP Bool xVcVmcPmm_B_PwdPossible; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_DISP Bool xVcVmcPmm_B_PwdReset; 
#endif


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_DISP Bool xVcVmcPmm_B_PwdTrig; 
#endif


#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Bool xVcVmcPmm_B_QfFault; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Bool xVcVmcPmm_B_QfFaultLongAcc; 
#endif


CVC_DISP Bool xVcVmcPmm_B_RunReqIceStall; 


#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool xVcVmcPmm_B_SRSeatBeltAT; 
#endif




#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_DISP Bool xVcVmcPmm_B_SafeISG; 
#endif




#if VcVmcPmm__HEP7_121M_StartModeHybrid_3
CVC_DISP Bool xVcVmcPmm_B_SafeISGPrio; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool xVcVmcPmm_B_SsActDriverLeaving; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool xVcVmcPmm_B_SsActSeatBeltAllow; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool xVcVmcPmm_B_SsActSeatBeltInhib; 
#endif


CVC_DISP Bool xVcVmcPmm_B_StallAbortNum; 
CVC_DISP Bool xVcVmcPmm_B_StallIceStrt; 
CVC_DISP Bool xVcVmcPmm_B_StallIceStrtActrFinishd; 
CVC_DISP Bool xVcVmcPmm_B_StallIceStrtEmi; 
CVC_DISP Bool xVcVmcPmm_B_StallRcvAT; 
CVC_DISP Bool xVcVmcPmm_B_StallRcvAbortInSpd; 
CVC_DISP Bool xVcVmcPmm_B_StallRcvCl; 
CVC_DISP Bool xVcVmcPmm_B_StallRcvClNtrl; 
CVC_DISP Bool xVcVmcPmm_B_StallRcvMT; 
CVC_DISP Bool xVcVmcPmm_B_StallRecovery; 
CVC_DISP Bool xVcVmcPmm_B_StallRunComInhbt; 
CVC_DISP Bool xVcVmcPmm_B_StallRunUnintd; 
CVC_DISP Bool xVcVmcPmm_B_StallRunning; 
CVC_DISP Bool xVcVmcPmm_B_StallStrtM; 


#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Bool xVcVmcPmm_B_StandStill; 
#endif


CVC_DISP Bool xVcVmcPmm_B_StartAllowedPath; 
CVC_DISP Bool xVcVmcPmm_B_Started; 
CVC_DISP Bool xVcVmcPmm_B_StartedDly; 
CVC_DISP Bool xVcVmcPmm_B_StopAllowedDep; 
CVC_DISP Bool xVcVmcPmm_B_StopAllowedPath; 


#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Bool xVcVmcPmm_B_StopInhibitDownHill; 
#endif




#if VcVmcPmm__HEP7_1150_Gradient_estimation_2
CVC_DISP Bool xVcVmcPmm_B_StopInhibitUpHill; 
#endif


CVC_DISP Bool xVcVmcPmm_B_StrtAbrt; 
CVC_DISP Bool xVcVmcPmm_B_StrtAbrtPre; 
CVC_DISP Bool xVcVmcPmm_B_StrtActrsRdy = 0; 
CVC_DISP Bool xVcVmcPmm_B_StrtMdeAcc; 
CVC_DISP Bool xVcVmcPmm_B_StrtMdeRunning; 
CVC_DISP Bool xVcVmcPmm_B_TmBlock; 
CVC_DISP Bool xVcVmcPmm_B_TmBlocked; 
CVC_DISP Bool xVcVmcPmm_B_TrailerPresent; 
CVC_DISP Bool xVcVmcPmm_B_TransBlock; 
CVC_DISP Bool xVcVmcPmm_B_TransBlocking; 
CVC_DISP Bool xVcVmcPmm_B_TransEngOnBlock; 


#ifdef SVmcPmm__HE171__lOperator35_AUX
CVC_DISP Bool xVcVmcPmm_B_TrnC3OilPres = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_DISP Bool xVcVmcPmm_B_TrnEngageReq; 
#endif




#ifdef SVmcPmm__HE477__lOperator18_AUX
CVC_DISP Bool xVcVmcPmm_B_TrnEngageReqHybrid = 0; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_DISP Bool xVcVmcPmm_B_TrnEngageReqIC; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_DISP Bool xVcVmcPmm_B_TrnEngageReqPre; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_TrnModOKIsgReq; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_VehSpdOKIsgBrk; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_VehSpdOKIsgDrv; 
#endif


CVC_DISP Bool xVcVmcPmm_B_Wait4CluStrt = 0; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Wait4CluStrtAccPedAct; 
#endif


CVC_DISP Bool xVcVmcPmm_B_Wait4CluStrtDly; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Wait4CluStrtLowVehSpd; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Wait4CluStrtTiOut; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Wait4CluStrtWhlAccHigh; 
#endif




#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool xVcVmcPmm_B_Wait4CluStrtWhlTqLow; 
#endif


CVC_DISP Bool xVcVmcPmm_B_Wait4Eng2Stop; 
CVC_DISP Bool xVcVmcPmm_B_Wait4EngStrtTiOut; 
CVC_DISP Bool yVcVmcPmm_B_12VStartEnable; 
CVC_DISP Bool yVcVmcPmm_B_AutoParkReq; 


#if Vc_Pvc_Hw_B_HVSystem == 0
CVC_DISP Bool yVcVmcPmm_B_BlockPushStartHMI; 
#endif


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool yVcVmcPmm_B_ClutchStartReq; 
#endif


CVC_DISP Bool yVcVmcPmm_B_CrShPathEnable; 


#ifdef SVmcPmm__HE1_VcVmcPmm_AUX
CVC_DISP Bool yVcVmcPmm_B_EfadActReq; 
#endif


CVC_DISP Bool yVcVmcPmm_B_EfadPathEnable; 
CVC_DISP Bool yVcVmcPmm_B_EngOnReq; 
CVC_DISP Bool yVcVmcPmm_B_EngOnReqEng; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqBrake; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqClim; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqEmLv; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqEms; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqFanAfterrun; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqFuel; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqObd; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqRc; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqSapp; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqTm; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqTot; 
CVC_DISP Bool yVcVmcPmm_B_EngRunReqTrans; 


#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_DISP Bool yVcVmcPmm_B_EradClutchReq; 
#endif




#ifdef SVmcPmm__HE614__lOperator11_AUX
CVC_DISP Bool yVcVmcPmm_B_EradDrReq; 
#endif


CVC_DISP Bool yVcVmcPmm_B_EradPathEnable; 
CVC_DISP Bool yVcVmcPmm_B_FCAdaptReq; 
CVC_DISP Bool yVcVmcPmm_B_FastIsgStopReq; 
CVC_DISP Bool yVcVmcPmm_B_IceStall; 


#if VcVmcPmm__HEP7_1240_Hybrid_Mode_Control_9
CVC_DISP Bool yVcVmcPmm_B_IsgActReq; 
#endif


CVC_DISP Bool yVcVmcPmm_B_IsgPathEnable; 
CVC_DISP Bool yVcVmcPmm_B_IsgStartReq; 
CVC_DISP Bool yVcVmcPmm_B_IsgStrtPahReq; 
CVC_DISP Bool yVcVmcPmm_B_PowerDownReq; 
CVC_DISP Bool yVcVmcPmm_B_PwrUpIceStrtReq; 


#if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
CVC_DISP Bool yVcVmcPmm_B_RunReqDriverHmi; 
#endif




#if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
CVC_DISP Bool yVcVmcPmm_B_RunReqSystemHmi; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsActAbsHMI; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsActAmbHMI; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsActDoorOpenHMI; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsActDrMdHMI; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsActHoodHMI; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsActSeatBeltHMI; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsActTrailerHMI; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsActive; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsAltitudeFault; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsAmbFault; 
#endif




#if Vc_Pvc_Sw_B_StopStart
CVC_DISP Bool yVcVmcPmm_B_SsRcfAct; 
#endif


CVC_DISP Bool yVcVmcPmm_B_StallPwdReq; 


#ifdef SVmcPmm__HE821__ransHeatReq_AUX
CVC_DISP Bool yVcVmcPmm_B_TransHeatReq; 
#endif




#if Vc_Pvc_Hw_B_AT
CVC_DISP Bool yVcVmcPmm_B_TrnEngageReqHev; 
#endif


CVC_DISP Bool yVcVmcPmm_B_UnintdStall; 
#include "CVC_DISP_END.h"







#include "CVC_CODE_START.h"
void RESTART_VcVmcPmm(void)
{
   rVcVmcPmm_D_EngRunReqBrake = 0;
   rVcVmcPmm_D_EngRunReqDrLeave = 0;
   rVcVmcPmm_D_EngRunReqFCAdapt = 0;
   rVcVmcPmm_D_TransModeReq = 0;

   
   #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
      xVcVmcPmm_B_12VStrtReq = 0;
   #endif

   

   
   #if VcVmcPmm__HEP7_1140_Brake_1
      xVcVmcPmm_B_BrkHillGradStart = 0;
   #endif

   
   xVcVmcPmm_B_DrLeavePowerDownReq = 0;
   xVcVmcPmm_B_EngOnReqTrans = 0;
   xVcVmcPmm_B_EngRunReqIsgStop = 0;
   xVcVmcPmm_B_IsgStopCoast = 0;
   xVcVmcPmm_B_IsgStopStandstillPre = 0;
   xVcVmcPmm_B_StrtActrsRdy = 0;

   
   #if Vc_Pvc_Hw_B_AT
      xVcVmcPmm_B_TrnC3OilPres = 0;
      xVcVmcPmm_B_TrnEngageReqHybrid = 0;
   #endif

   
   xVcVmcPmm_B_Wait4CluStrt = 0;
}
#include "CVC_CODE_END.h"


#include "CVC_CODE_START.h"
void VcVmcPmm(void)
{
   
   static Bool SVmcPmm__HE156_RSWE = 0;
   static Bool SVmcPmm__HE157_RSWE = 0;

   if (VcVmcPmm__HEP7_1000_Hev_11 != 0) {
      
      static UInt8 CVmcPmm__HE1_D_IceStatus = 0;

      
      static struct tag_SIBFS_1131_IceStatus_VmcPmm__HE_tp SIBFS_1131_IceStatus_VmcPmm__HE = {
         0, 
         0, 
         0, 
         0 
      }; 

      
      Float32 SVmcPmm__HE117_Switch;

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         Float32 SVmcPmm__HE130_Switch;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         Float32 SVmcPmm__HE142_MinMax;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         Float32 SVmcPmm__HE142_Prod1;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         Float32 SVmcPmm__HE143_MinMax;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         Float32 SVmcPmm__HE143_Prod1;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         Float32 SVmcPmm__HE144_MinMax;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         Float32 SVmcPmm__HE144_Prod1;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         Float32 SVmcPmm__HE147_Switch; 
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         Float32 SVmcPmm__HE152_MinMax;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         Float32 SVmcPmm__HE18_Product4;
      #endif

      
      Float32 SVmcPmm__HE228_Switch;
      UInt32 SVmcPmm__HE265_Switch;
      UInt32 SVmcPmm__HE266_Switch;
      UInt32 SVmcPmm__HE267_Switch;
      UInt32 SVmcPmm__HE269_Switch;
      UInt32 SVmcPmm__HE270_Switch;
      UInt32 SVmcPmm__HE271_Switch;
      UInt32 SVmcPmm__HE272_Switch;
      UInt32 SVmcPmm__HE273_Switch;
      UInt32 SVmcPmm__HE274_Switch;
      UInt32 SVmcPmm__HE275_Switch;
      UInt32 SVmcPmm__HE276_Switch;
      UInt32 SVmcPmm__HE277_Switch;
      UInt32 SVmcPmm__HE278_Switch;
      Float32 SVmcPmm__HE279_Switch;
      UInt32 SVmcPmm__HE280_Switch;
      UInt32 SVmcPmm__HE281_Switch;
      UInt32 SVmcPmm__HE283_Switch;
      UInt32 SVmcPmm__HE286_Switch;
      UInt32 SVmcPmm__HE287_Switch;
      UInt32 SVmcPmm__HE288_Switch;
      UInt32 SVmcPmm__HE289_Switch;
      UInt32 SVmcPmm__HE291_Switch;
      UInt32 SVmcPmm__HE292_Switch;
      UInt32 SVmcPmm__HE293_Switch;
      UInt32 SVmcPmm__HE297_Switch;
      UInt32 SVmcPmm__HE303_Switch;
      UInt32 SVmcPmm__HE304_Switch;

      
      #ifdef SVmcPmm__HE512_Switch_AUX
         Float32 SVmcPmm__HE512_Switch;
      #endif

      
      Float32 SVmcPmm__HE561_Switch;
      Float32 SVmcPmm__HE571_Switch;

      
      #ifdef SVmcPmm__HE821__ransHeatReq_AUX
         Float32 SVmcPmm__HE821_Tq_TransHeatReq;
      #endif

      
      Float32 SVmcPmm__HE848_Switch;

      
      Bool SVmcPmm__HE111_Switch;
      Bool SVmcPmm__HE112_Switch;
      Bool SVmcPmm__HE113_Switch;
      Bool SVmcPmm__HE114_Switch;

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         UInt8 SVmcPmm__HE125_Switch;
      #endif

      

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         UInt8 SVmcPmm__HE127_Switch;
      #endif

      

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         UInt8 SVmcPmm__HE128_Switch;
      #endif

      

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         UInt8 SVmcPmm__HE129_Switch;
      #endif

      

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         Bool SVmcPmm__HE131_Switch;
      #endif

      

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         UInt8 SVmcPmm__HE132_Switch;
      #endif

      
      Bool SVmcPmm__HE170_LogicalOperator2;
      Bool SVmcPmm__HE170_LogicalOperator6;
      Bool SVmcPmm__HE170_LogicalOperator7;
      Bool SVmcPmm__HE170__gicalOperator22;
      Bool SVmcPmm__HE170__gicalOperator37;
      Bool SVmcPmm__HE170__ionalOperator17;

      
      #if Vc_Pvc_Hw_B_AT
         Bool SVmcPmm__HE171_LogicalOperator3;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         Bool SVmcPmm__HE171__gicalOperator10;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         Bool SVmcPmm__HE171__gicalOperator18;
      #endif

      

      
      #ifdef SVmcPmm__HE171__lOperator35_AUX
         Bool SVmcPmm__HE171__gicalOperator35;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         Bool SVmcPmm__HE171__gicalOperator43;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         Bool SVmcPmm__HE171__gicalOperator49;
      #endif

      
      Bool SVmcPmm__HE172_LogOp1; 
      Bool SVmcPmm__HE172_LogOp47; 
      Bool SVmcPmm__HE172_LogOp48; 
      Bool SVmcPmm__HE172__ionalOperator20;
      Bool SVmcPmm__HE172__tionalOperator1;
      Bool SVmcPmm__HE205_LogicalOperator1;
      Bool SVmcPmm__HE205_LogicalOperator4;
      Bool SVmcPmm__HE205__gicalOperator12;
      Bool SVmcPmm__HE205__tionalOperator1;
      Bool SVmcPmm__HE206_LogicalOperator1;
      Bool SVmcPmm__HE206__gicalOperator12;
      Bool SVmcPmm__HE207_LogicalOperator1;
      Bool SVmcPmm__HE207__gicalOperator12;
      Bool SVmcPmm__HE208_LogicalOperator1;
      Bool SVmcPmm__HE208__gicalOperator12;
      Bool SVmcPmm__HE210_LogicalOperator1;
      Bool SVmcPmm__HE210__gicalOperator12;
      Bool SVmcPmm__HE216_LogicalOperator1;
      Bool SVmcPmm__HE216__gicalOperator12;
      Bool SVmcPmm__HE219_LogicalOperator1;
      Bool SVmcPmm__HE219__gicalOperator12;
      Bool SVmcPmm__HE223__ionalOperator11;
      Bool SVmcPmm__HE223__ionalOperator18;
      Bool SVmcPmm__HE223__tionalOperator1;
      Bool SVmcPmm__HE226_LogicalOperator3;
      Bool SVmcPmm__HE226_LogicalOperator6;
      Bool SVmcPmm__HE227_switch;
      Bool SVmcPmm__HE230_Logic1;
      UInt8 SVmcPmm__HE236_Switch;
      UInt8 SVmcPmm__HE237_Switch;
      UInt8 SVmcPmm__HE239_Switch;
      UInt8 SVmcPmm__HE242_Switch;
      UInt8 SVmcPmm__HE250_Switch;
      Bool SVmcPmm__HE252_Switch;
      UInt8 SVmcPmm__HE253_Switch;
      UInt8 SVmcPmm__HE254_Switch;
      UInt8 SVmcPmm__HE255_Switch;
      UInt8 SVmcPmm__HE256_Switch;
      UInt8 SVmcPmm__HE257_Switch;
      UInt8 SVmcPmm__HE258_Switch;
      Bool SVmcPmm__HE261_Switch;
      UInt8 SVmcPmm__HE262_Switch;
      UInt8 SVmcPmm__HE268_Switch;

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE26_LogicalOperator15;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE26_LogicalOperator23;
      #endif

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE27_LogicalOperator25;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE27___tionalOperator1;
      #endif

      
      UInt8 SVmcPmm__HE284_Switch;
      UInt8 SVmcPmm__HE285_Switch;
      UInt8 SVmcPmm__HE290_Switch;
      UInt8 SVmcPmm__HE295_Switch;
      UInt8 SVmcPmm__HE296_Switch;
      Bool SVmcPmm__HE298_Switch;
      UInt8 SVmcPmm__HE299_Switch;
      Bool SVmcPmm__HE300_Switch;
      UInt8 SVmcPmm__HE301_Switch;
      UInt8 SVmcPmm__HE307_Switch;
      UInt8 SVmcPmm__HE308_Switch;

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE32_Switch;
      #endif
      Bool SVmcPmm__HE334_Rel;
      Bool SVmcPmm__HE334_Rel1;

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE33_Switch;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE34_Switch;
      #endif
      Bool SVmcPmm__HE352_Switch;

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE35_Switch;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE36_Switch;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE37_Switch;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE38_Switch;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE39_Switch;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE40_Switch;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE41_Switch;
      #endif
      Bool SVmcPmm__HE428_Switch;

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE42_Switch;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         Bool SVmcPmm__HE44_Switch;
      #endif
      Bool SVmcPmm__HE458_Switch;

      
      #ifdef SVmcPmm__HE477_MinMax_AUX
         UInt8 SVmcPmm__HE477_MinMax;
      #endif

      

      
      #ifdef SVmcPmm__HE477__lOperator18_AUX
         Bool SVmcPmm__HE482_Switch;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         Bool SVmcPmm__HE484_Switch;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         Bool SVmcPmm__HE486_Switch;
      #endif

      

      
      #ifdef SVmcPmm__HE512_Switch_AUX
         Bool SVmcPmm__HE513_Logic1;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         Bool SVmcPmm__HE523_Rel;
      #endif

      
      Bool SVmcPmm__HE527_LogicalOperator;
      Bool SVmcPmm__HE532_Switch;
      Bool SVmcPmm__HE533_Switch;
      Bool SVmcPmm__HE544_Switch;
      Bool SVmcPmm__HE547_Switch;
      Bool SVmcPmm__HE548_Switch;
      Bool SVmcPmm__HE549_Switch;
      Bool SVmcPmm__HE550_Switch;
      Bool SVmcPmm__HE551_Switch;
      Bool SVmcPmm__HE552_Switch;
      Bool SVmcPmm__HE553_Switch;
      Bool SVmcPmm__HE557_Switch;
      Bool SVmcPmm__HE560_Switch;
      Bool SVmcPmm__HE562_Switch;
      Bool SVmcPmm__HE563_Switch;
      Bool SVmcPmm__HE564_Switch;
      Bool SVmcPmm__HE576_Switch;
      Bool SVmcPmm__HE578_Switch;
      Bool SVmcPmm__HE584__tionalOperator1;

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE60_Switch;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE62_Switch;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE66_Switch;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE73_Switch;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE74_Switch;
      #endif

      
      Bool SVmcPmm__HE827_Switch;
      Bool SVmcPmm__HE829_Switch;
      UInt8 SVmcPmm__HE843_Switch;
      UInt8 SVmcPmm__HE845_Switch;
      UInt8 SVmcPmm__HE846_Switch;

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE90_Rel;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE90_Rel1;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE91_Rel;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE91_Rel1;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE92_Rel;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE92_Rel1;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         Bool SVmcPmm__HE98_Switch;
      #endif

      

      
      UInt32 Aux_U32;

      
      static Float32 SVmcPmm__HE153__HillGradAcc2deg = 0.F; 

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static Float32 SVmcPmm__HE153__llGradAcc2deg_x[2] = 
         {
             0.F, 0.F
            
         }; 
      #endif

      

      
      #ifdef SVmcPmm__HE821__ransHeatReq_AUX
         static Float32 SVmcPmm__HE821___TransHeatReq_x[2] = 
         {
             0.F, 0.F
            
         }; 
      #endif

      

      
      
      #if VcVmcPmm__HEP7_1140_Brake_1
         static UInt8 SVmcPmm__HE138_p_BrVacuumVeh_x[2] = 
         {
             0, 0
            
         }; 
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static UInt8 SVmcPmm__HE154___HillGradient_c[2] = 
         {
             0, 0
            
         }; 
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static UInt8 SVmcPmm__HE154___HillGradient_r[2] = 
         {
             0, 0
            
         }; 
      #endif

      
      static Bool SVmcPmm__HE159_LogOp3 = 0;

      
      #ifdef SVmcPmm__HE173_Merge_AUX
         static UInt8 SVmcPmm__HE173_Merge = 0;
      #endif

      

      
      #ifdef SVmcPmm__HE173_Merge1_AUX
         static Bool SVmcPmm__HE173_Merge1 = 0;
      #endif

      

      
      #ifdef SVmcPmm__HE173_Merge1_AUX
         static Bool SVmcPmm__HE173_Merge3 = 0;
      #endif

      
      static Bool SVmcPmm__HE222_Rescaler = 0;
      static Bool SVmcPmm__HE30_Switch = 0;
      static Bool SVmcPmm__HE389__gicalOperator52 = 0;
      static UInt8 SVmcPmm__HE398_Switch = 0;
      static Bool SVmcPmm__HE403__gicalOperator52 = 0;
      static UInt8 SVmcPmm__HE416_Switch = 0;

      
      #ifdef SVmcPmm__HE477__lOperator18_AUX
         static Bool SVmcPmm__HE477__gicalOperator18 = 0;
      #endif

      
      static Bool SVmcPmm__HE489_Switch = 0;
      static Bool SVmcPmm__HE6_Merge3 = 0;

      
      static Float32 X_SVmcPmm__HE118_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE119_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE120_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE121_UnitDelay = 0.F;

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         static Float32 X_SVmcPmm__HE133_UnitDelay = 1e+30F;
      #endif

      

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         static Float32 X_SVmcPmm__HE134_UnitDelay = 1e+30F;
      #endif

      

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         static Float32 X_SVmcPmm__HE137_UnitDelay = 0.F;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static Float32 X_SVmcPmm__HE141_Del = 0.F;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static Float32 X_SVmcPmm__HE141_Del1 = 0.F;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static Float32 X_SVmcPmm__HE142_Del1 = 0.F;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static Float32 X_SVmcPmm__HE143_Del1 = 0.F;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static Float32 X_SVmcPmm__HE144_Del1 = 0.F;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static Float32 X_SVmcPmm__HE149_UnitDelay = 0.F;
      #endif

      
      static Float32 X_SVmcPmm__HE228_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE309_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE310_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE311_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE312_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE313_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE314_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE340_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE341_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE342_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE354_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE355_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE359_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE363_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE367_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE372_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE381_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE387_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE434_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE435_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE436_UnitDelay = 0.F;

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Float32 X_SVmcPmm__HE445_UnitDelay = 0.F;
      #endif

      

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Float32 X_SVmcPmm__HE446_UnitDelay = 0.F;
      #endif

      

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Float32 X_SVmcPmm__HE447_UnitDelay = 0.F;
      #endif

      

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Float32 X_SVmcPmm__HE448_UnitDelay = 0.F;
      #endif

      

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Float32 X_SVmcPmm__HE449_UnitDelay = 0.F;
      #endif

      
      static Float32 X_SVmcPmm__HE455_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE456_Del = 0.F;
      static Float32 X_SVmcPmm__HE456_Del1 = 0.F;

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         static Float32 X_SVmcPmm__HE45_UnitDelay = 1e+30F;
      #endif
      static Float32 X_SVmcPmm__HE461_UnitDelay = 0.F;

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         static Float32 X_SVmcPmm__HE46_UnitDelay = 0.F;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         static Float32 X_SVmcPmm__HE47_UnitDelay = 0.F;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         static Float32 X_SVmcPmm__HE48_UnitDelay = 0.F;
      #endif

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         static Float32 X_SVmcPmm__HE49_UnitDelay = 0.F;
      #endif

      
      #if Vc_Pvc_Hw_B_AT
         static Float32 X_SVmcPmm__HE507_UnitDelay = 0.F;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         static Float32 X_SVmcPmm__HE508_UnitDelay = 0.F;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         static Float32 X_SVmcPmm__HE509_UnitDelay = 0.F;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         static Float32 X_SVmcPmm__HE510_UnitDelay = 1e+30F;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         static Float32 X_SVmcPmm__HE511_UnitDelay = 1e+30F;
      #endif

      

      
      #ifdef SVmcPmm__HE512_Switch_AUX
         static Float32 X_SVmcPmm__HE512_UnitDelay = 0.F;
      #endif

      

      
      #ifdef SVmcPmm__HE477_MinMax_AUX
         static Float32 X_SVmcPmm__HE515_UnitDelay = 0.F;
      #endif

      

      
      #ifdef SVmcPmm__HE477_MinMax_AUX
         static Float32 X_SVmcPmm__HE516_UnitDelay = 1e+30F;
      #endif

      

      
      #ifdef SVmcPmm__HE477_MinMax_AUX
         static Float32 X_SVmcPmm__HE517_UnitDelay = 1e+30F;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         static Float32 X_SVmcPmm__HE523_UnitDelay = 0.F;
      #endif

      
      static Float32 X_SVmcPmm__HE579_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE580_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE581_UnitDelay = 1e+30F;
      static Float32 X_SVmcPmm__HE582_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE583_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE584_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE585_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE586_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE587_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE588_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE593_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE594_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE595_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE596_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE597_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE598_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE599_UnitDelay = 0.F;
      static Float32 X_SVmcPmm__HE600_UnitDelay = 0.F;

      
      #if Vc_Pvc_Sw_B_StopStart
         static Float32 X_SVmcPmm__HE76_UnitDelay = 1e+30F;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         static Float32 X_SVmcPmm__HE77_UnitDelay = 1e+30F;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         static Float32 X_SVmcPmm__HE78_UnitDelay = 0.F;
      #endif

      

      
      #ifdef SVmcPmm__HE821__ransHeatReq_AUX
         static Float32 X_SVmcPmm__HE819_UnitDelay = 0.F;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         static Float32 X_SVmcPmm__HE96_UnitDelay = 0.F;
      #endif

      

      
      static Bool X_SVmcPmm__HE110_UnitDelay1 = 0;

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         static Bool X_SVmcPmm__HE135_UnitDelay1 = 0;
      #endif

      

      
      #if VcVmcPmm__HEP7_1140_Brake_1
         static Bool X_SVmcPmm__HE136_UnitDelay1 = 0;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static Bool X_SVmcPmm__HE141_Del2 = 1;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static Bool X_SVmcPmm__HE150_UnitDelay1 = 0;
      #endif

      

      
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         static Bool X_SVmcPmm__HE151_UnitDelay1 = 0;
      #endif

      
      static UInt8 X_SVmcPmm__HE170_UnitDelay3 = 0;
      static Bool X_SVmcPmm__HE172_UnitDelay1 = 0;
      static UInt8 X_SVmcPmm__HE172_UnitDelay3 = 0;
      static Bool X_SVmcPmm__HE172_UnitDelay8 = 0;
      static Bool X_SVmcPmm__HE223_UnitDelay8 = 0;
      static Bool X_SVmcPmm__HE230_Delay = 0;
      static Bool X_SVmcPmm__HE231_Delay = 0;
      static Bool X_SVmcPmm__HE232_Delay = 0;
      static Bool X_SVmcPmm__HE233_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE334_UnitDelay = 0;
      static Bool X_SVmcPmm__HE335_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE336_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE337_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE338_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE339_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE349_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE350_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE351_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE356_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE360_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE364_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE369_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE378_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE384_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE3_UnitDelay10 = 0;
      static UInt8 X_SVmcPmm__HE3_UnitDelay2 = 0;
      static Bool X_SVmcPmm__HE432_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE433_UnitDelay1 = 0;

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Bool X_SVmcPmm__HE437_Delay = 0;
      #endif

      

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Bool X_SVmcPmm__HE438_Delay = 0;
      #endif

      

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Bool X_SVmcPmm__HE439_UnitDelay1 = 0;
      #endif

      

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Bool X_SVmcPmm__HE442_UnitDelay1 = 0;
      #endif

      

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Bool X_SVmcPmm__HE443_UnitDelay1 = 0;
      #endif

      

      
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         static Bool X_SVmcPmm__HE444_UnitDelay1 = 0;
      #endif

      
      static Bool X_SVmcPmm__HE452_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE454_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE456_Del2 = 1;
      static Bool X_SVmcPmm__HE457_Delay = 0;
      static Bool X_SVmcPmm__HE460_UnitDelay1 = 0;

      
      #if Vc_Pvc_Hw_B_AT
         static Bool X_SVmcPmm__HE480_Delay = 0;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         static Bool X_SVmcPmm__HE502_UnitDelay1 = 0;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         static Bool X_SVmcPmm__HE503_UnitDelay1 = 0;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         static Bool X_SVmcPmm__HE504_UnitDelay1 = 0;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         static Bool X_SVmcPmm__HE505_UnitDelay1 = 0;
      #endif

      

      
      #if Vc_Pvc_Hw_B_AT
         static Bool X_SVmcPmm__HE506_UnitDelay1 = 0;
      #endif

      

      
      #if Vc_Pvc_Hw_B_HVSystem == 0
         static Bool X_SVmcPmm__HE50_UnitDelay1 = 0;
      #endif

      
      #ifdef SVmcPmm__HE512_Switch_AUX
         static Bool X_SVmcPmm__HE513_Delay = 0;
      #endif

      

      
      #ifdef SVmcPmm__HE512_Switch_AUX
         static Bool X_SVmcPmm__HE514_UnitDelay1 = 0;
      #endif

      
      static Bool X_SVmcPmm__HE525_Delay = 0;
      static Bool X_SVmcPmm__HE526_Delay = 0;
      static Bool X_SVmcPmm__HE527_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE528_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE529_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE530_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE589_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE590_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE591_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE592_UnitDelay1 = 0;
      static UInt8 X_SVmcPmm__HE6_UnitDelay = 0;
      static UInt8 X_SVmcPmm__HE6_UnitDelay1 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay10 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay11 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay12 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay13 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay14 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay15 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay2 = 0;
      static UInt8 X_SVmcPmm__HE6_UnitDelay3 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay4 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay5 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay6 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay7 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay8 = 0;
      static Bool X_SVmcPmm__HE6_UnitDelay9 = 0;

      
      #ifdef SVmcPmm__HE821__ransHeatReq_AUX
         static Bool X_SVmcPmm__HE820_UnitDelay1 = 0;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         static Bool X_SVmcPmm__HE90_UnitDelay = 0;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         static Bool X_SVmcPmm__HE91_UnitDelay = 0;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         static Bool X_SVmcPmm__HE92_UnitDelay = 0;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         static Bool X_SVmcPmm__HE93_UnitDelay1 = 0;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         static Bool X_SVmcPmm__HE94_UnitDelay1 = 0;
      #endif

      

      
      #if Vc_Pvc_Sw_B_StopStart
         static Bool X_SVmcPmm__HE97_UnitDelay1 = 0;
      #endif

      

      
      if (X_SVmcPmm__HE6_UnitDelay14) {
         
         X_SVmcPmm__HE313_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE313_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE313_UnitDelay;
      }

      
      xVcVmcPmm_B_PTDisengagedAT = (sVcDtcAtr_D_TransMode == 4) || (sVcDtcAtr_D_TransMode == 5) ||
       ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATNeutral) && cVcVmcPmm_B_PTDGearLevAT) ||
       ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATPark) && cVcVmcPmm_B_PTDGearLevAT);

      
      if (yVcDtcAtr_B_AT) {
         
         SVmcPmm__HE827_Switch = xVcVmcPmm_B_PTDisengagedAT;
      }
      else {
         
         SVmcPmm__HE827_Switch = yVcScIn_B_PowertrainDisengaged;
      }

      
      if (yVcVdm_B_AbsCtrlActv) {
         
         X_SVmcPmm__HE312_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE312_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE312_UnitDelay;
      }

      
      if (sVcVdm_D_EngRunngReqByBrk == 1) {
         
         X_SVmcPmm__HE314_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE314_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE314_UnitDelay;
      }

      
      if (cVcVmcPmm_B_UseStartAllowedPath) {
         
         Bool SVmcPmm__HE238_Switch;
         Bool SVmcPmm__HE244_Switch;
         Bool SVmcPmm__HE251_Switch;
         Bool SVmcPmm__HE263_Switch;

         
         if (cVcVmcPmm_B_LosStrt) {
            
            SVmcPmm__HE251_Switch = !(yVcDsePcr_B_EngStartInhibtRq);
         }
         else {
            
            SVmcPmm__HE251_Switch = 1;
         }

         
         if (cVcVmcPmm_B_AbsStrt) {
            
            SVmcPmm__HE263_Switch = X_SVmcPmm__HE312_UnitDelay > cVcVmcPmm_t_AbsStrt;
         }
         else {
            
            SVmcPmm__HE263_Switch = 1;
         }

         
         if (cVcVmcPmm_B_BrkStrt) {
            
            SVmcPmm__HE238_Switch = X_SVmcPmm__HE314_UnitDelay > cVcVmcPmm_t_BrkStrt;
         }
         else {
            
            SVmcPmm__HE238_Switch = 1;
         }

         
         if (cVcVmcPmm_B_DepStrt) {
            
            Bool SVmcPmm__HE826_Switch;

            
            if (cVcVmcPmm_B_UseOldEngStrtAllwd) {
               
               SVmcPmm__HE826_Switch = yVcDepSs_B_StartAllowed;
            }
            else {
               
               SVmcPmm__HE826_Switch = yVcDepSs_B_EngStartAllowed;
            }

            
            if ((Vc_Pvc_Hw_B_Isg_CN != 0) || (Vc_Pvc_Hw_B_Efad_CN != 0)) {
               
               SVmcPmm__HE244_Switch = yVcDepTre_B_ISGTqAllw || SVmcPmm__HE826_Switch;
            }
            else {
               
               SVmcPmm__HE244_Switch = SVmcPmm__HE826_Switch;
            }
         }
         else {
            
            SVmcPmm__HE244_Switch = 1;
         }

         
         xVcVmcPmm_B_StartAllowedPath = ((cVcVmcPmm_B_ATComStrt && yVcDtcAtr_B_AT &&
          (X_SVmcPmm__HE313_UnitDelay <= cVcVmcPmm_t_ATComStrt)) || yVcPpmPsm_B_ForcedStart ||
          yVcPpmPsm_B_DrReady || SVmcPmm__HE827_Switch || cVcVmcPmm_B_PTDStrt) &&
          SVmcPmm__HE251_Switch && SVmcPmm__HE263_Switch && SVmcPmm__HE238_Switch &&
          SVmcPmm__HE244_Switch;
      }
      else {
         
         xVcVmcPmm_B_StartAllowedPath = 1;
      }

      
      if (cVcVmcPmm_B_UseDriver) {
         
         SVmcPmm__HE257_Switch = sVcDeDmm_D_EngRunReqDriver;
      }
      else {
         
         SVmcPmm__HE257_Switch = 0;
      }

      
      if (Vc_Pvc_Hw_B_Isg_CN >= 1 ) {
         
         SVmcPmm__HE111_Switch = X_SVmcPmm__HE3_UnitDelay2 <= cVcVmcPmm_D_StrtModLongIceStsDetn;
      }
      else {
         
         SVmcPmm__HE111_Switch = yVcEc_B_StartMotor;
      }

      
      xVcVmcPmm_B_EngRunningRpm = sVcEc_n_Eng > cVcVmcPmm_n_EngRunning;

      
      if (xVcVmcPmm_B_EngRunningRpm) {
         
         X_SVmcPmm__HE121_UnitDelay = X_SVmcPmm__HE121_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE121_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_EngRunningRpmDly = X_SVmcPmm__HE121_UnitDelay > cVcVmcPmm_t_Running;

      
      xVcVmcPmm_B_Started = sVcEc_n_Eng > cVcVmcPmm_n_EngStarted;

      
      if (xVcVmcPmm_B_Started) {
         
         X_SVmcPmm__HE119_UnitDelay = X_SVmcPmm__HE119_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE119_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_StartedDly = X_SVmcPmm__HE119_UnitDelay > cVcVmcPmm_t_Started;

      
      if (SVmcPmm__HE111_Switch) {
         
         SVmcPmm__HE114_Switch = xVcVmcPmm_B_EngRunningRpmDly;
      }
      else {
         
         SVmcPmm__HE114_Switch = xVcVmcPmm_B_EngRunningRpmDly || xVcVmcPmm_B_StartedDly;
      }

      
      if (cVcVmcPmm_B_UseIscActvnEMS) {
         
         if (cVcVmcPmm_B_UseTqSPM) {
            
            SVmcPmm__HE112_Switch = !(yVcCmnSta_B_StaExeTx);
         }
         else {
            
            SVmcPmm__HE112_Switch = yVcEc_B_IscActvnEMS;
         }
      }
      else {
         
         SVmcPmm__HE112_Switch = 1;
      }

      
      if (cVcVmcPmm_B_UseTqSPM) {
         
         rVcVmcPmm_rt_FCLvl = sVcInjFuCut_rt_Lvl;
      }
      else {
         
         rVcVmcPmm_rt_FCLvl = sVcEc_Ps_FCLvl;
      }

      
      xVcVmcPmm_B_EngRunning = SVmcPmm__HE114_Switch && SVmcPmm__HE112_Switch && (rVcVmcPmm_rt_FCLvl
        <= cVcVmcPmm_rt_FCLvlRunning);

      
      if (cVcVmcPmm_B_EngStoppedUseHiRes) {
         if (sVcEc_n_EngHiRes < sVcEc_n_Eng) {
            
            SVmcPmm__HE117_Switch = sVcEc_n_EngHiRes;
         }
         else {
            
            SVmcPmm__HE117_Switch = sVcEc_n_Eng;
         }
      }
      else {
         
         SVmcPmm__HE117_Switch = sVcEc_n_Eng;
      }

      
      if (SVmcPmm__HE117_Switch < cVcVmcPmm_n_EngStopped) {
         
         X_SVmcPmm__HE120_UnitDelay = X_SVmcPmm__HE120_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE120_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_EngStopped = X_SVmcPmm__HE120_UnitDelay > cVcVmcPmm_t_MinStopTime;

      
      if (yVcPpmRc_B_ChangeOfMindInhibit && (!(X_SVmcPmm__HE110_UnitDelay1))) {
         
         X_SVmcPmm__HE118_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE118_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE118_UnitDelay;
      }

      
      X_SVmcPmm__HE110_UnitDelay1 = yVcPpmRc_B_ChangeOfMindInhibit;

      
      if (cVcVmcPmm_B_UseComInhbtIceStatus) {
         
         SVmcPmm__HE113_Switch = yVcEc_B_StartMotor || (((!(yVcPpmRc_B_ChangeOfMindInhibit)) ||
          (X_SVmcPmm__HE118_UnitDelay > cVcVmcPmm_t_ComInhbtIceStatus)) &&
          X_SVmcPmm__HE3_UnitDelay10);
      }
      else {
         
         SVmcPmm__HE113_Switch = X_SVmcPmm__HE3_UnitDelay10;
      }
      
      if (SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE2_Stopping) {
         

         
         if (xVcVmcPmm_B_EngStopped) {
            
            SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE2_Stopping = 0;
            SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE3_Stopped = 1;
            CVmcPmm__HE1_D_IceStatus = 0;
         }
         else {
            
            if (SVmcPmm__HE113_Switch) {
               
               SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE2_Stopping = 0;
               SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE5_Starting = 1;
               CVmcPmm__HE1_D_IceStatus = 1;
            }
         }
         
      }
      else {
         if (SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE3_Stopped) {
            

            
            if (SVmcPmm__HE113_Switch) {
               
               SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE3_Stopped = 0;
               SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE5_Starting = 1;
               CVmcPmm__HE1_D_IceStatus = 1;
            }
            
         }
         else {
            if (SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE4_Running) {
               

               
               if (!(SVmcPmm__HE113_Switch)) {
                  
                  SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE4_Running = 0;
                  SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE2_Stopping = 1;
                  CVmcPmm__HE1_D_IceStatus = 3;
               }
               
            }
            else {
               if (SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE5_Starting) {
                  

                  
                  if (xVcVmcPmm_B_EngRunning) {
                     
                     SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE5_Starting = 0;
                     SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE4_Running = 1;
                     CVmcPmm__HE1_D_IceStatus = 2;
                  }
                  else {
                     
                     if (!(SVmcPmm__HE113_Switch)) {
                        
                        SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE5_Starting = 0;
                        SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE2_Stopping = 1;
                        CVmcPmm__HE1_D_IceStatus = 3;
                     }
                  }
                  
               }
               else {
                  
                  SIBFS_1131_IceStatus_VmcPmm__HE.CVmcPmm__HE3_Stopped = 1;
                  CVmcPmm__HE1_D_IceStatus = 0;
               }
            }
         }
      }
      

      
      xVcVmcPmm_B_IceStartRun = (CVmcPmm__HE1_D_IceStatus == 1) || (CVmcPmm__HE1_D_IceStatus == 2);

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         xVcVmcPmm_B_EngRunReqDriver = SVmcPmm__HE257_Switch >= 1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqDriver = SVmcPmm__HE257_Switch == 2;
      }

      
      if (cVcVmcPmm_B_UsePsm) {
         
         SVmcPmm__HE242_Switch = sVcPpmPsm_D_EngRunReqPsm;
      }
      else {
         
         SVmcPmm__HE242_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         xVcVmcPmm_B_EngRunReqPsm = SVmcPmm__HE242_Switch >= 1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqPsm = SVmcPmm__HE242_Switch == 2;
      }

      
      if (cVcVmcPmm_B_UseEm) {
         
         SVmcPmm__HE301_Switch = sVcVmcEm_D_EngRunReqEm;
      }
      else {
         
         SVmcPmm__HE301_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         xVcVmcPmm_B_EngRunReqEm = SVmcPmm__HE301_Switch >= 1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqEm = SVmcPmm__HE301_Switch == 2;
      }
      #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
         
         if (ts_VcVmcPmm__HEP7 > cVcVmcPmm_tc_BcmLongAccFilt) {
            
            SVmcPmm__HE144_MinMax = ts_VcVmcPmm__HEP7;
         }
         else {
            SVmcPmm__HE144_MinMax = cVcVmcPmm_tc_BcmLongAccFilt;
         }
         if (1e-06F > SVmcPmm__HE144_MinMax) {
            SVmcPmm__HE144_MinMax = 1e-06F;
         }

         
         if (SVmcPmm__HE144_MinMax != 0.F) {
            
            SVmcPmm__HE144_Prod1 = ts_VcVmcPmm__HEP7 / SVmcPmm__HE144_MinMax;
         }
         else {
            
            if (ts_VcVmcPmm__HEP7 < 0.F) {
               SVmcPmm__HE144_Prod1 = -3.402823466e+38F;
            }
            else {
               SVmcPmm__HE144_Prod1 = 3.402823466e+38F;
            }
         }

         
         rVcVmcPmm_a_BcmLongAccFilt = X_SVmcPmm__HE144_Del1 + ((sVcVdm_a_ALgt -
          X_SVmcPmm__HE144_Del1) * SVmcPmm__HE144_Prod1);

         
         X_SVmcPmm__HE144_Del1 = rVcVmcPmm_a_BcmLongAccFilt;

         
         SVmcPmm__HE18_Product4 = sVcScIn_v_VehSpdLgt / 3.6F;

         
         if (X_SVmcPmm__HE141_Del2) {
            
            rVcVmcPmm_a_VehAccFilt = 0.F;
         }
         else {
            
            
            #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
               Float32 SVmcPmm__HE141_MinMax;
            #endif

            

            
            #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
               Float32 SVmcPmm__HE141_MinMax1;
            #endif

            

            
            #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
               Float32 SVmcPmm__HE141_Prod;
            #endif

            

            
            #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
               Float32 SVmcPmm__HE141_Prod1;
            #endif

            

            
            #if VcVmcPmm__HEP7_1150_Gradient_estimation_2
               Float32 SVmcPmm__HE141_Sum;
            #endif

            

            
            SVmcPmm__HE141_Sum = SVmcPmm__HE18_Product4 - X_SVmcPmm__HE141_Del;

            
            if (ts_VcVmcPmm__HEP7 > 1e-06F) {
               
               SVmcPmm__HE141_MinMax1 = ts_VcVmcPmm__HEP7;
            }
            else {
               SVmcPmm__HE141_MinMax1 = 1e-06F;
            }

            
            if (SVmcPmm__HE141_MinMax1 != 0.F) {
               SVmcPmm__HE141_Prod = SVmcPmm__HE141_Sum / SVmcPmm__HE141_MinMax1;
            }
            else {
               if (SVmcPmm__HE141_Sum < 0.F) {
                  SVmcPmm__HE141_Prod = -3.402823466e+38F;
               }
               else {
                  SVmcPmm__HE141_Prod = 3.402823466e+38F;
               }
            }

            
            if (ts_VcVmcPmm__HEP7 > cVcVmcPmm_tc_VehAccFilt) {
               
               SVmcPmm__HE141_MinMax = ts_VcVmcPmm__HEP7;
            }
            else {
               SVmcPmm__HE141_MinMax = cVcVmcPmm_tc_VehAccFilt;
            }
            if (1e-06F > SVmcPmm__HE141_MinMax) {
               SVmcPmm__HE141_MinMax = 1e-06F;
            }

            
            if (SVmcPmm__HE141_MinMax != 0.F) {
               
               SVmcPmm__HE141_Prod1 = ts_VcVmcPmm__HEP7 / SVmcPmm__HE141_MinMax;
            }
            else {
               
               if (ts_VcVmcPmm__HEP7 < 0.F) {
                  SVmcPmm__HE141_Prod1 = -3.402823466e+38F;
               }
               else {
                  SVmcPmm__HE141_Prod1 = 3.402823466e+38F;
               }
            }

            
            rVcVmcPmm_a_VehAccFilt = X_SVmcPmm__HE141_Del1 + ((SVmcPmm__HE141_Prod -
             X_SVmcPmm__HE141_Del1) * SVmcPmm__HE141_Prod1);
         }

         
         X_SVmcPmm__HE141_Del = SVmcPmm__HE18_Product4;

         
         X_SVmcPmm__HE141_Del1 = rVcVmcPmm_a_VehAccFilt;

         
         X_SVmcPmm__HE141_Del2 = 0;

         
         if (yVcScIn_B_VehSpdDirRvs && cVcVmcPmm_B_UseWhlSpdDirection) {
            
            rVcVmcPmm_a_SignedHGVehFilt = -1.F * rVcVmcPmm_a_VehAccFilt;
         }
         else {
            
            rVcVmcPmm_a_SignedHGVehFilt = rVcVmcPmm_a_VehAccFilt;
         }

         
         rVcVmcPmm_a_MergedAcc = rVcVmcPmm_a_BcmLongAccFilt - rVcVmcPmm_a_SignedHGVehFilt;
         if (cVcVmcPmm_a_HillGradientMax < rVcVmcPmm_a_MergedAcc) {
            SVmcPmm__HE152_MinMax = cVcVmcPmm_a_HillGradientMax;
         }
         else {
            SVmcPmm__HE152_MinMax = rVcVmcPmm_a_MergedAcc;
         }
         if (SVmcPmm__HE152_MinMax > cVcVmcPmm_a_HillGradientMin) {
            rVcVmcPmm_a_MergedAccSaturated = SVmcPmm__HE152_MinMax;
         }
         else {
            rVcVmcPmm_a_MergedAccSaturated = cVcVmcPmm_a_HillGradientMin;
         }

         
         if ((sVcVmm_D_CarModSts1 == 5) && cVcVmcPmm_B_UseDefHGDynoMd) {
            
            SVmcPmm__HE147_Switch = cVcVmcPmm_a_HillGradientFault;
         }
         else {
            
            SVmcPmm__HE147_Switch = rVcVmcPmm_a_MergedAccSaturated;
         }

         
         xVcVmcPmm_B_StandStill = sVcScIn_v_VehSpdLgt < cVcVmcPmm_v_StandStillLoLim;

         
         if (xVcVmcPmm_B_StandStill) {
            
            X_SVmcPmm__HE149_UnitDelay = X_SVmcPmm__HE149_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE149_UnitDelay = 0.F;
         }

         
         TabIdxS18T6((const Float32 *) &(mVcVmcPmm_tc_HillGradient_r[0]), 6, sVcScIn_v_VehSpdLgt,
          SVmcPmm__HE154___HillGradient_r);

         
         if (ts_VcVmcPmm__HEP7 > cVcVmcPmm_tc_BrkTrqFilt) {
            
            SVmcPmm__HE142_MinMax = ts_VcVmcPmm__HEP7;
         }
         else {
            SVmcPmm__HE142_MinMax = cVcVmcPmm_tc_BrkTrqFilt;
         }
         if (1e-06F > SVmcPmm__HE142_MinMax) {
            SVmcPmm__HE142_MinMax = 1e-06F;
         }

         
         if (SVmcPmm__HE142_MinMax != 0.F) {
            
            SVmcPmm__HE142_Prod1 = ts_VcVmcPmm__HEP7 / SVmcPmm__HE142_MinMax;
         }
         else {
            
            if (ts_VcVmcPmm__HEP7 < 0.F) {
               SVmcPmm__HE142_Prod1 = -3.402823466e+38F;
            }
            else {
               SVmcPmm__HE142_Prod1 = 3.402823466e+38F;
            }
         }

         
         rVcVmcPmm_Tq_BrkTrqFilt = X_SVmcPmm__HE142_Del1 + ((sVcDseWt_Tq_BrkFricTqAtWhl -
          X_SVmcPmm__HE142_Del1) * SVmcPmm__HE142_Prod1);

         
         X_SVmcPmm__HE142_Del1 = rVcVmcPmm_Tq_BrkTrqFilt;

         
         TabIdxS18T6((const Float32 *) &(mVcVmcPmm_tc_HillGradient_c[0]), 4,
          rVcVmcPmm_Tq_BrkTrqFilt, SVmcPmm__HE154___HillGradient_c);

         
         rVcVmcPmm_tc_HillGradient = Tab2DIntpI1T6((const Float32 *)
          &(mVcVmcPmm_tc_HillGradient[0][0]), 4, &(SVmcPmm__HE154___HillGradient_r[0]),
          &(SVmcPmm__HE154___HillGradient_c[0]));

         
         if (X_SVmcPmm__HE149_UnitDelay > cVcVmcPmm_t_StandStill) {
            
            rVcVmcPmm_tc_HillGadient = cVcVmcPmm_tc_StandStill;
         }
         else {
            
            rVcVmcPmm_tc_HillGadient = rVcVmcPmm_tc_HillGradient;
         }

         
         if (ts_VcVmcPmm__HEP7 > rVcVmcPmm_tc_HillGadient) {
            
            SVmcPmm__HE143_MinMax = ts_VcVmcPmm__HEP7;
         }
         else {
            SVmcPmm__HE143_MinMax = rVcVmcPmm_tc_HillGadient;
         }
         if (1e-06F > SVmcPmm__HE143_MinMax) {
            SVmcPmm__HE143_MinMax = 1e-06F;
         }

         
         if (SVmcPmm__HE143_MinMax != 0.F) {
            
            SVmcPmm__HE143_Prod1 = ts_VcVmcPmm__HEP7 / SVmcPmm__HE143_MinMax;
         }
         else {
            
            if (ts_VcVmcPmm__HEP7 < 0.F) {
               SVmcPmm__HE143_Prod1 = -3.402823466e+38F;
            }
            else {
               SVmcPmm__HE143_Prod1 = 3.402823466e+38F;
            }
         }

         
         rVcVmcPmm_a_MergedAccFilt = X_SVmcPmm__HE143_Del1 + ((SVmcPmm__HE147_Switch -
          X_SVmcPmm__HE143_Del1) * SVmcPmm__HE143_Prod1);

         
         X_SVmcPmm__HE143_Del1 = rVcVmcPmm_a_MergedAccFilt;

         
         TabIdxS18T390((const Float32 *) &(tVcVmcPmm_Z_HillGradAcc2deg_x[0]), 5,
          rVcVmcPmm_a_MergedAccFilt, SVmcPmm__HE153__llGradAcc2deg_x);

         
         SVmcPmm__HE153__HillGradAcc2deg = Tab1DIntpI1T54((const Float32 *)
          &(tVcVmcPmm_Z_HillGradAcc2deg[0]), &(SVmcPmm__HE153__llGradAcc2deg_x[0]));

         
         xVcVmcPmm_B_QfFaultLongAcc = (sVcVdm_Qf_ALgtQf != cVcVmcPmm_D_QfEpbLongAccOK) &&
          (sVcVdm_Qf_ALgtQf != cVcVmcPmm_D_QfEpbLongAccInit);

         
         xVcVmcPmm_B_QfFault = xVcVmcPmm_B_QfFaultLongAcc || (!(yVcScIn_B_VehSpdLgtOk));

         
         xVcVmcPmm_B_StopInhibitUpHill = (SVmcPmm__HE153__HillGradAcc2deg >=
          cVcVmcPmm_Z_SetLimUpHill) || ((SVmcPmm__HE153__HillGradAcc2deg >
          cVcVmcPmm_Z_ResetLimUpHill) && X_SVmcPmm__HE150_UnitDelay1);

         
         X_SVmcPmm__HE150_UnitDelay1 = xVcVmcPmm_B_StopInhibitUpHill;

         
         xVcVmcPmm_B_StopInhibitDownHill = (SVmcPmm__HE153__HillGradAcc2deg <=
          cVcVmcPmm_Z_SetLimDownHill) || ((SVmcPmm__HE153__HillGradAcc2deg <
          cVcVmcPmm_Z_ResetLimDownHill) && X_SVmcPmm__HE151_UnitDelay1);

         
         X_SVmcPmm__HE151_UnitDelay1 = xVcVmcPmm_B_StopInhibitDownHill;

         
         xVcVmcPmm_B_GradOutOfLim = xVcVmcPmm_B_StopInhibitUpHill ||
          xVcVmcPmm_B_StopInhibitDownHill;

         
         xVcVmcPmm_B_HGSpdOK = sVcScIn_v_VehSpdLgt < cVcVmcPmm_v_SpeedLimitHG;

         
         xVcVmcPmm_B_BrkHGStart = xVcVmcPmm_B_GradOutOfLim && xVcVmcPmm_B_HGSpdOK;

         
         if (xVcVmcPmm_B_QfFault) {
            
            xVcVmcPmm_B_BrkHillGradStart = cVcVmcPmm_B_BrkHillGradStart;
         }
         else {
            
            xVcVmcPmm_B_BrkHillGradStart = xVcVmcPmm_B_BrkHGStart;
         }
      #endif
      #if VcVmcPmm__HEP7_1140_Brake_1
         
         if (cVcVmcPmm_B_BrkEngRunReq) {
            
            SVmcPmm__HE128_Switch = sVcVdm_D_EngRunngReqByBrk;
         }
         else {
            
            SVmcPmm__HE128_Switch = 0;
         }

         
         if (!(yVcEc_B_BCMNodeAlive)) {
            
            X_SVmcPmm__HE137_UnitDelay = X_SVmcPmm__HE137_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE137_UnitDelay = 0.F;
         }

         
         if ((X_SVmcPmm__HE137_UnitDelay > cVcVmcPmm_t_BrkEngRunReqAlive) &&
          cVcVmcPmm_B_BrkEngRunReqAlive) {
            
            SVmcPmm__HE132_Switch = 2;
         }
         else {
            
            SVmcPmm__HE132_Switch = 0;
         }

         
         if (cVcVmcPmm_B_BrkUseNegVacuum) {
            
            SVmcPmm__HE130_Switch = -1.F * sVcVdm_p_PVac;
         }
         else {
            
            SVmcPmm__HE130_Switch = sVcVdm_p_PVac;
         }

         
         xVcVmcPmm_B_BrkVacuumStart = SVmcPmm__HE130_Switch > cVcVmcPmm_p_BrVacuum;

         
         if (xVcVmcPmm_B_BrkVacuumStart && cVcVmcPmm_B_BrkVacuum) {
            
            SVmcPmm__HE125_Switch = 2;
         }
         else {
            
            SVmcPmm__HE125_Switch = 0;
         }

         
         TabIdxS18T6((const Float32 *) &(tVcVmcPmm_p_BrVacuumVeh_x[0]), 7, sVcScIn_v_VehSpdLgt,
          SVmcPmm__HE138_p_BrVacuumVeh_x);

         
         rVcVmcPmm_p_BrVacuumVeh = Tab1DIntpI1T6((const Float32 *) &(tVcVmcPmm_p_BrVacuumVeh[0]),
          &(SVmcPmm__HE138_p_BrVacuumVeh_x[0]));

         
         xVcVmcPmm_B_BrkVacuumVeh = SVmcPmm__HE130_Switch > rVcVmcPmm_p_BrVacuumVeh;

         
         if (xVcVmcPmm_B_BrkVacuumVeh && cVcVmcPmm_B_BrkVacuumVeh) {
            
            SVmcPmm__HE129_Switch = 2;
         }
         else {
            
            SVmcPmm__HE129_Switch = 0;
         }

         
         if (SVmcPmm__HE125_Switch > SVmcPmm__HE129_Switch) {
            
            sVcVmcPmm_D_EngRunReqBrkVac = SVmcPmm__HE125_Switch;
         }
         else {
            
            sVcVmcPmm_D_EngRunReqBrkVac = SVmcPmm__HE129_Switch;
         }

         
         if (yVcVdm_B_AbsCtrlActv) {
            
            X_SVmcPmm__HE134_UnitDelay = 0.F;
         }
         else {
            
            X_SVmcPmm__HE134_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE134_UnitDelay;
         }

         
         if ((X_SVmcPmm__HE134_UnitDelay <= cVcVmcPmm_t_BrkAbs) && cVcVmcPmm_B_BrkAbs) {
            
            SVmcPmm__HE127_Switch = 2;
         }
         else {
            
            SVmcPmm__HE127_Switch = 0;
         }

         
         X_SVmcPmm__HE135_UnitDelay1 = (SVmcPmm__HE153__HillGradAcc2deg >=
          cVcVmcPmm_Z_BrkHGSkipParkDownL) || ((SVmcPmm__HE153__HillGradAcc2deg >
          cVcVmcPmm_Z_BrkHGSkipParkDownH) && X_SVmcPmm__HE135_UnitDelay1);

         
         X_SVmcPmm__HE136_UnitDelay1 = (SVmcPmm__HE153__HillGradAcc2deg <=
          cVcVmcPmm_Z_BrkHGSkipParkUpL) || ((SVmcPmm__HE153__HillGradAcc2deg <
          cVcVmcPmm_Z_BrkHGSkipParkUpH) && X_SVmcPmm__HE136_UnitDelay1);

         
         xVcVmcPmm_B_BrkHGSkipParkPre = yVcDtcAtr_B_AT && X_SVmcPmm__HE135_UnitDelay1 &&
          X_SVmcPmm__HE136_UnitDelay1;

         
         xVcVmcPmm_B_BrkHGSkipPark = (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATPark) &&
          xVcVmcPmm_B_BrkHGSkipParkPre && cVcVmcPmm_B_BrkHGSkipPark;

         
         if (xVcVmcPmm_B_BrkHillGradStart) {
            
            X_SVmcPmm__HE133_UnitDelay = 0.F;
         }
         else {
            
            X_SVmcPmm__HE133_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE133_UnitDelay;
         }

         
         if (xVcVmcPmm_B_BrkHGSkipPark) {
            
            SVmcPmm__HE131_Switch = 0;
         }
         else {
            
            SVmcPmm__HE131_Switch = X_SVmcPmm__HE133_UnitDelay <= cVcVmcPmm_t_BrkHillGrad;
         }

         
         if (SVmcPmm__HE131_Switch && cVcVmcPmm_B_BrkHillGrad) {
            
            sVcVmcPmm_D_EngRunReqHG = cVcVmcPmm_D_BrkHillVal;
         }
         else {
            
            sVcVmcPmm_D_EngRunReqHG = 0;
         }

         
         rVcVmcPmm_D_EngRunReqBrake = 0;
         if (SVmcPmm__HE128_Switch > rVcVmcPmm_D_EngRunReqBrake) {
            rVcVmcPmm_D_EngRunReqBrake = SVmcPmm__HE128_Switch;
         }
         if (SVmcPmm__HE132_Switch > rVcVmcPmm_D_EngRunReqBrake) {
            rVcVmcPmm_D_EngRunReqBrake = SVmcPmm__HE132_Switch;
         }

         
         if (sVcVmcPmm_D_EngRunReqBrkVac > rVcVmcPmm_D_EngRunReqBrake) {
            
            rVcVmcPmm_D_EngRunReqBrake = sVcVmcPmm_D_EngRunReqBrkVac;
         }

         
         if (SVmcPmm__HE127_Switch > rVcVmcPmm_D_EngRunReqBrake) {
            rVcVmcPmm_D_EngRunReqBrake = SVmcPmm__HE127_Switch;
         }

         
         if (sVcVmcPmm_D_EngRunReqHG > rVcVmcPmm_D_EngRunReqBrake) {
            
            rVcVmcPmm_D_EngRunReqBrake = sVcVmcPmm_D_EngRunReqHG;
         }
      #endif

      
      if (cVcVmcPmm_B_UseBrake) {
         
         SVmcPmm__HE268_Switch = rVcVmcPmm_D_EngRunReqBrake;
      }
      else {
         
         SVmcPmm__HE268_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         yVcVmcPmm_B_EngRunReqBrake = SVmcPmm__HE268_Switch >= 1;
      }
      else {
         
         yVcVmcPmm_B_EngRunReqBrake = SVmcPmm__HE268_Switch == 2;
      }

      
      if (cVcVmcPmm_B_UseSapp) {
         
         SVmcPmm__HE290_Switch = sVcAsy_D_EngRunngReqByParkAssi;
      }
      else {
         
         SVmcPmm__HE290_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         yVcVmcPmm_B_EngRunReqSapp = SVmcPmm__HE290_Switch >= 1;
      }
      else {
         
         yVcVmcPmm_B_EngRunReqSapp = SVmcPmm__HE290_Switch == 2;
      }

      
      if (cVcVmcPmm_B_UseTrans) {
         
         SVmcPmm__HE307_Switch = sVcDseGb_D_TrsmEngRunReq;
      }
      else {
         
         SVmcPmm__HE307_Switch = 0;
      }

      
      if ((CVmcPmm__HE1_D_IceStatus == 2) || (CVmcPmm__HE1_D_IceStatus == 1)) {
         
         SVmcPmm__HE352_Switch = SVmcPmm__HE307_Switch >= 1;
      }
      else {
         
         SVmcPmm__HE352_Switch = SVmcPmm__HE307_Switch == 2;
      }

      
      SVmcPmm__HE205__tionalOperator1 = CVmcPmm__HE1_D_IceStatus == 0;

      
      SVmcPmm__HE205_LogicalOperator1 = SVmcPmm__HE352_Switch && (!(X_SVmcPmm__HE350_UnitDelay1)) &&
        SVmcPmm__HE205__tionalOperator1 && cVcVmcPmm_B_GlitchEngOnTrans;

      
      X_SVmcPmm__HE350_UnitDelay1 = SVmcPmm__HE352_Switch;

      
      if (SVmcPmm__HE205_LogicalOperator1 && (!(X_SVmcPmm__HE349_UnitDelay1))) {
         
         X_SVmcPmm__HE354_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE354_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE354_UnitDelay;
      }

      
      X_SVmcPmm__HE349_UnitDelay1 = SVmcPmm__HE205_LogicalOperator1;

      
      xVcVmcPmm_B_TransEngOnBlock = X_SVmcPmm__HE354_UnitDelay <= cVcVmcPmm_t_GlitchEngOnTrans;

      
      SVmcPmm__HE205_LogicalOperator4 = SVmcPmm__HE205__tionalOperator1 || (CVmcPmm__HE1_D_IceStatus
        == 3);

      
      SVmcPmm__HE205__gicalOperator12 = SVmcPmm__HE205_LogicalOperator4 && (SVmcPmm__HE307_Switch ==
        0) && cVcVmcPmm_B_MinStopTrans;

      
      if (SVmcPmm__HE205__gicalOperator12 && (!(X_SVmcPmm__HE351_UnitDelay1))) {
         
         X_SVmcPmm__HE355_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE355_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE355_UnitDelay;
      }

      
      X_SVmcPmm__HE351_UnitDelay1 = SVmcPmm__HE205__gicalOperator12;

      
      xVcVmcPmm_B_TransBlocking = X_SVmcPmm__HE355_UnitDelay <= cVcVmcPmm_t_MinStopTrans;

      
      xVcVmcPmm_B_TransBlock = SVmcPmm__HE205_LogicalOperator4 && xVcVmcPmm_B_TransBlocking;

      
      if (xVcVmcPmm_B_TransEngOnBlock || xVcVmcPmm_B_TransBlock) {
         
         yVcVmcPmm_B_EngRunReqTrans = 0;
      }
      else {
         
         yVcVmcPmm_B_EngRunReqTrans = SVmcPmm__HE352_Switch;
      }

      
      SVmcPmm__HE206_LogicalOperator1 = (CVmcPmm__HE1_D_IceStatus == 0) || (CVmcPmm__HE1_D_IceStatus
        == 3);

      
      if (cVcVmcPmm_B_UseEMS) {
         
         SVmcPmm__HE308_Switch = sVcEc_D_EngRunReqEMS;
      }
      else {
         
         SVmcPmm__HE308_Switch = 0;
      }

      
      SVmcPmm__HE206__gicalOperator12 = SVmcPmm__HE206_LogicalOperator1 && (SVmcPmm__HE308_Switch ==
        0) && cVcVmcPmm_B_MinStopEMS;

      
      if (SVmcPmm__HE206__gicalOperator12 && (!(X_SVmcPmm__HE356_UnitDelay1))) {
         
         X_SVmcPmm__HE359_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE359_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE359_UnitDelay;
      }

      
      X_SVmcPmm__HE356_UnitDelay1 = SVmcPmm__HE206__gicalOperator12;

      
      xVcVmcPmm_B_EMSBlocked = X_SVmcPmm__HE359_UnitDelay <= cVcVmcPmm_t_MinStopEMS;

      
      xVcVmcPmm_B_EMSBlock = SVmcPmm__HE206_LogicalOperator1 && xVcVmcPmm_B_EMSBlocked;

      
      if (xVcVmcPmm_B_EMSBlock) {
         
         yVcVmcPmm_B_EngRunReqEms = 0;
      }
      else {
         
         if ((CVmcPmm__HE1_D_IceStatus == 2) || (CVmcPmm__HE1_D_IceStatus == 1)) {
            
            yVcVmcPmm_B_EngRunReqEms = SVmcPmm__HE308_Switch >= 1;
         }
         else {
            
            yVcVmcPmm_B_EngRunReqEms = SVmcPmm__HE308_Switch == 2;
         }
      }

      
      SVmcPmm__HE207_LogicalOperator1 = (CVmcPmm__HE1_D_IceStatus == 0) || (CVmcPmm__HE1_D_IceStatus
        == 3);

      
      if (yVcCem_B_StopStrtReq1WdReq) {
         
         SVmcPmm__HE843_Switch = 2;
      }
      else {
         
         if (yVcCem_B_StrtInhbReq1WdReq) {
            
            SVmcPmm__HE843_Switch = 1;
         }
         else {
            
            SVmcPmm__HE843_Switch = 0;
         }
      }

      
      if (yVcCem_B_EngRunngReqByVehModMgrElectricalSystem) {
         
         SVmcPmm__HE845_Switch = 2;
      }
      else {
         
         SVmcPmm__HE845_Switch = 0;
      }

      
      if (SVmcPmm__HE843_Switch > SVmcPmm__HE845_Switch) {
         
         sVcVmcPmm_D_EngRunReqEmLv = SVmcPmm__HE843_Switch;
      }
      else {
         
         sVcVmcPmm_D_EngRunReqEmLv = SVmcPmm__HE845_Switch;
      }

      
      if (cVcVmcPmm_B_UseEmLv) {
         
         SVmcPmm__HE237_Switch = sVcVmcPmm_D_EngRunReqEmLv;
      }
      else {
         
         SVmcPmm__HE237_Switch = 0;
      }

      
      SVmcPmm__HE207__gicalOperator12 = SVmcPmm__HE207_LogicalOperator1 && (SVmcPmm__HE237_Switch ==
        0) && cVcVmcPmm_B_MinStopEmLv;

      
      if (SVmcPmm__HE207__gicalOperator12 && (!(X_SVmcPmm__HE360_UnitDelay1))) {
         
         X_SVmcPmm__HE363_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE363_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE363_UnitDelay;
      }

      
      X_SVmcPmm__HE360_UnitDelay1 = SVmcPmm__HE207__gicalOperator12;

      
      xVcVmcPmm_B_EmLvBlocked = X_SVmcPmm__HE363_UnitDelay <= cVcVmcPmm_t_MinStopEmLv;

      
      if (SVmcPmm__HE207_LogicalOperator1 && xVcVmcPmm_B_EmLvBlocked) {
         
         yVcVmcPmm_B_EngRunReqEmLv = 0;
      }
      else {
         
         if ((CVmcPmm__HE1_D_IceStatus == 2) || (CVmcPmm__HE1_D_IceStatus == 1)) {
            
            yVcVmcPmm_B_EngRunReqEmLv = SVmcPmm__HE237_Switch >= 1;
         }
         else {
            
            yVcVmcPmm_B_EngRunReqEmLv = SVmcPmm__HE237_Switch == 2;
         }
      }

      
      SVmcPmm__HE208_LogicalOperator1 = (CVmcPmm__HE1_D_IceStatus == 0) || (CVmcPmm__HE1_D_IceStatus
        == 3);

      
      if (yVcCem_B_EngRunngReqByVehModMgrClimate) {
         
         SVmcPmm__HE846_Switch = 2;
      }
      else {
         
         SVmcPmm__HE846_Switch = 0;
      }

      
      if (sVcCcm_D_EngRunngReqByClima > SVmcPmm__HE846_Switch) {
         
         sVcVmcPmm_D_EngRunReqClim = sVcCcm_D_EngRunngReqByClima;
      }
      else {
         
         sVcVmcPmm_D_EngRunReqClim = SVmcPmm__HE846_Switch;
      }

      
      if (cVcVmcPmm_B_UseClim) {
         
         SVmcPmm__HE236_Switch = sVcVmcPmm_D_EngRunReqClim;
      }
      else {
         
         SVmcPmm__HE236_Switch = 0;
      }

      
      SVmcPmm__HE208__gicalOperator12 = SVmcPmm__HE208_LogicalOperator1 && (SVmcPmm__HE236_Switch ==
        0) && cVcVmcPmm_B_MinStopClim;

      
      if (SVmcPmm__HE208__gicalOperator12 && (!(X_SVmcPmm__HE364_UnitDelay1))) {
         
         X_SVmcPmm__HE367_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE367_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE367_UnitDelay;
      }

      
      X_SVmcPmm__HE364_UnitDelay1 = SVmcPmm__HE208__gicalOperator12;

      
      xVcVmcPmm_B_ClimBlocked = X_SVmcPmm__HE367_UnitDelay <= cVcVmcPmm_t_MinStopClim;

      
      if (SVmcPmm__HE208_LogicalOperator1 && xVcVmcPmm_B_ClimBlocked) {
         
         yVcVmcPmm_B_EngRunReqClim = 0;
      }
      else {
         
         if ((CVmcPmm__HE1_D_IceStatus == 2) || (CVmcPmm__HE1_D_IceStatus == 1)) {
            
            yVcVmcPmm_B_EngRunReqClim = SVmcPmm__HE236_Switch >= 1;
         }
         else {
            
            yVcVmcPmm_B_EngRunReqClim = SVmcPmm__HE236_Switch == 2;
         }
      }

      
      if (cVcVmcPmm_B_UseLOS) {
         
         SVmcPmm__HE239_Switch = sVcDsePcr_D_EngRunRq;
      }
      else {
         
         SVmcPmm__HE239_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         xVcVmcPmm_B_EngRunReqPcr = SVmcPmm__HE239_Switch >= 1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqPcr = SVmcPmm__HE239_Switch == 2;
      }

      
      if (cVcVmcPmm_B_EngineArchitecture) {
         
         SVmcPmm__HE848_Switch = sVcEc_Te_EngClnt;
      }
      else {
         
         SVmcPmm__HE848_Switch = sVcEc_Te_EngCooltT;
      }
      if (Vc_Pvc_Hw_B_HVSystem_CN != 0) {
         
         if (cVcVmcPmm_B_DrLeaveEnable) {
            
            Bool SVmcPmm__HE157_LogOp3;

            if (!(SVmcPmm__HE157_RSWE)) {
               
               INIT_SVmcPmm____verLeaveVehicle();

               
               SVmcPmm__HE157_RSWE = 1;
            }
            
            if (yVcPpmPsm_B_DriveCycleActive) {
               
               X_SVmcPmm__HE163_UnitDelay = X_SVmcPmm__HE163_UnitDelay + ts_VcVmcPmm__HEP7;
            }
            else {
               
               X_SVmcPmm__HE163_UnitDelay = 0.F;
            }

            
            SVmcPmm__HE157_LogOp3 = (!(yVcScDep_B_DrvrPrsnt)) && (X_SVmcPmm__HE163_UnitDelay >
             cVcVmcPmm_t_DrLeaveDCADly) && (sVcScIn_v_VehSpdLgtMax < cVcVmcPmm_v_DrLeaveLim);

            
            if (SVmcPmm__HE157_LogOp3 && cVcVmcPmm_B_DrLeavePowerDown) {
               
               X_SVmcPmm__HE164_UnitDelay = X_SVmcPmm__HE164_UnitDelay + ts_VcVmcPmm__HEP7;
            }
            else {
               
               X_SVmcPmm__HE164_UnitDelay = 0.F;
            }

            
            xVcVmcPmm_B_DrLeavePowerDownReq = X_SVmcPmm__HE164_UnitDelay >
             cVcVmcPmm_t_DrLeavePwrDwnDly;

            
            xVcVmcPmm_B_DrLeaveKeepRun = SVmcPmm__HE157_LogOp3 && cVcVmcPmm_B_DrLeaveKeepRunReq;

            
            if (xVcVmcPmm_B_DrLeaveKeepRun) {
               
               rVcVmcPmm_D_EngRunReqDrLeave = 1;
            }
            else {
               
               rVcVmcPmm_D_EngRunReqDrLeave = 0;
            }

            
            if (SVmcPmm__HE157_LogOp3 && (CVmcPmm__HE1_D_IceStatus != 2) &&
             yVcDseEm_B_EngRunReqSocMin) {
               
               X_SVmcPmm__HE165_UnitDelay = X_SVmcPmm__HE165_UnitDelay + ts_VcVmcPmm__HEP7;
            }
            else {
               
               X_SVmcPmm__HE165_UnitDelay = 0.F;
            }

            
            yVcVmcPmm_B_AutoParkReq = X_SVmcPmm__HE165_UnitDelay > cVcVmcPmm_t_DrLeaveAutoParkReq;
         }
         else {
            
            SVmcPmm__HE157_RSWE = 0;
         }

         
         if (cVcVmcPmm_B_FCAdaptEnable) {
            
            Bool SVmcPmm__HE156_LogicalOperator2;
            Bool SVmcPmm__HE156_LogicalOperator3;
            Bool SVmcPmm__HE156_LogicalOperator5;
            Bool SVmcPmm__HE156__gicalOperator18;

            if (!(SVmcPmm__HE156_RSWE)) {
               
               INIT_SVmcPmm_____FuelCutRequest();

               
               SVmcPmm__HE156_RSWE = 1;
            }
            
            SVmcPmm__HE156_LogicalOperator2 = (cVcVmcPmm_B_UseEmiGpfFC &&
             yVcEmiGpf_B_FuelCutReqHybrid) || yVcObdSch_B_FuelCutReq;

            
            SVmcPmm__HE156__gicalOperator18 = (!(SVmcPmm__HE156_LogicalOperator2)) ||
             (sVcDtcAtr_D_LockUp < cVcVmcPmm_D_FCAdaptLockUpRst) || (sVcDtcAtr_D_TrgGear <
             cVcVmcPmm_D_FCAdaptGearRst) || (sVcEc_n_Eng < cVcVmcPmm_n_FCAdaptEngRst) ||
             (sVcScIn_v_VehSpdLgt < cVcVmcPmm_v_FCAdaptVehRst) || (SVmcPmm__HE848_Switch <
             cVcVmcPmm_Te_FCAdaptEngClntRst) || ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATPark) ||
             (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATNeutral));

            
            SVmcPmm__HE156_LogicalOperator3 = SVmcPmm__HE156_LogicalOperator2 && (sVcDtcAtr_D_LockUp
              >= cVcVmcPmm_D_FCAdaptLockUpSet) && (sVcDtcAtr_D_TrgGear >=
             cVcVmcPmm_D_FCAdaptGearSet) && (sVcEc_n_Eng >= cVcVmcPmm_n_FCAdaptEngSet) &&
             (sVcScIn_v_VehSpdLgt >= cVcVmcPmm_v_FCAdaptVehSet) && (SVmcPmm__HE848_Switch >=
             cVcVmcPmm_Te_FCAdaptEngClntSet) && (!(SVmcPmm__HE156__gicalOperator18));

            
            SVmcPmm__HE159_LogOp3 = SVmcPmm__HE156_LogicalOperator3 ||
             ((!(SVmcPmm__HE156__gicalOperator18)) && X_SVmcPmm__HE159_UnitDelay1);

            
            X_SVmcPmm__HE159_UnitDelay1 = SVmcPmm__HE159_LogOp3;

            
            SVmcPmm__HE156_LogicalOperator5 = yVcDtcTc_B_FcReq || cVcVmcPmm_B_FCAdaptIdle;

            
            if (!(SVmcPmm__HE156_LogicalOperator5)) {
               
               X_SVmcPmm__HE161_UnitDelay = X_SVmcPmm__HE161_UnitDelay + ts_VcVmcPmm__HEP7;
            }
            else {
               
               X_SVmcPmm__HE161_UnitDelay = 0.F;
            }

            
            xVcVmcPmm_B_FCAdaptAct = (SVmcPmm__HE156_LogicalOperator3 &&
             SVmcPmm__HE156_LogicalOperator5) || ((X_SVmcPmm__HE161_UnitDelay <=
             cVcVmcPmm_t_FCAdaptIdleDelayOff) && (!(SVmcPmm__HE156__gicalOperator18)) &&
             X_SVmcPmm__HE160_UnitDelay1);

            
            X_SVmcPmm__HE160_UnitDelay1 = xVcVmcPmm_B_FCAdaptAct;

            
            if (xVcVmcPmm_B_FCAdaptAct) {
               
               rVcVmcPmm_D_EngRunReqFCAdapt = 1;
            }
            else {
               
               rVcVmcPmm_D_EngRunReqFCAdapt = 0;
            }
         }
         else {
            
            SVmcPmm__HE156_RSWE = 0;
         }
      }
      else {
         
         SVmcPmm__HE156_RSWE = 0;

         
         SVmcPmm__HE157_RSWE = 0;
      }

      
      if (cVcVmcPmm_B_UseFCAdapt) {
         
         SVmcPmm__HE250_Switch = rVcVmcPmm_D_EngRunReqFCAdapt;
      }
      else {
         
         SVmcPmm__HE250_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         xVcVmcPmm_B_EngRunReqFCAdapt = SVmcPmm__HE250_Switch >= 1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqFCAdapt = SVmcPmm__HE250_Switch == 2;
      }

      
      SVmcPmm__HE210_LogicalOperator1 = (CVmcPmm__HE1_D_IceStatus == 0) || (CVmcPmm__HE1_D_IceStatus
        == 3);

      
      if (cVcVmcPmm_B_UseTm) {
         
         SVmcPmm__HE253_Switch = sVcTmStrt_D_EngRunReqTm;
      }
      else {
         
         SVmcPmm__HE253_Switch = 0;
      }

      
      SVmcPmm__HE210__gicalOperator12 = SVmcPmm__HE210_LogicalOperator1 && (SVmcPmm__HE253_Switch ==
        0) && cVcVmcPmm_B_MinStopTm;

      
      if (SVmcPmm__HE210__gicalOperator12 && (!(X_SVmcPmm__HE369_UnitDelay1))) {
         
         X_SVmcPmm__HE372_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE372_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE372_UnitDelay;
      }

      
      X_SVmcPmm__HE369_UnitDelay1 = SVmcPmm__HE210__gicalOperator12;

      
      xVcVmcPmm_B_TmBlocked = X_SVmcPmm__HE372_UnitDelay <= cVcVmcPmm_t_MinStopTm;

      
      xVcVmcPmm_B_TmBlock = SVmcPmm__HE210_LogicalOperator1 && xVcVmcPmm_B_TmBlocked;

      
      if (xVcVmcPmm_B_TmBlock) {
         
         yVcVmcPmm_B_EngRunReqTm = 0;
      }
      else {
         
         if ((CVmcPmm__HE1_D_IceStatus == 2) || (CVmcPmm__HE1_D_IceStatus == 1)) {
            
            yVcVmcPmm_B_EngRunReqTm = SVmcPmm__HE253_Switch >= 1;
         }
         else {
            
            yVcVmcPmm_B_EngRunReqTm = SVmcPmm__HE253_Switch == 2;
         }
      }

      
      if (cVcVmcPmm_B_UseAgedFuel) {
         
         SVmcPmm__HE254_Switch = sVcFsdPc_D_EngRunReqFuel;
      }
      else {
         
         SVmcPmm__HE254_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         yVcVmcPmm_B_EngRunReqFuel = SVmcPmm__HE254_Switch >= 1;
      }
      else {
         
         yVcVmcPmm_B_EngRunReqFuel = SVmcPmm__HE254_Switch == 2;
      }

      
      if (cVcVmcPmm_B_UseIsg) {
         
         SVmcPmm__HE255_Switch = X_SVmcPmm__HE6_UnitDelay3;
      }
      else {
         
         SVmcPmm__HE255_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         xVcVmcPmm_B_EngRunReqIsg = SVmcPmm__HE255_Switch >= 1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqIsg = SVmcPmm__HE255_Switch == 2;
      }

      
      if (cVcVmcPmm_B_UseRemoteStart) {
         
         SVmcPmm__HE256_Switch = sVcPpmPsm_D_EngRunReqRemote;
      }
      else {
         
         SVmcPmm__HE256_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         xVcVmcPmm_B_EngRunReqRemote = SVmcPmm__HE256_Switch >= 1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqRemote = SVmcPmm__HE256_Switch == 2;
      }

      
      if (cVcVmcPmm_B_UseStabCtrl) {
         
         SVmcPmm__HE258_Switch = sVcVmcAwd_D_EngRunReqStabCtrl;
      }
      else {
         
         SVmcPmm__HE258_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         xVcVmcPmm_B_EngRunReqStabCtrl = SVmcPmm__HE258_Switch >= 1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqStabCtrl = SVmcPmm__HE258_Switch == 2;
      }

      
      if (cVcVmcPmm_B_UseDrLeave) {
         
         SVmcPmm__HE284_Switch = rVcVmcPmm_D_EngRunReqDrLeave;
      }
      else {
         
         SVmcPmm__HE284_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         xVcVmcPmm_B_EngRunReqDrLeave = SVmcPmm__HE284_Switch >= 1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqDrLeave = SVmcPmm__HE284_Switch == 2;
      }

      
      SVmcPmm__HE216_LogicalOperator1 = (CVmcPmm__HE1_D_IceStatus == 0) || (CVmcPmm__HE1_D_IceStatus
        == 3);

      
      if (yVcCem_B_EngRunngReqByVehModMgrChassie) {
         
         rVcVmcPmm_D_EngRunReqChas = 2;
      }
      else {
         
         rVcVmcPmm_D_EngRunReqChas = 0;
      }

      
      if (cVcVmcPmm_B_UseChas) {
         
         SVmcPmm__HE285_Switch = rVcVmcPmm_D_EngRunReqChas;
      }
      else {
         
         SVmcPmm__HE285_Switch = 0;
      }

      
      SVmcPmm__HE216__gicalOperator12 = SVmcPmm__HE216_LogicalOperator1 && (SVmcPmm__HE285_Switch ==
        0) && cVcVmcPmm_B_MinStopChas;

      
      if (SVmcPmm__HE216__gicalOperator12 && (!(X_SVmcPmm__HE378_UnitDelay1))) {
         
         X_SVmcPmm__HE381_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE381_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE381_UnitDelay;
      }

      
      X_SVmcPmm__HE378_UnitDelay1 = SVmcPmm__HE216__gicalOperator12;

      
      xVcVmcPmm_B_ChasBlocked = X_SVmcPmm__HE381_UnitDelay <= cVcVmcPmm_t_MinStopChas;

      
      if (SVmcPmm__HE216_LogicalOperator1 && xVcVmcPmm_B_ChasBlocked) {
         
         xVcVmcPmm_B_EngRunReqChas = 0;
      }
      else {
         
         if ((CVmcPmm__HE1_D_IceStatus == 2) || (CVmcPmm__HE1_D_IceStatus == 1)) {
            
            xVcVmcPmm_B_EngRunReqChas = SVmcPmm__HE285_Switch >= 1;
         }
         else {
            
            xVcVmcPmm_B_EngRunReqChas = SVmcPmm__HE285_Switch == 2;
         }
      }

      
      if (cVcVmcPmm_B_UseObd) {
         
         SVmcPmm__HE295_Switch = sVcObdSch_D_EngRunReqObd;
      }
      else {
         
         SVmcPmm__HE295_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         yVcVmcPmm_B_EngRunReqObd = SVmcPmm__HE295_Switch >= 1;
      }
      else {
         
         yVcVmcPmm_B_EngRunReqObd = SVmcPmm__HE295_Switch == 2;
      }

      
      if (cVcVmcPmm_B_UseDep) {
         
         SVmcPmm__HE299_Switch = sVcScIn_D_EngRunReqDepTrq;
      }
      else {
         
         SVmcPmm__HE299_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         xVcVmcPmm_B_EngRunReqDep = SVmcPmm__HE299_Switch >= 1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqDep = SVmcPmm__HE299_Switch == 2;
      }

      
      SVmcPmm__HE219_LogicalOperator1 = (CVmcPmm__HE1_D_IceStatus == 0) || (CVmcPmm__HE1_D_IceStatus
        == 3);

      
      if (cVcVmcPmm_B_UseCEC) {
         
         SVmcPmm__HE296_Switch = sVcCmnEngRunReqCEC_D_Req;
      }
      else {
         
         SVmcPmm__HE296_Switch = 0;
      }

      
      SVmcPmm__HE219__gicalOperator12 = SVmcPmm__HE219_LogicalOperator1 && (SVmcPmm__HE296_Switch ==
        0) && cVcVmcPmm_B_MinStopCEC;

      
      if (SVmcPmm__HE219__gicalOperator12 && (!(X_SVmcPmm__HE384_UnitDelay1))) {
         
         X_SVmcPmm__HE387_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE387_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE387_UnitDelay;
      }

      
      X_SVmcPmm__HE384_UnitDelay1 = SVmcPmm__HE219__gicalOperator12;

      
      xVcVmcPmm_B_CECBlocked = X_SVmcPmm__HE387_UnitDelay <= cVcVmcPmm_t_MinStopCEC;

      
      xVcVmcPmm_B_CECBlock = SVmcPmm__HE219_LogicalOperator1 && xVcVmcPmm_B_CECBlocked;

      
      if (xVcVmcPmm_B_CECBlock) {
         
         xVcVmcPmm_B_EngRunReqCEC = 0;
      }
      else {
         
         if ((CVmcPmm__HE1_D_IceStatus == 2) || (CVmcPmm__HE1_D_IceStatus == 1)) {
            
            xVcVmcPmm_B_EngRunReqCEC = SVmcPmm__HE296_Switch >= 1;
         }
         else {
            
            xVcVmcPmm_B_EngRunReqCEC = SVmcPmm__HE296_Switch == 2;
         }
      }

      
      if (cVcVmcPmm_B_UseRc) {
         
         SVmcPmm__HE262_Switch = sVcPpmRc_D_EngRunReqRc;
      }
      else {
         
         SVmcPmm__HE262_Switch = 0;
      }

      
      if (xVcVmcPmm_B_IceStartRun) {
         
         yVcVmcPmm_B_EngRunReqRc = SVmcPmm__HE262_Switch >= 1;
      }
      else {
         
         yVcVmcPmm_B_EngRunReqRc = SVmcPmm__HE262_Switch == 2;
      }

      
      if (cVcVmcPmm_B_StallRunHiRes) {
         
         SVmcPmm__HE561_Switch = sVcEc_n_EngHiRes;
      }
      else {
         
         SVmcPmm__HE561_Switch = sVcEc_n_Eng;
      }

      
      if (cVcVmcPmm_B_StallRunStartM) {
         
         SVmcPmm__HE562_Switch = !(yVcEc_B_StartMotor);
      }
      else {
         
         SVmcPmm__HE562_Switch = 1;
      }

      
      if (yVcPpmRc_B_ChangeOfMindInhibit && (!(X_SVmcPmm__HE529_UnitDelay1))) {
         
         X_SVmcPmm__HE579_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE579_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE579_UnitDelay;
      }

      
      X_SVmcPmm__HE529_UnitDelay1 = yVcPpmRc_B_ChangeOfMindInhibit;

      
      if (cVcVmcPmm_B_StallRunComInhbt) {
         
         xVcVmcPmm_B_StallRunComInhbt = (!(yVcPpmRc_B_ChangeOfMindInhibit)) ||
          (X_SVmcPmm__HE579_UnitDelay > cVcVmcPmm_t_StallRunComInhbt);
      }
      else {
         
         xVcVmcPmm_B_StallRunComInhbt = 1;
      }

      
      SVmcPmm__HE172_LogOp1 = (SVmcPmm__HE561_Switch < cVcVmcPmm_n_EngStalled) &&
       X_SVmcPmm__HE6_UnitDelay14 && (CVmcPmm__HE1_D_IceStatus == 2) && SVmcPmm__HE562_Switch &&
       xVcVmcPmm_B_StallRunComInhbt;

      
      if (SVmcPmm__HE172_LogOp1) {
         
         X_SVmcPmm__HE582_UnitDelay = X_SVmcPmm__HE582_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE582_UnitDelay = 0.F;
      }

      
      if (cVcVmcPmm_B_StallRun) {
         
         xVcVmcPmm_B_StallRunning = X_SVmcPmm__HE582_UnitDelay > cVcVmcPmm_t_StallRun;
      }
      else {
         
         xVcVmcPmm_B_StallRunning = 0;
      }

      
      if ((!(yVcPpmPsm_B_DrReady)) && yVcEc_B_StartMotor) {
         
         X_SVmcPmm__HE583_UnitDelay = X_SVmcPmm__HE583_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE583_UnitDelay = 0.F;
      }

      
      if (cVcVmcPmm_B_StallStartM) {
         
         xVcVmcPmm_B_StallStrtM = X_SVmcPmm__HE583_UnitDelay > cVcVmcPmm_t_StallStrtM;
      }
      else {
         
         xVcVmcPmm_B_StallStrtM = 0;
      }

      
      if ((!(yVcPpmPsm_B_DrReady)) && (CVmcPmm__HE1_D_IceStatus == 1) && (X_SVmcPmm__HE6_UnitDelay1
       != 0)) {
         
         X_SVmcPmm__HE594_UnitDelay = X_SVmcPmm__HE594_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE594_UnitDelay = 0.F;
      }

      
      if (cVcVmcPmm_B_StallIceStrt) {
         
         Float32 SVmcPmm__HE570_Switch;

         
         if (cVcVmcPmm_B_Use7DCT && X_SVmcPmm__HE6_UnitDelay10 && ((sVcDtcAtr_D_GearLevAT ==
          cVc_D_GearLevATDrive) || (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATReverse))) {
            
            SVmcPmm__HE570_Switch = cVcVmcPmm_t_StallIceStrtIsgDrv;
         }
         else {
            
            SVmcPmm__HE570_Switch = cVcVmcPmm_t_StallIceStrt;
         }

         
         xVcVmcPmm_B_StallIceStrt = X_SVmcPmm__HE594_UnitDelay > SVmcPmm__HE570_Switch;
      }
      else {
         
         xVcVmcPmm_B_StallIceStrt = 0;
      }

      
      SVmcPmm__HE172_LogOp47 = (!(yVcPpmPsm_B_DrReady)) && (CVmcPmm__HE1_D_IceStatus == 1) &&
       (X_SVmcPmm__HE6_UnitDelay1 == 0);

      
      if (SVmcPmm__HE172_LogOp47) {
         
         X_SVmcPmm__HE599_UnitDelay = X_SVmcPmm__HE599_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE599_UnitDelay = 0.F;
      }

      
      if (sVcEc_n_Eng < cVcVmcPmm_n_StallEmiMinEngSpd) {
         
         X_SVmcPmm__HE597_UnitDelay = X_SVmcPmm__HE597_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE597_UnitDelay = 0.F;
      }

      
      if (SVmcPmm__HE172_LogOp47 && (X_SVmcPmm__HE597_UnitDelay > cVcVmcPmm_t_StallEmiMinEngSpd) &&
       cVcVmcPmm_B_StallEmiExtraCond) {
         
         X_SVmcPmm__HE598_UnitDelay = X_SVmcPmm__HE598_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE598_UnitDelay = 0.F;
      }

      
      if (cVcVmcPmm_B_StallIceStrtEmi) {
         
         xVcVmcPmm_B_StallIceStrtEmi = (X_SVmcPmm__HE599_UnitDelay > cVcVmcPmm_t_StallIceStrtEmi) ||
           (X_SVmcPmm__HE598_UnitDelay > cVcVmcPmm_t_StallIceStrtEmiExtra);
      }
      else {
         
         xVcVmcPmm_B_StallIceStrtEmi = 0;
      }

      
      SVmcPmm__HE172_LogOp48 = yVcEc_B_StartMotor || yVcDtcSt_B_StrtAct || yVcDtcSt_B_CluStrtAct;

      
      if (cVcVmcPmm_B_UseIceEnable) {
         
         SVmcPmm__HE829_Switch = yVcPpmPsm_B_IceEnabled;
      }
      else {
         
         SVmcPmm__HE829_Switch = yVcPpmPsm_B_DriveCycleActive;
      }

      
      X_SVmcPmm__HE592_UnitDelay1 = ((!(yVcPpmPsm_B_DrReady)) && (CVmcPmm__HE1_D_IceStatus == 1) &&
       ((!(SVmcPmm__HE172_LogOp48)) && X_SVmcPmm__HE525_Delay)) || (SVmcPmm__HE829_Switch &&
       (CVmcPmm__HE1_D_IceStatus != 2) && (CVmcPmm__HE1_D_IceStatus != 3) &&
       X_SVmcPmm__HE592_UnitDelay1);

      
      X_SVmcPmm__HE525_Delay = SVmcPmm__HE172_LogOp48;

      
      if (X_SVmcPmm__HE592_UnitDelay1) {
         
         X_SVmcPmm__HE600_UnitDelay = X_SVmcPmm__HE600_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE600_UnitDelay = 0.F;
      }

      
      if (cVcVmcPmm_B_StallIceStrtActrFinishd) {
         
         xVcVmcPmm_B_StallIceStrtActrFinishd = X_SVmcPmm__HE600_UnitDelay >
          cVcVmcPmm_t_StallIceStrtActrFinishd;
      }
      else {
         
         xVcVmcPmm_B_StallIceStrtActrFinishd = 0;
      }

      
      if (cVcVmcPmm_B_StrtAbortSoft) {
         
         SVmcPmm__HE544_Switch = yVcPpmRc_B_StrtAbortSoft;
      }
      else {
         
         SVmcPmm__HE544_Switch = 0;
      }

      
      if (cVcVmcPmm_B_StrtAbortHard) {
         
         SVmcPmm__HE533_Switch = yVcPpmRc_B_StrtAbortHard;
      }
      else {
         
         SVmcPmm__HE533_Switch = 0;
      }

      
      if (cVcVmcPmm_B_StallRcShutOff) {
         
         SVmcPmm__HE563_Switch = yVcPpmRc_B_ShutOffReq;
      }
      else {
         
         SVmcPmm__HE563_Switch = 0;
      }

      
      if ((!(X_SVmcPmm__HE6_UnitDelay10)) && X_SVmcPmm__HE6_UnitDelay6) {
         
         X_SVmcPmm__HE595_UnitDelay = X_SVmcPmm__HE595_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE595_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_IsgStrtAbort = (X_SVmcPmm__HE595_UnitDelay > cVcVmcPmm_t_IsgStrtPahReqTiOut) ||
       yVcDtcSt_B_IsgStrtAbort;

      
      if (cVcVmcPmm_B_StrtAbortIsg) {
         
         SVmcPmm__HE578_Switch = xVcVmcPmm_B_IsgStrtAbort;
      }
      else {
         
         SVmcPmm__HE578_Switch = 0;
      }

      
      if (cVcVmcPmm_B_StrtAbortClu) {
         
         SVmcPmm__HE560_Switch = yVcDtcSt_B_CluStrtAbort;
      }
      else {
         
         SVmcPmm__HE560_Switch = 0;
      }

      
      if (cVcVmcPmm_B_StrtAbrtCl) {
         
         Float32 SVmcPmm__HE572_Switch;

         
         if (cVcVmcPmm_B_UseClPedAdaptStrtAbrt) {
            
            SVmcPmm__HE572_Switch = sVcDtcAtr_X_ClPedAdapt;
         }
         else {
            
            SVmcPmm__HE572_Switch = sVcScDep_X_ClutchPedalPos;
         }

         
         SVmcPmm__HE550_Switch = SVmcPmm__HE572_Switch < cVcVmcPmm_X_StrtAbrtCl;
      }
      else {
         
         SVmcPmm__HE550_Switch = 1;
      }

      
      if (cVcVmcPmm_B_StrtAbrtIce) {
         
         SVmcPmm__HE548_Switch = CVmcPmm__HE1_D_IceStatus == 1;
      }
      else {
         
         SVmcPmm__HE548_Switch = 1;
      }

      
      if (cVcVmcPmm_B_StrtAbrtRpm) {
         
         SVmcPmm__HE549_Switch = sVcEc_n_Eng < cVcVmcPmm_n_StrtAbrtRpm;
      }
      else {
         
         SVmcPmm__HE549_Switch = 1;
      }

      
      if (cVcVmcPmm_B_StrtAbrtStrtM) {
         
         SVmcPmm__HE547_Switch = yVcEc_B_StartMotor;
      }
      else {
         
         SVmcPmm__HE547_Switch = 1;
      }

      
      if (cVcVmcPmm_B_StrtAbrtAcc) {
         
         SVmcPmm__HE551_Switch = sVcScIn_X_AccPedalPos < cVcVmcPmm_X_StrtAbrtAcc;
      }
      else {
         
         SVmcPmm__HE551_Switch = 1;
      }

      
      if (cVcVmcPmm_B_StrtAbrtDrReady) {
         
         SVmcPmm__HE564_Switch = !(yVcPpmPsm_B_DrReady);
      }
      else {
         
         SVmcPmm__HE564_Switch = 1;
      }

      
      if (cVcVmcPmm_B_StrtAbrtNtrl) {
         
         Bool SVmcPmm__HE555_Switch;

         
         if (cVcVmcPmm_B_StrtAbrtNtrlValid) {
            
            SVmcPmm__HE555_Switch = yVcScDep_B_NeutralMTValid;
         }
         else {
            
            SVmcPmm__HE555_Switch = 1;
         }

         
         SVmcPmm__HE552_Switch = (!(yVcScIn_B_NeutralMT)) && SVmcPmm__HE555_Switch;
      }
      else {
         
         SVmcPmm__HE552_Switch = 1;
      }

      
      xVcVmcPmm_B_StrtAbrtPre = SVmcPmm__HE550_Switch && SVmcPmm__HE548_Switch &&
       SVmcPmm__HE549_Switch && SVmcPmm__HE547_Switch && SVmcPmm__HE551_Switch &&
       SVmcPmm__HE564_Switch && SVmcPmm__HE552_Switch;

      
      if (xVcVmcPmm_B_StrtAbrtPre) {
         
         X_SVmcPmm__HE586_UnitDelay = X_SVmcPmm__HE586_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE586_UnitDelay = 0.F;
      }

      
      if (cVcVmcPmm_B_StrtAbrt) {
         
         xVcVmcPmm_B_StrtAbrt = X_SVmcPmm__HE586_UnitDelay > cVcVmcPmm_t_StrtAbrt;
      }
      else {
         
         xVcVmcPmm_B_StrtAbrt = 0;
      }

      
      if (cVcVmcPmm_B_UseDesDrvDir) {
         
         SVmcPmm__HE557_Switch = sVcDtcAtr_v_VehDrDirectionRaw >= cVcVmcPmm_v_StallReset;
      }
      else {
         
         SVmcPmm__HE557_Switch = 1;
      }

      
      if (cVcVmcPmm_B_StallRcvCrnk) {
         
         xVcVmcPmm_B_CrnkStallRecov = yVcPpmPsm_B_DrReady;
      }
      else {
         
         xVcVmcPmm_B_CrnkStallRecov = 0;
      }

      
      if (cVcVmcPmm_B_StallRcvAT) {
         
         Bool SVmcPmm__HE567_Switch;

         
         if (cVcVmcPmm_B_Use7DCT) {
            
            SVmcPmm__HE567_Switch = X_SVmcPmm__HE6_UnitDelay2;
         }
         else {
            
            SVmcPmm__HE567_Switch = 1;
         }

         
         xVcVmcPmm_B_StallRcvAT = (SVmcPmm__HE567_Switch && (sVcEc_n_Eng < cVcVmcPmm_n_StallRcv) &&
          (!(X_SVmcPmm__HE172_UnitDelay8)) && (SVmcPmm__HE827_Switch || (yVcScDep_B_AccFtOnPed &&
          cVcVmcPmm_B_StallRcvAccFtOnPed) || (yVcScIn_B_DrvrBrkgASILB &&
          cVcVmcPmm_B_StallRcvFootOnBrPed))) || xVcVmcPmm_B_CrnkStallRecov;
      }
      else {
         
         xVcVmcPmm_B_StallRcvAT = 0;
      }

      
      if (cVcVmcPmm_B_StallRcvFrcd) {
         
         xVcVmcPmm_B_ForcedStallStart = yVcPpmPsm_B_ForcedStart;
      }
      else {
         
         xVcVmcPmm_B_ForcedStallStart = 0;
      }

      
      if (yVcScIn_B_NeutralMT) {
         
         X_SVmcPmm__HE584_UnitDelay = X_SVmcPmm__HE584_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE584_UnitDelay = 0.F;
      }

      
      SVmcPmm__HE584__tionalOperator1 = X_SVmcPmm__HE584_UnitDelay > cVcVmcPmm_t_StallRcvNeutral;

      
      SVmcPmm__HE172__tionalOperator1 = sVcScIn_v_VehSpdLgt > cVcVmcPmm_v_StallRcvStart;

      
      if (SVmcPmm__HE172__tionalOperator1) {
         
         Float32 SVmcPmm__HE569_Switch;

         
         if (cVcVmcPmm_B_UseClPedAdaptStallRecovery) {
            
            SVmcPmm__HE569_Switch = sVcDtcAtr_X_ClPedAdapt;
         }
         else {
            
            SVmcPmm__HE569_Switch = sVcScDep_X_ClutchPedalPos;
         }

         
         SVmcPmm__HE553_Switch = SVmcPmm__HE569_Switch > cVcVmcPmm_X_StallRcvClOnly;
      }
      else {
         
         SVmcPmm__HE553_Switch = yVcScDep_B_FootOnClutchPedalASILB;
      }

      
      if (SVmcPmm__HE553_Switch) {
         
         X_SVmcPmm__HE587_UnitDelay = X_SVmcPmm__HE587_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE587_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_StallRcvCl = SVmcPmm__HE584__tionalOperator1 || (X_SVmcPmm__HE587_UnitDelay >
       cVcVmcPmm_t_StallRcvClDelay);

      
      if (cVcVmcPmm_B_UseClPedAdaptStallRecovery) {
         
         SVmcPmm__HE571_Switch = sVcDtcAtr_X_ClPedAdapt;
      }
      else {
         
         SVmcPmm__HE571_Switch = sVcScDep_X_ClutchPedalPos;
      }

      
      xVcVmcPmm_B_StallRcvClNtrl = (SVmcPmm__HE553_Switch && SVmcPmm__HE172__tionalOperator1) ||
       (((SVmcPmm__HE571_Switch > cVcVmcPmm_X_StallRcvClNtrl) || yVcScDep_B_FootOnClutchPedal) &&
       SVmcPmm__HE584__tionalOperator1);

      
      if (cVcVmcPmm_B_StallRcvClOnly) {
         
         SVmcPmm__HE576_Switch = xVcVmcPmm_B_StallRcvCl;
      }
      else {
         
         SVmcPmm__HE576_Switch = xVcVmcPmm_B_StallRcvClNtrl;
      }

      
      xVcVmcPmm_B_StallRcvMT = xVcVmcPmm_B_CrnkStallRecov || xVcVmcPmm_B_ForcedStallStart ||
       ((!(X_SVmcPmm__HE172_UnitDelay1)) && SVmcPmm__HE576_Switch);

      
      if (yVcFsdPc_B_RunDry && cVcVmcPmm_B_UseStallRcvBlock) {
         
         xVcVmcPmm_B_StallRecovery = 0;
      }
      else {
         
         if (yVcDtcAtr_B_AT) {
            
            xVcVmcPmm_B_StallRecovery = xVcVmcPmm_B_StallRcvAT;
         }
         else {
            
            xVcVmcPmm_B_StallRecovery = xVcVmcPmm_B_StallRcvMT;
         }
      }

      
      X_SVmcPmm__HE590_UnitDelay1 = xVcVmcPmm_B_StallRunning || xVcVmcPmm_B_StallStrtM ||
       xVcVmcPmm_B_StallIceStrt || xVcVmcPmm_B_StallIceStrtEmi ||
       xVcVmcPmm_B_StallIceStrtActrFinishd || SVmcPmm__HE544_Switch || SVmcPmm__HE533_Switch ||
       SVmcPmm__HE563_Switch || SVmcPmm__HE578_Switch || SVmcPmm__HE560_Switch ||
       xVcVmcPmm_B_StrtAbrt || (SVmcPmm__HE829_Switch && ((!(SVmcPmm__HE557_Switch)) ||
       (!(xVcVmcPmm_B_StallRecovery))) && X_SVmcPmm__HE590_UnitDelay1);

      
      SVmcPmm__HE527_LogicalOperator = X_SVmcPmm__HE590_UnitDelay1 &&
       (!(X_SVmcPmm__HE527_UnitDelay1));

      
      X_SVmcPmm__HE527_UnitDelay1 = X_SVmcPmm__HE590_UnitDelay1;

      
      if (CVmcPmm__HE1_D_IceStatus == 2) {
         
         X_SVmcPmm__HE596_UnitDelay = X_SVmcPmm__HE596_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE596_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_EngRunReqIceStall = SVmcPmm__HE527_LogicalOperator || (SVmcPmm__HE829_Switch &&
       (X_SVmcPmm__HE596_UnitDelay <= cVcVmcPmm_t_EngRunStall) && X_SVmcPmm__HE591_UnitDelay1);

      
      X_SVmcPmm__HE591_UnitDelay1 = xVcVmcPmm_B_EngRunReqIceStall;

      
      if (cVcVmcPmm_B_UseIceStall) {
         
         xVcVmcPmm_B_RunReqIceStall = xVcVmcPmm_B_EngRunReqIceStall;
      }
      else {
         
         xVcVmcPmm_B_RunReqIceStall = 0;
      }

      
      X_SVmcPmm__HE335_UnitDelay1 = (SVmcPmm__HE848_Switch < cVcVmcPmm_Te_EngClntEngRunReq) ||
       ((SVmcPmm__HE848_Switch <= cVcVmcPmm_Te_EngClntEngOffReq) && X_SVmcPmm__HE335_UnitDelay1);

      
      if (cVcVmcPmm_B_UseEngClntRunReq) {
         
         xVcVmcPmm_B_EngRunReqEngClnt = X_SVmcPmm__HE335_UnitDelay1;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqEngClnt = 0;
      }

      
      SVmcPmm__HE334_Rel = cVcVmcPmm_X_FanAfterrunLimHi <= sVcTmAf_Z_FanAfterrun;

      
      SVmcPmm__HE334_Rel1 = sVcTmAf_Z_FanAfterrun <= cVcVmcPmm_X_FanAfterrunLimLo;

      
      xVcVmcPmm_B_FanAfterrun = (SVmcPmm__HE334_Rel && (!(SVmcPmm__HE334_Rel1))) ||
       ((!(SVmcPmm__HE334_Rel)) && (!(SVmcPmm__HE334_Rel1)) && X_SVmcPmm__HE334_UnitDelay);

      
      X_SVmcPmm__HE334_UnitDelay = xVcVmcPmm_B_FanAfterrun;

      
      if (xVcVmcPmm_B_FanAfterrun) {
         
         X_SVmcPmm__HE340_UnitDelay = X_SVmcPmm__HE340_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE340_UnitDelay = 0.F;
      }

      
      if (CVmcPmm__HE1_D_IceStatus == 2) {
         
         if (cVcVmcPmm_B_UseFanAfterrun) {
            
            yVcVmcPmm_B_EngRunReqFanAfterrun = X_SVmcPmm__HE340_UnitDelay >
             cVcVmcPmm_t_FanAfterrunDelay;
         }
         else {
            
            yVcVmcPmm_B_EngRunReqFanAfterrun = 0;
         }
      }
      else {
         
         yVcVmcPmm_B_EngRunReqFanAfterrun = 0;
      }

      
      SVmcPmm__HE170_LogicalOperator2 = (CVmcPmm__HE1_D_IceStatus == 1) || (CVmcPmm__HE1_D_IceStatus
        == 2);

      
      if (SVmcPmm__HE170_LogicalOperator2 && (!(X_SVmcPmm__HE233_UnitDelay1))) {
         
         X_SVmcPmm__HE311_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE311_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE311_UnitDelay;
      }

      
      X_SVmcPmm__HE233_UnitDelay1 = SVmcPmm__HE170_LogicalOperator2;

      
      if (cVcVmcPmm_B_UseEngOnOff) {
         
         xVcVmcPmm_B_EngOnOff = X_SVmcPmm__HE311_UnitDelay <= cVcVmcPmm_t_EngOnOff;
      }
      else {
         
         xVcVmcPmm_B_EngOnOff = 0;
      }

      
      SVmcPmm__HE170_LogicalOperator7 = (!(X_SVmcPmm__HE6_UnitDelay14)) && (CVmcPmm__HE1_D_IceStatus
        == 0);

      
      if (!(SVmcPmm__HE170_LogicalOperator7)) {
         
         SVmcPmm__HE228_Switch = 0.F;
      }
      else {
         
         Float32 SVmcPmm__HE228_Switch1;

         
         if (SVmcPmm__HE170_LogicalOperator7) {
            
            SVmcPmm__HE228_Switch1 = ts_VcVmcPmm__HEP7;
         }
         else {
            
            SVmcPmm__HE228_Switch1 = 0.F;
         }

         
         SVmcPmm__HE228_Switch = SVmcPmm__HE228_Switch1 + X_SVmcPmm__HE228_UnitDelay;
      }
      if (1e+30F < SVmcPmm__HE228_Switch) {
         rVcVmcPmm_t_EngOff = 1e+30F;
      }
      else {
         rVcVmcPmm_t_EngOff = SVmcPmm__HE228_Switch;
      }

      
      X_SVmcPmm__HE228_UnitDelay = rVcVmcPmm_t_EngOff;

      
      if (cVcVmcPmm_B_UseEngOffMaxTime) {
         
         xVcVmcPmm_B_EngRunReqMaxTime = rVcVmcPmm_t_EngOff >= cVcVmcPmm_t_EngOffMax;
      }
      else {
         
         xVcVmcPmm_B_EngRunReqMaxTime = 0;
      }

      
      xVcVmcPmm_B_EngRunReqTotPre = xVcVmcPmm_B_EngRunReqDriver || xVcVmcPmm_B_EngRunReqPsm ||
       xVcVmcPmm_B_EngRunReqEm || yVcVmcPmm_B_EngRunReqBrake || yVcVmcPmm_B_EngRunReqSapp ||
       yVcVmcPmm_B_EngRunReqTrans || yVcVmcPmm_B_EngRunReqEms || yVcVmcPmm_B_EngRunReqEmLv ||
       yVcVmcPmm_B_EngRunReqClim || xVcVmcPmm_B_EngRunReqPcr || xVcVmcPmm_B_EngRunReqFCAdapt ||
       yVcVmcPmm_B_EngRunReqTm || yVcVmcPmm_B_EngRunReqFuel || xVcVmcPmm_B_EngRunReqIsg ||
       xVcVmcPmm_B_EngRunReqRemote || xVcVmcPmm_B_EngRunReqStabCtrl || xVcVmcPmm_B_EngRunReqDrLeave
       || xVcVmcPmm_B_EngRunReqChas || yVcVmcPmm_B_EngRunReqObd || xVcVmcPmm_B_EngRunReqDep ||
       xVcVmcPmm_B_EngRunReqCEC || yVcVmcPmm_B_EngRunReqRc || xVcVmcPmm_B_RunReqIceStall ||
       xVcVmcPmm_B_EngRunReqEngClnt || yVcVmcPmm_B_EngRunReqFanAfterrun || xVcVmcPmm_B_EngOnOff ||
       xVcVmcPmm_B_EngRunReqMaxTime || X_SVmcPmm__HE6_UnitDelay12;

      
      if (cVc_B_SeriesHev && (sVcDeDmm_D_DrvMode == 9)) {
         
         SVmcPmm__HE298_Switch = yVcVmcPmm_B_EngRunReqBrake;
      }
      else {
         
         SVmcPmm__HE298_Switch = xVcVmcPmm_B_EngRunReqTotPre;
      }

      
      if (X_SVmcPmm__HE170_UnitDelay3 == 4) {
         
         SVmcPmm__HE227_switch = (sVcEc_n_Eng > cVcVmcPmm_n_Wait4Eng2StopLimHighTest) &&
          (sVcEc_n_Eng < cVcVmcPmm_n_Wait4Eng2StopLimHigh);
      }
      else {
         
         SVmcPmm__HE227_switch = sVcEc_n_Eng < cVcVmcPmm_n_Wait4Eng2StopLim;
      }

      
      SVmcPmm__HE170__gicalOperator22 = SVmcPmm__HE298_Switch && SVmcPmm__HE227_switch &&
       (CVmcPmm__HE1_D_IceStatus == 3);

      
      if (SVmcPmm__HE170__gicalOperator22) {
         
         X_SVmcPmm__HE342_UnitDelay = X_SVmcPmm__HE342_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE342_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_Wait4EngStrtTiOut = X_SVmcPmm__HE342_UnitDelay > cVcVmcPmm_t_Wait4Eng2StopTiOut;

      
      if (cVcVmcPmm_B_UseWait4Eng2Stop) {
         
         xVcVmcPmm_B_Wait4Eng2Stop = (!(SVmcPmm__HE170__gicalOperator22)) ||
          xVcVmcPmm_B_Wait4EngStrtTiOut;
      }
      else {
         
         xVcVmcPmm_B_Wait4Eng2Stop = 1;
      }

      
      if (SVmcPmm__HE298_Switch) {
         
         X_SVmcPmm__HE341_UnitDelay = X_SVmcPmm__HE341_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE341_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_Wait4CluStrtDly = X_SVmcPmm__HE341_UnitDelay > cVcVmcPmm_t_Wait4EngRunReqTot;

      
      if (cVcVmcPmm_B_EngRunReqTot_swi) {
         
         yVcVmcPmm_B_EngRunReqTot = cVcVmcPmm_B_EngRunReqTot_dbi;
      }
      else {
         
         if (cVcVmcPmm_B_Use7DCT) {
            
            yVcVmcPmm_B_EngRunReqTot = (xVcVmcPmm_B_Wait4Eng2Stop && (!(X_SVmcPmm__HE6_UnitDelay7))
             && xVcVmcPmm_B_Wait4CluStrtDly) || X_SVmcPmm__HE6_UnitDelay12;
         }
         else {
            
            yVcVmcPmm_B_EngRunReqTot = SVmcPmm__HE298_Switch;
         }
      }

      
      SVmcPmm__HE230_Logic1 = (!(xVcVmcPmm_B_EngRunReqDriver)) && X_SVmcPmm__HE230_Delay;

      
      X_SVmcPmm__HE230_Delay = xVcVmcPmm_B_EngRunReqDriver;

      
      SVmcPmm__HE170__ionalOperator17 = sVcScIn_v_VehSpdLgt > cVcVmcPmm_v_WaitToReset;

      
      X_SVmcPmm__HE336_UnitDelay1 = (SVmcPmm__HE230_Logic1 && SVmcPmm__HE170__ionalOperator17) ||
       (SVmcPmm__HE170__ionalOperator17 && (!(xVcVmcPmm_B_EngRunReqDriver)) &&
       X_SVmcPmm__HE336_UnitDelay1);

      
      if (yVcDeDmm_B_EngRunReqDrReEval || SVmcPmm__HE230_Logic1 || X_SVmcPmm__HE336_UnitDelay1) {
         
         X_SVmcPmm__HE309_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE309_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE309_UnitDelay;
      }

      
      X_SVmcPmm__HE339_UnitDelay1 = yVcVmcPmm_B_EngRunReqTot || ((yVcVmcPmm_B_EngRunReqTot ||
       (X_SVmcPmm__HE309_UnitDelay > cVcVmcPmm_t_WaitToReset)) && X_SVmcPmm__HE339_UnitDelay1);

      
      if (cVcVmcPmm_B_UseTotEngRunReq) {
         
         SVmcPmm__HE300_Switch = yVcVmcPmm_B_EngRunReqTot;
      }
      else {
         
         SVmcPmm__HE300_Switch = X_SVmcPmm__HE339_UnitDelay1;
      }

      
      if (SVmcPmm__HE300_Switch) {
         
         X_SVmcPmm__HE310_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE310_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE310_UnitDelay;
      }

      
      if (SVmcPmm__HE829_Switch && (!(X_SVmcPmm__HE232_Delay))) {
         
         SVmcPmm__HE279_Switch = 0.F;
      }
      else {
         
         if (SVmcPmm__HE159_LogOp3) {
            
            SVmcPmm__HE279_Switch = cVcVmcPmm_t_EngOffFcAdapt;
         }
         else {
            
            SVmcPmm__HE279_Switch = cVcVmcPmm_t_EngOff;
         }
      }

      
      X_SVmcPmm__HE232_Delay = SVmcPmm__HE829_Switch;

      
      xVcVmcPmm_B_EngOnReqPre = X_SVmcPmm__HE310_UnitDelay <= SVmcPmm__HE279_Switch;

      
      if (cVcVmcPmm_B_LosStop) {
         
         SVmcPmm__HE252_Switch = yVcDsePcr_B_EngStopRq;
      }
      else {
         
         SVmcPmm__HE252_Switch = 0;
      }

      
      X_SVmcPmm__HE337_UnitDelay1 = (yVcFsdPc_B_RunDryCrkInhb && yVcFsdPc_B_RunDry &&
       cVcVmcPmm_B_UseRunDryInhb) || ((yVcPpmPsm_B_DriveCycleActive || (!(X_SVmcPmm__HE231_Delay)))
       && (!(cVcVmcPmm_B_UseRunDryInhbOnly)) && X_SVmcPmm__HE337_UnitDelay1);

      
      X_SVmcPmm__HE231_Delay = yVcPpmPsm_B_DriveCycleActive;

      
      if (cVcVmcPmm_B_RcShutOff) {
         
         SVmcPmm__HE261_Switch = yVcPpmRc_B_ShutOffReq;
      }
      else {
         
         SVmcPmm__HE261_Switch = 0;
      }

      
      SVmcPmm__HE170__gicalOperator37 = (sVcEc_n_Eng < cVcVmcPmm_n_IceStallMax) &&
       (X_SVmcPmm__HE590_UnitDelay1 || SVmcPmm__HE261_Switch);

      
      xVcVmcPmm_B_EngStopFast = SVmcPmm__HE252_Switch || yVcDepSs_B_EngFastStop ||
       X_SVmcPmm__HE337_UnitDelay1 || (!(SVmcPmm__HE829_Switch)) || SVmcPmm__HE170__gicalOperator37;

      
      SVmcPmm__HE170_LogicalOperator6 = xVcVmcPmm_B_EngOnReqPre && (!(xVcVmcPmm_B_EngStopFast));

      
      xVcVmcPmm_B_EngStart = xVcVmcPmm_B_StartAllowedPath && SVmcPmm__HE170_LogicalOperator6;

      
      if (cVcVmcPmm_B_DepStop) {
         
         xVcVmcPmm_B_StopAllowedDep = yVcDepSs_B_StopAllowed;
      }
      else {
         
         xVcVmcPmm_B_StopAllowedDep = 1;
      }

      
      xVcVmcPmm_B_StopAllowedPath = SVmcPmm__HE170__gicalOperator37 || xVcVmcPmm_B_StopAllowedDep;

      
      xVcVmcPmm_B_EngStop = (!(SVmcPmm__HE170_LogicalOperator6)) && xVcVmcPmm_B_StopAllowedPath;

      
      xVcVmcPmm_B_EngOnReqEng = xVcVmcPmm_B_EngStart || ((!(xVcVmcPmm_B_EngStop)) &&
       X_SVmcPmm__HE338_UnitDelay1);

      
      X_SVmcPmm__HE338_UnitDelay1 = xVcVmcPmm_B_EngOnReqEng;

      
      if (sVcEc_n_Eng < cVcVmcPmm_n_CFTStop) {
         
         X_SVmcPmm__HE455_UnitDelay = X_SVmcPmm__HE455_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE455_UnitDelay = 0.F;
      }

      
      X_SVmcPmm__HE454_UnitDelay1 = ((sVcScIn_v_VehSpdLgt < 1.F) && (cVcVmcPmm_B_CTFStart &&
       (!(X_SVmcPmm__HE452_UnitDelay1)))) || ((X_SVmcPmm__HE455_UnitDelay <= cVcVmcPmm_t_CTFStop) &&
        X_SVmcPmm__HE454_UnitDelay1);

      
      X_SVmcPmm__HE452_UnitDelay1 = cVcVmcPmm_B_CTFStart;

      
      if (132 == cVcVmcPmm_D_CTF) {
         
         yVcVmcPmm_B_EngOnReqEng = !(X_SVmcPmm__HE454_UnitDelay1);
      }
      else {
         
         yVcVmcPmm_B_EngOnReqEng = xVcVmcPmm_B_EngOnReqEng;
      }
      #if Vc_Pvc_Hw_B_AT
         
         if (yVcVmcPmm_B_EngOnReqEng) {
            
            X_SVmcPmm__HE510_UnitDelay = 0.F;
         }
         else {
            
            X_SVmcPmm__HE510_UnitDelay = X_SVmcPmm__HE510_UnitDelay + ts_VcVmcPmm__HEP7;
         }

         
         SVmcPmm__HE171__gicalOperator49 = (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATPark) ||
          (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATNeutral);

         
         if (SVmcPmm__HE171__gicalOperator49) {
            
            X_SVmcPmm__HE508_UnitDelay = X_SVmcPmm__HE508_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE508_UnitDelay = 0.F;
         }

         
         if (yVcVmcPmm_B_EngOnReqEng) {
            
            X_SVmcPmm__HE511_UnitDelay = 0.F;
         }
         else {
            
            X_SVmcPmm__HE511_UnitDelay = X_SVmcPmm__HE511_UnitDelay + ts_VcVmcPmm__HEP7;
         }

         
         if (!(yVcVmcTfa_B_CcOrAccActive)) {
            
            SVmcPmm__HE486_Switch = X_SVmcPmm__HE6_UnitDelay5;
         }
         else {
            
            if (X_SVmcPmm__HE511_UnitDelay <= cVcVmcPmm_t_IsgIceStopACCTimeout) {
               
               SVmcPmm__HE486_Switch = X_SVmcPmm__HE6_UnitDelay15;
            }
            else {
               
               SVmcPmm__HE486_Switch = X_SVmcPmm__HE6_UnitDelay5;
            }
         }

         
         xVcVmcPmm_B_EngOnReqTransPre = (X_SVmcPmm__HE510_UnitDelay <= ts_VcVmcPmm__HEP7) ||
          ((X_SVmcPmm__HE508_UnitDelay <= cVcVmcPmm_t_IsgIceStopTimeout) &&
          ((!(SVmcPmm__HE171__gicalOperator49)) || (!(X_SVmcPmm__HE6_UnitDelay13))) &&
          (((!(X_SVmcPmm__HE6_UnitDelay13)) && (!(X_SVmcPmm__HE6_UnitDelay9))) ||
          (!(X_SVmcPmm__HE6_UnitDelay5))) && (SVmcPmm__HE486_Switch || yVcDseGb_B_EngStopDlyReq ||
          (!(X_SVmcPmm__HE6_UnitDelay4))) && (!(X_SVmcPmm__HE6_UnitDelay8)) &&
          X_SVmcPmm__HE503_UnitDelay1);

         
         X_SVmcPmm__HE503_UnitDelay1 = xVcVmcPmm_B_EngOnReqTransPre;

         
         if ((Vc_Pvc_Hw_B_Efad_CN != 0) || (Vc_Pvc_Hw_B_Erad_CN != 0)) {
            
            SVmcPmm__HE482_Switch = xVcVmcPmm_B_EngOnReqTransPre;
         }
         else {
            
            SVmcPmm__HE482_Switch = yVcVmcPmm_B_EngOnReqEng;
         }
         #if VcVmcPmm__HEP7_1224_EngageReqHybrid_7
            
            SVmcPmm__HE477__gicalOperator18 = yVcVmcEm_B_EngageReq || yVcDeDmm_B_TrnEngageRqDr ||
             (yVcVmcPmm_B_EngRunReqBrake && cVcVmcPmm_B_TrnMdeUseBrake) || (xVcVmcPmm_B_EngRunReqPcr
              && cVcVmcPmm_B_TrnMdeUsePcr) || (yVcVmcPmm_B_EngRunReqTrans &&
             cVcVmcPmm_B_TrnMdeUseTrans) || (yVcVmcAwd_B_EngageReq && cVcVmcPmm_B_TrnMdeUseAwd) ||
             X_SVmcPmm__HE6_UnitDelay11;

            
            if (SVmcPmm__HE477__gicalOperator18) {
               
               X_SVmcPmm__HE515_UnitDelay = X_SVmcPmm__HE515_UnitDelay + ts_VcVmcPmm__HEP7;
            }
            else {
               
               X_SVmcPmm__HE515_UnitDelay = 0.F;
            }

            
            if (sVcEc_n_Eng >= cVcVmcPmm_n_TrnEngBlockMin) {
               
               X_SVmcPmm__HE516_UnitDelay = 0.F;
            }
            else {
               
               X_SVmcPmm__HE516_UnitDelay = X_SVmcPmm__HE516_UnitDelay + ts_VcVmcPmm__HEP7;
            }

            
            if (sVcEmiHeat_D_EngUseReq > sVcTmStrt_D_EngUseReq) {
               SVmcPmm__HE477_MinMax = sVcEmiHeat_D_EngUseReq;
            }
            else {
               SVmcPmm__HE477_MinMax = sVcTmStrt_D_EngUseReq;
            }

            
            if (SVmcPmm__HE477_MinMax == 1) {
               
               X_SVmcPmm__HE517_UnitDelay = 0.F;
            }
            else {
               
               X_SVmcPmm__HE517_UnitDelay = X_SVmcPmm__HE517_UnitDelay + ts_VcVmcPmm__HEP7;
            }

            
            xVcVmcPmm_B_TrnEngageReqHybrid = SVmcPmm__HE482_Switch &&
             SVmcPmm__HE477__gicalOperator18 && ((X_SVmcPmm__HE515_UnitDelay >
             cVcVmcPmm_t_TrnEngBlockMax) || yVcDeDmm_B_RespStartReq || yVcVmcAwd_B_EngageReq ||
             ((sVcDtcAtr_v_VehDrDirectionRaw >= cVcVmcPmm_v_TrnEngBlockMax) ||
             (X_SVmcPmm__HE516_UnitDelay > cVcVmcPmm_t_TrnEngRpmDly) || ((X_SVmcPmm__HE517_UnitDelay
              > cVcVmcPmm_t_TrnEngCatHeatDly) && (!(cVcVmcPmm_B_TrnEngBlockSkipEngUseReq))))) &&
             ((sVcDtcAtr_D_GearLevAT != cVc_D_GearLevATReverse) || (!(yVcGscPrn_B_EfadRvs)));
         #endif

         
         if (SVmcPmm__HE482_Switch) {
            
            
            #if Vc_Pvc_Hw_B_AT
               Bool SVmcPmm__HE519_Switch;
            #endif

            

            
            if (cVcVmcPmm_B_TrnMdeReqBrk) {
               
               SVmcPmm__HE519_Switch = rVcVmcPmm_D_EngRunReqBrake == 2;
            }
            else {
               
               SVmcPmm__HE519_Switch = 0;
            }

            
            xVcVmcPmm_B_TrnEngageReqIC = SVmcPmm__HE519_Switch || yVcDeDmm_B_TrnEngageRqDr ||
             yVcVscEcc_B_TrnEngageReq;
         }
         else {
            
            xVcVmcPmm_B_TrnEngageReqIC = 0;
         }

         
         if (((Vc_Pvc_Hw_B_Efad_CN != 0) || (Vc_Pvc_Hw_B_Erad_CN != 0)) && cVcVmcPmm_B_TrnMdeHev) {
            
            xVcVmcPmm_B_TrnEngageReqPre = xVcVmcPmm_B_TrnEngageReqHybrid;
         }
         else {
            
            if (cVcVmcPmm_B_TrnMdeIC) {
               
               xVcVmcPmm_B_TrnEngageReqPre = xVcVmcPmm_B_TrnEngageReqIC;
            }
            else {
               
               xVcVmcPmm_B_TrnEngageReqPre = SVmcPmm__HE482_Switch;
            }
         }

         
         if (!(xVcVmcPmm_B_TrnEngageReqPre)) {
            
            X_SVmcPmm__HE523_UnitDelay = X_SVmcPmm__HE523_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE523_UnitDelay = 0.F;
         }

         
         SVmcPmm__HE523_Rel = X_SVmcPmm__HE523_UnitDelay > cVcVmcPmm_t_CrShPahDiTiOut;

         
         SVmcPmm__HE171__gicalOperator18 = (sVcDtcCta_Tq_CrShInstReq < cVcVmcPmm_Tq_CrShRampDown) &&
           (sVcDtcCta_Tq_CrShInstReq > cVcVmcPmm_Tq_CrShRampUp);

         
         if (cVcVmcPmm_B_Use7DCT) {
            
            xVcVmcPmm_B_CrShPathDisabled = SVmcPmm__HE523_Rel || (yVcVmcWtc_B_CrShPathDisabled &&
             (sVcDtcAjc_Tq_DrCrShReqWhl < cVcVmcPmm_Tq_DrCrShRampDown) && (sVcDtcAjc_Tq_DrCrShReqWhl
              > cVcVmcPmm_Tq_DrCrShRampUp));
         }
         else {
            
            
            #if Vc_Pvc_Hw_B_AT
               Bool SVmcPmm__HE479__gicalOperator15;
            #endif

            

            
            SVmcPmm__HE479__gicalOperator15 = (sVcDtcAjc_Tq_DrPropFrntReq <
             cVcVmcPmm_Tq_PropFrntRampDown) && (sVcDtcAjc_Tq_DrPropFrntReq >
             cVcVmcPmm_Tq_PropFrntRampUp);

            
            if (cVcVmcPmm_B_UseEradHybrid) {
               
               xVcVmcPmm_B_CrShPathDisabled = SVmcPmm__HE523_Rel || (SVmcPmm__HE479__gicalOperator15
                 && yVcVmcWtd_B_FrntAxlePathDisabled);
            }
            else {
               
               if (cVcVmcPmm_B_UsePropFrntRampDown) {
                  
                  xVcVmcPmm_B_CrShPathDisabled = SVmcPmm__HE479__gicalOperator15;
               }
               else {
                  
                  xVcVmcPmm_B_CrShPathDisabled = SVmcPmm__HE171__gicalOperator18;
               }
            }
         }

         
         SVmcPmm__HE171__gicalOperator43 = (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive) ||
          (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATReverse);

         
         SVmcPmm__HE171__gicalOperator10 = xVcVmcPmm_B_CrShPathDisabled &&
          SVmcPmm__HE171__gicalOperator43;

         
         X_SVmcPmm__HE505_UnitDelay1 = (SVmcPmm__HE171__gicalOperator10 &&
          (!(X_SVmcPmm__HE480_Delay))) || (SVmcPmm__HE171__gicalOperator43 &&
          X_SVmcPmm__HE505_UnitDelay1);

         
         X_SVmcPmm__HE480_Delay = SVmcPmm__HE171__gicalOperator10;

         
         if (cVcVmcPmm_B_CrShPathEnable_swi) {
            
            SVmcPmm__HE489_Switch = cVcVmcPmm_B_CrShPathEnable_dbi;
         }
         else {
            
            SVmcPmm__HE489_Switch = (xVcVmcPmm_B_TrnEngageReqPre && X_SVmcPmm__HE505_UnitDelay1 &&
             SVmcPmm__HE829_Switch && (yVcScIn_B_PropulsionAllowed || cVcVmcPmm_B_IgnrPropAlwdCrSh)
             && (CVmcPmm__HE1_D_IceStatus == 2) && (yVcDsePcr_B_TransNtrlDisable ||
             (sVcDtcAtr_D_TransMode == 1) || (sVcDtcAtr_D_TransMode == 2))) ||
             (cVcVmcPmm_B_UseOldEngRevStgy && SVmcPmm__HE482_Switch && SVmcPmm__HE829_Switch &&
             (yVcScIn_B_PropulsionAllowed || cVcVmcPmm_B_IgnrPropAlwdCrSh) &&
             (CVmcPmm__HE1_D_IceStatus == 2) && (yVcDsePcr_B_TransNtrlDisable ||
             SVmcPmm__HE171__gicalOperator49));
         }

         
         if (SVmcPmm__HE171__gicalOperator49) {
            
            X_SVmcPmm__HE509_UnitDelay = X_SVmcPmm__HE509_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE509_UnitDelay = 0.F;
         }

         
         xVcVmcPmm_B_TrnEngageReq = (xVcVmcPmm_B_TrnEngageReqPre && ((sVcDtcAtr_v_VehDrDirectionRaw
          >= cVcVmcPmm_v_ReqEngDrDir) || (CVmcPmm__HE1_D_IceStatus == 2))) ||
          ((xVcVmcPmm_B_TrnEngageReqPre || (!(xVcVmcPmm_B_CrShPathDisabled))) &&
          (!(xVcVmcPmm_B_EngStopFast)) && (X_SVmcPmm__HE509_UnitDelay <= cVcVmcPmm_t_GearLevPNDlyOn)
           && X_SVmcPmm__HE502_UnitDelay1);

         
         X_SVmcPmm__HE502_UnitDelay1 = xVcVmcPmm_B_TrnEngageReq;

         
         SVmcPmm__HE171__gicalOperator35 = SVmcPmm__HE482_Switch &&
          (!(SVmcPmm__HE477__gicalOperator18));
         #if VcVmcPmm__HEP7_1223_C3OilPresBuildUp_6
            
            SVmcPmm__HE513_Logic1 = SVmcPmm__HE829_Switch && (!(X_SVmcPmm__HE513_Delay));

            
            X_SVmcPmm__HE513_Delay = SVmcPmm__HE829_Switch;

            
            if (SVmcPmm__HE513_Logic1) {
               
               SVmcPmm__HE512_Switch = 0.F;
            }
            else {
               
               
               #ifdef SVmcPmm__HE512_Switch_AUX
                  Float32 SVmcPmm__HE512_Switch1;
               #endif

               

               
               if ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive) && (sVcDtcAtr_v_VehDrDirectionRaw
                 > 4.F) && (!(SVmcPmm__HE171__gicalOperator35))) {
                  
                  SVmcPmm__HE512_Switch1 = ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  SVmcPmm__HE512_Switch1 = 0.F;
               }

               
               SVmcPmm__HE512_Switch = SVmcPmm__HE512_Switch1 + X_SVmcPmm__HE512_UnitDelay;
            }
            if (1e+30F < SVmcPmm__HE512_Switch) {
               rVcVmcPmm_t_TrnC3OilPres = 1e+30F;
            }
            else {
               rVcVmcPmm_t_TrnC3OilPres = SVmcPmm__HE512_Switch;
            }

            
            X_SVmcPmm__HE512_UnitDelay = rVcVmcPmm_t_TrnC3OilPres;

            
            X_SVmcPmm__HE514_UnitDelay1 = SVmcPmm__HE513_Logic1 || ((sVcDtcAtr_v_VehDrDirectionRaw
             <= cVcVmcPmm_v_TrnMdeC3OilPresMax) && (sVcTcm_Te_TrsmOilT <
             cVcVmcPmm_Te_TrnMdeC3OilPresMax) && X_SVmcPmm__HE514_UnitDelay1);

            
            xVcVmcPmm_B_TrnC3OilPres = (rVcVmcPmm_t_TrnC3OilPres < cVcVmcPmm_t_TrnMdeC3OilPresMax)
             && X_SVmcPmm__HE514_UnitDelay1 && cVcVmcPmm_B_TrnMdeUseC3OilPres;
         #endif

         
         X_SVmcPmm__HE506_UnitDelay1 = ((!(xVcVmcPmm_B_TrnC3OilPres)) && (sVcScIn_v_VehSpdLgt >
          cVcVmcPmm_v_TotNtrlSet)) || ((sVcScIn_v_VehSpdLgt > cVcVmcPmm_v_TotNtrlReset) &&
          X_SVmcPmm__HE506_UnitDelay1);

         
         if (cVcVmcPmm_D_TransModeReq_swi) {
            
            rVcVmcPmm_D_TransModeReq = cVcVmcPmm_D_TransModeReq_dbi;
         }
         else {
            
            
            #if Vc_Pvc_Hw_B_AT
               Bool SVmcPmm__HE490_Switch;
            #endif

            

            
            if (yVcDsePcr_B_TransNtrlRq) {
               
               SVmcPmm__HE490_Switch = 0;
            }
            else {
               
               SVmcPmm__HE490_Switch = xVcVmcPmm_B_TrnEngageReq;
            }

            
            if (SVmcPmm__HE490_Switch) {
               
               if (yVcVmcEm_B_NICEnable && cVcVmcPmm_B_TrnMdeHevUseNIC) {
                  
                  rVcVmcPmm_D_TransModeReq = cVcVmcPmm_D_TrnMdeHevReqEngNIC;
               }
               else {
                  
                  rVcVmcPmm_D_TransModeReq = cVcVmcPmm_D_TrnMdeReqEng;
               }
            }
            else {
               
               if ((yVcDsePcr_B_TransNtrlRq || (sVcDtcAtr_v_VehDrDirectionRaw <
                cVcVmcPmm_v_TotNtrlVehDrDir) || (sVcDtcAtr_D_TrgGear == -1) || (sVcDtcAtr_D_TrgGear
                > cVcVmcPmm_D_GearTotNtrl) || X_SVmcPmm__HE506_UnitDelay1 ||
                SVmcPmm__HE171__gicalOperator35) && ((Vc_Pvc_Hw_B_Efad_CN != 0) ||
                (Vc_Pvc_Hw_B_Erad_CN != 0))) {
                  
                  rVcVmcPmm_D_TransModeReq = cVcVmcPmm_D_TrnMdeReqTotNtrl;
               }
               else {
                  
                  rVcVmcPmm_D_TransModeReq = cVcVmcPmm_D_TrnMdeReqNtrl;
               }
            }
         }

         
         SVmcPmm__HE171_LogicalOperator3 = SVmcPmm__HE482_Switch && (!(xVcVmcPmm_B_EngStopFast));

         
         if (cVcVmcPmm_B_DepStopAT) {
            
            SVmcPmm__HE484_Switch = yVcDepSs_B_StopAllowed;
         }
         else {
            
            SVmcPmm__HE484_Switch = 1;
         }

         
         if (!(SVmcPmm__HE482_Switch)) {
            
            X_SVmcPmm__HE507_UnitDelay = X_SVmcPmm__HE507_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE507_UnitDelay = 0.F;
         }

         
         xVcVmcPmm_B_EngStopReqAT = (!(SVmcPmm__HE171_LogicalOperator3)) &&
          (X_SVmcPmm__HE590_UnitDelay1 || SVmcPmm__HE484_Switch) && (xVcVmcPmm_B_EngStopFast ||
          ((sVcScIn_v_VehSpdLgt < cVcVmcPmm_v_EngStopReqAT) && SVmcPmm__HE827_Switch &&
          (SVmcPmm__HE171__gicalOperator18 || cVcVmcPmm_B_CrShaftRampDownIgnore) && ((sVcEc_n_Eng <
          (sVcDtcIcl_n_IdleSpdBs + cVcVmcPmm_n_EngOnDelayOff)) || (X_SVmcPmm__HE507_UnitDelay >
          cVcVmcPmm_t_EngOnDelayOff) || cVcVmcPmm_B_EngOnDelayIgnore)));

         
         xVcVmcPmm_B_EngOnReqTrans = SVmcPmm__HE171_LogicalOperator3 ||
          ((!(xVcVmcPmm_B_EngStopReqAT)) && X_SVmcPmm__HE504_UnitDelay1);

         
         X_SVmcPmm__HE504_UnitDelay1 = xVcVmcPmm_B_EngOnReqTrans;

         
         yVcVmcPmm_B_TrnEngageReqHev = SVmcPmm__HE477__gicalOperator18;
      #endif

      
      if (cVcVmcPmm_B_EngOnReq_swi) {
         
         X_SVmcPmm__HE6_UnitDelay14 = cVcVmcPmm_B_EngOnReq_dbi;
      }
      else {
         
         if (133 == cVcVmcPmm_D_CTF) {
            
            X_SVmcPmm__HE6_UnitDelay14 = !(X_SVmcPmm__HE454_UnitDelay1);
         }
         else {
            
            if (cVc_B_SeriesHev) {
               
               X_SVmcPmm__HE6_UnitDelay14 = yVcVmcPmm_B_EngOnReqEng;
            }
            else {
               
               if (!(yVcDtcAtr_B_AT)) {
                  
                  X_SVmcPmm__HE6_UnitDelay14 = yVcVmcPmm_B_EngOnReqEng;
               }
               else {
                  
                  X_SVmcPmm__HE6_UnitDelay14 = xVcVmcPmm_B_EngOnReqTrans;
               }
            }
         }
      }

      
      X_SVmcPmm__HE3_UnitDelay10 = X_SVmcPmm__HE6_UnitDelay14;

      
      if (cVc_B_SeriesHev) {
         
         sVcVmcPmm_D_TransModeReq = 5;
      }
      else {
         
         sVcVmcPmm_D_TransModeReq = rVcVmcPmm_D_TransModeReq;
      }

      
      if (cVc_B_SeriesHev) {
         
         yVcVmcPmm_B_CrShPathEnable = 0;
      }
      else {
         
         if (!(yVcDtcAtr_B_AT)) {
            
            yVcVmcPmm_B_CrShPathEnable = 1;
         }
         else {
            
            yVcVmcPmm_B_CrShPathEnable = SVmcPmm__HE489_Switch;
         }
      }
      #if VcVmcPmm__HEP7_1240_Hybrid_Mode_Control_9
         #if Vc_Pvc_Hw_B_Efad
            
            if (cVcVmcPmm_B_UseEfadCode) {
               
               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE719_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE720_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE728_MinMax;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE728_Prod1;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE728_Sum3;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE732_MinMax;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE732_Prod1;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE732_Sum3;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE745_Switch1;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE765_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Float32 SVmcPmm__HE766_Switch;
               #endif

               

               
               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE637_LogicalOperator7;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE637__gicalOperator40;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE637__gicalOperator50;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638_LogicalOperator1;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638_LogicalOperator2;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638__gicalOperator14;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638__gicalOperator15;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638__gicalOperator16;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638__gicalOperator17;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638__gicalOperator40;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638__gicalOperator41;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638__gicalOperator42;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638__ionalOperator13;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638__ionalOperator22;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE638__tionalOperator6;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE639__gicalOperator16;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE639__gicalOperator20;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE639__gicalOperator21;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE639__gicalOperator23;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE639__ionalOperator13;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE639__ionalOperator18;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE672_LogicalOperator7;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE672__gicalOperator10;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE673__gicalOperator23;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE695_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE699_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE700_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE721_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE722_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE741_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE742_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE743__ationalOperator;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE747_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE748_Rel;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE748_Rel1;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE749_Rel;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE749_Rel1;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE750_Rel;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE750_Rel1;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE751_Rel;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE751_Rel1;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE752_Rel;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE752_Rel1;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  Bool SVmcPmm__HE828_Switch;
               #endif

               

               
               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static UInt8 SVmcPmm__HE730__rkRoadIncline_c[2] = 
                  {
                      0, 0
                     
                  }; 
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static UInt8 SVmcPmm__HE730__rkRoadIncline_r[2] = 
                  {
                      0, 0
                     
                  }; 
               #endif

               

               
               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE661_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE662_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE663_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE664_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE665_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE666_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE667_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE668_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE669_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE670_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE671_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE708_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE709_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE710_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE711_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE712_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE713_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE714_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE725_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE726_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE727_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE728_Del1 = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE732_Del1 = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE736_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE737_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE738_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE739_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE740_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE754_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE755_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE756_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE757_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE758_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE759_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE760_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE761_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE762_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE772_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE773_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE779_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Float32 X_SVmcPmm__HE780_UnitDelay = 0.F;
               #endif

               

               
               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE638_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE638_UnitDelay11 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static UInt8 X_SVmcPmm__HE638_UnitDelay12 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE638_UnitDelay2 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE638_UnitDelay3 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE638_UnitDelay4 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static UInt8 X_SVmcPmm__HE638_UnitDelay5 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static UInt8 X_SVmcPmm__HE638_UnitDelay6 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE638_UnitDelay7 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE638_UnitDelay8 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE638_UnitDelay9 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static UInt8 X_SVmcPmm__HE639_UnitDelay4 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE643_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE644_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE657_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE658_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE659_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE660_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE672_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE672_UnitDelay2 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE673_UnitDelay15 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE674_UnitDelay7 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE675_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE675_UnitDelay10 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE675_UnitDelay2 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE676_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE677_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE678_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE679_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE680_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE681_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE682_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE683_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE684_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE685_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE686_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE687_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE701_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE702_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE703_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE704_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE705_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE706_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE707_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE717_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE718_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE723_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE724_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE731_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE733_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE734_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE735_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE743_UnitDelay7 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE744_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE744_UnitDelay2 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE744_UnitDelay3 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE748_UnitDelay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE749_UnitDelay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE750_UnitDelay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE751_UnitDelay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE752_UnitDelay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE753_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE771_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE774_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE775_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE776_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE777_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                  static Bool X_SVmcPmm__HE778_UnitDelay1 = 0;
               #endif

               

               
               if (cVcVmcPmm_B_UseOld12VStrtAllwd) {
                  
                  SVmcPmm__HE828_Switch = yVcDepSs_B_StartAllowed;
               }
               else {
                  
                  SVmcPmm__HE828_Switch = yVcDepSs_B_12VStartEnable;
               }
               
               if (sVcScIn_v_VehSpdLgt < cVcVmcPmm_v_IsgStandStillVehSpdOK) {
                  
                  X_SVmcPmm__HE759_UnitDelay = X_SVmcPmm__HE759_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE759_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_IsgStandStillVehSpdOK = X_SVmcPmm__HE759_UnitDelay >
                cVcVmcPmm_t_IsgStandStillVehSpdOK;

               
               if (sVcVmcAwd_X_RoadGrad >= 0.F) {
                  
                  SVmcPmm__HE745_Switch1 = sVcVmcAwd_X_RoadGrad;
               }
               else {
                  
                  SVmcPmm__HE745_Switch1 = sVcVmcAwd_X_RoadGrad * -1.F;
               }

               
               SVmcPmm__HE751_Rel = (cVcVmcPmm_X_IsgStopRoadGradMaxHyst +
                cVcVmcPmm_X_IsgStopRoadGradMax) <= SVmcPmm__HE745_Switch1;

               
               SVmcPmm__HE751_Rel1 = SVmcPmm__HE745_Switch1 <= cVcVmcPmm_X_IsgStopRoadGradMax;

               
               X_SVmcPmm__HE751_UnitDelay = (SVmcPmm__HE751_Rel && (!(SVmcPmm__HE751_Rel1))) ||
                ((!(SVmcPmm__HE751_Rel)) && (!(SVmcPmm__HE751_Rel1)) && X_SVmcPmm__HE751_UnitDelay);

               
               xVcVmcPmm_B_IsgStopRoadGradOK = !(X_SVmcPmm__HE751_UnitDelay);

               
               SVmcPmm__HE639__gicalOperator20 = (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATReverse)
                || (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive);

               
               xVcVmcPmm_B_IsgStopStandstillPre = cVcVmcPmm_B_UseIsgStandStill &&
                (!(yVcVmcPmm_B_EngOnReqEng)) && (CVmcPmm__HE1_D_IceStatus != 0) &&
                xVcVmcPmm_B_IsgStandStillVehSpdOK && xVcVmcPmm_B_IsgStopRoadGradOK &&
                SVmcPmm__HE639__gicalOperator20;

               
               if (X_SVmcPmm__HE744_UnitDelay3) {
                  
                  X_SVmcPmm__HE780_UnitDelay = X_SVmcPmm__HE780_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE780_UnitDelay = 0.F;
               }

               
               if (X_SVmcPmm__HE744_UnitDelay3) {
                  
                  X_SVmcPmm__HE779_UnitDelay = X_SVmcPmm__HE779_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE779_UnitDelay = 0.F;
               }

               
               if (sVcVmcBsl_Tq_FrntReqWhl < cVcVmcPmm_Tq_IsgStandStillBslTqOK) {
                  
                  X_SVmcPmm__HE761_UnitDelay = X_SVmcPmm__HE761_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE761_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_IsgStandStillBslTqOK = X_SVmcPmm__HE761_UnitDelay >
                cVcVmcPmm_t_IsgStandStillBslTqOK;

               
               if (sVcVdm_Tq_BrkTqAtWhlsReq > cVcVmcPmm_Tq_IsgStandStillBrkTqOK) {
                  
                  X_SVmcPmm__HE760_UnitDelay = X_SVmcPmm__HE760_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE760_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_IsgStandStillBrkTqOK = X_SVmcPmm__HE760_UnitDelay >
                cVcVmcPmm_t_IsgStandStillBrkTqOK;

               
               SVmcPmm__HE639__gicalOperator16 = xVcVmcPmm_B_IsgStandStillBslTqOK &&
                xVcVmcPmm_B_IsgStandStillBrkTqOK;

               
               xVcVmcPmm_B_IsgStopStandstill = xVcVmcPmm_B_IsgStopStandstillPre &&
                SVmcPmm__HE639__gicalOperator16;

               
               xVcVmcPmm_B_IsgStopRunReqStandstill = X_SVmcPmm__HE744_UnitDelay1 &&
                ((!(SVmcPmm__HE639__gicalOperator16)) && X_SVmcPmm__HE774_Delay) &&
                ((sVcDseGb_D_EfadPathAct == 1) || cVcVmcPmm_B_IsgStopRunReqIgnrEfadPathAct) &&
                cVcVmcPmm_B_UseIsgStopRunReqStandstill;

               
               X_SVmcPmm__HE774_Delay = SVmcPmm__HE639__gicalOperator16;

               
               X_SVmcPmm__HE744_UnitDelay1 = xVcVmcPmm_B_IsgStopStandstill;

               
               SVmcPmm__HE750_Rel = (cVcVmcPmm_v_IsgStopCoastSpdHyst +
                cVcVmcPmm_v_IsgStopCoastSpdMax) <= sVcScIn_v_VehSpdLgt;

               
               SVmcPmm__HE750_Rel1 = sVcScIn_v_VehSpdLgt <= cVcVmcPmm_v_IsgStopCoastSpdMax;

               
               X_SVmcPmm__HE750_UnitDelay = (SVmcPmm__HE750_Rel && (!(SVmcPmm__HE750_Rel1))) ||
                ((!(SVmcPmm__HE750_Rel)) && (!(SVmcPmm__HE750_Rel1)) && X_SVmcPmm__HE750_UnitDelay);

               
               SVmcPmm__HE752_Rel = cVcVmcPmm_v_IsgStopCoastSpdMinOn <= sVcScIn_v_VehSpdLgt;

               
               SVmcPmm__HE752_Rel1 = sVcScIn_v_VehSpdLgt <= cVcVmcPmm_v_IsgStopCoastSpdMinOff;

               
               X_SVmcPmm__HE752_UnitDelay = (SVmcPmm__HE752_Rel && (!(SVmcPmm__HE752_Rel1))) ||
                ((!(SVmcPmm__HE752_Rel)) && (!(SVmcPmm__HE752_Rel1)) && X_SVmcPmm__HE752_UnitDelay);

               
               SVmcPmm__HE748_Rel = (cVcVmcPmm_Tq_IsgStopCoastDrReqHyst +
                cVcVmcPmm_Tq_IsgStopCoastDrReqMax) <= sVcVmcBsl_Tq_FrntReqWhl;

               
               SVmcPmm__HE748_Rel1 = sVcVmcBsl_Tq_FrntReqWhl <= cVcVmcPmm_Tq_IsgStopCoastDrReqMax;

               
               X_SVmcPmm__HE748_UnitDelay = (SVmcPmm__HE748_Rel && (!(SVmcPmm__HE748_Rel1))) ||
                ((!(SVmcPmm__HE748_Rel)) && (!(SVmcPmm__HE748_Rel1)) && X_SVmcPmm__HE748_UnitDelay);

               
               SVmcPmm__HE749_Rel = cVcVmcPmm_Tq_IsgStopCoastDrReqMin <= sVcVmcBsl_Tq_FrntReqWhl;

               
               SVmcPmm__HE749_Rel1 = sVcVmcBsl_Tq_FrntReqWhl <= (cVcVmcPmm_Tq_IsgStopCoastDrReqMin -
                 cVcVmcPmm_Tq_IsgStopCoastDrReqHyst);

               
               X_SVmcPmm__HE749_UnitDelay = (SVmcPmm__HE749_Rel && (!(SVmcPmm__HE749_Rel1))) ||
                ((!(SVmcPmm__HE749_Rel)) && (!(SVmcPmm__HE749_Rel1)) && X_SVmcPmm__HE749_UnitDelay);

               
               SVmcPmm__HE639__gicalOperator21 = (!(X_SVmcPmm__HE748_UnitDelay)) &&
                X_SVmcPmm__HE749_UnitDelay;

               
               xVcVmcPmm_B_IsgStopCoast = cVcVmcPmm_B_UseIsgStopCoast &&
                (!(yVcVmcPmm_B_EngOnReqEng)) && (!(X_SVmcPmm__HE750_UnitDelay)) &&
                X_SVmcPmm__HE752_UnitDelay && (CVmcPmm__HE1_D_IceStatus != 0) &&
                SVmcPmm__HE639__gicalOperator20 && SVmcPmm__HE639__gicalOperator21;

               
               xVcVmcPmm_B_IsgStopRunReqCoast = X_SVmcPmm__HE744_UnitDelay2 &&
                ((!(SVmcPmm__HE639__gicalOperator21)) && X_SVmcPmm__HE775_Delay) &&
                cVcVmcPmm_B_UseIsgStopRunReqCoast;

               
               X_SVmcPmm__HE775_Delay = SVmcPmm__HE639__gicalOperator21;

               
               X_SVmcPmm__HE744_UnitDelay2 = xVcVmcPmm_B_IsgStopCoast;

               
               X_SVmcPmm__HE778_UnitDelay1 = (sVcDseGb_D_EfadPathAct != 2) && (sVcDtcAtr_D_GearLevAT
                 == cVc_D_GearLevATDrive) && (xVcVmcPmm_B_IsgStopStandstill ||
                X_SVmcPmm__HE778_UnitDelay1);

               
               xVcVmcPmm_B_IsgStopPostRunReqStandstill = cVcVmcPmm_B_UseIsgStopPostRunReqStandstill
                && ((!(SVmcPmm__HE639__gicalOperator16)) && X_SVmcPmm__HE776_Delay) &&
                X_SVmcPmm__HE778_UnitDelay1;

               
               X_SVmcPmm__HE776_Delay = SVmcPmm__HE639__gicalOperator16;

               
               xVcVmcPmm_B_EngRunReqIsgStop = ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATReverse) ||
                (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive)) && ((sVcDseGb_D_EfadPathAct != 2)
                || (X_SVmcPmm__HE780_UnitDelay <= cVcVmcPmm_t_EngRunReqIsgStopMin)) &&
                (X_SVmcPmm__HE779_UnitDelay <= cVcVmcPmm_t_EngRunReqIsgStopMax) &&
                (((xVcVmcPmm_B_IsgStopRunReqStandstill || xVcVmcPmm_B_IsgStopRunReqCoast ||
                xVcVmcPmm_B_IsgStopPostRunReqStandstill) && (sVcDtcAtr_D_GearLevAT ==
                cVc_D_GearLevATDrive)) || X_SVmcPmm__HE777_UnitDelay1);

               
               X_SVmcPmm__HE777_UnitDelay1 = xVcVmcPmm_B_EngRunReqIsgStop;

               
               X_SVmcPmm__HE744_UnitDelay3 = xVcVmcPmm_B_EngRunReqIsgStop;

               
               xVcVmcPmm_B_Wait4CluStrtWhlTqLow = (sVcVmcWtd_Tq_FrntReqWhl <
                cVcVmcPmm_Tq_Wait4CluStrtEna) || ((sVcVmcWtd_Tq_FrntReqWhl <=
                cVcVmcPmm_Tq_Wait4CluStrtDi) && X_SVmcPmm__HE734_UnitDelay1);

               
               X_SVmcPmm__HE734_UnitDelay1 = xVcVmcPmm_B_Wait4CluStrtWhlTqLow;

               
               SVmcPmm__HE732_Sum3 = ts_VcVmcPmm__HEP7 + cVcVmcPmm_tc_VdmAccFilt;
               if (SVmcPmm__HE732_Sum3 > 1e-06F) {
                  SVmcPmm__HE732_MinMax = SVmcPmm__HE732_Sum3;
               }
               else {
                  SVmcPmm__HE732_MinMax = 1e-06F;
               }

               
               if (SVmcPmm__HE732_MinMax != 0.F) {
                  
                  SVmcPmm__HE732_Prod1 = ts_VcVmcPmm__HEP7 / SVmcPmm__HE732_MinMax;
               }
               else {
                  
                  if (ts_VcVmcPmm__HEP7 < 0.F) {
                     SVmcPmm__HE732_Prod1 = -3.402823466e+38F;
                  }
                  else {
                     SVmcPmm__HE732_Prod1 = 3.402823466e+38F;
                  }
               }

               
               rVcVmcPmm_a_Veh = X_SVmcPmm__HE732_Del1 + ((sVcVdm_a_ALgtStdFromWhlSpd -
                X_SVmcPmm__HE732_Del1) * SVmcPmm__HE732_Prod1);

               
               X_SVmcPmm__HE732_Del1 = rVcVmcPmm_a_Veh;

               
               xVcVmcPmm_B_Wait4CluStrtWhlAccHigh = (rVcVmcPmm_a_Veh > cVcVmcPmm_a_Wait4CluStrtEna)
                || ((rVcVmcPmm_a_Veh >= cVcVmcPmm_a_Wait4CluStrtDi) && X_SVmcPmm__HE733_UnitDelay1);

               
               X_SVmcPmm__HE733_UnitDelay1 = xVcVmcPmm_B_Wait4CluStrtWhlAccHigh;

               
               xVcVmcPmm_B_Wait4CluStrtAccPedAct = (sVcScIn_X_AccPedalPos >
                cVcVmcPmm_X_Wait4CluStrtEna) || ((sVcScIn_X_AccPedalPos >=
                cVcVmcPmm_X_Wait4CluStrtDi) && X_SVmcPmm__HE735_UnitDelay1);

               
               X_SVmcPmm__HE735_UnitDelay1 = xVcVmcPmm_B_Wait4CluStrtAccPedAct;

               
               xVcVmcPmm_B_Wait4CluStrtLowVehSpd = sVcScIn_v_VehSpdLgtMax <
                cVcVmcPmm_v_Efad12VStartMax;

               
               if (cVcVmcPmm_B_Use12vStrtPsblInCluStrtAbort) {
                  
                  SVmcPmm__HE742_Switch = X_SVmcPmm__HE675_UnitDelay1;
               }
               else {
                  
                  SVmcPmm__HE742_Switch = 1;
               }

               
               xVcVmcPmm_B_CluStrtTqRsvBlk = (sVcMtcAjc_Tq_EfadReqWhl > sVcDseWt_Tq_EfadMaxElDrvWhl)
                 && SVmcPmm__HE742_Switch;

               
               if (cVcVmcPmm_B_UseRespStrtReqInCluStrtAllw) {
                  
                  SVmcPmm__HE741_Switch = (yVcDeDmm_B_RespStartReq &&
                   cVcVmcPmm_B_UseRespStartReqFromDeDmm) || (yVcVmcEm_B_RespStartReq &&
                   cVcVmcPmm_B_UseRespStartreqFromVmcEm) || (xVcVmcPmm_B_CluStrtTqRsvBlk &&
                   cVcVmcPmm_B_UseTqOffsForCluStrtEval);
               }
               else {
                  
                  SVmcPmm__HE741_Switch = 1;
               }

               
               xVcVmcPmm_B_CluStrtAllwd = ((!(cVcVmcPmm_B_EfadUseFactory12VStrt)) ||
                (!(sVcDeDmm_B_DrMdeFactory))) && (!(X_SVmcPmm__HE675_UnitDelay2)) &&
                (!(X_SVmcPmm__HE675_UnitDelay10)) && (CVmcPmm__HE1_D_IceStatus != 2) &&
                ((CVmcPmm__HE1_D_IceStatus != cVcVmcPmm_D_IceStsStarting) || (sVcEc_n_Eng <=
                cVcVmcPmm_n_CluStrtAllwdEngSpdMax)) && ((!(xVcVmcPmm_B_EngRunReqIsgStop)) ||
                (!(cVcVmcPmm_B_IsgStopRunReqCluStrtBlkEna))) && ((!(cVcVmcPmm_B_CluStrtInDeplBlk))
                || (sVcDtcAtr_v_VehDrDirection >= cVcVmcPmm_v_CluStrtSpdAllw) ||
                ((!(yVcVmcEm_B_Depletion)) && (!(cVcVmcPmm_B_IgnrDepl))) ||
                (!(SVmcPmm__HE741_Switch)));

               
               SVmcPmm__HE673__gicalOperator23 = cVcVmcPmm_B_UseWait4CluStrt &&
                xVcVmcPmm_B_Wait4CluStrtWhlTqLow && xVcVmcPmm_B_Wait4CluStrtWhlAccHigh &&
                xVcVmcPmm_B_Wait4CluStrtAccPedAct && xVcVmcPmm_B_Wait4CluStrtLowVehSpd &&
                xVcVmcPmm_B_EngRunReqTotPre && ((6 != sVcDeDmm_D_DrvMode) && (sVcDeDmm_D_DrvMode !=
                11)) && (((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive) || (sVcDtcAtr_D_GearLevAT
                == cVc_D_GearLevATReverse)) && yVcGscSgs_B_CluStrtAvl && xVcVmcPmm_B_CluStrtAllwd);

               
               if (SVmcPmm__HE673__gicalOperator23) {
                  
                  X_SVmcPmm__HE737_UnitDelay = X_SVmcPmm__HE737_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE737_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_Wait4CluStrtTiOut = X_SVmcPmm__HE737_UnitDelay >
                cVcVmcPmm_t_Wait4CluStrtTiOut;

               
               xVcVmcPmm_B_Wait4CluStrt = SVmcPmm__HE673__gicalOperator23 &&
                (!(xVcVmcPmm_B_Wait4CluStrtTiOut));

               
               xVcVmcPmm_B_IsgStopPwrDwn = cVcVmcPmm_B_UseIsgStopPwrDwn &&
                (!(SVmcPmm__HE829_Switch)) && (CVmcPmm__HE1_D_IceStatus != 0);

               
               X_SVmcPmm__HE6_UnitDelay5 = xVcVmcPmm_B_IsgStopStandstill || xVcVmcPmm_B_IsgStopCoast
                 || xVcVmcPmm_B_IsgStopPwrDwn;

               
               X_SVmcPmm__HE753_UnitDelay1 = (sVcScIn_v_VehSpdLgt < cVcVmcPmm_v_EfadVehSpdOKIsgBrk)
                || ((sVcScIn_v_VehSpdLgt <= cVcVmcPmm_v_EfadVehSpdNOKIsgBrk) &&
                X_SVmcPmm__HE753_UnitDelay1);

               
               if (X_SVmcPmm__HE753_UnitDelay1) {
                  
                  X_SVmcPmm__HE756_UnitDelay = X_SVmcPmm__HE756_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE756_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_VehSpdOKIsgBrk = X_SVmcPmm__HE756_UnitDelay >
                cVcVmcPmm_t_EfadVehSpdOKIsgBrk;

               
               if (sVcVdm_Tq_BrkTqAtWhlsReq > cVcVmcPmm_Tq_EfadBrkOKIsgBrk) {
                  
                  X_SVmcPmm__HE757_UnitDelay = X_SVmcPmm__HE757_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE757_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_BrkOKIsgBrk = X_SVmcPmm__HE757_UnitDelay > cVcVmcPmm_t_EfadBrkOKIsgBrk;

               
               if (sVcScIn_X_AccPedalPos < cVcVmcPmm_X_EfadAccPedOKIsgBrk) {
                  
                  X_SVmcPmm__HE758_UnitDelay = X_SVmcPmm__HE758_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE758_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_AccPedOKIsgBrk = X_SVmcPmm__HE758_UnitDelay >
                cVcVmcPmm_t_EfadAccPedOKIsgBrk;

               
               SVmcPmm__HE639__ionalOperator13 = sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive;

               
               SVmcPmm__HE639__gicalOperator23 = yVcDseGbAvl_B_EfadIsgPathAvoid &&
                SVmcPmm__HE639__ionalOperator13;

               
               xVcVmcPmm_B_IsgChrgReqBrk = cVcVmcPmm_B_UseIsgBrk && xVcVmcPmm_B_VehSpdOKIsgBrk &&
                xVcVmcPmm_B_BrkOKIsgBrk && xVcVmcPmm_B_AccPedOKIsgBrk && yVcVmcEm_B_PrioChrgReq &&
                ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATReverse) ||
                SVmcPmm__HE639__gicalOperator23);

               
               if (yVcVmcEm_B_ChrgReq) {
                  
                  X_SVmcPmm__HE762_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE762_UnitDelay = X_SVmcPmm__HE762_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               if (CVmcPmm__HE1_D_IceStatus == 2) {
                  
                  X_SVmcPmm__HE754_UnitDelay = X_SVmcPmm__HE754_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE754_UnitDelay = 0.F;
               }

               
               if (cVcVmcPmm_B_TrnModIsgReq) {
                  
                  xVcVmcPmm_B_TrnModOKIsgReq = sVcDtcAtr_D_TransMode < 3;
               }
               else {
                  
                  xVcVmcPmm_B_TrnModOKIsgReq = sVcVmcPmm_D_TransModeReq < 3;
               }

               
               SVmcPmm__HE743__ationalOperator = sVcDeDmm_D_DrvMode == 13;

               
               if (yVcVmcEm_B_PrioChrgReq || (sVcEmiHeat_D_EngUseReq == 2)) {
                  
                  if (SVmcPmm__HE743__ationalOperator) {
                     
                     SVmcPmm__HE766_Switch = cVcVmcPmm_v_EfadVehSpdOKPrioIsgDrvHybridEco;
                  }
                  else {
                     
                     SVmcPmm__HE766_Switch = cVcVmcPmm_v_EfadVehSpdOKPrioIsgDrv;
                  }
               }
               else {
                  
                  if (SVmcPmm__HE743__ationalOperator) {
                     
                     SVmcPmm__HE766_Switch = cVcVmcPmm_v_EfadVehSpdOKIsgDrvHybridEco;
                  }
                  else {
                     
                     SVmcPmm__HE766_Switch = cVcVmcPmm_v_EfadVehSpdOKIsgDrv;
                  }
               }

               
               if (yVcVmcEm_B_PrioChrgReq || (sVcEmiHeat_D_EngUseReq == 2)) {
                  
                  if (SVmcPmm__HE743__ationalOperator) {
                     
                     SVmcPmm__HE765_Switch = cVcVmcPmm_v_EfadVehSpdNOKPrioIsgDrvHybridEco;
                  }
                  else {
                     
                     SVmcPmm__HE765_Switch = cVcVmcPmm_v_EfadVehSpdNOKPrioIsgDrv;
                  }
               }
               else {
                  
                  if (SVmcPmm__HE743__ationalOperator) {
                     
                     SVmcPmm__HE765_Switch = cVcVmcPmm_v_EfadVehSpdNOKIsgDrvHybridEco;
                  }
                  else {
                     
                     SVmcPmm__HE765_Switch = cVcVmcPmm_v_EfadVehSpdNOKIsgDrv;
                  }
               }

               
               X_SVmcPmm__HE771_UnitDelay1 = (sVcScIn_v_VehSpdLgt < SVmcPmm__HE766_Switch) ||
                ((sVcScIn_v_VehSpdLgt <= SVmcPmm__HE765_Switch) && X_SVmcPmm__HE771_UnitDelay1);

               
               if (X_SVmcPmm__HE771_UnitDelay1) {
                  
                  X_SVmcPmm__HE773_UnitDelay = X_SVmcPmm__HE773_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE773_UnitDelay = 0.F;
               }

               
               if (X_SVmcPmm__HE771_UnitDelay1) {
                  
                  X_SVmcPmm__HE772_UnitDelay = X_SVmcPmm__HE772_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE772_UnitDelay = 0.F;
               }

               
               if (yVcVmcEm_B_PrioChrgReq || (sVcEmiHeat_D_EngUseReq == 2)) {
                  
                  xVcVmcPmm_B_VehSpdOKIsgDrv = X_SVmcPmm__HE773_UnitDelay >
                   cVcVmcPmm_t_CatHeatVehSpdOKIsgDrv;
               }
               else {
                  
                  if (X_SVmcPmm__HE743_UnitDelay7) {
                     
                     xVcVmcPmm_B_VehSpdOKIsgDrv = X_SVmcPmm__HE771_UnitDelay1;
                  }
                  else {
                     
                     xVcVmcPmm_B_VehSpdOKIsgDrv = X_SVmcPmm__HE772_UnitDelay >
                      cVcVmcPmm_t_VehSpdOKIsgDrv;
                  }
               }

               
               xVcVmcPmm_B_IsgChrgReqDrv = (!(SVmcPmm__HE639__gicalOperator23)) &&
                SVmcPmm__HE639__ionalOperator13 && ((2 == sVcEmiHeat_D_EngUseReq) ||
                (X_SVmcPmm__HE762_UnitDelay <= cVcVmcPmm_t_ChrgReqDly)) &&
                (X_SVmcPmm__HE754_UnitDelay > cVcVmcPmm_t_EfadIceStsDlyIsgDrv) &&
                xVcVmcPmm_B_TrnModOKIsgReq && ((2 == sVcEmiHeat_D_EngUseReq) ||
                yVcVmcEm_B_PrioChrgReq || ((sVcDeDmm_D_DrvMode != 11) && ((!(yVcVmcEm_B_Charge)) ||
                (!(cVcVmcPmm_B_UseChargeInIsgReq))))) && xVcVmcPmm_B_VehSpdOKIsgDrv;

               
               SVmcPmm__HE639__ionalOperator18 = sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATNeutral;

               
               if (SVmcPmm__HE639__ionalOperator18) {
                  
                  X_SVmcPmm__HE755_UnitDelay = X_SVmcPmm__HE755_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE755_UnitDelay = 0.F;
               }

               
               if ((X_SVmcPmm__HE639_UnitDelay4 == 2) && (CVmcPmm__HE1_D_IceStatus == 2)) {
                  
                  SVmcPmm__HE747_Switch = X_SVmcPmm__HE755_UnitDelay > cVcVmcPmm_t_GearLevNDly;
               }
               else {
                  
                  SVmcPmm__HE747_Switch = SVmcPmm__HE639__ionalOperator18;
               }

               
               xVcVmcPmm_B_IsgChrgReq = ((CVmcPmm__HE1_D_IceStatus == 2) ||
                (CVmcPmm__HE1_D_IceStatus == 3)) && (xVcVmcPmm_B_IsgChrgReqBrk ||
                xVcVmcPmm_B_IsgChrgReqDrv || X_SVmcPmm__HE6_UnitDelay5 || (sVcDtcAtr_D_GearLevAT ==
                cVc_D_GearLevATPark) || SVmcPmm__HE747_Switch);

               
               xVcVmcPmm_B_IsgStrtGearLvrDEfadIsgAct = (sVcDtcAtr_D_GearLevAT ==
                cVc_D_GearLevATDrive) && (sVcDseGb_D_EfadPathAct == 1) && (sVcVmcPmm_D_TransModeReq
                == 1);

               
               if (cVcVmcPmm_B_IsgStrtInDUseEfadPathAct) {
                  
                  SVmcPmm__HE721_Switch = xVcVmcPmm_B_IsgStrtGearLvrDEfadIsgAct;
               }
               else {
                  
                  SVmcPmm__HE721_Switch = xVcVmcPmm_B_EngRunReqIsgStop;
               }

               
               if (X_SVmcPmm__HE672_UnitDelay1) {
                  
                  SVmcPmm__HE720_Switch = cVcVmcPmm_Tq_EfadIsgStrtEnaFlt;
               }
               else {
                  
                  SVmcPmm__HE720_Switch = cVcVmcPmm_Tq_EfadIsgStrtEna;
               }

               
               if (X_SVmcPmm__HE672_UnitDelay1) {
                  
                  SVmcPmm__HE719_Switch = cVcVmcPmm_Tq_EfadIsgStrtDiFlt;
               }
               else {
                  
                  SVmcPmm__HE719_Switch = cVcVmcPmm_Tq_EfadIsgStrtDi;
               }

               
               X_SVmcPmm__HE723_UnitDelay1 = (sVcVmcWtd_Tq_FrntReqWhl < SVmcPmm__HE720_Switch) ||
                ((sVcVmcWtd_Tq_FrntReqWhl <= SVmcPmm__HE719_Switch) && X_SVmcPmm__HE723_UnitDelay1);

               
               if (X_SVmcPmm__HE723_UnitDelay1) {
                  
                  X_SVmcPmm__HE725_UnitDelay = X_SVmcPmm__HE725_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE725_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_IsgStrtWhlTrqOK = X_SVmcPmm__HE725_UnitDelay >
                cVcVmcPmm_t_IsgStrtWhlTrqOK;

               
               SVmcPmm__HE672__gicalOperator10 = (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive) ||
                (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATReverse);

               
               if (sVcDtcAtr_v_VehDrDirection < cVcVmcPmm_v_VehSpdLimIsgStrtGearLvrDR) {
                  
                  X_SVmcPmm__HE726_UnitDelay = X_SVmcPmm__HE726_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE726_UnitDelay = 0.F;
               }

               
               TabIdxS18T6((const Float32 *) &(mVcVmcPmm_Z_BrkRoadIncline_r[0]), 8,
                sVcVdm_Tq_BrkTqAtWhlsReq, SVmcPmm__HE730__rkRoadIncline_r);

               
               SVmcPmm__HE728_Sum3 = ts_VcVmcPmm__HEP7 + cVcVmcPmm_tc_LatAccFilt;
               if (SVmcPmm__HE728_Sum3 > 1e-06F) {
                  SVmcPmm__HE728_MinMax = SVmcPmm__HE728_Sum3;
               }
               else {
                  SVmcPmm__HE728_MinMax = 1e-06F;
               }

               
               if (SVmcPmm__HE728_MinMax != 0.F) {
                  
                  SVmcPmm__HE728_Prod1 = ts_VcVmcPmm__HEP7 / SVmcPmm__HE728_MinMax;
               }
               else {
                  
                  if (ts_VcVmcPmm__HEP7 < 0.F) {
                     SVmcPmm__HE728_Prod1 = -3.402823466e+38F;
                  }
                  else {
                     SVmcPmm__HE728_Prod1 = 3.402823466e+38F;
                  }
               }

               
               X_SVmcPmm__HE728_Del1 = X_SVmcPmm__HE728_Del1 + ((sVcVdm_a_ALat -
                X_SVmcPmm__HE728_Del1) * SVmcPmm__HE728_Prod1);

               
               if (cVcVmcPmm_B_UseAwdRoadGrad) {
                  
                  rVcVmcPmm_Z_RoadGradient = sVcVmcAwd_X_RoadGrad;
               }
               else {
                  
                  rVcVmcPmm_Z_RoadGradient = X_SVmcPmm__HE728_Del1;
               }

               
               TabIdxS18T6((const Float32 *) &(mVcVmcPmm_Z_BrkRoadIncline_c[0]), 8,
                rVcVmcPmm_Z_RoadGradient, SVmcPmm__HE730__rkRoadIncline_c);

               
               rVcVmcPmm_Z_BrkRoadIncline =
                mVcVmcPmm_Z_BrkRoadIncline[SVmcPmm__HE730__rkRoadIncline_r[0]][SVmcPmm__HE730__rkRoadIncline_c[0]];

               
               xVcVmcPmm_B_BrkRoadIncline = rVcVmcPmm_Z_BrkRoadIncline == 1;

               
               xVcVmcPmm_B_EpbActive = (sVcVdm_D_EpbSts == cVcVmcPmm_D_EpbCoding1) ||
                (sVcVdm_D_EpbSts == cVcVmcPmm_D_EpbCoding2) || (sVcVdm_D_EpbSts ==
                cVcVmcPmm_D_EpbCoding3) || (sVcVdm_D_EpbSts == cVcVmcPmm_D_EpbCoding4);

               
               if (xVcVmcPmm_B_BrkRoadIncline || xVcVmcPmm_B_EpbActive) {
                  
                  X_SVmcPmm__HE727_UnitDelay = X_SVmcPmm__HE727_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE727_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_NonSysStrt = (!(yVcDeDmm_B_RespStartReq)) && (sVcDeDmm_D_EngRunReqDriver
                == 2);

               
               if (cVcVmcPmm_B_UseIsgStrtAtStndStill) {
                  
                  SVmcPmm__HE722_Switch = 1;
               }
               else {
                  
                  SVmcPmm__HE722_Switch = xVcVmcPmm_B_NonSysStrt;
               }

               
               SVmcPmm__HE672_LogicalOperator7 = X_SVmcPmm__HE672_UnitDelay2 ||
                (!(SVmcPmm__HE828_Switch)) || (SVmcPmm__HE848_Switch <
                cVcVmcPmm_Te_Efad12VStrtEngClntMin);

               
               xVcVmcPmm_B_IsgStrtGearLvrDRBraking = xVcVmcPmm_B_IsgStrtWhlTrqOK &&
                SVmcPmm__HE672__gicalOperator10 && (((X_SVmcPmm__HE726_UnitDelay >
                cVcVmcPmm_t_VehSpdLimIsgStrtGearLvrDR) && (X_SVmcPmm__HE727_UnitDelay >
                cVcVmcPmm_t_BrkLimIsgStrtGearLvrDR) && SVmcPmm__HE722_Switch) ||
                SVmcPmm__HE672_LogicalOperator7);

               
               xVcVmcPmm_B_IsgStrtGearLvrDR = SVmcPmm__HE721_Switch ||
                xVcVmcPmm_B_IsgStrtGearLvrDRBraking;

               
               if (SVmcPmm__HE829_Switch) {
                  
                  X_SVmcPmm__HE739_UnitDelay = X_SVmcPmm__HE739_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE739_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_DrvCycActvFirstStrtTiOut = X_SVmcPmm__HE739_UnitDelay >
                cVcVmcPmm_t_DrvCycActvFirstStrt;

               
               xVcVmcPmm_B_DrvCycActvFirstStrt = (sVcTcm_Te_TrsmOilT < cVcVmcPmm_Te_TrnOil) &&
                SVmcPmm__HE829_Switch && (!(xVcVmcPmm_B_DrvCycActvFirstStrtTiOut));

               
               if (X_SVmcPmm__HE6_UnitDelay14) {
                  
                  X_SVmcPmm__HE738_UnitDelay = X_SVmcPmm__HE738_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE738_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_EngOnReqTiOut = X_SVmcPmm__HE738_UnitDelay > cVcVmcPmm_t_EngOnReqDly;

               
               xVcVmcPmm_B_EngOnReqDly = X_SVmcPmm__HE6_UnitDelay14 &&
                (!(xVcVmcPmm_B_EngOnReqTiOut)) && cVcVmcPmm_B_UseEngOnReqDly;

               
               xVcVmcPmm_B_Efad2IceUnavl = yVcDsePcr_B_IsgStartDisableRq || yVcDsePcr_B_IsgDisableRq
                 || yVcDseGb_B_EfadIsgPathNotAvl;

               
               xVcVmcPmm_B_Efad2WhlUnavl = yVcDseGb_B_EfadWhlPathNotAvl ||
                yVcDsePcr_B_EfadDisableRq;

               
               xVcVmcPmm_B_EfadUnavl = (xVcVmcPmm_B_Efad2IceUnavl && xVcVmcPmm_B_Efad2WhlUnavl) ||
                ((!(yVcDepTre_B_ISGTqAllw)) && (sVcDtcAtr_D_GearLevAT != cVc_D_GearLevATReverse));

               
               xVcVmcPmm_B_IsgStrtAllwd = ((!(sVcDeDmm_B_DrMdeFactory)) ||
                (!(cVcVmcPmm_B_EfadUseFactory12VStrt))) && (sVcCidd_D_IsgModSts != 7) &&
                (CVmcPmm__HE1_D_IceStatus != 2) && ((CVmcPmm__HE1_D_IceStatus !=
                cVcVmcPmm_D_IceStsStarting) || (sVcEc_n_Eng <= cVcVmcPmm_n_IsgStrtAllwdEngSpdMax) ||
                 xVcVmcPmm_B_DrvCycActvFirstStrt || xVcVmcPmm_B_EngOnReqDly) &&
                (!(X_SVmcPmm__HE674_UnitDelay7)) && (!(yVcDsePcr_B_IsgStartDisableRq)) &&
                (((!(xVcVmcPmm_B_Efad2IceUnavl)) && (!(xVcVmcPmm_B_EfadUnavl))) ||
                xVcVmcPmm_B_DrvCycActvFirstStrt);

               
               xVcVmcPmm_B_IsgStrtPsbl = cVcVmcPmm_B_EfadUseIsgStrt && (xVcVmcPmm_B_IsgStrtGearLvrDR
                 || (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATPark) || (sVcDtcAtr_D_GearLevAT ==
                cVc_D_GearLevATNeutral)) && xVcVmcPmm_B_IsgStrtAllwd;

               
               xVcVmcPmm_B_CluStrtVehSpdOK = (sVcDtcAtr_v_VehDrDirection >
                cVcVmcPmm_v_EfadCluStrtEna) || ((sVcDtcAtr_v_VehDrDirection >=
                cVcVmcPmm_v_EfadCluStrtDi) && X_SVmcPmm__HE707_UnitDelay1);

               
               X_SVmcPmm__HE707_UnitDelay1 = xVcVmcPmm_B_CluStrtVehSpdOK;

               
               xVcVmcPmm_B_CluStrtPsbl = cVcVmcPmm_B_EfadUseCluStrt && xVcVmcPmm_B_CluStrtVehSpdOK
                && ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive) || (sVcDtcAtr_D_GearLevAT ==
                cVc_D_GearLevATReverse)) && yVcGscSgs_B_CluStrtAvl && xVcVmcPmm_B_CluStrtAllwd;

               
               SVmcPmm__HE638_LogicalOperator1 = xVcVmcPmm_B_CluStrtPsbl &&
                ((!(X_SVmcPmm__HE638_UnitDelay3)) && (!(X_SVmcPmm__HE638_UnitDelay1))) &&
                X_SVmcPmm__HE6_UnitDelay14;

               
               if (cVcVmcPmm_B_CluStrtReq_swi) {
                  
                  SVmcPmm__HE695_Switch = cVcVmcPmm_B_CluStrtReq_dbi;
               }
               else {
                  
                  SVmcPmm__HE695_Switch = SVmcPmm__HE638_LogicalOperator1 &&
                   (!(X_SVmcPmm__HE686_UnitDelay1));
               }

               
               X_SVmcPmm__HE686_UnitDelay1 = SVmcPmm__HE638_LogicalOperator1;

               
               X_SVmcPmm__HE703_UnitDelay1 = SVmcPmm__HE695_Switch || (X_SVmcPmm__HE6_UnitDelay14 &&
                 ((CVmcPmm__HE1_D_IceStatus != 2) || yVcDtcSt_B_CluStrtAct) &&
                (yVcDtcSt_B_CluStrtAct || (!(X_SVmcPmm__HE678_Delay))) &&
                (!(X_SVmcPmm__HE638_UnitDelay4)) && SVmcPmm__HE829_Switch &&
                X_SVmcPmm__HE703_UnitDelay1);

               
               X_SVmcPmm__HE678_Delay = yVcDtcSt_B_CluStrtAct;

               
               SVmcPmm__HE638__gicalOperator16 = xVcVmcPmm_B_IsgStrtPsbl &&
                ((!(X_SVmcPmm__HE703_UnitDelay1)) && (!(X_SVmcPmm__HE638_UnitDelay7))) &&
                X_SVmcPmm__HE6_UnitDelay14;

               
               xVcVmcPmm_B_IsgStrtGearLvrDRAbort = cVcVmcPmm_B_IsgStrtGearLvrDRAbortEna &&
                SVmcPmm__HE672__gicalOperator10 && ((!(xVcVmcPmm_B_IsgStrtGearLvrDRBraking)) &&
                X_SVmcPmm__HE718_Delay) && (!(SVmcPmm__HE721_Switch));

               
               X_SVmcPmm__HE718_Delay = xVcVmcPmm_B_IsgStrtGearLvrDRBraking;

               
               X_SVmcPmm__HE702_UnitDelay1 = (SVmcPmm__HE638__gicalOperator16 &&
                (!(X_SVmcPmm__HE687_UnitDelay1))) || (X_SVmcPmm__HE6_UnitDelay14 &&
                (yVcDtcSt_B_StrtAct || (!(X_SVmcPmm__HE679_Delay))) &&
                (!(X_SVmcPmm__HE638_UnitDelay9)) && SVmcPmm__HE829_Switch &&
                ((!(xVcVmcPmm_B_IsgStrtGearLvrDRAbort)) || X_SVmcPmm__HE638_UnitDelay8) &&
                X_SVmcPmm__HE702_UnitDelay1);

               
               X_SVmcPmm__HE679_Delay = yVcDtcSt_B_StrtAct;

               
               X_SVmcPmm__HE687_UnitDelay1 = SVmcPmm__HE638__gicalOperator16;

               
               if (cVcVmcPmm_B_IsgStrtPahReq_swi) {
                  
                  X_SVmcPmm__HE6_UnitDelay6 = cVcVmcPmm_B_IsgStrtPahReq_dbi;
               }
               else {
                  
                  X_SVmcPmm__HE6_UnitDelay6 = X_SVmcPmm__HE702_UnitDelay1;
               }

               
               X_SVmcPmm__HE638_UnitDelay1 = X_SVmcPmm__HE6_UnitDelay6;

               
               xVcVmcPmm_B_IsgReq = xVcVmcPmm_B_IsgChrgReq || X_SVmcPmm__HE6_UnitDelay6;

               
               if (SVmcPmm__HE829_Switch) {
                  
                  X_SVmcPmm__HE670_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE670_UnitDelay = X_SVmcPmm__HE670_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               if (CVmcPmm__HE1_D_IceStatus != 0) {
                  
                  X_SVmcPmm__HE663_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE663_UnitDelay = X_SVmcPmm__HE663_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               xVcVmcPmm_B_Efad2IcePahReq = (xVcVmcPmm_B_IsgReq || xVcVmcPmm_B_Efad2WhlUnavl) &&
                (SVmcPmm__HE829_Switch || ((X_SVmcPmm__HE670_UnitDelay <=
                cVcVmcPmm_t_IsgDrCycStopMax) && (X_SVmcPmm__HE663_UnitDelay <=
                cVcVmcPmm_t_IsgDrCycStop))) && ((!(xVcVmcPmm_B_EfadUnavl)) &&
                (!(xVcVmcPmm_B_Efad2IceUnavl)));

               
               if (xVcVmcPmm_B_Efad2IcePahReq) {
                  
                  X_SVmcPmm__HE664_UnitDelay = X_SVmcPmm__HE664_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE664_UnitDelay = 0.F;
               }

               
               if ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive) || (sVcDtcAtr_D_GearLevAT ==
                cVc_D_GearLevATReverse)) {
                  
                  X_SVmcPmm__HE671_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE671_UnitDelay = X_SVmcPmm__HE671_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               xVcVmcPmm_B_Efad2WhlPahReq = (!(xVcVmcPmm_B_Efad2IcePahReq)) &&
                (X_SVmcPmm__HE671_UnitDelay <= cVcVmcPmm_t_GearLevDRDly) &&
                yVcPpmPsm_B_DriveCycleActive && yVcPpmPsm_B_PropulsionAllowed &&
                ((!(xVcVmcPmm_B_EfadUnavl)) && (!(xVcVmcPmm_B_Efad2WhlUnavl)));

               
               if (xVcVmcPmm_B_Efad2WhlPahReq) {
                  
                  X_SVmcPmm__HE667_UnitDelay = X_SVmcPmm__HE667_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE667_UnitDelay = 0.F;
               }

               
               if (!(SVmcPmm__HE829_Switch)) {
                  
                  X_SVmcPmm__HE661_UnitDelay = X_SVmcPmm__HE661_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE661_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_DrvCycTiOut = X_SVmcPmm__HE661_UnitDelay > cVcVmcPmm_t_EfadDrvCycTiOut;

               
               xVcVmcPmm_B_Efad2IceReqRst = xVcVmcPmm_B_EfadUnavl || ((xVcVmcPmm_B_Efad2IceUnavl ||
                ((!(xVcVmcPmm_B_Efad2IcePahReq)) && (!(xVcVmcPmm_B_Efad2WhlPahReq))) ||
                (!(SVmcPmm__HE829_Switch))) && (xVcVmcPmm_B_DrvCycTiOut ||
                (yVcVmcWtc_B_EfadPathDisabled && yVcDtcTc_B_IsgPathDisabled)));

               
               xVcVmcPmm_B_Efad2IceReq = (xVcVmcPmm_B_Efad2IcePahReq && ((X_SVmcPmm__HE664_UnitDelay
                 > cVcVmcPmm_t_EfadPahDiTiOut) || yVcVmcWtc_B_EfadPathDisabled)) ||
                (((!(xVcVmcPmm_B_Efad2WhlPahReq)) || ((X_SVmcPmm__HE667_UnitDelay <=
                cVcVmcPmm_t_IsgPahDiTiOut) && (!(yVcDtcTc_B_IsgPathDisabled)))) &&
                (!(xVcVmcPmm_B_Efad2IceReqRst)) && X_SVmcPmm__HE660_UnitDelay1);

               
               X_SVmcPmm__HE660_UnitDelay1 = xVcVmcPmm_B_Efad2IceReq;

               
               if ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATNeutral) || (sVcDtcAtr_D_GearLevAT ==
                cVc_D_GearLevATPark)) {
                  
                  X_SVmcPmm__HE666_UnitDelay = X_SVmcPmm__HE666_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE666_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_GearLvrNotDRDetn = X_SVmcPmm__HE666_UnitDelay >
                cVcVmcPmm_t_EfadGearLvrPNDetn;

               
               xVcVmcPmm_B_EfadDisengdReq = (((xVcVmcPmm_B_GearLvrNotDRDetn &&
                ((!(yVcScDep_B_DrvrPrsnt)) || (sVcScIn_v_VehSpdLgt >
                cVcVmcPmm_v_EfadGearLvrPNDiseng) || cVcVmcPmm_B_EfadGearLvrPNDisengEna)) ||
                (sVcDtcAtr_D_GearLevAT == 7) || (!(yVcPpmPsm_B_DriveCycleActive))) &&
                ((yVcDtcTc_B_IsgPathDisabled && yVcVmcWtc_B_EfadPathDisabled) ||
                xVcVmcPmm_B_DrvCycTiOut)) || (!(yVcPpmPsm_B_PropulsionAllowed)) ||
                xVcVmcPmm_B_EfadUnavl;

               
               if (cVcVmcPmm_D_EfadPathReq_swi) {
                  
                  X_SVmcPmm__HE639_UnitDelay4 = cVcVmcPmm_D_EfadPathReq_dbi;
               }
               else {
                  
                  if (xVcVmcPmm_B_Efad2IceReq) {
                     
                     X_SVmcPmm__HE639_UnitDelay4 = 1;
                  }
                  else {
                     
                     if (xVcVmcPmm_B_EfadDisengdReq) {
                        
                        X_SVmcPmm__HE639_UnitDelay4 = 5;
                     }
                     else {
                        
                        X_SVmcPmm__HE639_UnitDelay4 = 2;
                     }
                  }
               }

               
               SVmcPmm__HE173_Merge1 = (SVmcPmm__HE829_Switch || X_SVmcPmm__HE6_UnitDelay5) &&
                (X_SVmcPmm__HE639_UnitDelay4 == 1);

               
               if (sVcDseEm_rt_IsgMaxTorqueLoss < cVcVmcPmm_rt_EfadStrtAllow) {
                  
                  X_SVmcPmm__HE710_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE710_UnitDelay = X_SVmcPmm__HE710_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               xVcVmcPmm_B_ElecMotLowAvailTrq = X_SVmcPmm__HE710_UnitDelay <=
                cVcVmcPmm_t_EfadRunReqDelay;

               
               if (xVcVmcPmm_B_ElecMotLowAvailTrq) {
                  
                  X_SVmcPmm__HE6_UnitDelay3 = 1;
               }
               else {
                  
                  X_SVmcPmm__HE6_UnitDelay3 = 0;
               }

               
               if (X_SVmcPmm__HE6_UnitDelay14) {
                  
                  X_SVmcPmm__HE712_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE712_UnitDelay = X_SVmcPmm__HE712_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               if (CVmcPmm__HE1_D_IceStatus == 2) {
                  
                  X_SVmcPmm__HE713_UnitDelay = X_SVmcPmm__HE713_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE713_UnitDelay = 0.F;
               }

               
               SVmcPmm__HE638__gicalOperator14 = (!(SVmcPmm__HE829_Switch)) ||
                (X_SVmcPmm__HE713_UnitDelay > cVcVmcPmm_t_IceRunng12VStrt);

               
               if (SVmcPmm__HE829_Switch && (!(X_SVmcPmm__HE731_Delay))) {
                  
                  X_SVmcPmm__HE736_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE736_UnitDelay = X_SVmcPmm__HE736_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               X_SVmcPmm__HE731_Delay = SVmcPmm__HE829_Switch;

               
               xVcVmcPmm_B_Dly12VStrtVehPwrUp = cVcVmcPmm_B_UseDly12VStrtVehPwrUp &&
                (X_SVmcPmm__HE736_UnitDelay <= cVcVmcPmm_t_FirstStrtDlyOff) &&
                ((!(sVcDeDmm_B_DrMdeFactory)) || (!(cVcVmcPmm_B_EfadUseFactory12VStrt))) &&
                (sVcPpmPsm_D_EngRunReqPsm == 2);

               
               xVcVmcPmm_B_12VStrtAllwd = (!(xVcVmcPmm_B_Dly12VStrtVehPwrUp)) &&
                (!(X_SVmcPmm__HE673_UnitDelay15)) && (sVcDseGb_D_EfadPathAct != 1) &&
                (CVmcPmm__HE1_D_IceStatus != 2) && ((CVmcPmm__HE1_D_IceStatus !=
                cVcVmcPmm_D_IceStsStarting) || (sVcEc_n_Eng <= cVcVmcPmm_n_12VStrtAllwdEngSpdMax))
                && (!(xVcVmcPmm_B_Wait4CluStrt));

               
               xVcVmcPmm_B_12VStrtPsbl = cVcVmcPmm_B_EfadUse12VStrt && ((sVcScIn_v_VehSpdLgtMax <
                cVcVmcPmm_v_Efad12VStartMax) && (sVcScIn_v_VehSpdLgtMax >
                cVcVmcPmm_v_Efad12VStartMin)) && (SVmcPmm__HE828_Switch ||
                cVcVmcPmm_B_Efad12VStrtEnblIngoreDep) && (SVmcPmm__HE848_Switch >=
                cVcVmcPmm_Te_Efad12VStrtEngClntMin) && xVcVmcPmm_B_12VStrtAllwd;

               
               X_SVmcPmm__HE675_UnitDelay1 = xVcVmcPmm_B_12VStrtPsbl;

               
               if (cVcVmcPmm_B_12VStrtTrigNewPos) {
                  
                  SVmcPmm__HE700_Switch = X_SVmcPmm__HE6_UnitDelay14;
               }
               else {
                  
                  SVmcPmm__HE700_Switch = X_SVmcPmm__HE6_UnitDelay14 &&
                   (!(X_SVmcPmm__HE681_UnitDelay1));
               }

               
               X_SVmcPmm__HE681_UnitDelay1 = X_SVmcPmm__HE6_UnitDelay14;

               
               SVmcPmm__HE638__gicalOperator15 = xVcVmcPmm_B_12VStrtPsbl &&
                ((!(X_SVmcPmm__HE703_UnitDelay1)) && (!(X_SVmcPmm__HE6_UnitDelay6))) &&
                SVmcPmm__HE700_Switch;

               
               if (cVcVmcPmm_B_12VStrtTrigNewPos) {
                  
                  SVmcPmm__HE699_Switch = SVmcPmm__HE638__gicalOperator15 &&
                   (!(X_SVmcPmm__HE685_UnitDelay1));
               }
               else {
                  
                  SVmcPmm__HE699_Switch = SVmcPmm__HE638__gicalOperator15;
               }

               
               X_SVmcPmm__HE685_UnitDelay1 = SVmcPmm__HE638__gicalOperator15;

               
               X_SVmcPmm__HE701_UnitDelay1 = SVmcPmm__HE699_Switch || (X_SVmcPmm__HE6_UnitDelay14 &&
                 (!(X_SVmcPmm__HE638_UnitDelay11)) && SVmcPmm__HE829_Switch &&
                (CVmcPmm__HE1_D_IceStatus != 2) && X_SVmcPmm__HE701_UnitDelay1);

               
               if (cVcVmcPmm_B_12VStrtReq_swi) {
                  
                  X_SVmcPmm__HE638_UnitDelay3 = cVcVmcPmm_B_12VStrtReq_dbi;
               }
               else {
                  
                  X_SVmcPmm__HE638_UnitDelay3 = X_SVmcPmm__HE701_UnitDelay1;
               }

               
               X_SVmcPmm__HE638_UnitDelay7 = X_SVmcPmm__HE638_UnitDelay3;

               
               if (SVmcPmm__HE638__gicalOperator14) {
                  
                  rVcVmcPmm_D_12VStrtCnt = 0;
               }
               else {
                  
                  rVcVmcPmm_D_12VStrtCnt = (UInt8) (X_SVmcPmm__HE638_UnitDelay12 + ((UInt8)
                   (X_SVmcPmm__HE638_UnitDelay3 && (!(X_SVmcPmm__HE683_UnitDelay1)))));
               }

               
               X_SVmcPmm__HE683_UnitDelay1 = X_SVmcPmm__HE638_UnitDelay3;

               
               X_SVmcPmm__HE638_UnitDelay12 = rVcVmcPmm_D_12VStrtCnt;

               
               SVmcPmm__HE638__ionalOperator22 = rVcVmcPmm_D_12VStrtCnt <
                cVcVmcPmm_D_Efad12VStrtMax;

               
               xVcVmcPmm_B_12VStrtActrRdy = (X_SVmcPmm__HE712_UnitDelay >
                cVcVmcPmm_t_12VStrtActrRdyDly) && xVcVmcPmm_B_12VStrtPsbl &&
                SVmcPmm__HE638__ionalOperator22;

               
               if (X_SVmcPmm__HE6_UnitDelay14) {
                  
                  X_SVmcPmm__HE711_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE711_UnitDelay = X_SVmcPmm__HE711_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               if (CVmcPmm__HE1_D_IceStatus == 2) {
                  
                  X_SVmcPmm__HE708_UnitDelay = X_SVmcPmm__HE708_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE708_UnitDelay = 0.F;
               }

               
               SVmcPmm__HE638_LogicalOperator2 = (!(SVmcPmm__HE829_Switch)) ||
                (X_SVmcPmm__HE708_UnitDelay > cVcVmcPmm_t_IceRunngIsgStrt);

               
               if (SVmcPmm__HE638_LogicalOperator2) {
                  
                  rVcVmcPmm_D_IsgStrtCnt = 0;
               }
               else {
                  
                  rVcVmcPmm_D_IsgStrtCnt = (UInt8) (X_SVmcPmm__HE638_UnitDelay6 + ((UInt8)
                   (X_SVmcPmm__HE6_UnitDelay6 && (!(X_SVmcPmm__HE684_UnitDelay1)))));
               }

               
               X_SVmcPmm__HE684_UnitDelay1 = X_SVmcPmm__HE6_UnitDelay6;

               
               X_SVmcPmm__HE638_UnitDelay6 = rVcVmcPmm_D_IsgStrtCnt;

               
               SVmcPmm__HE638__tionalOperator6 = rVcVmcPmm_D_IsgStrtCnt <
                cVcVmcPmm_D_EfadIsgStrtMax;

               
               xVcVmcPmm_B_IsgStrtActrRdy = (X_SVmcPmm__HE711_UnitDelay >
                cVcVmcPmm_t_IsgStrtActrRdyDly) && xVcVmcPmm_B_IsgStrtPsbl &&
                SVmcPmm__HE638__tionalOperator6;

               
               if (X_SVmcPmm__HE638_UnitDelay2) {
                  
                  X_SVmcPmm__HE709_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE709_UnitDelay = X_SVmcPmm__HE709_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               X_SVmcPmm__HE638_UnitDelay2 = X_SVmcPmm__HE6_UnitDelay14;

               
               if (CVmcPmm__HE1_D_IceStatus == 2) {
                  
                  X_SVmcPmm__HE714_UnitDelay = X_SVmcPmm__HE714_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE714_UnitDelay = 0.F;
               }

               
               SVmcPmm__HE638__gicalOperator17 = (!(SVmcPmm__HE829_Switch)) ||
                (X_SVmcPmm__HE714_UnitDelay > cVcVmcPmm_t_IceRunngCluStrt);

               
               if (SVmcPmm__HE638__gicalOperator17) {
                  
                  rVcVmcPmm_D_CluStrtCnt = 0;
               }
               else {
                  
                  rVcVmcPmm_D_CluStrtCnt = (UInt8) (X_SVmcPmm__HE638_UnitDelay5 + ((UInt8)
                   (X_SVmcPmm__HE703_UnitDelay1 && (!(X_SVmcPmm__HE682_UnitDelay1)))));
               }

               
               X_SVmcPmm__HE682_UnitDelay1 = X_SVmcPmm__HE703_UnitDelay1;

               
               X_SVmcPmm__HE638_UnitDelay5 = rVcVmcPmm_D_CluStrtCnt;

               
               SVmcPmm__HE638__ionalOperator13 = rVcVmcPmm_D_CluStrtCnt <
                cVcVmcPmm_D_EfadCluStrtMax;

               
               xVcVmcPmm_B_CluStrtActrRdy = (X_SVmcPmm__HE709_UnitDelay >
                cVcVmcPmm_t_CluStrtActrRdyDly) && xVcVmcPmm_B_CluStrtPsbl &&
                SVmcPmm__HE638__ionalOperator13;

               
               xVcVmcPmm_B_StrtActrsRdy = (!(SVmcPmm__HE829_Switch)) || xVcVmcPmm_B_12VStrtActrRdy
                || xVcVmcPmm_B_IsgStrtActrRdy || xVcVmcPmm_B_CluStrtActrRdy;

               
               if (cVcVmcPmm_B_IsgPathEnable_swi) {
                  
                  X_SVmcPmm__HE6_UnitDelay13 = cVcVmcPmm_B_IsgPathEnable_dbi;
               }
               else {
                  
                  X_SVmcPmm__HE6_UnitDelay13 = xVcVmcPmm_B_Efad2IcePahReq &&
                   ((!(yVcGscAsr_B_EfadNoTqReq)) && (!(yVcDsePcr_B_IsgNoTqRq))) &&
                   (yVcScIn_B_PropulsionAllowed || cVcVmcPmm_B_IgnrPropAlwdIsg) &&
                   (X_SVmcPmm__HE639_UnitDelay4 == 1) && (sVcDseGb_D_EfadPathAct == 1) &&
                   (sVcCidd_D_IsgModSts == 2);
               }

               
               X_SVmcPmm__HE743_UnitDelay7 = X_SVmcPmm__HE6_UnitDelay13;

               
               X_SVmcPmm__HE675_UnitDelay2 = X_SVmcPmm__HE6_UnitDelay13;

               
               SVmcPmm__HE637__gicalOperator50 = (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive) ||
                (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATReverse);

               
               if (SVmcPmm__HE637__gicalOperator50) {
                  
                  X_SVmcPmm__HE662_UnitDelay = X_SVmcPmm__HE662_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE662_UnitDelay = 0.F;
               }

               
               SVmcPmm__HE637__gicalOperator40 = (yVcVmcWtc_B_EfadPathDisabled ||
                (X_SVmcPmm__HE662_UnitDelay > cVcVmcPmm_t_EfadPahDiTiOut)) &&
                SVmcPmm__HE637__gicalOperator50;

               
               xVcVmcPmm_B_GarageShiftEfadPahDiOK = (SVmcPmm__HE637__gicalOperator40 &&
                (!(X_SVmcPmm__HE644_Delay))) || (SVmcPmm__HE637__gicalOperator50 &&
                X_SVmcPmm__HE658_UnitDelay1);

               
               X_SVmcPmm__HE658_UnitDelay1 = xVcVmcPmm_B_GarageShiftEfadPahDiOK;

               
               X_SVmcPmm__HE644_Delay = SVmcPmm__HE637__gicalOperator40;

               
               SVmcPmm__HE637_LogicalOperator7 = xVcVmcPmm_B_Efad2WhlPahReq &&
                ((!(yVcDsePcr_B_EfadNoTqRq)) && (!(yVcGscAsr_B_EfadNoTqReq))) &&
                (yVcScIn_B_PropulsionAllowed || cVcVmcPmm_B_IgnrPropAlwdEfad) &&
                (X_SVmcPmm__HE639_UnitDelay4 == 2) && (sVcDseGb_D_EfadPathAct == 2) &&
                (sVcCidd_D_IsgModSts == 2) && (yVcDseGbGear_B_ParkLockNotEngd ||
                cVcVmcPmm_B_EfadPathEnaParkEngd) && xVcVmcPmm_B_GarageShiftEfadPahDiOK;

               
               if (yVcGscGar_B_EfadShiftInProgress) {
                  
                  X_SVmcPmm__HE668_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE668_UnitDelay = X_SVmcPmm__HE668_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               if (yVcGscGar_B_EfadShiftInProgress) {
                  
                  X_SVmcPmm__HE665_UnitDelay = X_SVmcPmm__HE665_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE665_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_EvenGearShiftAct = ((!(SVmcPmm__HE637_LogicalOperator7)) &&
                X_SVmcPmm__HE643_Delay && xVcVmcPmm_B_GarageShiftEfadPahDiOK &&
                yVcGscGar_B_EfadShiftInProgress) || ((X_SVmcPmm__HE668_UnitDelay <=
                cVcVmcPmm_t_EfadShftProgsOffDly) && (X_SVmcPmm__HE665_UnitDelay <=
                cVcVmcPmm_t_EfadShftProgsTimeOut) && xVcVmcPmm_B_Efad2WhlPahReq &&
                (X_SVmcPmm__HE639_UnitDelay4 == 2) && (!(yVcDsePcr_B_EfadNoTqRq)) &&
                (!(xVcVmcPmm_B_DrvCycTiOut)) && X_SVmcPmm__HE657_UnitDelay1);

               
               X_SVmcPmm__HE657_UnitDelay1 = xVcVmcPmm_B_EvenGearShiftAct;

               
               X_SVmcPmm__HE643_Delay = SVmcPmm__HE637_LogicalOperator7;

               
               if (cVcVmcPmm_B_EfadPathEnable_swi) {
                  
                  X_SVmcPmm__HE6_UnitDelay4 = cVcVmcPmm_B_EfadPathEnable_dbi;
               }
               else {
                  
                  X_SVmcPmm__HE6_UnitDelay4 = SVmcPmm__HE637_LogicalOperator7 ||
                   xVcVmcPmm_B_EvenGearShiftAct;
               }

               
               yVcVmcPmm_B_EfadActReq = (X_SVmcPmm__HE639_UnitDelay4 == 2) &&
                yVcPpmPsm_B_DriveCycleActive;

               
               if (!(yVcDepTre_B_ISGTqAllw)) {
                  
                  X_SVmcPmm__HE669_UnitDelay = X_SVmcPmm__HE669_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE669_UnitDelay = 0.F;
               }

               
               X_SVmcPmm__HE659_UnitDelay1 = SVmcPmm__HE173_Merge1 || yVcVmcPmm_B_EfadActReq ||
                ((!(xVcVmcPmm_B_DrvCycTiOut)) && (X_SVmcPmm__HE669_UnitDelay <=
                cVcVmcPmm_t_EfadTrqAllowTiOut) && (sVcDseGb_D_EfadPathAct != 5) &&
                X_SVmcPmm__HE659_UnitDelay1);

               
               if (cVcVmcPmm_D_EfadModReq_swi) {
                  
                  rVcVmcPmm_D_EfadModReq = cVcVmcPmm_D_EfadModReq_dbi;
               }
               else {
                  
                  if (yVcDsePcr_B_IsgUdcCtrlRq && (sVcDseGb_D_EfadPathAct == 1)) {
                     
                     rVcVmcPmm_D_EfadModReq = 4;
                  }
                  else {
                     
                     
                     #ifdef SVmcPmm__HE1_VcVmcPmm_AUX
                        Bool SVmcPmm__HE637__gicalOperator35;
                     #endif

                     

                     
                     SVmcPmm__HE637__gicalOperator35 = (sVcDseGb_D_EfadPathAct ==
                      cVcVmcPmm_D_EfadPathAllwd1) || (sVcDseGb_D_EfadPathAct ==
                      cVcVmcPmm_D_EfadPathAllwd2);

                     
                     if ((sVcDtcCtc_D_EfadModeReq == 5) && SVmcPmm__HE637__gicalOperator35) {
                        
                        rVcVmcPmm_D_EfadModReq = 5;
                     }
                     else {
                        
                        if ((sVcDtcCtc_D_EfadModeReq == 3) && SVmcPmm__HE637__gicalOperator35) {
                           
                           rVcVmcPmm_D_EfadModReq = 3;
                        }
                        else {
                           
                           if (yVcGscAsr_B_EfadNoTqReq || X_SVmcPmm__HE659_UnitDelay1) {
                              
                              rVcVmcPmm_D_EfadModReq = 2;
                           }
                           else {
                              
                              rVcVmcPmm_D_EfadModReq = 1;
                           }
                        }
                     }
                  }
               }

               
               SVmcPmm__HE173_Merge = rVcVmcPmm_D_EfadModReq;

               
               if (cVcVmcPmm_B_IsgStrtReq_swi) {
                  
                  X_SVmcPmm__HE6_UnitDelay10 = cVcVmcPmm_B_IsgStrtReq_dbi;
               }
               else {
                  
                  X_SVmcPmm__HE6_UnitDelay10 = X_SVmcPmm__HE6_UnitDelay6 &&
                   X_SVmcPmm__HE6_UnitDelay13;
               }

               
               X_SVmcPmm__HE638_UnitDelay8 = X_SVmcPmm__HE6_UnitDelay10;

               
               xVcVmcPmm_B_12VStrtReq = X_SVmcPmm__HE638_UnitDelay3;

               
               SVmcPmm__HE173_Merge3 = xVcVmcPmm_B_12VStrtReq;

               
               yVcVmcPmm_B_ClutchStartReq = X_SVmcPmm__HE703_UnitDelay1;

               
               sVcVmcPmm_D_EfadPathReq = X_SVmcPmm__HE639_UnitDelay4;

               
               if (sVcDseEm_rt_IsgMaxTorqueLossStart < cVcVmcPmm_rt_EfadLowAvailTrq) {
                  
                  X_SVmcPmm__HE740_UnitDelay = X_SVmcPmm__HE740_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE740_UnitDelay = 0.F;
               }

               
               xVcVmcPmm_B_IsgStrtLowAvailTrq = X_SVmcPmm__HE740_UnitDelay >
                cVcVmcPmm_t_EfadLowAvailTrqDly;

               
               SVmcPmm__HE638__gicalOperator40 = X_SVmcPmm__HE6_UnitDelay14 ||
                X_SVmcPmm__HE638_UnitDelay3;

               
               X_SVmcPmm__HE704_UnitDelay1 = ((!(SVmcPmm__HE638__gicalOperator40)) &&
                X_SVmcPmm__HE680_Delay && (!(SVmcPmm__HE638__ionalOperator22)) &&
                (rVcVmcPmm_D_12VStrtCnt > 0)) || ((!(SVmcPmm__HE638__gicalOperator14)) &&
                X_SVmcPmm__HE704_UnitDelay1);

               
               X_SVmcPmm__HE680_Delay = SVmcPmm__HE638__gicalOperator40;

               
               if (cVcVmcPmm_B_12VStrtBlk_swi) {
                  
                  xVcVmcPmm_B_12VStrtBlk = cVcVmcPmm_B_12VStrtBlk_dbi;
               }
               else {
                  
                  xVcVmcPmm_B_12VStrtBlk = X_SVmcPmm__HE704_UnitDelay1;
               }

               
               X_SVmcPmm__HE638_UnitDelay11 = xVcVmcPmm_B_12VStrtBlk;

               
               X_SVmcPmm__HE673_UnitDelay15 = xVcVmcPmm_B_12VStrtBlk;

               
               X_SVmcPmm__HE672_UnitDelay2 = xVcVmcPmm_B_12VStrtBlk;

               
               SVmcPmm__HE638__gicalOperator41 = X_SVmcPmm__HE6_UnitDelay14 ||
                X_SVmcPmm__HE6_UnitDelay10;

               
               X_SVmcPmm__HE706_UnitDelay1 = ((!(SVmcPmm__HE638__gicalOperator41)) &&
                X_SVmcPmm__HE677_Delay && (!(SVmcPmm__HE638__tionalOperator6)) &&
                (rVcVmcPmm_D_IsgStrtCnt > 0)) || ((!(SVmcPmm__HE638_LogicalOperator2)) &&
                X_SVmcPmm__HE706_UnitDelay1);

               
               X_SVmcPmm__HE677_Delay = SVmcPmm__HE638__gicalOperator41;

               
               if (cVcVmcPmm_B_IsgStrtBlk_swi) {
                  
                  xVcVmcPmm_B_IsgStrtBlk = cVcVmcPmm_B_IsgStrtBlk_dbi;
               }
               else {
                  
                  xVcVmcPmm_B_IsgStrtBlk = X_SVmcPmm__HE706_UnitDelay1;
               }

               
               X_SVmcPmm__HE638_UnitDelay9 = xVcVmcPmm_B_IsgStrtBlk;

               
               X_SVmcPmm__HE674_UnitDelay7 = xVcVmcPmm_B_IsgStrtBlk;

               
               SVmcPmm__HE638__gicalOperator42 = X_SVmcPmm__HE6_UnitDelay14 ||
                X_SVmcPmm__HE703_UnitDelay1;

               
               X_SVmcPmm__HE705_UnitDelay1 = ((!(SVmcPmm__HE638__gicalOperator42)) &&
                X_SVmcPmm__HE676_Delay && (!(SVmcPmm__HE638__ionalOperator13)) &&
                (rVcVmcPmm_D_CluStrtCnt > 0)) || ((!(SVmcPmm__HE638__gicalOperator17)) &&
                X_SVmcPmm__HE705_UnitDelay1);

               
               X_SVmcPmm__HE676_Delay = SVmcPmm__HE638__gicalOperator42;

               
               if (cVcVmcPmm_B_CluStrtBlk_swi) {
                  
                  xVcVmcPmm_B_CluStrtBlk = cVcVmcPmm_B_CluStrtBlk_dbi;
               }
               else {
                  
                  xVcVmcPmm_B_CluStrtBlk = X_SVmcPmm__HE705_UnitDelay1;
               }

               
               X_SVmcPmm__HE638_UnitDelay4 = xVcVmcPmm_B_CluStrtBlk;

               
               X_SVmcPmm__HE675_UnitDelay10 = xVcVmcPmm_B_CluStrtBlk;

               
               xVcVmcPmm_B_IsgStrtLimLoosen = ((!(X_SVmcPmm__HE6_UnitDelay14)) &&
                X_SVmcPmm__HE717_Delay && (rVcVmcPmm_D_IsgStrtCnt >=
                cVcVmcPmm_D_EfadIsgStrLoosenLim)) || (SVmcPmm__HE672_LogicalOperator7 &&
                xVcVmcPmm_B_CluStrtBlk) || (SVmcPmm__HE829_Switch && (CVmcPmm__HE1_D_IceStatus != 2)
                 && X_SVmcPmm__HE724_UnitDelay1);

               
               X_SVmcPmm__HE724_UnitDelay1 = xVcVmcPmm_B_IsgStrtLimLoosen;

               
               X_SVmcPmm__HE717_Delay = X_SVmcPmm__HE6_UnitDelay14;

               
               X_SVmcPmm__HE672_UnitDelay1 = xVcVmcPmm_B_IsgStrtLimLoosen;
            }
         #endif
         #if Vc_Pvc_Hw_B_Erad
            
            if (cVcVmcPmm_B_UseEradCode) {
               
               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  Float32 SVmcPmm__HE615_Switch1;
               #endif

               

               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  Float32 SVmcPmm__HE622_Switch;
               #endif

               

               
               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  Bool SVmcPmm__HE614__gicalOperator11;
               #endif

               

               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  Bool SVmcPmm__HE614__tionalOperator9;
               #endif

               

               
               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  static Float32 X_SVmcPmm__HE624_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  static Float32 X_SVmcPmm__HE625_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  static Float32 X_SVmcPmm__HE626_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  static Float32 X_SVmcPmm__HE630_UnitDelay = 0.F;
               #endif

               

               
               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  static Bool X_SVmcPmm__HE618_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  static Bool X_SVmcPmm__HE627_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  static Bool X_SVmcPmm__HE628_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE614__lOperator11_AUX
                  static Bool X_SVmcPmm__HE629_UnitDelay1 = 0;
               #endif

               

               
               if ((!(yVcVmcPmm_B_EngOnReqEng)) || yVcDeDmm_B_EradEngageRqDr ||
                yVcVmcEm_B_EradEngageRqEm || yVcDsePcr_B_EradEngageRq || yVcVmcAwd_B_EngageReq) {
                  
                  X_SVmcPmm__HE630_UnitDelay = X_SVmcPmm__HE630_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE630_UnitDelay = 0.F;
               }

               
               if (X_SVmcPmm__HE630_UnitDelay > cVcVmcPmm_t_EradOnGlitch) {
                  
                  X_SVmcPmm__HE624_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE624_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE624_UnitDelay;
               }

               
               if (cVcVmcPmm_B_EradRmpDwnTqSignal) {
                  
                  SVmcPmm__HE622_Switch = sVcMtcTc_Tq_EradReqWhl;
               }
               else {
                  
                  SVmcPmm__HE622_Switch = sVcDseWt_Tq_PropRear;
               }

               
               if (SVmcPmm__HE622_Switch >= 0.F) {
                  
                  SVmcPmm__HE615_Switch1 = SVmcPmm__HE622_Switch;
               }
               else {
                  
                  SVmcPmm__HE615_Switch1 = SVmcPmm__HE622_Switch * -1.F;
               }

               
               SVmcPmm__HE614__tionalOperator9 = SVmcPmm__HE615_Switch1 < cVcVmcPmm_Tq_ERADRampDown;

               
               X_SVmcPmm__HE628_UnitDelay1 = (X_SVmcPmm__HE624_UnitDelay <=
                cVcVmcPmm_t_EradOffGlitch) || (((!(yVcVmcPmm_B_CrShPathEnable)) ||
                (!(SVmcPmm__HE614__tionalOperator9))) && X_SVmcPmm__HE628_UnitDelay1);

               
               SVmcPmm__HE614__gicalOperator11 = yVcScIn_B_DrvgDirRvsDes || yVcScIn_B_DrvgDirFwdDes;

               
               X_SVmcPmm__HE629_UnitDelay1 = (sVcScIn_v_VehSpdLgtMax <= cVcVmcPmm_v_EradOnSpdLim) ||
                 ((sVcScIn_v_VehSpdLgtMax < cVcVmcPmm_v_EradOffSpdLim) &&
                X_SVmcPmm__HE629_UnitDelay1);

               
               yVcVmcPmm_B_EradDrReq = X_SVmcPmm__HE628_UnitDelay1 &&
                SVmcPmm__HE614__gicalOperator11 && X_SVmcPmm__HE629_UnitDelay1;

               
               xVcVmcPmm_B_EradAllow = SVmcPmm__HE829_Switch && (!(yVcDsePcr_B_EradDisableRq)) &&
                yVcPpmPsm_B_PropulsionAllowed && (yVcDepTre_B_ERADTqAllw || cVcVmcPmm_B_ERADTqAllw);

               
               xVcVmcPmm_B_EradEngageReq = yVcVmcPmm_B_EradDrReq && xVcVmcPmm_B_EradAllow;

               
               if (cVcVmcPmm_B_EradPathEnable_swi) {
                  
                  X_SVmcPmm__HE6_UnitDelay8 = cVcVmcPmm_B_EradPathEnable_dbi;
               }
               else {
                  
                  X_SVmcPmm__HE6_UnitDelay8 = xVcVmcPmm_B_EradEngageReq &&
                   (!(yVcDsePcr_B_EradNoTqRq)) && (sVcIem_D_WhlMotSysModSts == 2) &&
                   yVcIem_B_WhlMotSysCluSts;
               }

               
               if (cVcVmcPmm_D_WhlMotSysCluOperTypReq_swi) {
                  
                  sVcVmcPmm_D_WhlMotSysCluOperTypReq = cVcVmcPmm_D_WhlMotSysCluOperTypReq_dbi;
               }
               else {
                  
                  sVcVmcPmm_D_WhlMotSysCluOperTypReq = sVcDeDmm_D_EradEngageModeReq;
               }

               
               if (!(xVcVmcPmm_B_EradEngageReq)) {
                  
                  X_SVmcPmm__HE626_UnitDelay = X_SVmcPmm__HE626_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE626_UnitDelay = 0.F;
               }

               
               if ((!(SVmcPmm__HE614__gicalOperator11)) && X_SVmcPmm__HE618_Delay) {
                  
                  X_SVmcPmm__HE625_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE625_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE625_UnitDelay;
               }

               
               X_SVmcPmm__HE618_Delay = SVmcPmm__HE614__gicalOperator11;

               
               X_SVmcPmm__HE627_UnitDelay1 = xVcVmcPmm_B_EradEngageReq ||
                ((X_SVmcPmm__HE626_UnitDelay <= cVcVmcPmm_t_EradDisable) &&
                ((X_SVmcPmm__HE625_UnitDelay <= cVcVmcPmm_t_EradNtrlGlitch) ||
                (((!(yVcVmcWtd_B_EradPathDisabled)) && (!(cVcVmcPmm_B_EradIgnrPathDisable))) ||
                (!(SVmcPmm__HE614__tionalOperator9)))) && X_SVmcPmm__HE627_UnitDelay1);

               
               xVcVmcPmm_B_EradSpdCtrl = (!(yVcIem_B_WhlMotSysCluSts)) && xVcVmcPmm_B_EradAllow &&
                yVcScIn_B_DrvgDirRvsDes && (sVcScIn_v_VehSpdLgt >= cVcVmcPmm_v_EradSpdCtrl);

               
               if (X_SVmcPmm__HE627_UnitDelay1) {
                  
                  sVcVmcPmm_D_WhlMotSysModReq = 2;
               }
               else {
                  
                  if (xVcVmcPmm_B_EradSpdCtrl) {
                     
                     sVcVmcPmm_D_WhlMotSysModReq = 3;
                  }
                  else {
                     
                     sVcVmcPmm_D_WhlMotSysModReq = 1;
                  }
               }

               
               yVcVmcPmm_B_EradClutchReq = X_SVmcPmm__HE627_UnitDelay1;
            }
         #endif
         #if VcVmcPmm__HEP7_1243_Isg_8
            
            if (cVcVmcPmm_B_UseIsgCode) {
               
               
               #ifdef SVmcPmm__HE784__lOperator19_AUX
                  Float32 SVmcPmm__HE787_Switch1;
               #endif

               

               
               #ifdef SVmcPmm__HE784__lOperator19_AUX
                  Float32 SVmcPmm__HE791_Switch;
               #endif

               

               
               #ifdef SVmcPmm__HE808__calOperator_AUX
                  Float32 SVmcPmm__HE810_Switch;
               #endif

               

               
               
               #ifdef SVmcPmm__HE784__lOperator19_AUX
                  Bool SVmcPmm__HE784__gicalOperator19;
               #endif

               

               
               #ifdef SVmcPmm__HE808__calOperator_AUX
                  Bool SVmcPmm__HE808_LogicalOperator;
               #endif

               

               
               #ifdef SVmcPmm__HE818_Switch_AUX
                  Bool SVmcPmm__HE818_Switch;
               #endif

               

               
               
               #ifdef SVmcPmm__HE784_Merge_AUX
                  static UInt8 SVmcPmm__HE784_Merge = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE784_Merge5_AUX
                  static UInt8 SVmcPmm__HE784_Merge5 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE808__calOperator_AUX
                  static UInt8 SVmcPmm__HE817___IsgStrtAllow_x[2] = 
                  {
                      0, 0
                     
                  }; 
               #endif

               

               
               
               #ifdef SVmcPmm__HE784__lOperator19_AUX
                  static Float32 X_SVmcPmm__HE795_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE784__lOperator19_AUX
                  static Float32 X_SVmcPmm__HE804_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE784__lOperator19_AUX
                  static Float32 X_SVmcPmm__HE805_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE784__lOperator19_AUX
                  static Float32 X_SVmcPmm__HE806_UnitDelay = 0.F;
               #endif

               

               
               #ifdef SVmcPmm__HE808__calOperator_AUX
                  static Float32 X_SVmcPmm__HE814_UnitDelay = 1e+30F;
               #endif

               

               
               #ifdef SVmcPmm__HE808__calOperator_AUX
                  static Float32 X_SVmcPmm__HE815_UnitDelay = 1e+30F;
               #endif

               

               
               
               #ifdef SVmcPmm__HE808__calOperator_AUX
                  static Bool X_SVmcPmm__HE785_InitValue1 = 1;
               #endif

               

               
               #ifdef SVmcPmm__HE784__lOperator19_AUX
                  static Bool X_SVmcPmm__HE788_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE784__lOperator19_AUX
                  static Bool X_SVmcPmm__HE802_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE784_Merge5_AUX
                  static Bool X_SVmcPmm__HE803_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE808__calOperator_AUX
                  static Bool X_SVmcPmm__HE807_Delay = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE808__calOperator_AUX
                  static Bool X_SVmcPmm__HE808_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE808__calOperator_AUX
                  static Bool X_SVmcPmm__HE809_UnitDelay1 = 0;
               #endif

               

               
               #ifdef SVmcPmm__HE808__calOperator_AUX
                  static Bool X_SVmcPmm__HE816_UnitDelay1 = 0;
               #endif

               

               
               if (sVcDseEm_rt_IsgMaxTorqueLoss < cVcVmcPmm_rt_IsgStrtAllow) {
                  
                  X_SVmcPmm__HE804_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE804_UnitDelay = X_SVmcPmm__HE804_UnitDelay + ts_VcVmcPmm__HEP7;
               }

               
               if (X_SVmcPmm__HE804_UnitDelay <= cVcVmcPmm_t_IsgRunReqDelay) {
                  
                  X_SVmcPmm__HE6_UnitDelay3 = 1;
               }
               else {
                  
                  X_SVmcPmm__HE6_UnitDelay3 = 0;
               }

               
               if (CVmcPmm__HE1_D_IceStatus == 0) {
                  
                  X_SVmcPmm__HE806_UnitDelay = X_SVmcPmm__HE806_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE806_UnitDelay = 0.F;
               }

               
               SVmcPmm__HE784__gicalOperator19 = (!(X_SVmcPmm__HE6_UnitDelay14)) &&
                (X_SVmcPmm__HE806_UnitDelay > cVcVmcPmm_t_IsgICEStop);

               
               if (SVmcPmm__HE784__gicalOperator19 && (!(X_SVmcPmm__HE788_UnitDelay1))) {
                  
                  X_SVmcPmm__HE795_UnitDelay = 0.F;
               }
               else {
                  
                  X_SVmcPmm__HE795_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE795_UnitDelay;
               }

               
               X_SVmcPmm__HE788_UnitDelay1 = SVmcPmm__HE784__gicalOperator19;

               
               SVmcPmm__HE173_Merge1 = ((X_SVmcPmm__HE795_UnitDelay > cVcVmcPmm_t_IsgAdapt) ||
                cVcVmcPmm_B_SkipIsgCalibration) && SVmcPmm__HE829_Switch;

               
               xVcVmcPmm_B_IsgEnable = SVmcPmm__HE173_Merge1 && (yVcDepTre_B_ISGTqAllw ||
                cVcVmcPmm_B_ISGTqAllw) && (!(yVcDsePcr_B_IsgDisableRq));

               
               if (cVcVmcPmm_B_IsgPathEnable_swi) {
                  
                  X_SVmcPmm__HE6_UnitDelay13 = cVcVmcPmm_B_IsgPathEnable_dbi;
               }
               else {
                  
                  X_SVmcPmm__HE6_UnitDelay13 = xVcVmcPmm_B_IsgEnable && (!(yVcDsePcr_B_IsgNoTqRq))
                   && (sVcCidd_D_IsgModSts == 2);
               }

               
               X_SVmcPmm__HE803_UnitDelay1 = (cVcVmcPmm_B_UseIsgSpdCtrlStrt &&
                X_SVmcPmm__HE6_UnitDelay14 && (X_SVmcPmm__HE6_UnitDelay == 2)) ||
                ((CVmcPmm__HE1_D_IceStatus != 2) && X_SVmcPmm__HE803_UnitDelay1);

               
               if (!(xVcVmcPmm_B_IsgEnable)) {
                  
                  X_SVmcPmm__HE805_UnitDelay = X_SVmcPmm__HE805_UnitDelay + ts_VcVmcPmm__HEP7;
               }
               else {
                  
                  X_SVmcPmm__HE805_UnitDelay = 0.F;
               }

               
               if (cVcVmcPmm_B_IsgRmpDwnTqSignal) {
                  
                  SVmcPmm__HE791_Switch = sVcDtcTc_Tq_IsgReqCrSh;
               }
               else {
                  
                  SVmcPmm__HE791_Switch = sVcDseCt_Tq_IsgCrSh;
               }

               
               if (SVmcPmm__HE791_Switch >= 0.F) {
                  
                  SVmcPmm__HE787_Switch1 = SVmcPmm__HE791_Switch;
               }
               else {
                  
                  SVmcPmm__HE787_Switch1 = SVmcPmm__HE791_Switch * -1.F;
               }

               
               xVcVmcPmm_B_IsgActrTqRampDwn = SVmcPmm__HE787_Switch1 < cVcVmcPmm_Tq_IsgRampDown;

               
               X_SVmcPmm__HE802_UnitDelay1 = xVcVmcPmm_B_IsgEnable || ((X_SVmcPmm__HE805_UnitDelay
                <= cVcVmcPmm_t_IsgDisable) && (((!(yVcDtcTc_B_IsgPathDisabled)) &&
                (!(cVcVmcPmm_B_IsgIgnrPathDisable))) || (!(xVcVmcPmm_B_IsgActrTqRampDwn))) &&
                X_SVmcPmm__HE802_UnitDelay1);

               
               if (X_SVmcPmm__HE802_UnitDelay1) {
                  
                  if (yVcDsePcr_B_IsgUdcCtrlRq) {
                     
                     SVmcPmm__HE173_Merge = 4;
                  }
                  else {
                     
                     if (X_SVmcPmm__HE803_UnitDelay1) {
                        
                        SVmcPmm__HE173_Merge = 3;
                     }
                     else {
                        
                        SVmcPmm__HE173_Merge = 2;
                     }
                  }
               }
               else {
                  
                  SVmcPmm__HE173_Merge = 1;
               }
               #if Vc_Pvc_Hw_B_12VStartMotor == 0
                  
                  if (cVcVmcPmm_B_IsgStrtUseSpdCtrl) {
                     
                     SVmcPmm__HE818_Switch = !(X_SVmcPmm__HE803_UnitDelay1);
                  }
                  else {
                     
                     SVmcPmm__HE818_Switch = 1;
                  }

                  
                  SVmcPmm__HE784_Merge5 = (UInt8) (X_SVmcPmm__HE6_UnitDelay14 &&
                   X_SVmcPmm__HE6_UnitDelay13 && (!(yVcDsePcr_B_IsgStartDisableRq)) &&
                   SVmcPmm__HE818_Switch);

                  
                  SVmcPmm__HE784_Merge = (UInt8) 0;
               #endif
               #if Vc_Pvc_Hw_B_12VStartMotor
                  
                  if (cVcVmcPmm_B_UseOilTemp) {
                     
                     SVmcPmm__HE810_Switch = sVcTmTeOil_Te_EngOil;
                  }
                  else {
                     
                     SVmcPmm__HE810_Switch = SVmcPmm__HE848_Switch;
                  }

                  
                  X_SVmcPmm__HE816_UnitDelay1 = (SVmcPmm__HE829_Switch &&
                   (!(X_SVmcPmm__HE809_UnitDelay1))) || ((SVmcPmm__HE829_Switch ||
                   (!(X_SVmcPmm__HE807_Delay))) && (CVmcPmm__HE1_D_IceStatus != 2) &&
                   X_SVmcPmm__HE816_UnitDelay1);

                  
                  X_SVmcPmm__HE807_Delay = SVmcPmm__HE829_Switch;

                  
                  X_SVmcPmm__HE809_UnitDelay1 = SVmcPmm__HE829_Switch;

                  
                  TabIdxS18T6((const Float32 *) &(tVcVmcPmm_Tq_IsgStrtAllow_x[0]), 6, sVcEc_n_Eng,
                   SVmcPmm__HE817___IsgStrtAllow_x);

                  
                  rVcVmcPmm_Tq_EradMaxLimNoLim = Tab1DIntpI1T6((const Float32 *)
                   &(tVcVmcPmm_Tq_IsgStrtAllow[0]), &(SVmcPmm__HE817___IsgStrtAllow_x[0]));

                  
                  if ((sVcDseEm_Tq_IsgMaxAvail >= rVcVmcPmm_Tq_EradMaxLimNoLim) &&
                   (sVcDseEm_Pw_IsgMaxAllowPrio >= cVcVmcPmm_Pw_IsgStrtAllow) &&
                   (sVcDseEm_rt_IsgMaxTorqueLoss >= cVcVmcPmm_rt_IsgStrtAllow)) {
                     
                     X_SVmcPmm__HE815_UnitDelay = 0.F;
                  }
                  else {
                     
                     X_SVmcPmm__HE815_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE815_UnitDelay;
                  }

                  
                  xVcVmcPmm_B_IsgStrtOk = X_SVmcPmm__HE6_UnitDelay13 && ((SVmcPmm__HE810_Switch >=
                   cVcVmcPmm_Te_IsgStartPossible) || cVcVmcPmm_B_IsgStrtTempOverride) &&
                   ((!(yVcDsePcr_B_IsgStartDisableRq)) || cVcVmcPmm_B_IsgStrtPcrOverride) &&
                   ((!(yVcFsdPc_B_RunDry)) || cVcVmcPmm_B_IsgStrtRunDryOverride) &&
                   ((!(X_SVmcPmm__HE816_UnitDelay1)) || cVcVmcPmm_B_IsgStrtFirstStartOverride) &&
                   (X_SVmcPmm__HE815_UnitDelay <= cVcVmcPmm_t_IsgRunReqDelay) &&
                   ((!(X_SVmcPmm__HE803_UnitDelay1)) || cVcVmcPmm_B_IsgStrtSpdCtrlOverride);

                  
                  SVmcPmm__HE808_LogicalOperator = X_SVmcPmm__HE6_UnitDelay14 &&
                   (!(X_SVmcPmm__HE808_UnitDelay1));

                  
                  X_SVmcPmm__HE808_UnitDelay1 = X_SVmcPmm__HE6_UnitDelay14;

                  
                  if (SVmcPmm__HE808_LogicalOperator) {
                     
                     X_SVmcPmm__HE814_UnitDelay = 0.F;
                  }
                  else {
                     
                     X_SVmcPmm__HE814_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE814_UnitDelay;
                  }

                  
                  if (SVmcPmm__HE808_LogicalOperator || ((X_SVmcPmm__HE814_UnitDelay <=
                   cVcVmcPmm_t_IsgStrtOkDelay) && (!(X_SVmcPmm__HE785_InitValue1)))) {
                     
                     X_SVmcPmm__HE785_InitValue1 = xVcVmcPmm_B_IsgStrtOk;
                  }

                  
                  if (cVcVmcPmm_B_IsgStartEnable_swi) {
                     
                     SVmcPmm__HE784_Merge5 = (UInt8) cVcVmcPmm_B_IsgStartEnable_dbi;
                  }
                  else {
                     
                     SVmcPmm__HE784_Merge5 = (UInt8) X_SVmcPmm__HE785_InitValue1;
                  }

                  
                  xVcVmcPmm_B_12VStrtOk = sVcScIn_v_VehSpdLgt <= cVcVmcPmm_v_12VStrtMax;

                  
                  if (cVcVmcPmm_B_12VStartEnable_swi) {
                     
                     SVmcPmm__HE784_Merge = (UInt8) cVcVmcPmm_B_12VStartEnable_dbi;
                  }
                  else {
                     
                     SVmcPmm__HE784_Merge = (UInt8) (xVcVmcPmm_B_12VStrtOk &&
                      (!(xVcVmcPmm_B_IsgStrtOk)) && (!(X_SVmcPmm__HE785_InitValue1)));
                  }
               #endif

               
               X_SVmcPmm__HE6_UnitDelay10 = SVmcPmm__HE784_Merge5 != 0;

               
               SVmcPmm__HE173_Merge3 = SVmcPmm__HE784_Merge != 0;
            }
         #endif
         #if Vc_Pvc_Hw_B_TqConverterGbx
            
            TabIdxS18T390((const Float32 *) &(tVcVmcPmm_Tq_TransHeatReq_x[0]), 6,
             sVcDtcAtr_v_VehDrDirectionRaw, SVmcPmm__HE821___TransHeatReq_x);

            
            SVmcPmm__HE821_Tq_TransHeatReq = Tab1DIntpI1T54((const Float32 *)
             &(tVcVmcPmm_Tq_TransHeatReq[0]), &(SVmcPmm__HE821___TransHeatReq_x[0]));

            
            if (SVmcPmm__HE829_Switch && (sVcDseEm_Tq_EradMaxAvailWhl <=
             SVmcPmm__HE821_Tq_TransHeatReq)) {
               
               X_SVmcPmm__HE819_UnitDelay = X_SVmcPmm__HE819_UnitDelay + ts_VcVmcPmm__HEP7;
            }
            else {
               
               X_SVmcPmm__HE819_UnitDelay = 0.F;
            }

            
            X_SVmcPmm__HE820_UnitDelay1 = (X_SVmcPmm__HE819_UnitDelay >
             cVcVmcPmm_t_TransHeatDelayOn) || ((sVcDseEm_Tq_EradMaxAvailWhl <=
             (SVmcPmm__HE821_Tq_TransHeatReq + cVcVmcPmm_Tq_TransHeatReqOffset)) &&
             X_SVmcPmm__HE820_UnitDelay1);

            
            yVcVmcPmm_B_TransHeatReq = X_SVmcPmm__HE820_UnitDelay1;
         #endif

         
         SVmcPmm__HE6_Merge3 = SVmcPmm__HE173_Merge3;

         
         sVcVmcPmm_D_IsgModReq = SVmcPmm__HE173_Merge;

         
         yVcVmcPmm_B_IsgActReq = SVmcPmm__HE173_Merge1;
      #endif

      
      X_SVmcPmm__HE6_UnitDelay15 = xVcVmcPmm_B_IsgStopStandstillPre;

      
      X_SVmcPmm__HE6_UnitDelay11 = xVcVmcPmm_B_EngRunReqIsgStop;

      
      X_SVmcPmm__HE6_UnitDelay9 = xVcVmcPmm_B_IsgStopCoast;

      
      X_SVmcPmm__HE6_UnitDelay7 = xVcVmcPmm_B_Wait4CluStrt;

      
      X_SVmcPmm__HE6_UnitDelay12 = xVcVmcPmm_B_EngRunReqIsgStop;

      
      X_SVmcPmm__HE6_UnitDelay2 = xVcVmcPmm_B_StrtActrsRdy;

      
      if (CVmcPmm__HE1_D_IceStatus == 2) {
         
         X_SVmcPmm__HE593_UnitDelay = X_SVmcPmm__HE593_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE593_UnitDelay = 0.F;
      }

      
      if ((X_SVmcPmm__HE593_UnitDelay > cVcVmcPmm_t_EngRunStall) || (!(SVmcPmm__HE829_Switch))) {
         
         rVcVmcPmm_D_StallAbortNum = 0;
      }
      else {
         
         rVcVmcPmm_D_StallAbortNum = (UInt8) (X_SVmcPmm__HE172_UnitDelay3 + ((UInt8)
          SVmcPmm__HE527_LogicalOperator));
      }

      
      X_SVmcPmm__HE172_UnitDelay3 = rVcVmcPmm_D_StallAbortNum;

      
      xVcVmcPmm_B_StallAbortNum = rVcVmcPmm_D_StallAbortNum >= cVcVmcPmm_D_AbortStart;

      
      if (SVmcPmm__HE829_Switch && (!(X_SVmcPmm__HE530_UnitDelay1))) {
         
         X_SVmcPmm__HE581_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE581_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE581_UnitDelay;
      }

      
      X_SVmcPmm__HE530_UnitDelay1 = SVmcPmm__HE829_Switch;

      
      if (SVmcPmm__HE829_Switch && (!(X_SVmcPmm__HE528_UnitDelay1))) {
         
         X_SVmcPmm__HE580_UnitDelay = 0.F;
      }
      else {
         
         X_SVmcPmm__HE580_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE580_UnitDelay;
      }

      
      X_SVmcPmm__HE528_UnitDelay1 = SVmcPmm__HE829_Switch;

      
      if (cVcVmcPmm_B_AbrtFrstStrtStall) {
         
         xVcVmcPmm_B_AbrtFrstStrtStall = X_SVmcPmm__HE590_UnitDelay1 && (X_SVmcPmm__HE581_UnitDelay
          > cVcVmcPmm_t_BlockAbrtFrstDrCycle) && (X_SVmcPmm__HE580_UnitDelay <=
          cVcVmcPmm_t_AbrtFrstDrCycle);
      }
      else {
         
         xVcVmcPmm_B_AbrtFrstStrtStall = 0;
      }

      
      if (cVcVmcPmm_B_AbrtNtrlAdapt) {
         
         xVcVmcPmm_B_AbrtNtrlAdapt = (!(yVcScDep_B_NeutralMTValid)) && X_SVmcPmm__HE590_UnitDelay1;
      }
      else {
         
         xVcVmcPmm_B_AbrtNtrlAdapt = 0;
      }

      
      if (X_SVmcPmm__HE590_UnitDelay1) {
         
         X_SVmcPmm__HE585_UnitDelay = X_SVmcPmm__HE585_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE585_UnitDelay = 0.F;
      }

      
      if (cVcVmcPmm_B_AbrtStallTime) {
         
         xVcVmcPmm_B_AbrtStallTime = X_SVmcPmm__HE585_UnitDelay > cVcVmcPmm_t_AbrtStall;
      }
      else {
         
         xVcVmcPmm_B_AbrtStallTime = 0;
      }

      
      if (cVcVmcPmm_B_AbrtStallGp) {
         
         xVcVmcPmm_B_AbrtStallGp = sVcGp_D_StopStart != 2;
      }
      else {
         
         xVcVmcPmm_B_AbrtStallGp = 0;
      }

      
      if (cVcVmcPmm_B_AbrtStallRcvInSpd) {
         
         xVcVmcPmm_B_StallRcvAbortInSpd = (sVcScIn_v_VehSpdLgt >= cVcVmcPmm_v_VehMaxStallRcv) &&
          X_SVmcPmm__HE590_UnitDelay1;
      }
      else {
         
         xVcVmcPmm_B_StallRcvAbortInSpd = 0;
      }

      
      if (cVcVmcPmm_B_AbrtStallSsRcfSet) {
         
         xVcVmcPmm_B_AbrtStallSsRcfSet = yVcEc_B_SsRcfSet;
      }
      else {
         
         xVcVmcPmm_B_AbrtStallSsRcfSet = 0;
      }

      
      if (cVcVmcPmm_B_AbrtStallAbortHard) {
         
         xVcVmcPmm_B_AbrtStallAbortHard = yVcPpmRc_B_StrtAbortHard;
      }
      else {
         
         xVcVmcPmm_B_AbrtStallAbortHard = 0;
      }

      
      if (cVcVmcPmm_B_AbrtStallSeatBelt) {
         
         xVcVmcPmm_B_AbrtStallSeatBelt = X_SVmcPmm__HE590_UnitDelay1 &&
          (!(yVcCem_B_BltLockStAtDrvr));
      }
      else {
         
         xVcVmcPmm_B_AbrtStallSeatBelt = 0;
      }

      
      if (cVcVmcPmm_B_AbrtStallMicHev) {
         
         xVcVmcPmm_B_AbrtStallMicHev = sVcDeDmm_D_MicHevMode == 0;
      }
      else {
         
         xVcVmcPmm_B_AbrtStallMicHev = 0;
      }

      
      if (cVcVmcPmm_B_AbrtStallEngClntL) {
         
         xVcVmcPmm_B_AbrtStallEngClntL = SVmcPmm__HE848_Switch < cVcVmcPmm_Te_AbrtStallEngClntL;
      }
      else {
         
         xVcVmcPmm_B_AbrtStallEngClntL = 0;
      }

      
      if (cVcVmcPmm_B_AbrtStallRcShutOff) {
         
         xVcVmcPmm_B_AbrtStallRcShutOff = yVcPpmRc_B_ShutOffReq;
      }
      else {
         
         xVcVmcPmm_B_AbrtStallRcShutOff = 0;
      }

      
      X_SVmcPmm__HE172_UnitDelay8 = xVcVmcPmm_B_StallAbortNum || xVcVmcPmm_B_AbrtFrstStrtStall ||
       xVcVmcPmm_B_AbrtNtrlAdapt || xVcVmcPmm_B_AbrtStallTime || xVcVmcPmm_B_AbrtStallGp ||
       xVcVmcPmm_B_StallRcvAbortInSpd || xVcVmcPmm_B_AbrtStallSsRcfSet ||
       xVcVmcPmm_B_AbrtStallAbortHard || xVcVmcPmm_B_AbrtStallSeatBelt ||
       xVcVmcPmm_B_AbrtStallMicHev || xVcVmcPmm_B_AbrtStallEngClntL ||
       xVcVmcPmm_B_AbrtStallRcShutOff;

      
      X_SVmcPmm__HE172_UnitDelay1 = X_SVmcPmm__HE172_UnitDelay8;

      
      xVcVmcPmm_B_DrDoorOpen = sVcCem_D_DoorDrvrSts == cVcVmcPmm_D_DrDoorOpen;
      #if Vc_Pvc_Hw_B_HVSystem == 0
         
         if (sVcEc_n_Eng <= cVcVmcPmm_n_PwdRpmOnly) {
            
            X_SVmcPmm__HE46_UnitDelay = X_SVmcPmm__HE46_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE46_UnitDelay = 0.F;
         }

         
         if (cVcVmcPmm_B_PwdRpmOnly) {
            
            SVmcPmm__HE36_Switch = X_SVmcPmm__HE46_UnitDelay > cVcVmcPmm_t_PwdRpm;
         }
         else {
            
            SVmcPmm__HE36_Switch = CVmcPmm__HE1_D_IceStatus == 0;
         }

         
         if (cVcVmcPmm_B_PwdRcShutOffDCA) {
            
            SVmcPmm__HE32_Switch = yVcPpmPsm_B_DriveCycleActive && yVcPpmRc_B_ShutOffReq;
         }
         else {
            
            SVmcPmm__HE32_Switch = yVcPpmRc_B_ShutOffReq;
         }

         
         if (SVmcPmm__HE32_Switch) {
            
            X_SVmcPmm__HE48_UnitDelay = X_SVmcPmm__HE48_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE48_UnitDelay = 0.F;
         }

         
         if (cVcVmcPmm_B_PwdRcShutOff) {
            
            SVmcPmm__HE41_Switch = X_SVmcPmm__HE48_UnitDelay > cVcVmcPmm_t_PwdRcShutOff;
         }
         else {
            
            SVmcPmm__HE41_Switch = 0;
         }

         
         if (cVcVmcPmm_B_PwdSpeedLimit) {
            
            SVmcPmm__HE39_Switch = sVcScIn_v_VehSpdLgt < cVcVmcPmm_v_PwdSpeedLimit;
         }
         else {
            
            SVmcPmm__HE39_Switch = 1;
         }

         
         xVcVmcPmm_B_PwdPossible = yVcPpmPsm_B_DriveCycleActive && ((yVcPpmRc_B_StrtAbortHard &&
          cVcVmcPmm_B_PwdDrReadyAbortHard) || (!(yVcPpmPsm_B_DrReady))) && (SVmcPmm__HE36_Switch ||
          SVmcPmm__HE41_Switch) && SVmcPmm__HE39_Switch;

         
         if (cVcVmcPmm_B_PwdSeatBeltDoor) {
            
            
            #if Vc_Pvc_Hw_B_HVSystem == 0
               Bool SVmcPmm__HE31_Switch;
            #endif

            
            if (cVcVmcPmm_B_PwdIgnoreQfDrDoor) {
               
               SVmcPmm__HE31_Switch = 0;
            }
            else {
               
               SVmcPmm__HE31_Switch = sVcCem_Qf_DoorDrvrSts != 3;
            }

            
            SVmcPmm__HE44_Switch = xVcVmcPmm_B_DrDoorOpen || SVmcPmm__HE31_Switch;
         }
         else {
            
            SVmcPmm__HE44_Switch = 0;
         }

         
         SVmcPmm__HE26_LogicalOperator15 = (((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATPark) &&
          cVcVmcPmm_B_PwdSeatBeltP) || ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATNeutral) &&
          cVcVmcPmm_B_PwdSeatBeltN)) && (!(yVcCem_B_BltLockStAtDrvr));

         
         SVmcPmm__HE26_LogicalOperator23 = SVmcPmm__HE44_Switch && SVmcPmm__HE26_LogicalOperator15;

         
         if (SVmcPmm__HE26_LogicalOperator15) {
            
            X_SVmcPmm__HE47_UnitDelay = X_SVmcPmm__HE47_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE47_UnitDelay = 0.F;
         }

         
         if (cVcVmcPmm_B_PwdSeatBelt) {
            
            if (yVcDtcAtr_B_AT && cVcVmcPmm_B_PwdUseSeatBeltAT) {
               
               SVmcPmm__HE40_Switch = SVmcPmm__HE26_LogicalOperator23 || (X_SVmcPmm__HE47_UnitDelay
                > cVcVmcPmm_t_PwdSeatBeltAT);
            }
            else {
               
               SVmcPmm__HE40_Switch = !(yVcCem_B_BltLockStAtDrvr);
            }
         }
         else {
            
            SVmcPmm__HE40_Switch = 0;
         }

         
         if (cVcVmcPmm_B_PwdRcfDep) {
            
            SVmcPmm__HE33_Switch = yVcEc_B_SsRcfSet;
         }
         else {
            
            SVmcPmm__HE33_Switch = 0;
         }

         
         if (cVcVmcPmm_B_PwdAbrtStall) {
            
            SVmcPmm__HE34_Switch = X_SVmcPmm__HE172_UnitDelay8;
         }
         else {
            
            SVmcPmm__HE34_Switch = 0;
         }

         
         if (cVcVmcPmm_B_PwdAbortHard) {
            
            SVmcPmm__HE35_Switch = yVcPpmRc_B_StrtAbortHard;
         }
         else {
            
            SVmcPmm__HE35_Switch = 0;
         }

         
         if (cVcVmcPmm_B_PwdTransFailure) {
            
            SVmcPmm__HE37_Switch = yVcTcm_B_TrsmNeutFailr && yVcDtcAtr_B_AT;
         }
         else {
            
            SVmcPmm__HE37_Switch = 0;
         }

         
         if (cVcVmcPmm_B_PwdTCMNodeAlive) {
            
            SVmcPmm__HE38_Switch = (!(yVcEc_B_TCMNodeAlive)) && yVcDtcAtr_B_AT;
         }
         else {
            
            SVmcPmm__HE38_Switch = 0;
         }

         
         if (sVcDtcAtr_D_TransMode != sVcSpMon_D_PtTrsmModReq) {
            
            X_SVmcPmm__HE49_UnitDelay = X_SVmcPmm__HE49_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE49_UnitDelay = 0.F;
         }

         
         if (cVcVmcPmm_B_PwdTCMModeFail) {
            
            SVmcPmm__HE42_Switch = (X_SVmcPmm__HE49_UnitDelay > cVcVmcPmm_t_PwdTcmModeFail) &&
             yVcDtcAtr_B_AT;
         }
         else {
            
            SVmcPmm__HE42_Switch = 0;
         }

         
         xVcVmcPmm_B_PwdTrig = SVmcPmm__HE40_Switch || SVmcPmm__HE33_Switch || SVmcPmm__HE34_Switch
          || SVmcPmm__HE35_Switch || SVmcPmm__HE37_Switch || SVmcPmm__HE38_Switch ||
          SVmcPmm__HE42_Switch;

         
         xVcVmcPmm_B_PwdReset = (!(yVcPpmPsm_B_DriveCycleActive)) || ((CVmcPmm__HE1_D_IceStatus ==
          1) || (CVmcPmm__HE1_D_IceStatus == 2));

         
         X_SVmcPmm__HE50_UnitDelay1 = (xVcVmcPmm_B_PwdPossible && xVcVmcPmm_B_PwdTrig) ||
          ((!(xVcVmcPmm_B_PwdReset)) && X_SVmcPmm__HE50_UnitDelay1);

         
         if (cVcVmcPmm_B_UsePowerDownReq) {
            
            SVmcPmm__HE30_Switch = X_SVmcPmm__HE50_UnitDelay1;
         }
         else {
            
            SVmcPmm__HE30_Switch = 0;
         }

         
         if (SVmcPmm__HE30_Switch && SVmcPmm__HE26_LogicalOperator23) {
            
            X_SVmcPmm__HE45_UnitDelay = 0.F;
         }
         else {
            
            X_SVmcPmm__HE45_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE45_UnitDelay;
         }

         
         yVcVmcPmm_B_BlockPushStartHMI = X_SVmcPmm__HE45_UnitDelay <= cVcVmcPmm_t_BlockPsmPwd;
      #endif
      #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
         
         if (cVcVmcPmm_B_UseStartModeHybrid) {
            
            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               UInt8 SVmcPmm__HE389_MinMax;
            #endif

            

            
            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               static Bool X_SVmcPmm__HE390_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               static Bool X_SVmcPmm__HE391_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               static Bool X_SVmcPmm__HE392_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               static Bool X_SVmcPmm__HE393_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               static Bool X_SVmcPmm__HE394_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               static Bool X_SVmcPmm__HE395_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               static Bool X_SVmcPmm__HE399_UnitDelay1 = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               static Bool X_SVmcPmm__HE400_UnitDelay1 = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               static Bool X_SVmcPmm__HE401_UnitDelay1 = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121M_StartModeHybrid_3
               static Bool X_SVmcPmm__HE402_UnitDelay1 = 0;
            #endif

            

            
            X_SVmcPmm__HE402_UnitDelay1 = (!(SVmcPmm__HE829_Switch)) || ((CVmcPmm__HE1_D_IceStatus
             != 2) && X_SVmcPmm__HE402_UnitDelay1);

            
            SVmcPmm__HE389__gicalOperator52 = X_SVmcPmm__HE402_UnitDelay1 &&
             (yVcDsePcr_B_PwrUpIceStrtReq || yVcVmcEm_B_PwrUpIceStrtReq ||
             (yVcVmcPmm_B_EngRunReqTrans && cVcVmcPmm_B_PwrUpIceStrtReqUseTrans));

            
            xVcVmcPmm_B_SafeISGPrio = yVcDsePcr_B_SafeEngStrtReq || ((yVcVmcPmm_B_EngRunReqFuel ||
             xVcVmcPmm_B_EngRunReqPsm || SVmcPmm__HE389__gicalOperator52) && (SVmcPmm__HE829_Switch
             && (!(X_SVmcPmm__HE391_Delay)))) || ((SVmcPmm__HE829_Switch ||
             (!(X_SVmcPmm__HE393_Delay))) && ((!(xVcVmcPmm_B_EngOnReqEng)) ||
             X_SVmcPmm__HE395_Delay) && X_SVmcPmm__HE400_UnitDelay1);

            
            X_SVmcPmm__HE400_UnitDelay1 = xVcVmcPmm_B_SafeISGPrio;

            
            X_SVmcPmm__HE395_Delay = xVcVmcPmm_B_EngOnReqEng;

            
            X_SVmcPmm__HE393_Delay = SVmcPmm__HE829_Switch;

            
            X_SVmcPmm__HE391_Delay = SVmcPmm__HE829_Switch;

            
            xVcVmcPmm_B_FastStart = yVcDeDmm_B_RespStartReq || (((yVcDtcEsc_B_Active &&
             cVcVmcPmm_B_StrtMdeEscCond) || ((sVcDtcAtr_n_TrgGear - sVcDtcIcl_n_IdleSpdBs) >=
             cVcVmcPmm_n_StrtDiffFast)) && ((sVcVmcPmm_D_TransModeReq <= 2) ||
             cVcVmcPmm_B_StrtMdeSkipTrnMde));

            
            X_SVmcPmm__HE399_UnitDelay1 = xVcVmcPmm_B_FastStart || (((!(xVcVmcPmm_B_EngOnReqEng)) ||
              X_SVmcPmm__HE392_Delay) && X_SVmcPmm__HE399_UnitDelay1);

            
            X_SVmcPmm__HE392_Delay = xVcVmcPmm_B_EngOnReqEng;

            
            if (sVcEmiHeat_D_EngUseReq > sVcTmStrt_D_EngUseReq) {
               SVmcPmm__HE389_MinMax = sVcEmiHeat_D_EngUseReq;
            }
            else {
               SVmcPmm__HE389_MinMax = sVcTmStrt_D_EngUseReq;
            }

            
            xVcVmcPmm_B_SafeISG = (cVcVmcPmm_B_SerialModeSafeBISG && (SVmcPmm__HE389_MinMax == 1) &&
              (sVcVmcPmm_D_TransModeReq > 2)) || ((SVmcPmm__HE829_Switch ||
             (!(X_SVmcPmm__HE390_Delay))) && ((!(xVcVmcPmm_B_EngOnReqEng)) ||
             X_SVmcPmm__HE394_Delay) && X_SVmcPmm__HE401_UnitDelay1);

            
            X_SVmcPmm__HE401_UnitDelay1 = xVcVmcPmm_B_SafeISG;

            
            X_SVmcPmm__HE394_Delay = xVcVmcPmm_B_EngOnReqEng;

            
            X_SVmcPmm__HE390_Delay = SVmcPmm__HE829_Switch;

            
            if (xVcVmcPmm_B_SafeISGPrio) {
               
               SVmcPmm__HE398_Switch = cVcVmcPmm_D_SafeBISG;
            }
            else {
               
               if (X_SVmcPmm__HE399_UnitDelay1) {
                  
                  SVmcPmm__HE398_Switch = cVcVmcPmm_D_FastBISG;
               }
               else {
                  
                  if (xVcVmcPmm_B_SafeISG) {
                     
                     SVmcPmm__HE398_Switch = cVcVmcPmm_D_SafeBISG;
                  }
                  else {
                     
                     SVmcPmm__HE398_Switch = cVcVmcPmm_D_NormalBISG;
                  }
               }
            }
         }
      #endif
      #if VcVmcPmm__HEP7_1270_12VStartEnable_10
         
         SVmcPmm__HE6_Merge3 = 1;
      #endif

      
      xVcVmcPmm_B_FastEngmtTrqDemand = yVcDeDmm_B_RespStartReq && ((!(yVcVmcTfa_B_CcActive)) ||
       cVcVmcPmm_B_IgnrCcActive) && (sVcScIn_X_AccPedalPos >= cVcVmcPmm_X_AccPedFastEngmtMin);

      
      if (X_SVmcPmm__HE456_Del2) {
         
         rVcVmcPmm_Xd_AccPedalPos = 0.F;
      }
      else {
         
         Float32 SVmcPmm__HE456_MinMax1;
         Float32 SVmcPmm__HE456_MinMax2;
         Float32 SVmcPmm__HE456_Prod;
         Float32 SVmcPmm__HE456_Prod1;
         Float32 SVmcPmm__HE456_Sum;
         Float32 SVmcPmm__HE456_Sum3;

         
         SVmcPmm__HE456_Sum = sVcScIn_X_AccPedalPos - X_SVmcPmm__HE456_Del;

         
         if (ts_VcVmcPmm__HEP7 > 1e-06F) {
            
            SVmcPmm__HE456_MinMax1 = ts_VcVmcPmm__HEP7;
         }
         else {
            SVmcPmm__HE456_MinMax1 = 1e-06F;
         }

         
         if (SVmcPmm__HE456_MinMax1 != 0.F) {
            SVmcPmm__HE456_Prod = SVmcPmm__HE456_Sum / SVmcPmm__HE456_MinMax1;
         }
         else {
            if (SVmcPmm__HE456_Sum < 0.F) {
               SVmcPmm__HE456_Prod = -3.402823466e+38F;
            }
            else {
               SVmcPmm__HE456_Prod = 3.402823466e+38F;
            }
         }

         
         SVmcPmm__HE456_Sum3 = ts_VcVmcPmm__HEP7 + cVcVmcPmm_tc_AccPedDer;
         if (SVmcPmm__HE456_Sum3 > 1e-06F) {
            SVmcPmm__HE456_MinMax2 = SVmcPmm__HE456_Sum3;
         }
         else {
            SVmcPmm__HE456_MinMax2 = 1e-06F;
         }

         
         if (SVmcPmm__HE456_MinMax2 != 0.F) {
            
            SVmcPmm__HE456_Prod1 = ts_VcVmcPmm__HEP7 / SVmcPmm__HE456_MinMax2;
         }
         else {
            
            if (ts_VcVmcPmm__HEP7 < 0.F) {
               SVmcPmm__HE456_Prod1 = -3.402823466e+38F;
            }
            else {
               SVmcPmm__HE456_Prod1 = 3.402823466e+38F;
            }
         }

         
         rVcVmcPmm_Xd_AccPedalPos = X_SVmcPmm__HE456_Del1 + ((SVmcPmm__HE456_Prod -
          X_SVmcPmm__HE456_Del1) * SVmcPmm__HE456_Prod1);
      }

      
      X_SVmcPmm__HE456_Del = sVcScIn_X_AccPedalPos;

      
      X_SVmcPmm__HE456_Del1 = rVcVmcPmm_Xd_AccPedalPos;

      
      X_SVmcPmm__HE456_Del2 = 0;

      
      xVcVmcPmm_B_FastEngmtPwrDemand = yVcVmcEm_B_RespStartReq && (rVcVmcPmm_Xd_AccPedalPos >
       cVcVmcPmm_Xd_AccPedFastEngmtMin);

      
      if (cVcVmcPmm_B_FastEngmtIsgStrtUseStartReq) {
         
         SVmcPmm__HE458_Switch = X_SVmcPmm__HE6_UnitDelay10;
      }
      else {
         
         SVmcPmm__HE458_Switch = X_SVmcPmm__HE6_UnitDelay6;
      }

      
      xVcVmcPmm_B_FastEngmtIsgStrt = SVmcPmm__HE458_Switch && ((sVcDtcAtr_D_GearLevAT ==
       cVc_D_GearLevATDrive) || (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATReverse)) &&
       (sVcVdm_Tq_BrkTqAtWhlsReq <= cVcVmcPmm_Tq_FastEngmtIsgStrtBrkTqMax);

      
      SVmcPmm__HE226_LogicalOperator3 = (sVcVmcPmm_D_TransModeReq == 1) && ((sVcScDep_D_DrvgDirDes
       == 1) || (sVcScDep_D_DrvgDirDes == 3));

      
      SVmcPmm__HE226_LogicalOperator6 = (xVcVmcPmm_B_FastEngmtTrqDemand ||
       xVcVmcPmm_B_FastEngmtPwrDemand || xVcVmcPmm_B_FastEngmtIsgStrt) &&
       SVmcPmm__HE226_LogicalOperator3;

      
      if (yVcVmcPmm_B_CrShPathEnable) {
         
         X_SVmcPmm__HE461_UnitDelay = X_SVmcPmm__HE461_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE461_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_EngmtModFast = (SVmcPmm__HE226_LogicalOperator6 && (!(X_SVmcPmm__HE457_Delay))) ||
        (SVmcPmm__HE226_LogicalOperator3 && (X_SVmcPmm__HE461_UnitDelay <=
       cVcVmcPmm_t_EngEngmtFastRstDelay) && X_SVmcPmm__HE460_UnitDelay1);

      
      X_SVmcPmm__HE460_UnitDelay1 = xVcVmcPmm_B_EngmtModFast;

      
      X_SVmcPmm__HE457_Delay = SVmcPmm__HE226_LogicalOperator6;

      
      if (xVcVmcPmm_B_EngmtModFast) {
         
         sVcVmcPmm_D_EngagementMode = cVcVmcPmm_D_EngmtModFast;
      }
      else {
         
         sVcVmcPmm_D_EngagementMode = cVcVmcPmm_D_EngmtModSmooth;
      }
      #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
         
         if (cVcVmcPmm_B_UseStartModeHybrid12V) {
            
            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               UInt8 SVmcPmm__HE403_MinMax;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               Bool SVmcPmm__HE403__gicalOperator11;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               Bool SVmcPmm__HE403__gicalOperator12;
            #endif

            

            
            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE404_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE405_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE406_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE407_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE408_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE409_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE410_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE411_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE412_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE413_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE414_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE415_Delay = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE422_UnitDelay1 = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE423_UnitDelay1 = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE424_UnitDelay1 = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE425_UnitDelay1 = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE426_UnitDelay1 = 0;
            #endif

            

            
            #if VcVmcPmm__HEP7_121N_StartModeHybrid12V_4
               static Bool X_SVmcPmm__HE427_UnitDelay1 = 0;
            #endif

            

            
            X_SVmcPmm__HE425_UnitDelay1 = (!(SVmcPmm__HE829_Switch)) || ((CVmcPmm__HE1_D_IceStatus
             != 2) && X_SVmcPmm__HE425_UnitDelay1);

            
            SVmcPmm__HE403__gicalOperator52 = X_SVmcPmm__HE425_UnitDelay1 &&
             (yVcDsePcr_B_PwrUpIceStrtReq || yVcVmcEm_B_PwrUpIceStrtReq ||
             xVcVmcPmm_B_EngRunReqEngClnt || (yVcVmcPmm_B_EngRunReqTrans &&
             cVcVmcPmm_B_PwrUpIceStrtReqUseTrans));

            
            X_SVmcPmm__HE424_UnitDelay1 = yVcDsePcr_B_SafeEngStrtReq || yVcFsdPc_B_RunDry ||
             (cVcVmcPmm_B_UseLastStrtMod && (rVcVmcPmm_D_StallAbortNum >= ((UInt8)
             (cVcVmcPmm_D_AbortStart - 1)))) || ((SVmcPmm__HE829_Switch ||
             (!(X_SVmcPmm__HE409_Delay))) && ((!(xVcVmcPmm_B_EngOnReqEng)) ||
             X_SVmcPmm__HE411_Delay) && X_SVmcPmm__HE424_UnitDelay1);

            
            X_SVmcPmm__HE411_Delay = xVcVmcPmm_B_EngOnReqEng;

            
            X_SVmcPmm__HE409_Delay = SVmcPmm__HE829_Switch;

            
            X_SVmcPmm__HE427_UnitDelay1 = ((sVcVmcPmm_D_EngagementMode == cVcVmcPmm_D_EngmtModFast)
             && ((sVcDtcAtr_D_GearLevAT == cVcVmcPmm_D_GearLevRespStrtOK1) || (sVcDtcAtr_D_GearLevAT
              == cVcVmcPmm_D_GearLevRespStrtOK2) || cVcVmcPmm_B_IgnoreGearLevRespStrt)) ||
             ((SVmcPmm__HE829_Switch || (!(X_SVmcPmm__HE405_Delay))) &&
             ((!(xVcVmcPmm_B_EngOnReqEng)) || X_SVmcPmm__HE408_Delay) &&
             X_SVmcPmm__HE427_UnitDelay1);

            
            X_SVmcPmm__HE408_Delay = xVcVmcPmm_B_EngOnReqEng;

            
            X_SVmcPmm__HE405_Delay = SVmcPmm__HE829_Switch;

            
            if (sVcTmStrt_D_EngUseReq > sVcEmiHeat_D_EngUseReq) {
               SVmcPmm__HE403_MinMax = sVcTmStrt_D_EngUseReq;
            }
            else {
               SVmcPmm__HE403_MinMax = sVcEmiHeat_D_EngUseReq;
            }

            
            xVcVmcPmm_B_EmiStrt = (cVcVmcPmm_B_UseFirstStartMode && (sVcVmcPmm_D_TransModeReq > 2)
             && (SVmcPmm__HE403_MinMax == 1)) || SVmcPmm__HE403__gicalOperator52 ||
             ((SVmcPmm__HE829_Switch || (!(X_SVmcPmm__HE404_Delay))) &&
             ((!(xVcVmcPmm_B_EngOnReqEng)) || X_SVmcPmm__HE410_Delay) &&
             X_SVmcPmm__HE422_UnitDelay1);

            
            X_SVmcPmm__HE422_UnitDelay1 = xVcVmcPmm_B_EmiStrt;

            
            X_SVmcPmm__HE410_Delay = xVcVmcPmm_B_EngOnReqEng;

            
            X_SVmcPmm__HE404_Delay = SVmcPmm__HE829_Switch;

            
            SVmcPmm__HE403__gicalOperator11 = ((!(SVmcPmm__HE829_Switch)) && X_SVmcPmm__HE412_Delay)
              || (xVcVmcPmm_B_EngOnReqEng && (!(X_SVmcPmm__HE414_Delay)));

            
            X_SVmcPmm__HE414_Delay = xVcVmcPmm_B_EngOnReqEng;

            
            X_SVmcPmm__HE412_Delay = SVmcPmm__HE829_Switch;

            
            X_SVmcPmm__HE426_UnitDelay1 = X_SVmcPmm__HE6_UnitDelay10 ||
             (((!(SVmcPmm__HE403__gicalOperator11)) || X_SVmcPmm__HE413_Delay) &&
             X_SVmcPmm__HE426_UnitDelay1);

            
            X_SVmcPmm__HE413_Delay = SVmcPmm__HE403__gicalOperator11;

            
            SVmcPmm__HE403__gicalOperator12 = ((!(SVmcPmm__HE829_Switch)) && X_SVmcPmm__HE406_Delay)
              || (xVcVmcPmm_B_EngOnReqEng && (!(X_SVmcPmm__HE407_Delay)));

            
            X_SVmcPmm__HE407_Delay = xVcVmcPmm_B_EngOnReqEng;

            
            X_SVmcPmm__HE406_Delay = SVmcPmm__HE829_Switch;

            
            X_SVmcPmm__HE423_UnitDelay1 = SVmcPmm__HE6_Merge3 ||
             (((!(SVmcPmm__HE403__gicalOperator12)) || X_SVmcPmm__HE415_Delay) &&
             X_SVmcPmm__HE423_UnitDelay1);

            
            X_SVmcPmm__HE415_Delay = SVmcPmm__HE403__gicalOperator12;

            
            if (X_SVmcPmm__HE424_UnitDelay1) {
               
               SVmcPmm__HE416_Switch = 0;
            }
            else {
               
               if (X_SVmcPmm__HE427_UnitDelay1) {
                  
                  SVmcPmm__HE416_Switch = 3;
               }
               else {
                  
                  if (xVcVmcPmm_B_EmiStrt) {
                     
                     SVmcPmm__HE416_Switch = 0;
                  }
                  else {
                     
                     if (X_SVmcPmm__HE426_UnitDelay1) {
                        
                        SVmcPmm__HE416_Switch = 2;
                     }
                     else {
                        
                        if (X_SVmcPmm__HE423_UnitDelay1) {
                           
                           if (cVcVmcPmm_B_UseStrtMde3All12vStrt) {
                              
                              SVmcPmm__HE416_Switch = 3;
                           }
                           else {
                              
                              SVmcPmm__HE416_Switch = 1;
                           }
                        }
                        else {
                           
                           SVmcPmm__HE416_Switch = cVcVmcPmm_D_StrtModDft;
                        }
                     }
                  }
               }
            }
         }

         
         SVmcPmm__HE222_Rescaler = 1;
      #endif

      
      SVmcPmm__HE223__ionalOperator11 = sVcScIn_X_AccPedalPos > cVcVmcPmm_X_StrtMdeAcc;

      
      SVmcPmm__HE223__ionalOperator18 = CVmcPmm__HE1_D_IceStatus == 2;

      
      if (SVmcPmm__HE223__ionalOperator18) {
         
         X_SVmcPmm__HE436_UnitDelay = X_SVmcPmm__HE436_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE436_UnitDelay = 0.F;
      }

      
      if (!(SVmcPmm__HE223__ionalOperator11)) {
         
         X_SVmcPmm__HE435_UnitDelay = X_SVmcPmm__HE435_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE435_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_StrtMdeAcc = (SVmcPmm__HE223__ionalOperator11 &&
       (!(SVmcPmm__HE223__ionalOperator18))) || ((X_SVmcPmm__HE436_UnitDelay <=
       cVcVmcPmm_t_StrtMdeAccRun) && (X_SVmcPmm__HE435_UnitDelay <= cVcVmcPmm_t_StrtMdeAccRst) &&
       X_SVmcPmm__HE433_UnitDelay1);

      
      X_SVmcPmm__HE433_UnitDelay1 = xVcVmcPmm_B_StrtMdeAcc;

      
      SVmcPmm__HE223__tionalOperator1 = CVmcPmm__HE1_D_IceStatus == 2;

      
      if (SVmcPmm__HE223__tionalOperator1) {
         
         X_SVmcPmm__HE434_UnitDelay = X_SVmcPmm__HE434_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE434_UnitDelay = 0.F;
      }

      
      if (cVcVmcPmm_B_StrtMdeStopTrig) {
         
         SVmcPmm__HE428_Switch = (CVmcPmm__HE1_D_IceStatus == 3) && X_SVmcPmm__HE223_UnitDelay8;
      }
      else {
         
         SVmcPmm__HE428_Switch = X_SVmcPmm__HE434_UnitDelay > cVcVmcPmm_t_StrtMdeRunning;
      }

      
      X_SVmcPmm__HE223_UnitDelay8 = SVmcPmm__HE223__tionalOperator1;

      
      xVcVmcPmm_B_StrtMdeRunning = (SVmcPmm__HE428_Switch && SVmcPmm__HE829_Switch) ||
       (SVmcPmm__HE829_Switch && X_SVmcPmm__HE432_UnitDelay1);

      
      X_SVmcPmm__HE432_UnitDelay1 = xVcVmcPmm_B_StrtMdeRunning;

      
      if (cVcVmcPmm_D_StartMode_swi) {
         
         X_SVmcPmm__HE3_UnitDelay2 = cVcVmcPmm_D_StartMode_dbi;
      }
      else {
         
         if (Vc_Pvc_Hw_B_Isg_CN >= 1 ) {
            
            if (!(SVmcPmm__HE222_Rescaler)) {
               
               X_SVmcPmm__HE3_UnitDelay2 = SVmcPmm__HE398_Switch;
            }
            else {
               
               X_SVmcPmm__HE3_UnitDelay2 = SVmcPmm__HE416_Switch;
            }
         }
         else {
            
            if (xVcVmcPmm_B_StrtMdeRunning) {
               
               if (cVcVmcPmm_B_StrtMdeSet) {
                  
                  if (xVcVmcPmm_B_StrtMdeAcc) {
                     
                     X_SVmcPmm__HE3_UnitDelay2 = 2;
                  }
                  else {
                     
                     X_SVmcPmm__HE3_UnitDelay2 = 1;
                  }
               }
               else {
                  
                  X_SVmcPmm__HE3_UnitDelay2 = 0;
               }
            }
            else {
               
               X_SVmcPmm__HE3_UnitDelay2 = 0;
            }
         }
      }

      
      X_SVmcPmm__HE6_UnitDelay = X_SVmcPmm__HE3_UnitDelay2;

      
      X_SVmcPmm__HE170_UnitDelay3 = X_SVmcPmm__HE3_UnitDelay2;

      
      X_SVmcPmm__HE6_UnitDelay1 = X_SVmcPmm__HE3_UnitDelay2;

      
      sVcVmcPmm_D_StartMode = X_SVmcPmm__HE3_UnitDelay2;

      
      yVcVmcPmm_B_StallPwdReq = X_SVmcPmm__HE172_UnitDelay8;

      
      yVcVmcPmm_B_FCAdaptReq = SVmcPmm__HE159_LogOp3;

      
      sVcVmcPmm_D_IceStatus = CVmcPmm__HE1_D_IceStatus;

      
      yVcVmcPmm_B_EngOnReq = X_SVmcPmm__HE6_UnitDelay14;

      
      yVcVmcPmm_B_FastIsgStopReq = X_SVmcPmm__HE6_UnitDelay5;

      
      yVcVmcPmm_B_IsgStrtPahReq = X_SVmcPmm__HE6_UnitDelay6;

      
      yVcVmcPmm_B_EradPathEnable = X_SVmcPmm__HE6_UnitDelay8;

      
      yVcVmcPmm_B_IsgPathEnable = X_SVmcPmm__HE6_UnitDelay13;

      
      yVcVmcPmm_B_EfadPathEnable = X_SVmcPmm__HE6_UnitDelay4;

      
      yVcVmcPmm_B_IsgStartReq = X_SVmcPmm__HE6_UnitDelay10;

      
      yVcVmcPmm_B_12VStartEnable = SVmcPmm__HE6_Merge3;

      
      yVcVmcPmm_B_IceStall = X_SVmcPmm__HE590_UnitDelay1;

      
      if (SVmcPmm__HE172_LogOp1) {
         
         X_SVmcPmm__HE588_UnitDelay = X_SVmcPmm__HE588_UnitDelay + ts_VcVmcPmm__HEP7;
      }
      else {
         
         X_SVmcPmm__HE588_UnitDelay = 0.F;
      }

      
      xVcVmcPmm_B_StallRunUnintd = X_SVmcPmm__HE588_UnitDelay > cVcVmcPmm_t_StallRunUnintd;

      
      if (cVcVmcPmm_B_StallRunUnintd) {
         
         SVmcPmm__HE532_Switch = xVcVmcPmm_B_StallRunUnintd;
      }
      else {
         
         SVmcPmm__HE532_Switch = 0;
      }

      
      SVmcPmm__HE172__ionalOperator20 = CVmcPmm__HE1_D_IceStatus == 2;

      
      X_SVmcPmm__HE589_UnitDelay1 = SVmcPmm__HE532_Switch || (yVcPpmRc_B_ShutOffReq &&
       cVcVmcPmm_B_UnintdStallRcShOff) || (((!(SVmcPmm__HE172__ionalOperator20)) ||
       X_SVmcPmm__HE526_Delay) && SVmcPmm__HE829_Switch && X_SVmcPmm__HE589_UnitDelay1);

      
      X_SVmcPmm__HE526_Delay = SVmcPmm__HE172__ionalOperator20;

      
      yVcVmcPmm_B_UnintdStall = X_SVmcPmm__HE589_UnitDelay1;

      
      yVcVmcPmm_B_PwrUpIceStrtReq = SVmcPmm__HE389__gicalOperator52 ||
       SVmcPmm__HE403__gicalOperator52;

      
      if (xVcVmcPmm_B_EngOnOff) {
         
         Aux_U32 = 1;
      }
      else {
         
         Aux_U32 = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqDriver) {
         
         SVmcPmm__HE265_Switch = 2;
      }
      else {
         
         SVmcPmm__HE265_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqPsm) {
         
         SVmcPmm__HE266_Switch = 4;
      }
      else {
         
         SVmcPmm__HE266_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqEm) {
         
         SVmcPmm__HE267_Switch = 8;
      }
      else {
         
         SVmcPmm__HE267_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqTm) {
         
         SVmcPmm__HE269_Switch = 16;
      }
      else {
         
         SVmcPmm__HE269_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqDep) {
         
         SVmcPmm__HE270_Switch = 32;
      }
      else {
         
         SVmcPmm__HE270_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqTrans) {
         
         SVmcPmm__HE271_Switch = 64;
      }
      else {
         
         SVmcPmm__HE271_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqClim) {
         
         SVmcPmm__HE272_Switch = 128;
      }
      else {
         
         SVmcPmm__HE272_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqPcr) {
         
         SVmcPmm__HE273_Switch = 256;
      }
      else {
         
         SVmcPmm__HE273_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqFCAdapt) {
         
         SVmcPmm__HE274_Switch = 512;
      }
      else {
         
         SVmcPmm__HE274_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqBrake) {
         
         SVmcPmm__HE275_Switch = 1024;
      }
      else {
         
         SVmcPmm__HE275_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqFuel) {
         
         SVmcPmm__HE276_Switch = 2048;
      }
      else {
         
         SVmcPmm__HE276_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqIsg) {
         
         SVmcPmm__HE277_Switch = 4096;
      }
      else {
         
         SVmcPmm__HE277_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqStabCtrl) {
         
         SVmcPmm__HE278_Switch = 8192;
      }
      else {
         
         SVmcPmm__HE278_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqDrLeave) {
         
         SVmcPmm__HE280_Switch = 16384;
      }
      else {
         
         SVmcPmm__HE280_Switch = 0;
      }

      
      if (xVcVmcPmm_B_RunReqIceStall) {
         
         SVmcPmm__HE281_Switch = 32768;
      }
      else {
         
         SVmcPmm__HE281_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqChas) {
         
         SVmcPmm__HE283_Switch = 131072;
      }
      else {
         
         SVmcPmm__HE283_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqObd) {
         
         SVmcPmm__HE286_Switch = 262144;
      }
      else {
         
         SVmcPmm__HE286_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqRc) {
         
         SVmcPmm__HE287_Switch = 524288;
      }
      else {
         
         SVmcPmm__HE287_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqSapp) {
         
         SVmcPmm__HE288_Switch = 1048576;
      }
      else {
         
         SVmcPmm__HE288_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqEms) {
         
         SVmcPmm__HE289_Switch = 2097152;
      }
      else {
         
         SVmcPmm__HE289_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqEmLv) {
         
         SVmcPmm__HE291_Switch = 4194304;
      }
      else {
         
         SVmcPmm__HE291_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqRemote) {
         
         SVmcPmm__HE292_Switch = 8388608;
      }
      else {
         
         SVmcPmm__HE292_Switch = 0;
      }

      
      if (yVcVmcPmm_B_EngRunReqFanAfterrun) {
         
         SVmcPmm__HE293_Switch = 16777216;
      }
      else {
         
         SVmcPmm__HE293_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqCEC) {
         
         SVmcPmm__HE297_Switch = 33554432;
      }
      else {
         
         SVmcPmm__HE297_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqEngClnt) {
         
         SVmcPmm__HE303_Switch = 67108864;
      }
      else {
         
         SVmcPmm__HE303_Switch = 0;
      }

      
      if (xVcVmcPmm_B_EngRunReqMaxTime) {
         
         SVmcPmm__HE304_Switch = 67108864;
      }
      else {
         
         SVmcPmm__HE304_Switch = 0;
      }
      Aux_U32 += SVmcPmm__HE265_Switch;
      Aux_U32 += SVmcPmm__HE266_Switch;
      Aux_U32 += SVmcPmm__HE267_Switch;
      Aux_U32 += SVmcPmm__HE269_Switch;
      Aux_U32 += SVmcPmm__HE270_Switch;
      Aux_U32 += SVmcPmm__HE271_Switch;
      Aux_U32 += SVmcPmm__HE272_Switch;
      Aux_U32 += SVmcPmm__HE273_Switch;
      Aux_U32 += SVmcPmm__HE274_Switch;
      Aux_U32 += SVmcPmm__HE275_Switch;
      Aux_U32 += SVmcPmm__HE276_Switch;
      Aux_U32 += SVmcPmm__HE277_Switch;
      Aux_U32 += SVmcPmm__HE278_Switch;
      Aux_U32 += SVmcPmm__HE280_Switch;
      Aux_U32 += SVmcPmm__HE281_Switch;
      Aux_U32 += SVmcPmm__HE283_Switch;
      Aux_U32 += SVmcPmm__HE286_Switch;
      Aux_U32 += SVmcPmm__HE287_Switch;
      Aux_U32 += SVmcPmm__HE288_Switch;
      Aux_U32 += SVmcPmm__HE289_Switch;
      Aux_U32 += SVmcPmm__HE291_Switch;
      Aux_U32 += SVmcPmm__HE292_Switch;
      Aux_U32 += SVmcPmm__HE293_Switch;
      Aux_U32 += SVmcPmm__HE297_Switch;
      Aux_U32 += SVmcPmm__HE303_Switch;
      rVcVmcPmm_D_EngRunReqLogg = Aux_U32 + SVmcPmm__HE304_Switch;

      
      sVcVmcPmm_D_EngRunReqLogg = rVcVmcPmm_D_EngRunReqLogg;

      
      sVcVmcPmm_Z_HillGradientDeg = SVmcPmm__HE153__HillGradAcc2deg;

      
      yVcVmcPmm_B_PowerDownReq = SVmcPmm__HE30_Switch || xVcVmcPmm_B_DrLeavePowerDownReq;
      #if VcVmcPmm__HEP7_121P_EngRunReqDispHmi_5
         
         if (xVcVmcPmm_B_EngRunReqFCAdapt) {
            
            X_SVmcPmm__HE446_UnitDelay = X_SVmcPmm__HE446_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE446_UnitDelay = 0.F;
         }

         
         if (xVcVmcPmm_B_EngRunReqPcr || yVcVmcPmm_B_EngRunReqClim || xVcVmcPmm_B_EngRunReqPsm ||
          yVcVmcPmm_B_EngRunReqFuel) {
            
            X_SVmcPmm__HE447_UnitDelay = X_SVmcPmm__HE447_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE447_UnitDelay = 0.F;
         }

         
         if (yVcVmcPmm_B_EngRunReqBrake) {
            
            X_SVmcPmm__HE449_UnitDelay = X_SVmcPmm__HE449_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE449_UnitDelay = 0.F;
         }

         
         if (!(xVcVmcPmm_B_EngRunReqEm)) {
            
            X_SVmcPmm__HE448_UnitDelay = X_SVmcPmm__HE448_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE448_UnitDelay = 0.F;
         }

         
         X_SVmcPmm__HE443_UnitDelay1 = ((X_SVmcPmm__HE448_UnitDelay > cVcVmcPmm_t_RunReqObdDelayHmi)
           && yVcVmcPmm_B_EngRunReqObd) || (yVcVmcPmm_B_EngRunReqObd &&
          X_SVmcPmm__HE443_UnitDelay1);

         
         X_SVmcPmm__HE442_UnitDelay1 = ((sVcScIn_v_VehSpdLgt >= cVcVmcPmm_v_TransRunRqDlyMaxHmi) &&
          yVcVmcPmm_B_EngRunReqTrans) || (yVcVmcPmm_B_EngRunReqTrans &&
          X_SVmcPmm__HE442_UnitDelay1);

         
         if (yVcVmcPmm_B_EngRunReqTrans) {
            
            X_SVmcPmm__HE445_UnitDelay = X_SVmcPmm__HE445_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE445_UnitDelay = 0.F;
         }

         
         xVcVmcPmm_B_HeatUpEOP = (yVcVmcPmm_B_EngRunReqTrans && (SVmcPmm__HE829_Switch &&
          (!(X_SVmcPmm__HE439_UnitDelay1)))) || ((SVmcPmm__HE829_Switch ||
          (!(X_SVmcPmm__HE437_Delay))) && (yVcVmcPmm_B_EngRunReqTrans ||
          (!(X_SVmcPmm__HE438_Delay))) && X_SVmcPmm__HE444_UnitDelay1);

         
         X_SVmcPmm__HE444_UnitDelay1 = xVcVmcPmm_B_HeatUpEOP;

         
         X_SVmcPmm__HE438_Delay = yVcVmcPmm_B_EngRunReqTrans;

         
         X_SVmcPmm__HE437_Delay = SVmcPmm__HE829_Switch;

         
         X_SVmcPmm__HE439_UnitDelay1 = SVmcPmm__HE829_Switch;

         
         yVcVmcPmm_B_RunReqSystemHmi = ((yVcTmStrt_B_EngRunTmLong || yVcCmnEngRunReqCEC_B_ReqLong)
          && yVcVmcPmm_B_EngRunReqTot) || (X_SVmcPmm__HE446_UnitDelay >
          cVcVmcPmm_t_FCAdaptRunReqOnDelayHmi) || (X_SVmcPmm__HE447_UnitDelay >
          cVcVmcPmm_t_RunReqOnDelayHmi) || (X_SVmcPmm__HE449_UnitDelay >
          cVcVmcPmm_t_BrakeRunReqOnDelayHmi) || X_SVmcPmm__HE443_UnitDelay1 ||
          (X_SVmcPmm__HE442_UnitDelay1 || (X_SVmcPmm__HE445_UnitDelay >
          cVcVmcPmm_t_TransRunReqOnDelayHmi)) || xVcVmcPmm_B_HeatUpEOP;

         
         yVcVmcPmm_B_RunReqDriverHmi = xVcVmcPmm_B_EngRunReqDriver || xVcVmcPmm_B_EngRunReqEm;
      #endif

      
      xVcVmcPmm_B_TrailerPresent = yVcTrm_B_TrlrPrsnt ||
       yVcCem_B_EngRunngReqByVehModMgrTrailerPrsnt;
      #if Vc_Pvc_Sw_B_StopStart
         
         if (cVcVmcPmm_B_SsActHood) {
            
            yVcVmcPmm_B_SsActHoodHMI = (sVcCem_D_HoodSts == 1) && (sVcVmm_D_CarModSts1 != 5);
         }
         else {
            
            yVcVmcPmm_B_SsActHoodHMI = 0;
         }

         
         SVmcPmm__HE90_Rel = cVcVmcPmm_Te_AmbHighH <= sVcEc_Te_Amb;

         
         SVmcPmm__HE90_Rel1 = sVcEc_Te_Amb <= cVcVmcPmm_Te_AmbHighL;

         
         xVcVmcPmm_B_AmbTempH = (SVmcPmm__HE90_Rel && (!(SVmcPmm__HE90_Rel1))) ||
          ((!(SVmcPmm__HE90_Rel)) && (!(SVmcPmm__HE90_Rel1)) && X_SVmcPmm__HE90_UnitDelay);

         
         X_SVmcPmm__HE90_UnitDelay = xVcVmcPmm_B_AmbTempH;

         
         SVmcPmm__HE91_Rel = cVcVmcPmm_Te_AmbLowH <= sVcEc_Te_Amb;

         
         SVmcPmm__HE91_Rel1 = sVcEc_Te_Amb <= cVcVmcPmm_Te_AmbLowL;

         
         X_SVmcPmm__HE91_UnitDelay = (SVmcPmm__HE91_Rel && (!(SVmcPmm__HE91_Rel1))) ||
          ((!(SVmcPmm__HE91_Rel)) && (!(SVmcPmm__HE91_Rel1)) && X_SVmcPmm__HE91_UnitDelay);

         
         xVcVmcPmm_B_AmbTempL = !(X_SVmcPmm__HE91_UnitDelay);

         
         if ((sVcEc_Qf_TeAmb == 3) && cVcVmcPmm_B_SsActTemp) {
            
            yVcVmcPmm_B_SsAmbFault = xVcVmcPmm_B_AmbTempH || xVcVmcPmm_B_AmbTempL;
         }
         else {
            
            yVcVmcPmm_B_SsAmbFault = 0;
         }

         
         if (cVcVmcPmm_B_SsActTempStrt) {
            
            SVmcPmm__HE66_Switch = yVcVmcPmm_B_SsAmbFault;
         }
         else {
            
            SVmcPmm__HE66_Switch = yVcVmcPmm_B_SsAmbFault && ((CVmcPmm__HE1_D_IceStatus == 1) ||
             (CVmcPmm__HE1_D_IceStatus == 2));
         }

         
         yVcVmcPmm_B_SsActAmbHMI = SVmcPmm__HE66_Switch && cVcVmcPmm_B_UseSsActTemp;

         
         SVmcPmm__HE92_Rel = cVcVmcPmm_p_AmbH <= sVcEc_p_Amb;

         
         SVmcPmm__HE92_Rel1 = sVcEc_p_Amb <= cVcVmcPmm_p_AmbL;

         
         X_SVmcPmm__HE92_UnitDelay = (SVmcPmm__HE92_Rel && (!(SVmcPmm__HE92_Rel1))) ||
          ((!(SVmcPmm__HE92_Rel)) && (!(SVmcPmm__HE92_Rel1)) && X_SVmcPmm__HE92_UnitDelay);

         
         xVcVmcPmm_B_AmbPresLow = !(X_SVmcPmm__HE92_UnitDelay);

         
         if (cVcVmcPmm_B_SsActAmbPres) {
            
            yVcVmcPmm_B_SsAltitudeFault = xVcVmcPmm_B_AmbPresLow;
         }
         else {
            
            yVcVmcPmm_B_SsAltitudeFault = 0;
         }

         
         X_SVmcPmm__HE93_UnitDelay1 = (SVmcPmm__HE153__HillGradAcc2deg >=
          cVcVmcPmm_Z_SsActTrailerUpHillH) || ((SVmcPmm__HE153__HillGradAcc2deg >
          cVcVmcPmm_Z_SsActTrailerUpHillL) && X_SVmcPmm__HE93_UnitDelay1);

         
         if (cVcVmcPmm_B_SsActTrailer) {
            
            yVcVmcPmm_B_SsActTrailerHMI = X_SVmcPmm__HE93_UnitDelay1 && xVcVmcPmm_B_TrailerPresent;
         }
         else {
            
            yVcVmcPmm_B_SsActTrailerHMI = 0;
         }

         
         if (!(yVcCem_B_BltLockStAtDrvr)) {
            
            X_SVmcPmm__HE96_UnitDelay = X_SVmcPmm__HE96_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE96_UnitDelay = 0.F;
         }

         
         SVmcPmm__HE27___tionalOperator1 = sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATPark;

         
         xVcVmcPmm_B_SsActSeatBeltInhib = (X_SVmcPmm__HE96_UnitDelay > cVcVmcPmm_t_SsActSeatBelt) ||
           ((!(yVcCem_B_BltLockStAtDrvr)) && (!(SVmcPmm__HE27___tionalOperator1)));

         
         if (cVcVmcPmm_B_SsActSeatBeltNoSeq) {
            
            xVcVmcPmm_B_SsActSeatBeltAllow = yVcCem_B_BltLockStAtDrvr;
         }
         else {
            
            xVcVmcPmm_B_SsActSeatBeltAllow = (yVcCem_B_BltLockStAtDrvr &&
             (SVmcPmm__HE27___tionalOperator1 && (!(X_SVmcPmm__HE94_UnitDelay1)))) ||
             ((!(SVmcPmm__HE27___tionalOperator1)) && yVcCem_B_BltLockStAtDrvr);
         }

         
         X_SVmcPmm__HE94_UnitDelay1 = SVmcPmm__HE27___tionalOperator1;

         
         xVcVmcPmm_B_SRSeatBeltAT = xVcVmcPmm_B_SsActSeatBeltInhib ||
          ((!(xVcVmcPmm_B_SsActSeatBeltAllow)) && X_SVmcPmm__HE97_UnitDelay1);

         
         X_SVmcPmm__HE97_UnitDelay1 = xVcVmcPmm_B_SRSeatBeltAT;

         
         if (cVcVmcPmm_B_SsActSeatBelt) {
            
            if (yVcDtcAtr_B_AT && cVcVmcPmm_B_SsActSeatBeltPrkBlock) {
               
               yVcVmcPmm_B_SsActSeatBeltHMI = xVcVmcPmm_B_SRSeatBeltAT;
            }
            else {
               
               yVcVmcPmm_B_SsActSeatBeltHMI = !(yVcCem_B_BltLockStAtDrvr);
            }
         }
         else {
            
            yVcVmcPmm_B_SsActSeatBeltHMI = 0;
         }

         
         if (!(yVcCem_B_BltLockStAtDrvr)) {
            
            SVmcPmm__HE98_Switch = cVcVmcPmm_B_SsActDoorNoBelt;
         }
         else {
            
            SVmcPmm__HE98_Switch = ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATPark) &&
             cVcVmcPmm_B_SsActDoorBeltP) || ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATReverse) &&
             cVcVmcPmm_B_SsActDoorBeltR) || ((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATNeutral) &&
             cVcVmcPmm_B_SsActDoorBeltN) || (((sVcDtcAtr_D_GearLevAT == cVc_D_GearLevATDrive) ||
             (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevAT4th) || (sVcDtcAtr_D_GearLevAT ==
             cVc_D_GearLevAT3rd) || (sVcDtcAtr_D_GearLevAT == cVc_D_GearLevAT2nd)) &&
             cVcVmcPmm_B_SsActDoorBeltD);
         }

         
         xVcVmcPmm_B_SsActDriverLeaving = yVcDtcAtr_B_AT && xVcVmcPmm_B_DrDoorOpen &&
          SVmcPmm__HE98_Switch;

         
         if (cVcVmcPmm_B_SsActDriverLeaving) {
            
            yVcVmcPmm_B_SsActDoorOpenHMI = xVcVmcPmm_B_SsActDriverLeaving;
         }
         else {
            
            yVcVmcPmm_B_SsActDoorOpenHMI = 0;
         }

         
         if (yVcVdm_B_AbsCtrlActv) {
            
            X_SVmcPmm__HE77_UnitDelay = 0.F;
         }
         else {
            
            X_SVmcPmm__HE77_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE77_UnitDelay;
         }

         
         if (cVcVmcPmm_B_SsActAbs) {
            
            SVmcPmm__HE60_Switch = X_SVmcPmm__HE77_UnitDelay <= cVcVmcPmm_t_SsActAbs;
         }
         else {
            
            SVmcPmm__HE60_Switch = 0;
         }

         
         if (sVcVdm_D_EngRunngReqByBrk == 1) {
            
            X_SVmcPmm__HE76_UnitDelay = 0.F;
         }
         else {
            
            X_SVmcPmm__HE76_UnitDelay = ts_VcVmcPmm__HEP7 + X_SVmcPmm__HE76_UnitDelay;
         }

         
         if (cVcVmcPmm_B_SsActBrk) {
            
            SVmcPmm__HE62_Switch = X_SVmcPmm__HE76_UnitDelay <= cVcVmcPmm_t_SsActBrk;
         }
         else {
            
            SVmcPmm__HE62_Switch = 0;
         }

         
         if (sVcDtcAtr_D_TransMode != sVcSpMon_D_PtTrsmModReq) {
            
            X_SVmcPmm__HE78_UnitDelay = X_SVmcPmm__HE78_UnitDelay + ts_VcVmcPmm__HEP7;
         }
         else {
            
            X_SVmcPmm__HE78_UnitDelay = 0.F;
         }

         
         if (cVcVmcPmm_B_SsActRcfSetAlt) {
            
            SVmcPmm__HE73_Switch = yVcEc_B_SsRcfSetAlt;
         }
         else {
            
            SVmcPmm__HE73_Switch = 0;
         }

         
         if (cVcVmcPmm_B_SsActRcfSet) {
            
            SVmcPmm__HE74_Switch = yVcEc_B_SsRcfSet;
         }
         else {
            
            SVmcPmm__HE74_Switch = 0;
         }

         
         SVmcPmm__HE27_LogicalOperator25 = (sVcDeDmm_D_DrvMode == cVcVmcPmm_D_SsActDrMd1) ||
          (sVcDeDmm_D_DrvMode == cVcVmcPmm_D_SsActDrMd2) || (sVcDeDmm_D_DrvMode ==
          cVcVmcPmm_D_SsActDrMd3);

         
         if (cVcVmcPmm_B_SsActDrMdInv) {
            
            yVcVmcPmm_B_SsActDrMdHMI = !(SVmcPmm__HE27_LogicalOperator25);
         }
         else {
            
            yVcVmcPmm_B_SsActDrMdHMI = SVmcPmm__HE27_LogicalOperator25;
         }

         
         if (cVcVmcPmm_B_UseSsActive) {
            
            
            #if Vc_Pvc_Sw_B_StopStart
               Bool SVmcPmm__HE55_Switch;
            #endif

            

            
            #if Vc_Pvc_Sw_B_StopStart
               Bool SVmcPmm__HE56_Switch;
            #endif

            

            
            #if Vc_Pvc_Sw_B_StopStart
               Bool SVmcPmm__HE57_Switch;
            #endif

            

            
            #if Vc_Pvc_Sw_B_StopStart
               Bool SVmcPmm__HE59_Switch;
            #endif

            

            
            #if Vc_Pvc_Sw_B_StopStart
               Bool SVmcPmm__HE61_Switch;
            #endif

            

            
            #if Vc_Pvc_Sw_B_StopStart
               Bool SVmcPmm__HE70_Switch;
            #endif

            

            
            #if Vc_Pvc_Sw_B_StopStart
               Bool SVmcPmm__HE71_Switch;
            #endif

            

            
            if (cVcVmcPmm_B_SsActGpSs) {
               
               SVmcPmm__HE56_Switch = sVcGp_D_StopStart != 2;
            }
            else {
               
               SVmcPmm__HE56_Switch = 0;
            }

            
            if (cVcVmcPmm_B_SsActNtrl) {
               
               SVmcPmm__HE57_Switch = (!(yVcScDep_B_NeutralMTValid)) && (!(yVcDtcAtr_B_AT));
            }
            else {
               
               SVmcPmm__HE57_Switch = 0;
            }

            
            if (cVcVmcPmm_B_SsActEcoMde) {
               
               SVmcPmm__HE61_Switch = !(yVcDeDmm_B_EcoModeSs);
            }
            else {
               
               SVmcPmm__HE61_Switch = 0;
            }

            
            if (cVcVmcPmm_B_SsActTransFailure) {
               
               SVmcPmm__HE55_Switch = yVcTcm_B_TrsmNeutFailr && yVcDtcAtr_B_AT;
            }
            else {
               
               SVmcPmm__HE55_Switch = 0;
            }

            
            if (cVcVmcPmm_B_SsActTCMNodeAlive) {
               
               SVmcPmm__HE70_Switch = yVcDtcAtr_B_AT && (!(yVcEc_B_TCMNodeAlive));
            }
            else {
               
               SVmcPmm__HE70_Switch = 0;
            }

            
            if (cVcVmcPmm_B_SsActTCMModeFail) {
               
               SVmcPmm__HE71_Switch = yVcDtcAtr_B_AT && (X_SVmcPmm__HE78_UnitDelay >
                cVcVmcPmm_t_SsActTcmModeFail);
            }
            else {
               
               SVmcPmm__HE71_Switch = 0;
            }

            
            if (cVcVmcPmm_B_SsActTipSport) {
               
               SVmcPmm__HE59_Switch = yVcDeDmm_B_TipSport;
            }
            else {
               
               SVmcPmm__HE59_Switch = 0;
            }

            
            yVcVmcPmm_B_SsActive = (!(SVmcPmm__HE60_Switch)) && (!(SVmcPmm__HE62_Switch)) &&
             (!(SVmcPmm__HE56_Switch)) && (!(SVmcPmm__HE57_Switch)) && (!(SVmcPmm__HE61_Switch)) &&
             (!(yVcVmcPmm_B_SsActDoorOpenHMI)) && (!(yVcVmcPmm_B_SsActSeatBeltHMI)) &&
             (!(yVcVmcPmm_B_SsActAmbHMI)) && (!(yVcVmcPmm_B_SsActTrailerHMI)) &&
             (!(SVmcPmm__HE55_Switch)) && (!(SVmcPmm__HE70_Switch)) && (!(SVmcPmm__HE71_Switch)) &&
             (!(SVmcPmm__HE73_Switch)) && (!(SVmcPmm__HE74_Switch)) &&
             (!(yVcVmcPmm_B_SsAltitudeFault)) && (!(SVmcPmm__HE59_Switch)) &&
             (!(yVcVmcPmm_B_SsActHoodHMI)) && (!(yVcVmcPmm_B_SsActDrMdHMI));
         }
         else {
            
            yVcVmcPmm_B_SsActive = 1;
         }

         
         yVcVmcPmm_B_SsRcfAct = (!(yVcVmcPmm_B_SsActive)) && (SVmcPmm__HE73_Switch ||
          SVmcPmm__HE74_Switch);

         
         yVcVmcPmm_B_SsActAbsHMI = SVmcPmm__HE60_Switch || SVmcPmm__HE62_Switch;
      #endif
   }
   else {
      
      SVmcPmm__HE156_RSWE = 0;

      
      SVmcPmm__HE157_RSWE = 0;
   }
}
#include "CVC_CODE_END.h"


#include "CVC_CODE_START.h"
void INIT_SVmcPmm_____FuelCutRequest(void)
{
   
   X_SVmcPmm__HE159_UnitDelay1 = 0;

   
   X_SVmcPmm__HE160_UnitDelay1 = 0;

   
   X_SVmcPmm__HE161_UnitDelay = 0.F;
}
#include "CVC_CODE_END.h"


#include "CVC_CODE_START.h"
void INIT_SVmcPmm____verLeaveVehicle(void)
{
   
   X_SVmcPmm__HE163_UnitDelay = 0.F;

   
   X_SVmcPmm__HE164_UnitDelay = 0.F;

   
   X_SVmcPmm__HE165_UnitDelay = 0.F;
}
#include "CVC_CODE_END.h"


#endif 


