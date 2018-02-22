__author__ = 'Zylanx'

from myhdl import block, Signal, intbv

from executionnode.components import PC, PCClamper

@block
def ClampedPC(clk, rst, clkEnable, pcControlBits, dataLoad, pcOut):
	""" PC (Program Counter).

	inputs:
	clk -- clock
	rst -- reset
	clkEnable -- clock enable

	load -- load value into program counter

	dataLoad -- data to load in

	outputs:
	pcOut -- PC output value
	"""
	clampedData = Signal(intbv(0, 0, 16))
	
	pc_clamp_1 = PCClamper(dataLoad, clampedData)
	pc_1 = PC(clk, rst, clkEnable, pcControlBits, clampedData, pcOut)
	
	return pc_clamp_1, pc_1