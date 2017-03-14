# Generated from Count.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


package foo;


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\5\27\b\1\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\3\6\3\r\n")
        buf.write(u"\3\r\3\16\3\16\3\4\6\4\22\n\4\r\4\16\4\23\3\4\3\4\2\2")
        buf.write(u"\5\3\3\5\4\7\5\3\2\4\3\2\62;\5\2\13\f\17\17\"\"\30\2")
        buf.write(u"\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\3\t\3\2\2\2\5\f\3")
        buf.write(u"\2\2\2\7\21\3\2\2\2\t\n\7.\2\2\n\4\3\2\2\2\13\r\t\2\2")
        buf.write(u"\2\f\13\3\2\2\2\r\16\3\2\2\2\16\f\3\2\2\2\16\17\3\2\2")
        buf.write(u"\2\17\6\3\2\2\2\20\22\t\3\2\2\21\20\3\2\2\2\22\23\3\2")
        buf.write(u"\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\25\3\2\2\2\25\26")
        buf.write(u"\b\4\2\2\26\b\3\2\2\2\5\2\16\23\3\b\2\2")
        return buf.getvalue()


class CountLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    INT = 2
    WS = 3

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"','" ]

    symbolicNames = [ u"<INVALID>",
            u"INT", u"WS" ]

    ruleNames = [ u"T__0", u"INT", u"WS" ]

    grammarFileName = u"Count.g4"

    def __init__(self, input=None):
        super(CountLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    int count = 0;


