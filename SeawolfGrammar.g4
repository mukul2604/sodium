grammar SeawolfGrammar;

prog:   statmt+ ;

statmt:   expr NEWLINE              # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   expr op = (MUL | DIV) expr                     # MulDiv
    |   expr op = MOD expr                             # Modulo
    |   expr op = EXP expr                             # Exponential
    |   expr op = (ADD | SUB) expr                     # AddSub
    |   expr op = (LS | GT | LE | GE | EQL | NE) expr  # Relational
    |   NOT expr                                       # LogicalNOT
    |   expr op = (AND | OR) expr                      # Logical
    |   INT                         # int
    |   ID                          # id
    |   '(' expr ')'                # parens
    ;


MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
MOD :   '%' ;
EXP :   '**' ;
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
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
