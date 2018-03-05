# Generated from I:/Github/TIS-100_EvalKit/PythonSource/assembler\TIS100.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TIS100Parser import TIS100Parser
else:
    from TIS100Parser import TIS100Parser

# This class defines a complete generic visitor for a parse tree produced by TIS100Parser.

class TIS100Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by TIS100Parser#start.
    def visitStart(self, ctx:TIS100Parser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#line.
    def visitLine(self, ctx:TIS100Parser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#instr.
    def visitInstr(self, ctx:TIS100Parser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#ArgsOne.
    def visitArgsOne(self, ctx:TIS100Parser.ArgsOneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#ArgsTwo.
    def visitArgsTwo(self, ctx:TIS100Parser.ArgsTwoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#ArgsEmpty.
    def visitArgsEmpty(self, ctx:TIS100Parser.ArgsEmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#argument.
    def visitArgument(self, ctx:TIS100Parser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#opcode.
    def visitOpcode(self, ctx:TIS100Parser.OpcodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#const.
    def visitConst(self, ctx:TIS100Parser.ConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#reg.
    def visitReg(self, ctx:TIS100Parser.RegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#commport.
    def visitCommport(self, ctx:TIS100Parser.CommportContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#label.
    def visitLabel(self, ctx:TIS100Parser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#labelRef.
    def visitLabelRef(self, ctx:TIS100Parser.LabelRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TIS100Parser#comment.
    def visitComment(self, ctx:TIS100Parser.CommentContext):
        return self.visitChildren(ctx)



del TIS100Parser