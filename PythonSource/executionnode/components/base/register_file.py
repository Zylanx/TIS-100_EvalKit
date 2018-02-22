__author__ = 'Zylanx'

from myhdl import *

from executionnode.utils import regOpEnum

@block
def RegisterFile(clk, rst, clkEnable, regOp, dataIn, dataOut, debugACC, debugBAK):

	registerFile = [Signal(intbv(0, -999, 1000)) for _ in range(2)]
	curAcc = Signal(bool(0))
	
	@always_seq(clk.posedge, reset=rst)
	def clkProc():
		if clkEnable:
			if regOp == regOpEnum.STORE:
				registerFile[curAcc].next = dataIn
			elif regOp == regOpEnum.SAV:
				registerFile[not curAcc].next = registerFile[curAcc]
			elif regOp == regOpEnum.SWP:
				curAcc.next = not curAcc
	
	@always_comb
	def combProc():
		dataOut.next = registerFile[curAcc]
		
		# Set debug outputs
		debugACC.next = registerFile[curAcc]
		debugBAK.next = registerFile[not curAcc]

	return clkProc, combProc