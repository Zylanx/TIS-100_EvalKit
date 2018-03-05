__author__ = 'Zylanx'

if __name__ is not None and "." in __name__:
	from .asminstruction import Nop, Add, Mov, Sub, Neg, Sav, Swp, Jmp, Jro
	from .nodes import LabelMarker, LabelNode, RegNode, CommPortNode, ConstNode
else:
	from asminstruction import Nop, Add, Mov, Sub, Neg, Sav, Swp, Jmp, Jro
	from nodes import LabelMarker, LabelNode, RegNode, CommPortNode, ConstNode

class LabelExistsError(Exception):
	pass

class LabelNotExistsError(Exception):
	pass

class ASMProgram:
	def __init__(self, symbolTable):
		self.symbolTable = symbolTable
		self.lineNum = 0
		self.labels = {}.fromkeys(symbolTable, None)
		self.instrs = []
		
		for key in self.labels:
			self.labels[key] = LabelMarker(key, None)
	
	def convertToMarker(self, labelNode):
		if not self.labels.get(labelNode.value, None):
			raise LabelNotExistsError("Label doesn't exist: " + labelNode.value)
		return self.labels[labelNode.value]
	
	def genInstr(self, lineNum, opcode, arguments):
		if opcode == "add":
			return Add(lineNum, opcode, arguments)
		elif opcode == "mov":
			return Mov(lineNum, opcode, arguments)
		elif opcode == "sub":
			return Sub(lineNum, opcode, arguments)
		elif opcode == "neg":
			return Neg(lineNum, opcode, arguments)
		elif opcode == "sav":
			return Sav(lineNum, opcode, arguments)
		elif opcode == "swp":
			return Swp(lineNum, opcode, arguments)
		elif opcode == "jmp":
			return Jmp(lineNum, opcode, arguments)
		elif opcode == "jro":
			return Jro(lineNum, opcode, arguments)
		return Nop(lineNum, opcode, arguments)
	
	def addLabel(self, labelNode):
		labelVal = labelNode.value
		if self.labels.get(labelVal, LabelMarker("", None)).lineNum:
			raise LabelExistsError("Label already defined: " + labelVal)
		self.labels[labelVal].lineNum = self.lineNum
		
	def addInstr(self, opcode, arguments):
		arguments = arguments
		for index, arg in enumerate(arguments):
			if isinstance(arg, LabelNode):
				arguments[index] = self.convertToMarker(arg)
		
		self.instrs.append(self.genInstr(self.lineNum, opcode, arguments))
		self.lineNum += 1
	
	def assemble(self):
		assembledProg = []
		for instr in self.instrs:
			assembledProg.append(instr.assemble())
		return assembledProg
	
	@property
	def assembled(self):
		return self.assemble()