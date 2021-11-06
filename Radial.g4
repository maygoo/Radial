// The grammar for Radial written for use with ANTLR 4

grammar Radial;

program
    : expression
    ;

expression
    : expression '+' expression     # Add
    | NUMBER                        # Number
    ;

NUMBER: [0-9]+ ;
WS: [ \t\r\n]+ -> skip ;
// test grammar accepts positive integers added together