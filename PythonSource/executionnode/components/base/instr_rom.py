__author__ = 'Zylanx'

from myhdl import *


@block
def InstrROM(addr, dataOut, instrList):
	""" TODO: Add more complex instrList helper funcs"""
	
	@always_comb
	def romProc():
		dataOut.next = instrList[int(addr)]
	
	return romProc