grammar LabeledExpr; 

prog:   statmt+ ;

statmt:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   INT                         # int
    |   ID                          # id
    |   '(' expr ')'                # parens
    |   mylist                      # myList
    ;

mylist
  : STARTL elems? ENDL              
  ;
elems
  : elem (SEP elem)*
  ;

elem: INT;

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
// List symbols
STARTL : '[';
ENDL : ']';
SEP : ',';
WS  :   [ \t]+ -> skip ; // toss out whitespace
