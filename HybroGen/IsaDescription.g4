// -*- antlr -*-
grammar IsaDescription;
// Grammar part
isadescription : headerlines isalines;
// Header description
headerlines    : (commentline | archline | emptyline)+ ;
archline       : 'ARCH' NAME (INT)+ NEWLINE            ;
// Instruction set description
isalines       : (commentline | emptyline | isaline)*  ;
commentline    : COMMENT                               ;
isaline        : bindescr '|' asmdescr NEWLINE         ;
emptyline      : NEWLINE                               ;
bindescr       : binelem +                             ;
binelem        : binvalue | regbin | expbin            ;
binvalue       : INT                                   ;
regbin         : NAME    '[' INT (SEMICOL INT)? ']'    ;
expbin         : CINLINE '[' INT (SEMICOL INT)? ']'    ;
asmdescr       : extname arith INT INT semname opname (reglist)? ;
extname		   : NAME ;
arith          : ('i'|'u'|'f') ;
opname         : NAME;
regName        : NAME ;
semname        : NAME;
reglist        : regName (regName)*;

// Lexer part
WS            : [ \t]+   -> skip ;
COMMENT       : '#' .*? NEWLINE ;
INT           : [0-9]+ ;
NAME          : [A-Za-z] [A-Za-z0-9_.]* ;
NEWLINE       : '\r'? '\n' ;
SEMICOL       : ':';
CINLINE       :  '{' ~[}]+ '}';
