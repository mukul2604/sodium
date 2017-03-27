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
        self.err = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # self.err.append([msg,e])
        self.err.append('SYNTAX ERROR' + ' Line:' + str(line) + ' Col:' + str(column))

    def getError(self):
        return self.err

#     def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
#         raise Exception("Oh2 no!!")
#
#     def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
#         raise Exception("Oh3 no!!")
#
#     def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
#         raise Exception("Oh4 no!!")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1].strip())
    else:
        input_stream = InputStream(sys.stdin.readline().strip())

    lexer = SeawolfGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SeawolfGrammarParser(token_stream)
    errorListener = MyErrorListener()
    parser._listeners = [errorListener]
    tree = parser.prog()
    visitor = CustomVisitor()
    visitor.visit(tree)

    errors = errorListener.getError()
    for x in errors:
        print(x)
