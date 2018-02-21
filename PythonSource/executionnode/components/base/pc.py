__author__ = 'Zylanx'

from myhdl import *

from executionnode.utils import PCControlInterface

@block
def PC(clk, rst, clkEnable, controlBits: PCControlInterface, dataLoad, pcOut):
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
	count = Signal(modbv(0, 0, 16))
	
	@always_comb
	def outProc():
		pcOut.next = count
	
	@always_seq(clk.posedge, reset=rst)
	def clkProc():
		if clkEnable:
			if controlBits.load:
				count.next = dataLoad
			elif controlBits.inc:
				count.next = count + 1
	
	return outProc, clkProc