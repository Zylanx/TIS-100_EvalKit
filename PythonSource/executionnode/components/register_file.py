__author__ = 'Zylanx'

from myhdl import *

@block
def RegisterFile(clk, rst, ce, load, sav, swp, data_in, data_out, acc, bak):

	registerFile = [Signal(intbv(0, -999, 1000)) for i in range(2)]
	curAcc = Signal(bool(0))
	
	@always_seq(clk.posedge, reset=rst)
	def clkProc():
		if ce:
			if load:
				registerFile[curAcc].next = data_in
			elif sav:
				registerFile[not curAcc].next = registerFile[curAcc]
			elif swp:
				curAcc.next = not curAcc
	
	# @always_seq(clk.posedge, reset=rst)
	# def swapProc():
	# 	nonlocal curAcc
	#
	# 	if ce:
	# 		if swp:
	# 			curAcc = not curAcc
	#
	# @always_seq(clk.posedge, reset=rst)
	# def loadProc():
	# 	nonlocal curAcc
	#
	# 	if ce:
	# 		if load:
	# 			registerFile[curAcc].next = data_in
	
	@always_comb
	def combProc():
		data_out.next = registerFile[curAcc]
		acc.next = registerFile[curAcc]
		bak.next = registerFile[not curAcc]
	
	# return swapProc, loadProc, combProc
	return clkProc, combProc