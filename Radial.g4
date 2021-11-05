// The grammar for Radial written for use with ANTLR 4

grammar Radial;

program
    : expression
    ;

expression
    : expression '+' expression 
    | NUMBER
    ;

NUMBER: [0-9]+ ;

// test grammar accepts positive integers added together