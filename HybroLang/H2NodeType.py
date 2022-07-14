from enum import Enum

class H2NodeType(Enum):
    """Type definition for H2Node
    (python disallow extending Enum for classes with other variable than the enumeration)
    """
    CONST    =  1
    VARIABLE =  2
    OPERATOR =  3
    R        =  4
    W        =  5
    RTN      =  6
    LOOP     =  7
    LABEL    =  8
    BA       =  9
    BLE      = 10
    BGE      = 11
    BGT      = 12
    BLT      = 13
    BEQ      = 14
    BNE      = 15
    CALLBACK = 16
    CMP      = 17
    CMPNE    = 18
    CMPEQ    = 19
    CMPLT    = 20
    CMPGE    = 21
    CMPGT    = 22
    CMPLE    = 23
    BNEZ     = 24
    BEQZ     = 25
    MVIF     = 26
    MVFI     = 27
