__author__ = 'Zylanx'

from myhdl import *

@block
def PC(clk, rst, ce, inc, load, load_data, pc_out):
	""" PC (Program Counter).
	
	inputs:
	clk -- clock
	rst -- reset
	ce -- clock enable
	
	load -- load value into program counter
	
	loac_data -- address to load in
	
	outputs:
	pc_out -- PC output value
	"""
	count = Signal(modbv(0, 0, 16))
	
	@always_comb
	def outProc():
		pc_out.next = count
	
	@always_seq(clk.posedge, reset=rst)
	def clkProc():
		if ce:
			if load:
				count.next = load_data
			elif inc:
				count.next = count + 1
	
	return outProc, clkProc

