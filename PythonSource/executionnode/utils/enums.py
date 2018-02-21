__author__ = 'Zylanx'

from myhdl import enum

from functools import wraps

opcodeEnum = enum("ADD", "MOV", "SUB", "NEG", "SAV", "SWP", "JMP", "JRO")

portType = enum("NIL", "ACC", "LEFT", "RIGHT", "UP", "DOWN", "ANY", "LAST")

commOpType = enum("RX", "TX", "RX_TX")

regOpType = enum("NOP", "STORE", "SAV", "SWP")

def convToPortType(toConv):
	if toConv == 0:
		return portType.NIL
	elif toConv == 1:
		return portType.ACC
	elif toConv == 2:
		return portType.LEFT
	elif toConv == 3:
		return portType.RIGHT
	elif toConv == 4:
		return portType.UP
	elif toConv == 5:
		return portType.DOWN
	elif toConv == 6:
		return portType.ANY
	elif toConv == 7:
		return portType.LAST
	else:
		return portType.NIL

def convToOpcodeEnum(toConv):
	if toConv == 0:
		return opcodeEnum.ADD
	elif toConv == 1:
		return opcodeEnum.MOV
	elif toConv == 2:
		return opcodeEnum.SUB
	elif toConv == 3:
		return opcodeEnum.NEG
	elif toConv == 4:
		return opcodeEnum.SAV
	elif toConv == 5:
		return opcodeEnum.SWP
	elif toConv == 6:
		return opcodeEnum.JMP
	elif toConv == 7:
		return opcodeEnum.JRO
	else:
		return opcodeEnum.ADD