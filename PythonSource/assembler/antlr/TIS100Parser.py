# Generated from I:/Github/TIS-100_EvalKit/PythonSource/assembler\TIS100.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("P\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\5\2")
        buf.write("\34\n\2\3\2\7\2\37\n\2\f\2\16\2\"\13\2\3\2\5\2%\n\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\5\3,\n\3\3\4\5\4/\n\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\5\59\n\5\3\6\3\6\3\6\3\6\5\6?\n\6\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\3")
        buf.write("\3\2\4\17\2N\2 \3\2\2\2\4+\3\2\2\2\6.\3\2\2\2\b8\3\2\2")
        buf.write("\2\n>\3\2\2\2\f@\3\2\2\2\16B\3\2\2\2\20D\3\2\2\2\22F\3")
        buf.write("\2\2\2\24H\3\2\2\2\26K\3\2\2\2\30M\3\2\2\2\32\34\5\4\3")
        buf.write("\2\33\32\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35\37\7\25")
        buf.write("\2\2\36\33\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2 !\3\2\2\2")
        buf.write("!$\3\2\2\2\" \3\2\2\2#%\5\4\3\2$#\3\2\2\2$%\3\2\2\2%&")
        buf.write("\3\2\2\2&\'\7\2\2\3\'\3\3\2\2\2(,\5\30\r\2),\5\6\4\2*")
        buf.write(",\5\24\13\2+(\3\2\2\2+)\3\2\2\2+*\3\2\2\2,\5\3\2\2\2-")
        buf.write("/\5\24\13\2.-\3\2\2\2./\3\2\2\2/\60\3\2\2\2\60\61\5\f")
        buf.write("\7\2\61\62\5\b\5\2\62\7\3\2\2\2\639\5\n\6\2\64\65\5\n")
        buf.write("\6\2\65\66\5\n\6\2\669\3\2\2\2\679\3\2\2\28\63\3\2\2\2")
        buf.write("8\64\3\2\2\28\67\3\2\2\29\t\3\2\2\2:?\5\16\b\2;?\5\20")
        buf.write("\t\2<?\5\22\n\2=?\5\26\f\2>:\3\2\2\2>;\3\2\2\2><\3\2\2")
        buf.write("\2>=\3\2\2\2?\13\3\2\2\2@A\t\2\2\2A\r\3\2\2\2BC\7\22\2")
        buf.write("\2C\17\3\2\2\2DE\7\20\2\2E\21\3\2\2\2FG\7\21\2\2G\23\3")
        buf.write("\2\2\2HI\7\23\2\2IJ\7\3\2\2J\25\3\2\2\2KL\7\23\2\2L\27")
        buf.write("\3\2\2\2MN\7\24\2\2N\31\3\2\2\2\t\33 $+.8>")
        return buf.getvalue()


class TIS100Parser ( Parser ):

    grammarFileName = "TIS100.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Mov", "Add", "Sub", "Neg", 
                      "Sav", "Swp", "Jmp", "Jez", "Jnz", "Jgz", "Jlz", "Jro", 
                      "REG", "COMMPORT", "CONST", "LABEL_ID", "COMMENT", 
                      "EOL", "WS" ]

    RULE_start = 0
    RULE_line = 1
    RULE_instr = 2
    RULE_argumentList = 3
    RULE_argument = 4
    RULE_opcode = 5
    RULE_const = 6
    RULE_reg = 7
    RULE_commport = 8
    RULE_label = 9
    RULE_labelRef = 10
    RULE_comment = 11

    ruleNames =  [ "start", "line", "instr", "argumentList", "argument", 
                   "opcode", "const", "reg", "commport", "label", "labelRef", 
                   "comment" ]

    EOF = Token.EOF
    T__0=1
    Mov=2
    Add=3
    Sub=4
    Neg=5
    Sav=6
    Swp=7
    Jmp=8
    Jez=9
    Jnz=10
    Jgz=11
    Jlz=12
    Jro=13
    REG=14
    COMMPORT=15
    CONST=16
    LABEL_ID=17
    COMMENT=18
    EOL=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TIS100Parser.EOF, 0)

        def EOL(self, i:int=None):
            if i is None:
                return self.getTokens(TIS100Parser.EOL)
            else:
                return self.getToken(TIS100Parser.EOL, i)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TIS100Parser.LineContext)
            else:
                return self.getTypedRuleContext(TIS100Parser.LineContext,i)


        def getRuleIndex(self):
            return TIS100Parser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = TIS100Parser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 25
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TIS100Parser.Mov) | (1 << TIS100Parser.Add) | (1 << TIS100Parser.Sub) | (1 << TIS100Parser.Neg) | (1 << TIS100Parser.Sav) | (1 << TIS100Parser.Swp) | (1 << TIS100Parser.Jmp) | (1 << TIS100Parser.Jez) | (1 << TIS100Parser.Jnz) | (1 << TIS100Parser.Jgz) | (1 << TIS100Parser.Jlz) | (1 << TIS100Parser.Jro) | (1 << TIS100Parser.LABEL_ID) | (1 << TIS100Parser.COMMENT))) != 0):
                        self.state = 24
                        self.line()


                    self.state = 27
                    self.match(TIS100Parser.EOL) 
                self.state = 32
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TIS100Parser.Mov) | (1 << TIS100Parser.Add) | (1 << TIS100Parser.Sub) | (1 << TIS100Parser.Neg) | (1 << TIS100Parser.Sav) | (1 << TIS100Parser.Swp) | (1 << TIS100Parser.Jmp) | (1 << TIS100Parser.Jez) | (1 << TIS100Parser.Jnz) | (1 << TIS100Parser.Jgz) | (1 << TIS100Parser.Jlz) | (1 << TIS100Parser.Jro) | (1 << TIS100Parser.LABEL_ID) | (1 << TIS100Parser.COMMENT))) != 0):
                self.state = 33
                self.line()


            self.state = 36
            self.match(TIS100Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comment(self):
            return self.getTypedRuleContext(TIS100Parser.CommentContext,0)


        def instr(self):
            return self.getTypedRuleContext(TIS100Parser.InstrContext,0)


        def label(self):
            return self.getTypedRuleContext(TIS100Parser.LabelContext,0)


        def getRuleIndex(self):
            return TIS100Parser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = TIS100Parser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 41
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.comment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.instr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.label()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # OpcodeContext

        def argumentList(self):
            return self.getTypedRuleContext(TIS100Parser.ArgumentListContext,0)


        def opcode(self):
            return self.getTypedRuleContext(TIS100Parser.OpcodeContext,0)


        def label(self):
            return self.getTypedRuleContext(TIS100Parser.LabelContext,0)


        def getRuleIndex(self):
            return TIS100Parser.RULE_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstr" ):
                listener.enterInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstr" ):
                listener.exitInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = TIS100Parser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TIS100Parser.LABEL_ID:
                self.state = 43
                self.label()


            self.state = 46
            localctx.op = self.opcode()
            self.state = 47
            self.argumentList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TIS100Parser.RULE_argumentList

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArgsTwoContext(ArgumentListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TIS100Parser.ArgumentListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TIS100Parser.ArgumentContext)
            else:
                return self.getTypedRuleContext(TIS100Parser.ArgumentContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgsTwo" ):
                listener.enterArgsTwo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgsTwo" ):
                listener.exitArgsTwo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgsTwo" ):
                return visitor.visitArgsTwo(self)
            else:
                return visitor.visitChildren(self)


    class ArgsEmptyContext(ArgumentListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TIS100Parser.ArgumentListContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgsEmpty" ):
                listener.enterArgsEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgsEmpty" ):
                listener.exitArgsEmpty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgsEmpty" ):
                return visitor.visitArgsEmpty(self)
            else:
                return visitor.visitChildren(self)


    class ArgsOneContext(ArgumentListContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TIS100Parser.ArgumentListContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def argument(self):
            return self.getTypedRuleContext(TIS100Parser.ArgumentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgsOne" ):
                listener.enterArgsOne(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgsOne" ):
                listener.exitArgsOne(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgsOne" ):
                return visitor.visitArgsOne(self)
            else:
                return visitor.visitChildren(self)



    def argumentList(self):

        localctx = TIS100Parser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_argumentList)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = TIS100Parser.ArgsOneContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.argument()
                pass

            elif la_ == 2:
                localctx = TIS100Parser.ArgsTwoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.argument()
                self.state = 51
                self.argument()
                pass

            elif la_ == 3:
                localctx = TIS100Parser.ArgsEmptyContext(self, localctx)
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ArgumentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const(self):
            return self.getTypedRuleContext(TIS100Parser.ConstContext,0)


        def reg(self):
            return self.getTypedRuleContext(TIS100Parser.RegContext,0)


        def commport(self):
            return self.getTypedRuleContext(TIS100Parser.CommportContext,0)


        def labelRef(self):
            return self.getTypedRuleContext(TIS100Parser.LabelRefContext,0)


        def getRuleIndex(self):
            return TIS100Parser.RULE_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument" ):
                listener.enterArgument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument" ):
                listener.exitArgument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = TIS100Parser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_argument)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TIS100Parser.CONST]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.const()
                pass
            elif token in [TIS100Parser.REG]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.reg()
                pass
            elif token in [TIS100Parser.COMMPORT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.commport()
                pass
            elif token in [TIS100Parser.LABEL_ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
                self.labelRef()
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

    class OpcodeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Mov(self):
            return self.getToken(TIS100Parser.Mov, 0)

        def Add(self):
            return self.getToken(TIS100Parser.Add, 0)

        def Sub(self):
            return self.getToken(TIS100Parser.Sub, 0)

        def Neg(self):
            return self.getToken(TIS100Parser.Neg, 0)

        def Sav(self):
            return self.getToken(TIS100Parser.Sav, 0)

        def Swp(self):
            return self.getToken(TIS100Parser.Swp, 0)

        def Jmp(self):
            return self.getToken(TIS100Parser.Jmp, 0)

        def Jez(self):
            return self.getToken(TIS100Parser.Jez, 0)

        def Jnz(self):
            return self.getToken(TIS100Parser.Jnz, 0)

        def Jgz(self):
            return self.getToken(TIS100Parser.Jgz, 0)

        def Jlz(self):
            return self.getToken(TIS100Parser.Jlz, 0)

        def Jro(self):
            return self.getToken(TIS100Parser.Jro, 0)

        def getRuleIndex(self):
            return TIS100Parser.RULE_opcode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcode" ):
                listener.enterOpcode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcode" ):
                listener.exitOpcode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcode" ):
                return visitor.visitOpcode(self)
            else:
                return visitor.visitChildren(self)




    def opcode(self):

        localctx = TIS100Parser.OpcodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_opcode)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << TIS100Parser.Mov) | (1 << TIS100Parser.Add) | (1 << TIS100Parser.Sub) | (1 << TIS100Parser.Neg) | (1 << TIS100Parser.Sav) | (1 << TIS100Parser.Swp) | (1 << TIS100Parser.Jmp) | (1 << TIS100Parser.Jez) | (1 << TIS100Parser.Jnz) | (1 << TIS100Parser.Jgz) | (1 << TIS100Parser.Jlz) | (1 << TIS100Parser.Jro))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(TIS100Parser.CONST, 0)

        def getRuleIndex(self):
            return TIS100Parser.RULE_const

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConst" ):
                listener.enterConst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConst" ):
                listener.exitConst(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConst" ):
                return visitor.visitConst(self)
            else:
                return visitor.visitChildren(self)




    def const(self):

        localctx = TIS100Parser.ConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_const)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(TIS100Parser.CONST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RegContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REG(self):
            return self.getToken(TIS100Parser.REG, 0)

        def getRuleIndex(self):
            return TIS100Parser.RULE_reg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReg" ):
                listener.enterReg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReg" ):
                listener.exitReg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReg" ):
                return visitor.visitReg(self)
            else:
                return visitor.visitChildren(self)




    def reg(self):

        localctx = TIS100Parser.RegContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_reg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(TIS100Parser.REG)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommportContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMPORT(self):
            return self.getToken(TIS100Parser.COMMPORT, 0)

        def getRuleIndex(self):
            return TIS100Parser.RULE_commport

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommport" ):
                listener.enterCommport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommport" ):
                listener.exitCommport(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommport" ):
                return visitor.visitCommport(self)
            else:
                return visitor.visitChildren(self)




    def commport(self):

        localctx = TIS100Parser.CommportContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_commport)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(TIS100Parser.COMMPORT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL_ID(self):
            return self.getToken(TIS100Parser.LABEL_ID, 0)

        def getRuleIndex(self):
            return TIS100Parser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = TIS100Parser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(TIS100Parser.LABEL_ID)
            self.state = 71
            self.match(TIS100Parser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LabelRefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LABEL_ID(self):
            return self.getToken(TIS100Parser.LABEL_ID, 0)

        def getRuleIndex(self):
            return TIS100Parser.RULE_labelRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabelRef" ):
                listener.enterLabelRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabelRef" ):
                listener.exitLabelRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabelRef" ):
                return visitor.visitLabelRef(self)
            else:
                return visitor.visitChildren(self)




    def labelRef(self):

        localctx = TIS100Parser.LabelRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_labelRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(TIS100Parser.LABEL_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(TIS100Parser.COMMENT, 0)

        def getRuleIndex(self):
            return TIS100Parser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = TIS100Parser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(TIS100Parser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





