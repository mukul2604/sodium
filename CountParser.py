# Generated from Count.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


package foo;

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\5\17\4\2\t\2\3\2\3\2\3\2\3\2\3\2\7\2\n\n\2\f\2\16\2")
        buf.write(u"\r\13\2\3\2\2\2\3\2\2\2\16\2\4\3\2\2\2\4\5\7\4\2\2\5")
        buf.write(u"\13\b\2\1\2\6\7\7\3\2\2\7\b\7\4\2\2\b\n\b\2\1\2\t\6\3")
        buf.write(u"\2\2\2\n\r\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3\3\2")
        buf.write(u"\2\2\r\13\3\2\2\2\3\13")
        return buf.getvalue()


class CountParser ( Parser ):

    grammarFileName = "Count.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"','" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"INT", u"WS" ]

    RULE_list = 0

    ruleNames =  [ u"list" ]

    EOF = Token.EOF
    T__0=1
    INT=2
    WS=3

    def __init__(self, input):
        super(CountParser, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    int count = 0;


    class ListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(CountParser.ListContext, self).__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i=None):
            if i is None:
                return self.getTokens(CountParser.INT)
            else:
                return self.getToken(CountParser.INT, i)

        def getRuleIndex(self):
            return CountParser.RULE_list

        def enterRule(self, listener):
            if hasattr(listener, "enterList"):
                listener.enterList(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitList"):
                listener.exitList(self)




    def list(self):

        localctx = CountParser.ListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(CountParser.INT)
            count++;
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CountParser.T__0:
                self.state = 4
                self.match(CountParser.T__0)
                self.state = 5
                self.match(CountParser.INT)
                count++;
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self._ctx.stop = self._input.LT(-1)
            System.out.println(count+" ints");
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





