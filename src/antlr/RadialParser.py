# Generated from Radial.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\3\3\3\5\3\31\n")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("\'\n\4\f\4\16\4*\13\4\3\4\3\4\5\4.\n\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\5\5\66\n\5\3\6\3\6\3\6\3\6\5\6<\n\6\3\6\3\6\3")
        buf.write("\6\7\6A\n\6\f\6\16\6D\13\6\3\6\3\6\3\7\3\7\3\7\3\7\7\7")
        buf.write("L\n\7\f\7\16\7O\13\7\3\7\3\7\3\7\5\7T\n\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\7\7\\\n\7\f\7\16\7_\13\7\3\b\3\b\3\b\5\b")
        buf.write("d\n\b\3\b\2\3\f\t\2\4\6\b\n\f\16\2\4\3\2\n\f\3\2\b\t\2")
        buf.write("m\2\23\3\2\2\2\4\30\3\2\2\2\6-\3\2\2\2\b\65\3\2\2\2\n")
        buf.write("\67\3\2\2\2\fS\3\2\2\2\16c\3\2\2\2\20\22\5\4\3\2\21\20")
        buf.write("\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\3\3\2\2\2\25\23\3\2\2\2\26\31\5\n\6\2\27\31\5\6\4\2\30")
        buf.write("\26\3\2\2\2\30\27\3\2\2\2\31\5\3\2\2\2\32\33\5\f\7\2\33")
        buf.write("\34\7\r\2\2\34.\3\2\2\2\35\36\5\b\5\2\36\37\7\r\2\2\37")
        buf.write(".\3\2\2\2 !\7\23\2\2!\"\7\16\2\2\"#\5\f\7\2#$\7\17\2\2")
        buf.write("$(\7\20\2\2%\'\5\6\4\2&%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2")
        buf.write("()\3\2\2\2)+\3\2\2\2*(\3\2\2\2+,\7\21\2\2,.\3\2\2\2-\32")
        buf.write("\3\2\2\2-\35\3\2\2\2- \3\2\2\2.\7\3\2\2\2/\60\7\7\2\2")
        buf.write("\60\66\7\6\2\2\61\62\7\7\2\2\62\63\7\6\2\2\63\64\3\2\2")
        buf.write("\2\64\66\5\f\7\2\65/\3\2\2\2\65\61\3\2\2\2\66\t\3\2\2")
        buf.write("\2\678\7\7\2\289\7\6\2\29;\7\16\2\2:<\7\6\2\2;:\3\2\2")
        buf.write("\2;<\3\2\2\2<=\3\2\2\2=>\7\17\2\2>B\7\20\2\2?A\5\6\4\2")
        buf.write("@?\3\2\2\2AD\3\2\2\2B@\3\2\2\2BC\3\2\2\2CE\3\2\2\2DB\3")
        buf.write("\2\2\2EF\7\21\2\2F\13\3\2\2\2GH\b\7\1\2HI\7\6\2\2IM\7")
        buf.write("\16\2\2JL\5\f\7\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2")
        buf.write("\2\2NP\3\2\2\2OM\3\2\2\2PT\7\17\2\2QT\5\16\b\2RT\7\6\2")
        buf.write("\2SG\3\2\2\2SQ\3\2\2\2SR\3\2\2\2T]\3\2\2\2UV\f\6\2\2V")
        buf.write("W\t\2\2\2W\\\5\f\7\7XY\f\5\2\2YZ\t\3\2\2Z\\\5\f\7\6[U")
        buf.write("\3\2\2\2[X\3\2\2\2\\_\3\2\2\2][\3\2\2\2]^\3\2\2\2^\r\3")
        buf.write("\2\2\2_]\3\2\2\2`d\7\3\2\2ad\7\4\2\2bd\7\5\2\2c`\3\2\2")
        buf.write("\2ca\3\2\2\2cb\3\2\2\2d\17\3\2\2\2\16\23\30(-\65;BMS[")
        buf.write("]c")
        return buf.getvalue()


class RadialParser ( Parser ):

    grammarFileName = "Radial.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "';'", "'('", "')'", "'{'", "'}'", "'='", "'if'" ]

    symbolicNames = [ "<INVALID>", "INT", "DEC", "STR", "LABEL", "TYPE", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "END", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "EQUALS", "IF", "WS", 
                      "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_statement_func = 1
    RULE_statement = 2
    RULE_var_def = 3
    RULE_func_def = 4
    RULE_expression = 5
    RULE_literal = 6

    ruleNames =  [ "program", "statement_func", "statement", "var_def", 
                   "func_def", "expression", "literal" ]

    EOF = Token.EOF
    INT=1
    DEC=2
    STR=3
    LABEL=4
    TYPE=5
    ADD=6
    SUB=7
    MUL=8
    DIV=9
    MOD=10
    END=11
    LPAREN=12
    RPAREN=13
    LBRACE=14
    RBRACE=15
    EQUALS=16
    IF=17
    WS=18
    LINE_COMMENT=19
    BLOCK_COMMENT=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_func(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RadialParser.Statement_funcContext)
            else:
                return self.getTypedRuleContext(RadialParser.Statement_funcContext,i)


        def getRuleIndex(self):
            return RadialParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = RadialParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RadialParser.INT) | (1 << RadialParser.DEC) | (1 << RadialParser.STR) | (1 << RadialParser.LABEL) | (1 << RadialParser.TYPE) | (1 << RadialParser.IF))) != 0):
                self.state = 14
                self.statement_func()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_def(self):
            return self.getTypedRuleContext(RadialParser.Func_defContext,0)


        def statement(self):
            return self.getTypedRuleContext(RadialParser.StatementContext,0)


        def getRuleIndex(self):
            return RadialParser.RULE_statement_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_func" ):
                return visitor.visitStatement_func(self)
            else:
                return visitor.visitChildren(self)




    def statement_func(self):

        localctx = RadialParser.Statement_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement_func)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.func_def()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(RadialParser.ExpressionContext,0)


        def END(self):
            return self.getToken(RadialParser.END, 0)

        def var_def(self):
            return self.getTypedRuleContext(RadialParser.Var_defContext,0)


        def IF(self):
            return self.getToken(RadialParser.IF, 0)

        def LPAREN(self):
            return self.getToken(RadialParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RadialParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(RadialParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(RadialParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RadialParser.StatementContext)
            else:
                return self.getTypedRuleContext(RadialParser.StatementContext,i)


        def getRuleIndex(self):
            return RadialParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = RadialParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RadialParser.INT, RadialParser.DEC, RadialParser.STR, RadialParser.LABEL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.expression(0)
                self.state = 25
                self.match(RadialParser.END)
                pass
            elif token in [RadialParser.TYPE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.var_def()
                self.state = 28
                self.match(RadialParser.END)
                pass
            elif token in [RadialParser.IF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.match(RadialParser.IF)
                self.state = 31
                self.match(RadialParser.LPAREN)
                self.state = 32
                self.expression(0)
                self.state = 33
                self.match(RadialParser.RPAREN)
                self.state = 34
                self.match(RadialParser.LBRACE)
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RadialParser.INT) | (1 << RadialParser.DEC) | (1 << RadialParser.STR) | (1 << RadialParser.LABEL) | (1 << RadialParser.TYPE) | (1 << RadialParser.IF))) != 0):
                    self.state = 35
                    self.statement()
                    self.state = 40
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 41
                self.match(RadialParser.RBRACE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(RadialParser.TYPE, 0)

        def LABEL(self):
            return self.getToken(RadialParser.LABEL, 0)

        def expression(self):
            return self.getTypedRuleContext(RadialParser.ExpressionContext,0)


        def getRuleIndex(self):
            return RadialParser.RULE_var_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_def" ):
                return visitor.visitVar_def(self)
            else:
                return visitor.visitChildren(self)




    def var_def(self):

        localctx = RadialParser.Var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_def)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.match(RadialParser.TYPE)
                self.state = 46
                self.match(RadialParser.LABEL)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(RadialParser.TYPE)
                self.state = 48
                self.match(RadialParser.LABEL)


                self.state = 50
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(RadialParser.TYPE, 0)

        def LABEL(self, i:int=None):
            if i is None:
                return self.getTokens(RadialParser.LABEL)
            else:
                return self.getToken(RadialParser.LABEL, i)

        def LPAREN(self):
            return self.getToken(RadialParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(RadialParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(RadialParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(RadialParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RadialParser.StatementContext)
            else:
                return self.getTypedRuleContext(RadialParser.StatementContext,i)


        def getRuleIndex(self):
            return RadialParser.RULE_func_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_def" ):
                return visitor.visitFunc_def(self)
            else:
                return visitor.visitChildren(self)




    def func_def(self):

        localctx = RadialParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(RadialParser.TYPE)
            self.state = 54
            self.match(RadialParser.LABEL)
            self.state = 55
            self.match(RadialParser.LPAREN)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==RadialParser.LABEL:
                self.state = 56
                self.match(RadialParser.LABEL)


            self.state = 59
            self.match(RadialParser.RPAREN)
            self.state = 60
            self.match(RadialParser.LBRACE)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RadialParser.INT) | (1 << RadialParser.DEC) | (1 << RadialParser.STR) | (1 << RadialParser.LABEL) | (1 << RadialParser.TYPE) | (1 << RadialParser.IF))) != 0):
                self.state = 61
                self.statement()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(RadialParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RadialParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RadialParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RadialParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RadialParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(RadialParser.ADD, 0)
        def SUB(self):
            return self.getToken(RadialParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class CallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RadialParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LABEL(self):
            return self.getToken(RadialParser.LABEL, 0)
        def LPAREN(self):
            return self.getToken(RadialParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(RadialParser.RPAREN, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RadialParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RadialParser.ExpressionContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RadialParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RadialParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(RadialParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(RadialParser.MUL, 0)
        def DIV(self):
            return self.getToken(RadialParser.DIV, 0)
        def MOD(self):
            return self.getToken(RadialParser.MOD, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class LitContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RadialParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(RadialParser.LiteralContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit" ):
                return visitor.visitLit(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RadialParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LABEL(self):
            return self.getToken(RadialParser.LABEL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = RadialParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = RadialParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 70
                self.match(RadialParser.LABEL)
                self.state = 71
                self.match(RadialParser.LPAREN)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RadialParser.INT) | (1 << RadialParser.DEC) | (1 << RadialParser.STR) | (1 << RadialParser.LABEL))) != 0):
                    self.state = 72
                    self.expression(0)
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 78
                self.match(RadialParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = RadialParser.LitContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 79
                self.literal()
                pass

            elif la_ == 3:
                localctx = RadialParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self.match(RadialParser.LABEL)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 91
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 89
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = RadialParser.MulContext(self, RadialParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 83
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 84
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << RadialParser.MUL) | (1 << RadialParser.DIV) | (1 << RadialParser.MOD))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 85
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = RadialParser.AddContext(self, RadialParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 86
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 87
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==RadialParser.ADD or _la==RadialParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 88
                        self.expression(4)
                        pass

             
                self.state = 93
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return RadialParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StrContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RadialParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STR(self):
            return self.getToken(RadialParser.STR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr" ):
                return visitor.visitStr(self)
            else:
                return visitor.visitChildren(self)


    class DecContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RadialParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DEC(self):
            return self.getToken(RadialParser.DEC, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDec" ):
                return visitor.visitDec(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a RadialParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(RadialParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = RadialParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_literal)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [RadialParser.INT]:
                localctx = RadialParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(RadialParser.INT)
                pass
            elif token in [RadialParser.DEC]:
                localctx = RadialParser.DecContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(RadialParser.DEC)
                pass
            elif token in [RadialParser.STR]:
                localctx = RadialParser.StrContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.match(RadialParser.STR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




