/*****************************************************************************
 *                                CEA - LIST                                 *
 *  Reproduction and Communication of this document is strictly prohibited   *
 *        unless specifically authorized in writing by CEA - LIST.           *
 * ------------------------------------------------------------------------- *
 *                            LIST / DCSIN / LFIM                            *
 * ------------------------------------------------------------------------- *
 * @file    csram_opcodes.h                                                  *
 * @date    January 2021                                                     *
 * @author  Roman Gauchi <roman.gauchi@cea.fr>                               *
 * @version 2.0                                                              *
 ****************************************************************************/

#ifndef __CSRAM_OPCODES_H__
#define __CSRAM_OPCODES_H__

// CSRAM Opcodes
// 8-bit wide instructions
#define CSRAM_OPC_COPYEQ8                       0x18
#define CSRAM_OPC_COPYGEQ8                      0x19
#define CSRAM_OPC_COPYGT8                       0x1A
#define CSRAM_OPC_COPYLEQ8                      0x1B
#define CSRAM_OPC_COPYLT8                       0x1C
#define CSRAM_OPC_COPYNEQ8                      0x1D
#define CSRAM_OPC_BCAST8                        0x10
#define CSRAM_OPC_SLLI8                         0x20
#define CSRAM_OPC_SRLI8                         0x21
#define CSRAM_OPC_ADDS8                         0x48
#define CSRAM_OPC_ADD8                          0x38
#define CSRAM_OPC_SUB8                          0x39
#define CSRAM_OPC_SUBS8                         0x49
#define CSRAM_OPC_CMP8                          0x3A
#define CSRAM_OPC_MUL8                          0x3B
#define CSRAM_OPC_FMAC8                         0x3C
// 16-bit wide instructions
#define CSRAM_OPC_COPYEQ16                      0x58
#define CSRAM_OPC_COPYGEQ16                     0x59
#define CSRAM_OPC_COPYGT16                      0x5A
#define CSRAM_OPC_COPYLEQ16                     0x5B
#define CSRAM_OPC_COPYLT16                      0x5C
#define CSRAM_OPC_COPYNEQ16                     0x5D
#define CSRAM_OPC_BCAST16                       0x50
#define CSRAM_OPC_SLLI16                        0x60
#define CSRAM_OPC_SRLI16                        0x61
#define CSRAM_OPC_ADDS16                        0x88
#define CSRAM_OPC_ADD16                         0x78
#define CSRAM_OPC_SUB16                         0x79
#define CSRAM_OPC_SUBS16                        0x89
#define CSRAM_OPC_CMP16                         0x7A
#define CSRAM_OPC_MUL16                         0x7B
#define CSRAM_OPC_FMAC16                        0x7C
// 32-bit wide instructions
#define CSRAM_OPC_HSWAP32                       0x81
#define CSRAM_OPC_COPYEQ32                      0x98
#define CSRAM_OPC_COPYGEQ32                     0x99
#define CSRAM_OPC_COPYGT32                      0x9A
#define CSRAM_OPC_COPYLEQ32                     0x9B
#define CSRAM_OPC_COPYLT32                      0x9C
#define CSRAM_OPC_COPYNEQ32                     0x9D
#define CSRAM_OPC_BCAST32                       0x90
#define CSRAM_OPC_SLLI32                        0xA0
#define CSRAM_OPC_SRLI32                        0xA1
#define CSRAM_OPC_ADDS32                        0xC8
#define CSRAM_OPC_ADD32                         0xB8
#define CSRAM_OPC_SUB32                         0xB9
#define CSRAM_OPC_SUBS32                        0xC9
#define CSRAM_OPC_CMP32                         0xBA
#define CSRAM_OPC_MUL32                         0xBB
#define CSRAM_OPC_FMAC32                        0xBC
// 64-bit wide instructions
#define CSRAM_OPC_HSWAP64                       0xC1
// Line wide instructions
#define CSRAM_OPC_COPY                          0xC0
#define CSRAM_OPC_NOT                           0xE2
#define CSRAM_OPC_REDOR                         0xE3
#define CSRAM_OPC_AND                           0xE8
#define CSRAM_OPC_OR                            0xE9
#define CSRAM_OPC_XOR                           0xEA
#define CSRAM_OPC_NAND                          0xEB
#define CSRAM_OPC_NOR                           0xEC
#define CSRAM_OPC_XNOR                          0xED

#endif /* __CSRAM_OPCODES_H__ */
