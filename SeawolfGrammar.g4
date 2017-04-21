grammar SeawolfGrammar;

prog:   statmt+ ;

statmt:   expr NEWLINE              # printExpr
    |   ID '=' expr ';' NEWLINE     # assign
    |   NEWLINE                     # blank
    ;

expr:   SUB INT                                        # negint
    |   SUB REAL                                       # negreal
    |   INT                                            # int
    |   REAL                                           # real
    |   STRING                                         # string
    |   ID                                             # id
    |   listexpr                                       # list
    |   '(' expr ')'                                   # parens
    |   expr '[' expr ']'                              # Indexing
    |   expr op = (MUL | DIV) expr                     # MulDiv
    |   expr op = MOD expr                             # Modulo
    |   <assoc=right> expr op = EXP expr               # Exponential
    |   expr op = FLRDIV expr                          # FloorDiv
    |   expr op = (ADD | SUB) expr                     # AddSub
    |   expr op = IN expr                              # Inoperation
    |   expr op = (LS | GT | LE | GE | EQL | NE) expr  # Relational
    |   NOT expr                                       # LogicalNOT
    |   expr op = (AND | OR) expr                      # Logical
    ;

listexpr: '[' list_ ']';
list_ :  expr ',' list_
          |  expr | empty_list
          ;
empty_list: '[' WS ']';

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
MOD :   '%' ;
EXP :   '**' ;
FLRDIV:  '//' ;
ADD :   '+' ;
SUB :   '-' ;
COMMA : ',';

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

ID  :   [a-zA-Z][A-Za-z0-9_]* ;      // match identifiers
INT :   [0-9]+ ;         // match integers
REAL:   INT ( '.' (INT)? )?  ; // real numbers
fragment STRING_ESCAPE_SEQ
 : '\\' .
 ;
STRING: '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n"] )* '"';
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
