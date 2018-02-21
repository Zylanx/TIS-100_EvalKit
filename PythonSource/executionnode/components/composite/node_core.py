__author__ = 'Zylanx'

from myhdl import block, always_comb, always_seq, intbv, Signal

from executionnode.components import InstrROM, ControlUnit, RegisterFile, ClampedPC, ALU, TransferControlUnit

from executionnode.utils import StatusBitInterface
from executionnode.utils import regOpType

@block
def NodeCore(clk, rst, clkEnable, rxLeft, txLeft):
	""""""
	""" Variables/Constants """
	instrList = (128, 253, 0, 2)
	
	""" Signals """
	# ROM
	addr = Signal(intbv(0, 0, 16)) #
	instr = Signal(intbv(0, 0, 2**16)) #
	
	# Control Unit
	jmpEnable = Signal(0) #
	
	rxPort = Signal(0) #
	txPort = Signal(0) #
	
	# Register File
	regOp = Signal(regOpType.NOP) #
	dataPipeOut = Signal(intbv(0, -999, 1000))
	accOut = Signal(intbv(0, -999, 1000))
	dataPipeIn = Signal(intbv(0, -999, 1000))
	
	# PC
	pcControlBits = Signal(bool(0)) #
	pcDataLoad = Signal(intbv(0, -999, 1000))
	
	# ALU
	aluStatusBits = StatusBitInterface() #
	aluOp = Signal(0) #
	
	# Transfer Control Unit
	commStart = Signal(bool(0)) #
	commPause = Signal(bool(0)) #
	commType = Signal(bool(0)) #
	txData = Signal(intbv(0, -999, 1000))
	rxData = Signal(intbv(0, -999, 1000))
	
	""" Instances """
	rom_1 = InstrROM(addr, instr, instrList)
	
	control_unit_1 = ControlUnit(clk, rst, clkEnable, instr, aluStatusBits, jmpEnable, rxPort, txPort)
	registers_1 = RegisterFile(clk, rst, clkEnable, regOp, dataPipeOut, accOut, Signal(0), Signal(0))
	pc_1 = ClampedPC(clk, rst, clkEnable, pcControlBits, pcDataLoad, addr)
	alu_1 = ALU(accOut, dataPipeIn, aluOp, aluStatusBits, dataPipeOut)
	
	tcu_1 = TransferControlUnit(clk, rst, clkEnable, commStart, commPause, commType, rxPort, txPort, txData, rxData, rxLeft, Signal(0), Signal(0), Signal(0), txLeft, Signal(0), Signal(0), Signal(0))
	
	return rom_1, control_unit_1, registers_1, pc_1, alu_1, tcu_1