/*
 *  vcc_nvm_struct.h - struct for NVM signals
 */

#ifndef VCC_NVM_STRUCT_H
#define VCC_NVM_STRUCT_H

#include "tl_basetypes.h"
#include "CVC_NVM_START.h"
struct NVM_LIST_CRITICAL1 {
   UInt32  _sVcTest_t_UInt32;
   Int16   _sVcTest_t_Int16;
   UInt16 unused[53];
}; /* 6 bytes used of 112 */
#include "CVC_NVM_END.h"

#include "CVC_NVM_START.h"
struct NVM_LIST_32 {
   UInt32 unused[56];
}; /* 0 bytes used of 224 */
#include "CVC_NVM_END.h"

#include "CVC_NVM_START.h"
struct NVM_LIST_16 {
   UInt16 unused[56];
}; /* 0 bytes used of 112 */
#include "CVC_NVM_END.h"

#include "CVC_NVM_START.h"
struct NVM_LIST_8 {
   UInt8 unused[56];
}; /* 0 bytes used of 56 */
#include "CVC_NVM_END.h"

#include "PREDECL_START.h"
extern struct NVM_LIST_CRITICAL1 nvm_list_critical1;
extern struct NVM_LIST_32 nvm_list_32;
extern struct NVM_LIST_16 nvm_list_16;
extern struct NVM_LIST_8 nvm_list_8;
#include "PREDECL_END.h"


#define sVcTest_t_UInt32                         nvm_list_critical1._sVcTest_t_UInt32
#define sVcTest_t_Int16                          nvm_list_critical1._sVcTest_t_Int16

#endif /* VCC_NVM_STRUCT_H */
