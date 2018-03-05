__author__ = 'Zylanx'

# from .antlr.TIS100Visitor import TIS100Visitor
if __name__ is not None and "." in __name__:
	from .antlr.TIS100Visitor import TIS100Visitor
	from .asmprogram import ASMProgram, LabelNode, RegNode, CommPortNode, ConstNode
else:
	from antlr.TIS100Visitor import TIS100Visitor
	from asmprogram import ASMProgram, LabelNode, RegNode, CommPortNode, ConstNode

# def visitStart(self, ctx: TIS100Parser.StartContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#line.
# def visitLine(self, ctx: TIS100Parser.LineContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#instr.
# def visitInstr(self, ctx: TIS100Parser.InstrContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#argumentList.
# def visitArgumentList(self, ctx: TIS100Parser.ArgumentListContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#argument.
# def visitArgument(self, ctx: TIS100Parser.ArgumentContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#opcode.
# def visitOpcode(self, ctx: TIS100Parser.OpcodeContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#const.
# def visitConst(self, ctx: TIS100Parser.ConstContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#reg.
# def visitReg(self, ctx: TIS100Parser.RegContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#commport.
# def visitCommport(self, ctx: TIS100Parser.CommportContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#label.
# def visitLabel(self, ctx: TIS100Parser.LabelContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#labelRef.
# def visitLabelRef(self, ctx: TIS100Parser.LabelRefContext):
# 	return self.visitChildren(ctx)
#
#
# # Visit a parse tree produced by TIS100Parser#comment.
# def visitComment(self, ctx: TIS100Parser.CommentContext):
# 	return self.visitChildren(ctx)

class SymbolTableBuilder(TIS100Visitor):
	def __init__(self, *args, **kwargs):
		self.symbolTable = set()
		super().__init__(*args, **kwargs)

	def visitStart(self, ctx):
		self.visitChildren(ctx)
		return self.symbolTable

	def visitLabel(self, ctx):
		if ctx.LABEL_ID().getText():
			self.symbolTable.add(ctx.LABEL_ID().getText())


class CompilerVisitor(TIS100Visitor):
	def __init__(self, symbolTable, *args, **kwargs):
		self.asmProg = ASMProgram(symbolTable)
		super().__init__(*args, **kwargs)
	
	def visitStart(self, ctx):
		self.visitChildren(ctx)
		return self.asmProg
	
	def visitLabel(self, ctx):
		label = LabelNode(ctx.LABEL_ID().getText())
		self.asmProg.addLabel(label)
	
	def visitInstr(self, ctx):
		if ctx.label():
			self.visit(ctx.label())
		self.asmProg.addInstr(self.visit(ctx.op), self.visit(ctx.argumentList()))
		# return self.visitChildren(ctx)
	
	def visitOpcode(self, ctx):
		return ctx.getText().lower()
	
	def visitArgsOne(self, ctx):
		return [self.visit(ctx.argument())]
	
	def visitArgsTwo(self, ctx):
		return [self.visit(ctx.argument(0)), self.visit(ctx.argument(1))]
	
	def visitArgsEmpty(self, ctx):
		return []
	
	def visitReg(self, ctx):
		return RegNode(ctx.REG().getText().lower())
	
	def visitCommport(self, ctx):
		return CommPortNode(ctx.COMMPORT().getText())
	
	def visitLabelRef(self, ctx):
		return LabelNode(ctx.LABEL_ID().getText())
	
	def visitConst(self, ctx):
		return ConstNode(int(ctx.CONST().getText()))