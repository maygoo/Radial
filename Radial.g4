// The grammar for Radial written for use with ANTLR 4

grammar Radial;

// parser rules
program
    : statement_func*
    ;

statement_func
    : func_def
    | statement
    ;

statement
    : expression END
    | var_def END
    | IF LPAREN expression RPAREN LBRACE statement* RBRACE
    ;

var_def
    : TYPE LABEL
    | TYPE LABEL () expression
    ;

func_def
    : TYPE LABEL LPAREN LABEL? RPAREN LBRACE statement* RBRACE
    ;

// no need to unravel expressions for operator precedence (antlr4 book chp 14)
expression
    : LABEL LPAREN expression* RPAREN               # Call
    | expression op=(MUL | DIV | MOD) expression    # Mul
    | expression op=(ADD | SUB) expression          # Add
    | literal                                       # Lit
    | LABEL                                         # Var
    ;

literal
    : INT   # Int
    | DEC   # Dec
    | STR   # Str
    ;

// lexer rules
INT: [0-9]+ ;
DEC: [0-9]+ '.' [0-9]*;
STR: ('\'' .? '\'') | ('"' .? '"') ;
LABEL: [a-zA-Z_]+ ;

TYPE: ('int' | 'float' | 'str' | 'list' | 'void') ;

ADD: '+' ;
SUB: '-' ;
MUL: '*' ;
DIV: '/' ;
MOD: '%' ;
END: ';' ;

LPAREN: '(' ;
RPAREN: ')' ;
LBRACE: '{' ;
RBRACE: '}' ;

EQUALS: '=' ;

IF: 'if' ;

WS: [ \t\r\n]+ -> skip ;
LINE_COMMENT: '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;
//TODO try moving comments to separate channel to preserve them in the ir