grammar SeawolfGrammar;

prog:  code_block EOF?  ;

code_block: stat*;

stat:   PRINT LPAREN expr RPAREN SEMICOL            # printExpr
    |   (ID | listid) ASSIGN expr SEMICOL           # assign
    |   if_statement                                # ifstat
    |   while_statement                             # whilestat
    |   braced_statement                            # blockstat
    |   NEWLINE                                     # blank
    ;

while_statement
 : WHILE  condition_block
 ;

if_statement
 : IF condition_block (ELSE IF condition_block)* (ELSE cond_stat_block)?
 ;

 condition_block
 : LPAREN expr RPAREN cond_stat_block
 ;

 cond_stat_block
 : braced_statement
 | stat
 ;

braced_statement
 : LBRACE code_block RBRACE
 ;


expr:   SUB INT                                        # negint
    |   SUB REAL                                       # negreal
    |   INT                                            # int
    |   REAL                                           # real
    |   STRING                                         # string
    |   ID                                             # id
    |   listexpr                                       # list
    |   LPAREN expr RPAREN                         # parens
    |   expr SQLPAREN expr SQRPAREN                              # Indexing
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

listid : ID list_index+;
list_index : (SQLPAREN (ID | INT ) SQRPAREN);
listexpr: SQLPAREN list_  SQRPAREN;
list_ :  expr COMMA list_
          |  expr | empty_list
          ;
empty_list: SQLPAREN WS SQRPAREN;

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
MOD :   '%' ;
EXP :   '**' ;
FLRDIV:  '//' ;
ADD :   '+' ;
SUB :   '-' ;
COMMA : ',';
SEMICOL: ';';
ASSIGN: '=';

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

LBRACE : '{';
RBRACE : '}';
LPAREN : '(';
RPAREN : ')';
SQLPAREN : '[';
SQRPAREN : ']';
PRINT : 'print';
IF : 'if';
ELSE : 'else';
WHILE : 'while';
ID  :   [a-zA-Z][A-Za-z0-9_]* ;      // match identifiers

INT :   [0-9]+ ;         // match integers
REAL:   INT ( '.' (INT)? )?  ; // real numbers
fragment STRING_ESCAPE_SEQ
 : '\\' .
 ;
STRING: '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n"] )* '"';
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
