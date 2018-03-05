__author__ = 'Zylanx'

print("I need to work out how to make this work properly with all the relative imports etc. Probably need to split main.py out from the rest of the package. Else make a small script outside the module that interfaces with it")

import sys
from antlr4 import *
# if __name__ is not None and "." in __name__:
# 	from .antlr.TIS100Lexer import TIS100Lexer
# 	from .antlr.TIS100Parser import TIS100Parser
# 	from .antlr.TIS100Listener import TIS100Listener
# 	from .asmprogram import ASMProgram
# 	from .compiler import CompilerVisitor, SymbolTableBuilder
# else:
# 	from antlr.TIS100Lexer import TIS100Lexer
# 	from antlr.TIS100Parser import TIS100Parser
# 	from antlr.TIS100Listener import TIS100Listener
# 	from asmprogram import ASMProgram
# 	from compiler import CompilerVisitor, SymbolTableBuilder

from .antlr.TIS100Lexer import TIS100Lexer
from .antlr.TIS100Parser import TIS100Parser
from .antlr.TIS100Listener import TIS100Listener
from .asmprogram import ASMProgram
from .compiler import CompilerVisitor, SymbolTableBuilder


def main(argv):
	# input = FileStream(argv[1])
	inputstr = " ".join([bytes(x, "utf-8").decode("unicode-escape") for x in argv[1:]])
	
	input = InputStream(inputstr)
	lexer = TIS100Lexer(input)
	stream = CommonTokenStream(lexer)
	parser = TIS100Parser(stream)
	tree = parser.start()
	# printer = TIS100Listener()
	# walker = ParseTreeWalker()
	# walker.walk(printer, tree)
	symbolTable = SymbolTableBuilder().visit(tree)
	compiler = CompilerVisitor(symbolTable)
	compiledProg = compiler.visit(tree)
	print("---Input---")
	print(inputstr)
	print("\n---Labels---")
	print(compiledProg.labels)
	print("\n---Instructions---")
	print(compiledProg.instrs)
	print("\n---Compiled Array---")
	print(compiledProg.assembled)
	print("\n---Output---")
	print("\n".join(compiledProg.assembled))


if __name__ == '__main__':
	main(sys.argv)