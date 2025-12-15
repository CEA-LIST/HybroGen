/*****************************************************************************
 *                                CEA - LIST                                 *
 *  Reproduction and Communication of this document is strictly prohibited   *
 *        unless specifically authorized in writing by CEA - LIST.           *
 * ------------------------------------------------------------------------- *
 *                            LIST / DCSIN / LFIM                            *
 * ------------------------------------------------------------------------- *
 * @file    csram_isa.h                                                      *
 * @date    January 2021                                                     *
 * @author  Roman Gauchi <roman.gauchi@cea.fr>                               *
 * @version 2.0                                                              *
 ****************************************************************************/

#ifndef __CSRAM_ISA_H__
#define __CSRAM_ISA_H__

// CSRAM Instruction Set Architecture (ISA)
#define CSRAM_ISA_OPCODE_START                  50
#define CSRAM_ISA_OPCODE_SIZE                   8
#define CSRAM_ISA_OPCODE_MASK                   0xFF
#define CSRAM_ISA_NMC_ENABLE_START              58
#define CSRAM_ISA_NMC_ENABLE_SIZE               6
#define CSRAM_ISA_NMC_ENABLE_MASK               0x3F
#define CSRAM_ISA_NMC_ENABLE_VALUE              0b100000
#define CSRAM_ISA_TYPE_START                    53
#define CSRAM_ISA_TYPE_SIZE                     3
#define CSRAM_ISA_TYPE_MASK                     0x7
#define CSRAM_ISA_TYPE_MI_VALUE                 0b000
#define CSRAM_ISA_TYPE_MR_VALUE                 0b011
#define CSRAM_ISA_TYPE_MU_VALUE                 0b010
#define CSRAM_ISA_TYPE_LI_VALUE                 0b100
#define CSRAM_ISA_TYPE_LR_VALUE                 0b101
#define CSRAM_ISA_TYPE_AI_VALUE                 0b110
#define CSRAM_ISA_TYPE_AR_VALUE                 0b111

// Format types
// R-type
#define CSRAM_ISA_RTYPE_DEST_START              34
#define CSRAM_ISA_RTYPE_DEST_SIZE               16
#define CSRAM_ISA_RTYPE_DEST_MASK               0xFFFF
#define CSRAM_ISA_RTYPE_SRC2_START              16
#define CSRAM_ISA_RTYPE_SRC2_SIZE               16
#define CSRAM_ISA_RTYPE_SRC2_MASK               0xFFFF
#define CSRAM_ISA_RTYPE_SRC1_START              0
#define CSRAM_ISA_RTYPE_SRC1_SIZE               16
#define CSRAM_ISA_RTYPE_SRC1_MASK               0xFFFF
// I-type
#define CSRAM_ISA_ITYPE_DEST_START              34
#define CSRAM_ISA_ITYPE_DEST_SIZE               16
#define CSRAM_ISA_ITYPE_DEST_MASK               0xFFFF
#define CSRAM_ISA_ITYPE_IMM_START               16
#define CSRAM_ISA_ITYPE_IMM_SIZE                16
#define CSRAM_ISA_ITYPE_IMM_MASK                0xFFFF
#define CSRAM_ISA_ITYPE_SRC1_START              0
#define CSRAM_ISA_ITYPE_SRC1_SIZE               16
#define CSRAM_ISA_ITYPE_SRC1_MASK               0xFFFF
// U-type
#define CSRAM_ISA_UTYPE_DEST_START              34
#define CSRAM_ISA_UTYPE_DEST_SIZE               16
#define CSRAM_ISA_UTYPE_DEST_MASK               0xFFFF
#define CSRAM_ISA_UTYPE_IMM_START               0
#define CSRAM_ISA_UTYPE_IMM_SIZE                32
#define CSRAM_ISA_UTYPE_IMM_MASK                0xFFFFFFFF


#endif /* __CSRAM_ISA_H__ */
