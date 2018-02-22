__author__ = 'Zylanx'

from myhdl import block, always_comb, always_seq, intbv, Signal

from executionnode.utils import PCControlInterface, StatusBitInterface
from executionnode.utils import opcodeEnum, commOpEnum, regOpEnum, portTypeEnum, aluOpEnum, inputPipeSrcEnum

# Workaround for MyHDL analysis being unable to process module attributes while in functions
portTypeEnum_NIL = portTypeEnum.NIL
portTypeEnum_ACC = portTypeEnum.ACC


# TODO: This could be optimised by doing things _properly_.


# TODO: This needs a whole redesign.
# When I was first designed this, I was still learning VHDL.
# I still am, but I have a bit more of an idea about design now and it is very poor in this.

@block
def ControlUnit(instr, commPause, commStart, commType, inputPipeSrc, aluOp, aluStatusBits: StatusBitInterface, pcControlBits: PCControlInterface, regOp, jmpEnable, rxPort, txPort):
	
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
		tempPort = int(testedPort.val)
		if tempPort == portTypeEnum_NIL or tempPort == portTypeEnum_ACC:
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
	def tcuPortProc():
		rxPort.next = src
		txPort.next = dest
		
	@always_comb
	def commTypeProc():
		commType.next = commOpEnum.RX
		
		if not opcodeType:
			if opcode == opcodeEnum.MOV:
				if isCommPort(src):
					if isCommPort(dest):
						commType.next = commOpEnum.RX_TX
				else:
					if isCommPort(dest):
						commType.next = commOpEnum.TX
		else:
			if isCommPort(constDest):
				commType.next = commOpEnum.TX
				
	@always_comb
	def aluOpProc():
		aluOp.next = aluOpEnum.ADD
		
		if opcodeType == 0:
			if opcode == opcodeEnum.MOV:
				# TODO: This is a big one. Remove the alu from the loop for moving. Will likely slightly decrease time
				aluOp.next = aluOpEnum.PASS_OTHER
			elif opcode == opcodeEnum.SUB:
				aluOp.next = aluOpEnum.SUB
			elif opcode == opcodeEnum.NEG:
				aluOp.next = aluOpEnum.NEG
			elif opcode == opcodeEnum.JMP:
				aluOp.next = aluOpEnum.PASS_OTHER
			elif opcode == opcodeEnum.JRO:
				aluOp.next = aluOpEnum.PASS_OTHER
			else:
				pass
		elif opcodeType == 1: # Special Opcodes
			if opcode[2] == opcodeEnum.ADD:
				""" ADD
				Handled by the initial value """
				pass
			else:
				""" MOV """
				aluOp.next = aluOpEnum.PASS_OTHER
		else:
			pass
	
	@always_comb
	def aluInputPipeProc():
		""" TODO: This is a terrible way to do this and needs a redesign """
		inputPipeSrc.next = inputPipeSrcEnum.NIL
		
		if opcodeType == 0:
			if opcode == opcodeEnum.JRO and jroType == 0:
				inputPipeSrc.next = inputPipeSrcEnum.JRO_OFFSET
			else:
				if src == portTypeEnum.NIL:
					pass
				elif src == portTypeEnum.ACC:
					inputPipeSrc.next = inputPipeSrcEnum.ACC
				else:
					inputPipeSrc.next = inputPipeSrcEnum.COMM_PORT
		else:
			inputPipeSrc.next = inputPipeSrcEnum.CONST
			
	@always_comb
	def jmpEnableProc():
		jmpEnable.next = 0
		
		if opcodeType == 0:
			if opcode == opcodeEnum.JRO:
				jmpEnable.next = 1
			elif opcode == opcodeEnum.JMP:
				if jmpFlags[2] and aluStatusBits.eq: # Equal to 0
					jmpEnable.next = 1
				elif jmpFlags[1] and aluStatusBits.gt:
					jmpEnable.next = 1
				elif jmpFlags[0] and aluStatusBits.lt:
					jmpEnable.next = 1
	
	# TODO: Check this actually covers all cases
	@always_comb
	def commStartProc():
		commStart.next = 0
		
		if opcodeType == 0:
			if opcode == opcodeEnum.ADD:
				if isCommPort(src):
					commStart.next = 1
			elif opcode == opcodeEnum.MOV:
				if isCommPort(src) or isCommPort(dest):
					commStart.next = 1
			elif opcode == opcodeEnum.SUB:
				if isCommPort(src):
					commStart.next = 1
			elif opcode == opcodeEnum.JRO:
				if jroType:
					if isCommPort(jroSrc):
						commStart.next = 1
		else:
			if opcode[2] == opcodeEnum.MOV:
				if isCommPort(constDest):
					commStart.next = 1
	
	@always_comb
	def pcControlProc():
		pcControlBits.inc.next = 0
		pcControlBits.load.next = 0
		
		if not commPause:
			pcControlBits.inc.next = 1
			
	@always_comb
	def regControlProc():
		regOp.next = regOpEnum.NOP
		
		if not commPause:
			if not opcodeType:
				if opcode == opcodeEnum.ADD:
					regOp.next = regOpEnum.STORE
				elif opcode == opcodeEnum.MOV:
					if dest == portTypeEnum.ACC:
						regOp.next = regOpEnum.STORE
				elif opcode == opcodeEnum.SUB:
					regOp.next = regOpEnum.STORE
				elif opcode == opcodeEnum.NEG:
					regOp.next = regOpEnum.STORE
				elif opcode == opcodeEnum.SAV:
					regOp.next = regOpEnum.SAV
				elif opcode == opcodeEnum.SWP:
					regOp.next = regOpEnum.SWP
			else:
				if opcode[2] == opcodeEnum.ADD:
					regOp.next = regOpEnum.STORE
				else:
					if constDest == portTypeEnum.ACC:
						regOp.next = regOpEnum.STORE
			
	
	return instrAliasProc, tcuPortProc, commTypeProc, aluOpProc, aluInputPipeProc, jmpEnableProc, commStartProc, pcControlProc, regControlProc