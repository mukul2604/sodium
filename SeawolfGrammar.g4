grammar SeawolfGrammar;

prog:   statmt+ ;

statmt:   expr NEWLINE              # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   SUB INT                                        # negint
    |   SUB REAL                                       # negreal
    |   expr op = (MUL | DIV) expr                     # MulDiv
    |   expr op = MOD expr                             # Modulo
    |   <assoc=right> expr op = EXP expr               # Exponential
    |   expr op = FLRDIV expr                          # FloorDiv
    |   expr op = (ADD | SUB) expr                     # AddSub
    |   expr op = (LS | GT | LE | GE | EQL | NE) expr  # Relational
    |   NOT expr                                       # LogicalNOT
    |   expr op = (AND | OR) expr                      # Logical
    |   INT                                            # int
    |   REAL                                           # real
    |   STRING                   # string
    |   ID                       # id
    |   '(' expr ')'             # parens
    ;


MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
MOD :   '%' ;
EXP :   '**' ;
FLRDIV:  '//' ;
ADD :   '+' ;
SUB :   '-' ;

// Relational Operators
LS  :   '<' ;
GT  :   '>' ;
LE  :   '<=' ;
GE  :   '>=' ;
EQL :   '==' ;
NE  :   '<>' ;

// Logical Operators
NOT : 'not' ;
AND : 'and' ;
OR  : 'or' ;
// Operands

ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
REAL:   INT ( '.' (INT)? )?  ; // real numbers
STRING: '\'' [ a-zA-Z0-9\t]* '\''  | '\"' [ a-zA-Z0-9\t]* '\"' ;
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
