// -*- antlr -*-
grammar RegisterDescription;
// Grammar part
registerdescription : headerlines registerlines ;
// Header description
headerlines    : (commentline | emptyline)+;
// Register set description
commentline    : COMMENT ;
emptyline      : NEWLINE;
registerlines  : (commentline | registerline | emptyline)+;
registerline   : extension regbankvec regbank registerlist registerwidth registerfunctionlist NEWLINE?;
registerlist : registerprefix ;
registerprefix :  PREFIX ('-' INT)?;
//registernumber : INT ('-' INT)? ;
registerfunctionlist : registerfunction | registerfunctionwn;
registerfunction : FUNCNAME;
registerfunctionwn : REGWN ('-' INT)?;
regbankvec    : ('v')?;
regbank       : ('i' | 'f');
registerwidth : INT;
extension     : NAME;

// Lexer part
WS            : [ \t]+   -> skip ;
COMMENT       : '#' .*? NEWLINE  -> skip;
INT           : [0-9]+ ;
FUNCNAME      : ('Z' | 'RA'| 'FP' | 'SP' | 'GP' | 'TP' | 'X') ;
REGWN         : ('T' | 'I' | 'O') INT;
NEWLINE       : '\r'? '\n' ;
PREFIX        : '$' [A-Za-z]* INT;
NAME          : [A-Za-z] [A-Za-z0-9_.]* ;
