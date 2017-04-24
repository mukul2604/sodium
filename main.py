# Name: Mukul Sharma  ID:110900654

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from SeawolfGrammarLexer import SeawolfGrammarLexer
from SeawolfGrammarParser import SeawolfGrammarParser
from CustomVisitor import CustomVisitor
from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def __init__(self):
        super(MyErrorListener, self).__init__()
        self.err = {}

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if line in self.err:
            return
        print("SYNTAX ERROR")
        exit(-1)

    def get_error(self):
        return self.err


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1].strip())
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = SeawolfGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SeawolfGrammarParser(token_stream)
    errorListener = MyErrorListener()
    parser._listeners = [errorListener]
    tree = parser.prog()
    visitor = CustomVisitor()
    visitor.visit(tree)

    # errors = errorListener.get_error()
    # for x in errors.values():
    #     print(x)
