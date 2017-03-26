import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from SeawolfGrammarLexer import SeawolfGrammarLexer
from SeawolfGrammarParser import SeawolfGrammarParser
from CustomVisitor import CustomVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1].strip())
    else:
        input_stream = InputStream(sys.stdin.readline().strip())

    lexer = SeawolfGrammarLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SeawolfGrammarParser(token_stream)
    tree = parser.prog()
    visitor = CustomVisitor()
    visitor.visit(tree)
