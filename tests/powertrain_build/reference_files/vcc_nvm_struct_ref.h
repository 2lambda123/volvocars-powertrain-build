/*
 *  vcc_nvm_struct.h - struct for NVM signals
 */

#ifndef VCC_NVM_STRUCT_H
#define VCC_NVM_STRUCT_H

#include "tl_basetypes.h"
#include "CVC_NVM_START.h"
struct NVM_LIST_8 {
   Bool    _sVcAesMo_rt_NvmMafLrngLd1Ne1;
   UInt8 unused[55];
}; /* 1 bytes used of 56 */
#include "CVC_NVM_END.h"

#include "CVC_NVM_START.h"
struct NVM_LIST_16 {
   UInt16 unused[240];
}; /* 0 bytes used of 480 */
#include "CVC_NVM_END.h"

#include "CVC_NVM_START.h"
struct NVM_LIST_32 {
   UInt32  _sVcAcCtrl_t_CmprRunTiNVM;
   Float32 _sVcAesHw_X_VntAdpnOffs;
   Float32 _sVcAesMo_Ar_ArrayTest[4][2];
   Float32 _sVcAesMo_Ar_NvmThrAdpn;
   UInt32 unused[964];
}; /* 44 bytes used of 3900 */
#include "CVC_NVM_END.h"

#include "CVC_NVM_P_START.h"
struct NVM_LIST_8_PER {
   UInt8 unused[56];
}; /* 0 bytes used of 56 */
#include "CVC_NVM_P_END.h"

#include "CVC_NVM_P_START.h"
struct NVM_LIST_16_PER {
   UInt16 unused[240];
}; /* 0 bytes used of 480 */
#include "CVC_NVM_P_END.h"

#include "CVC_NVM_P_START.h"
struct NVM_LIST_32_PER {
   UInt32  _sVcAcCtrl_t_Test1;
   UInt32 unused[189];
}; /* 4 bytes used of 760 */
#include "CVC_NVM_P_END.h"

#include "PREDECL_START.h"
extern struct NVM_LIST_8 nvm_list_8;
extern struct NVM_LIST_16 nvm_list_16;
extern struct NVM_LIST_32 nvm_list_32;
extern struct NVM_LIST_8_PER nvm_list_8_per;
extern struct NVM_LIST_16_PER nvm_list_16_per;
extern struct NVM_LIST_32_PER nvm_list_32_per;
#include "PREDECL_END.h"


#define sVcAesMo_rt_NvmMafLrngLd1Ne1             nvm_list_8._sVcAesMo_rt_NvmMafLrngLd1Ne1
#define sVcAcCtrl_t_CmprRunTiNVM                 nvm_list_32._sVcAcCtrl_t_CmprRunTiNVM
#define sVcAesHw_X_VntAdpnOffs                   nvm_list_32._sVcAesHw_X_VntAdpnOffs
#define sVcAesMo_Ar_ArrayTest                    nvm_list_32._sVcAesMo_Ar_ArrayTest
#define sVcAesMo_Ar_NvmThrAdpn                   nvm_list_32._sVcAesMo_Ar_NvmThrAdpn
#define sVcAcCtrl_t_Test1                        nvm_list_32_per._sVcAcCtrl_t_Test1

#endif /* VCC_NVM_STRUCT_H */
