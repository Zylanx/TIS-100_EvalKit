__author__ = 'Zylanx'

from myhdl import block, always_comb, always, intbv, Signal

from executionnode.components import InstrROM, InstrBreakout, ControlUnit, RegisterFile, ClampedPC, ALU, TransferControlUnit

from executionnode.utils import StatusBitInterface, CommInterface, PCControlInterface
from executionnode.utils import regOpEnum, portTypeEnum, aluOpEnum, commOpEnum, inputPipeSrcEnum

@block
def NodeCore(clk, rst, clkEnable, dataOut, rxLeft, txLeft, instrList):
	""""""
	""" Variables/Constants """
	
	""" Signals """
	# ROM
	addr = Signal(intbv(0, 0, 16))
	instr = Signal(intbv(0, 0, 2**16))
	
	# Instruction Breakout
	jmpDest = Signal(intbv(0, -999, 1000))
	jroOffset = Signal(intbv(0, -999, 1000))
	const = Signal(intbv(0, -999, 1000))
	
	# Control Unit
	inputPipeSrc = Signal(inputPipeSrcEnum.intbv(inputPipeSrcEnum.NIL))
	
	jmpEnable = Signal(bool(0))
	
	rxPort = Signal(portTypeEnum.intbv(portTypeEnum.NIL))
	txPort = Signal(portTypeEnum.intbv(portTypeEnum.NIL))
	
	# Register File
	regOp = Signal(regOpEnum.intbv(regOpEnum.NOP))
	dataPipeOut = Signal(intbv(0, -999, 1000))
	accOut = Signal(intbv(0, -999, 1000))
	dataPipeIn = Signal(intbv(0, -999, 1000))
	
	# PC
	pcControlBits = PCControlInterface()
	pcDataLoad = Signal(intbv(0, -999, 1000))
	
	# ALU
	aluStatusBits = StatusBitInterface() #
	aluOp = Signal(aluOpEnum.intbv(aluOpEnum.ADD))
	
	# Transfer Control Unit
	commStart = Signal(bool(0)) #
	commPause = Signal(bool(0)) #
	commType = Signal(commOpEnum.intbv(commOpEnum.RX))
	txData = Signal(intbv(0, -999, 1000))
	rxData = Signal(intbv(0, -999, 1000))
	
	# Others
	nil = Signal(intbv(0, -999, 1000))
	
	""" Instances """
	rom_1 = InstrROM(addr, instr, instrList)
	
	instr_breakout_1 = InstrBreakout(instr, jmpDest, jroOffset, const)
	control_unit_1 = ControlUnit(instr, commPause, commStart, commType, inputPipeSrc, aluOp, aluStatusBits, pcControlBits, regOp, jmpEnable, rxPort, txPort)
	registers_1 = RegisterFile(clk, rst, clkEnable, regOp, dataPipeOut, accOut, Signal(intbv(0, -999, 1000)), Signal(intbv(0, -999, 1000)))
	pc_1 = ClampedPC(clk, rst, clkEnable, pcControlBits, pcDataLoad, addr)
	alu_1 = ALU(accOut, dataPipeIn, aluOp, aluStatusBits, dataPipeOut)
	
	tcu_1 = TransferControlUnit(clk, rst, clkEnable, commStart, commPause, commType, rxPort, txPort, txData, rxData, rxLeft, CommInterface(-999, 1000), CommInterface(-999, 1000), CommInterface(-999, 1000), txLeft, CommInterface(-999, 1000), CommInterface(-999, 1000), CommInterface(-999, 1000))
	
	""" Processes """
	@always(nil)
	def nilProc():
		nil.next = 0
	
	@always_comb
	def pcDataLoadProc():
		pcDataLoad.next = dataPipeOut
	
	@always_comb
	def inputPipeProc():
		dataPipeIn.next = nil
		
		if inputPipeSrc == inputPipeSrcEnum.ACC:
			dataPipeIn.next = accOut
		elif inputPipeSrc == inputPipeSrcEnum.COMM_PORT:
			dataPipeIn.next = rxData
		elif inputPipeSrc == inputPipeSrcEnum.JMP_DEST:
			dataPipeIn.next = jmpDest
		elif inputPipeSrc == inputPipeSrcEnum.JRO_OFFSET:
			dataPipeIn.next = jroOffset
		elif inputPipeSrc == inputPipeSrcEnum.CONST:
			dataPipeIn.next = const
		else:
			pass
	
	@always_comb
	def txDataProc():
		txData.next = dataPipeOut
	
	@always_comb
	def dataOutProc():
		dataOut.next = rxData
		# dataOut.next = accOut
	
	return rom_1, instr_breakout_1, control_unit_1, registers_1, pc_1, alu_1, tcu_1, nilProc, pcDataLoadProc, inputPipeProc, txDataProc, dataOutProc