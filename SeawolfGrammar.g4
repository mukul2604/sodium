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
    |   expr op = IN expr                              # Inoperationstring
    |   expr op = (LS | GT | LE | GE | EQL | NE) expr  # Relational
    |   NOT expr                                       # LogicalNOT
    |   expr op = (AND | OR) expr                      # Logical
    |   INT                                            # int
    |   REAL                                           # real
    |   STRING                                         # string
    |   ID                                             # id
    |   '(' expr ')'                                   # parens
    |   expr '[' expr ']'                              # Stringindexing
    |   listexpr                                       # List
    ;

listexpr: '[' LIST ']';


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

IN : 'in';
// Operands

ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
REAL:   INT ( '.' (INT)? )?  ; // real numbers
fragment STRING_ESCAPE_SEQ
 : '\\' .
 ;
STRING: '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n"] )* '"';
LISTELEM : (STRING | REAL | STRING);
LIST:  LISTELEM (',' LISTELEM)* ;
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
