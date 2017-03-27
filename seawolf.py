import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from SeawolfGrammarLexer import SeawolfGrammarLexer
from SeawolfGrammarParser import SeawolfGrammarParser
from CustomVisitor import CustomVisitor
# from antlr4.error.ErrorListener import ErrorListener
# from antlr4.error.ErrorStrategy import  ErrorStrategy

#
# class MyErrorListener(ErrorListener):
#     def __init__(self):
#         super(MyErrorListener, self).__init__()
#         self.err = []
#
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         self.err.append(msg)
#         # return "SYNTAX ERROR"
#
#     def getError(self):
#         return self.err
#
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
    # parser._listeners = MyErrorListener()
    tree = parser.prog()
    visitor = CustomVisitor()
    visitor.visit(tree)
    #
    # listeners = parser.getParseListeners()
    # errors = listeners[0]
    #
    # for msg in errors.getError():
    #     print(msg)
