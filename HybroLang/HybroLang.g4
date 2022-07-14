// -*- antlr -*-
grammar HybroLang;
// Grammar for HybroLang

// Grammar part
compilationunit : ( function ) +								;
function		: fndcl fnbody									;
fndcl		 	: datatype Name fnprototype						;
fnprototype 	: '(' paramdcllist ')'							;
fnbody			: '{' (localvardef)* actionlist returnexpr? '}'	;
paramdcllist    : vardcl ( ',' vardcl)*							;
localvardef		: vardcllist ';'								;
vardcllist		: vardcl ( ',' Name)*							;
vardcl			: datatype Name             					;
actionlist		: (action)* 			     					;
condexpr        : varorvalue condOperator varorvalue    		;
action			:  affectexpr ';'
			    | 'for' '(' affectexpr ';' condexpr ';' affectexpr ')' '{' actionlist '}';
returnexpr		: 'return' unaryexpr ';'         				;
affectexpr      : Name '=' unaryexpr
                | Name '[' unaryexpr ']' '=' unaryexpr			;
unaryexpr 		: unaryexpr op=('*'|'/')   unaryexpr
    			| unaryexpr op=('+'|'-')   unaryexpr
    			| unaryexpr op=('<<'|'>>') unaryexpr
    			| unaryexpr op=('&&'|'||') unaryexpr
                | varorvalue                       				;
varorvalue      : Name  '[' unaryexpr ']'           # varorvalueArray
    			| constvalue                        # varorvalueConst
                | Name 					    		# varorvalueVar		;
datatype        : typebase wordlen=intconstvalue vectorlen=intconstvalue  ;
intconstvalue   : IntegerConstant | constinline				;
constvalue		: IntegerConstant | DecimalFloatingConstant | constinline;
constinline     : INLINE;
// Arithmetics int and variant : integer, unsigned integer, saturated int,
// float and variant : floating point, complex
// other : ipv4 & v6
typebase 		: ('int' | 'uint' | 'sint' | 'suint' | 'flt' | 'cpl' | 'pix' | 'ipv4' | 'ipv6') '[]'?;

// Fragement parts
// fragment
// https://github.com/antlr/grammars-v4/blob/master/c/C.g4
		 DecimalFloatingConstant 	:  FractionalConstant ExponentPart? FloatingSuffix? ;
fragment ExponentPart 			    :   'e' Sign? DigitSequence
								    |   'E' Sign? DigitSequence    	;
fragment FloatingSuffix             :   'f' | 'l' | 'F' | 'L'   	;

fragment FractionalConstant    		:   DigitSequence? '.' DigitSequence
									|   DigitSequence '.'			;
		 IntegerConstant    		:   DigitSequence 			;
		 DecimalConstant    		:   NonzeroDigit Digit*    		;
fragment DigitSequence				:   Digit+    					;
fragment Digit    					:   [0-9]   					;
fragment NonzeroDigit   			:   [1-9]   					;
fragment Sign    					:   '+' | '-'    				;

// Lexer part
condOperator				: ('==' | '!=' | '<'| '>'| '<=' | '>=')	;
Name          				: [A-Za-z] [A-Za-z0-9_]* 				;
INLINE 						: '#(' ~[)]+ ')'						;
// Skipped text
WhiteSpace		            		: [ \t]+ -> skip 			;
LineComment							: '//' .*? NewLine  -> skip	;
NewLine								: '\r'? '\n'  -> skip		;
