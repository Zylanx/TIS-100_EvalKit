__author__ = 'Zylanx'

from myhdl import block, always_comb, always_seq, intbv, Signal

from executionnode.utils import PCControlInterface, StatusBitInterface
from executionnode.utils import opcodeEnum, commOpType, regOpType, portType

from executionnode.utils.enums import convToPortType, convToOpcodeEnum

# ADD, MOV, SUB, NEG, SAV, SWP, JMP, JRO = range(8)

@block
def ControlUnit(clk, rst, clkEnable, instr, commPause, commStart, commType: commOpType, aluOp, aluStatusBits: StatusBitInterface, pcControlBits: PCControlInterface, regOp: regOpType, jmpEnable, rxPort, txPort):
	
	opcodeType = Signal(intbv(0)[0])
	opcode = Signal(intbv(0)[3:])
	src = Signal(intbv(0)[3:])
	dest = Signal(intbv(0)[3:])
	jmpFlags = Signal(intbv(0)[3:])
	jroType = Signal(intbv(0)[0])
	jroSrc = Signal(intbv(0)[3:])
	jroOffset = Signal(intbv(0)[5:])
	jmpDest = Signal(intbv(0)[4:])
	constDest = Signal(intbv(0)[3:])
	const = Signal(intbv(0)[11:])
	
	def isCommPort(testedPort):
		""" MyHDL's enum type is _MASSIVELY_ flawed. To the point
		 that it completely ruins the design and makes it impossible to convert around
		 like what should be possible without editing the design.
		 So instead I have to hard code values. """
		""" TODO: make an issue about this on the MyHDL repo """
		# TODO: make an issue about this on the MyHDL repo
		tempPort = int(testedPort.val)
		if tempPort == 0 or tempPort == 1:
			return False
		else:
			return True
	
	@always_comb
	def instrAliasProc():
		opcodeType.next = instr[15]
		opcode.next = instr[15:12]
		src.next = instr[12:9]
		dest.next = instr[9:6]
		jmpFlags.next = instr[12:9]
		jroType.next = instr[8]
		jroSrc.next = instr[12:9]
		jroOffset.next = instr[5:]
		jmpDest.next = instr[4:]
		constDest.next = instr[14:11]
		const.next = instr[11:]
	
	@always_comb
	def transferControlUnitProc():
		rxPort.next = convToPortType(src)
		txPort.next = convToPortType(dest)
		
	@always_comb
	def commTypeProc():
		commType.next = commOpType.RX
		
		if not opcodeType:
			if convToOpcodeEnum(opcode) == opcodeEnum.MOV:
				if isCommPort(src):
					if isCommPort(dest):
						commType.next = commOpType.RX_TX
				else:
					if isCommPort(dest):
						commType.next = commOpType.TX
		else:
			if isCommPort(constDest):
				commType.next = commOpType.TX
				
	@always_comb
	def aluOpProc():
		if convToOpcodeEnum(opcode) == opcodeEnum.ADD:
			pass
		elif convToOpcodeEnum(opcode) == opcodeEnum.MOV:
			pass
		elif convToOpcodeEnum(opcode) == opcodeEnum.SUB:
			pass
		elif convToOpcodeEnum(opcode) == opcodeEnum.NEG:
			pass
		elif convToOpcodeEnum(opcode) == opcodeEnum.SAV:
			pass
		elif convToOpcodeEnum(opcode) == opcodeEnum.SWP:
			pass
		elif convToOpcodeEnum(opcode) == opcodeEnum.JMP:
			pass
		elif convToOpcodeEnum(opcode) == opcodeEnum.JRO:
			pass
	
	return instrAliasProc, transferControlUnitProc, commTypeProc, aluOpProc