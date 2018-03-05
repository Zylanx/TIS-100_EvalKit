__author__ = 'Zylanx'

if __name__ is not None and "." in __name__:
	from .nodes import LabelMarker, RegNode, CommPortNode, ConstNode
else:
	from nodes import LabelMarker, RegNode, CommPortNode, ConstNode

from copy import deepcopy
from collections import abc
from bitstring import Bits

class InvalidArgumentError(Exception):
	pass

class InvalidPortError(Exception):
	pass

def portToBin(port):
	if port == "nil":
		return "000"
	elif port == "acc":
		return "001"
	elif port == "left":
		return "010"
	elif port == "right":
		return "011"
	elif port == "up":
		return "100"
	elif port == "down":
		return "101"
	elif port == "any":
		return "110"
	elif port == "last":
		return "111"
	raise InvalidPortError("Port name is not valid")

def jmpToMask(opcode):
	if opcode == "jmp":
		return "111"
	elif opcode == "jez":
		return "100"
	elif opcode == "jnz":
		return "011"
	elif opcode == "jgz":
		return "010"
	elif opcode == "jlz":
		return "001"
	return "000"

def accepts(argIndex, *allowed):
	def decorator(cls):
		allowedList = []
		for arg in allowed:
			if isinstance(arg, abc.Iterable):
				allowedList.extend(arg)
			else:
				allowedList.append(arg)
		
		setattr(cls, "_allowedArgTypes", deepcopy(cls._allowedArgTypes))
		cls._allowedArgTypes[argIndex].extend(allowedList)
		return cls
	return decorator


class AsmInstruction:
	_allowedArgTypes = {0: [], 1: []}
	
	def __init__(self, lineNum, opcode, argumentList):
		self.lineNum = lineNum
		self.opcode = opcode
		self.argumentList = argumentList
		self.acceptArguments()
	
	def __repr__(self):
		return "{}({}, \"{}\", {})".format(self.__class__.__name__, self.lineNum, self.opcode, self.argumentList)
	
	def assemble(self):
		return ""
		
	def acceptArguments(self):
		if len(self.argumentList) > 2:
			raise InvalidArgumentError("Too many arguments")
		
		for index, arg in enumerate(self.argumentList):
			if type(arg) not in self._allowedArgTypes[index]:
				raise InvalidArgumentError("Argument not allowed")

class Nop(AsmInstruction):
	def assemble(self):
		return "0000000000000000"

@accepts(0, RegNode, CommPortNode, ConstNode)
class Add(AsmInstruction):
	def assemble(self):
		if isinstance(self.argumentList[0], ConstNode):
			return Bits("0b10, 0b000, int:11={}".format(self.argumentList[0].value)).bin
		else:
			returnBits = Bits("0b0000, 0b{}, ".format(portToBin(self.argumentList[0].value)))
			returnBits += Bits("0b0") * (16 - len(returnBits))
			return returnBits.bin

@accepts(0, RegNode, CommPortNode, ConstNode)
@accepts(1, RegNode, CommPortNode)
class Mov(AsmInstruction):
	def assemble(self):
		if isinstance(self.argumentList[0], ConstNode):
			return Bits("0b11, 0b{}, int:11={}".format(portToBin(self.argumentList[1].value), self.argumentList[0].value)).bin
		else:
			returnBits = Bits("0b0001, 0b{}, 0b{}".format(portToBin(self.argumentList[0].value), portToBin(self.argumentList[1].value)))
			returnBits += Bits("0b0") * (16 - len(returnBits))
			return returnBits.bin

@accepts(0, RegNode, CommPortNode, ConstNode)
class Sub(AsmInstruction):
	def assemble(self):
		if isinstance(self.argumentList[0], ConstNode):
			return Add(self.opcode, self.argumentList).assemble()
		else:
			returnBits = Bits("0b0010, 0b{}".format(portToBin(self.argumentList[0].value)))
			returnBits += Bits("0b0") * (16 - len(returnBits))
			return returnBits.bin

class Neg(AsmInstruction):
	def assemble(self):
		return Bits("0b0011, 12*(0b0)").bin

class Sav(AsmInstruction):
	def assemble(self):
		return Bits("0b0100, 12*(0b0)").bin

class Swp(AsmInstruction):
	def assemble(self):
		return Bits("0b0101, 12*(0b0)").bin

@accepts(0, LabelMarker)
class Jmp(AsmInstruction):
	def assemble(self):
		returnBits = Bits("0b0110")
		returnBits += "0b" + jmpToMask(self.opcode)
		returnBits += "0b00000"
		returnBits += "uint:4={}".format(self.argumentList[0].lineNum)
		return returnBits.bin

@accepts(0, RegNode, CommPortNode, ConstNode)
class Jro(AsmInstruction):
	def assemble(self):
		returnBits = Bits("0b0111")
		if isinstance(self.argumentList[0], ConstNode):
			returnBits += "0b0000000"
			returnBits += "int:5={}".format(self.argumentList[0].value)
		else:
			returnBits += "0b{}1".format(portToBin(self.argumentList[0].value))
			returnBits += Bits("0b0") * (16 - len(returnBits))
		return returnBits.bin