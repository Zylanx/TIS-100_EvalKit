__author__ = 'Zylanx'

from myhdl import *

@block
def InstrBreakout(instr, jmpDest, jroOffset, const):
	""" TODO: Surely I don't need to use something like this?"""
	
	@always_comb
	def breakoutProc():
		jmpDest.next = instr[4:]
		jroOffset.next = instr[5:].signed()
		if instr[11:].signed() > 999:
			const.next = 999
		elif instr[11:].signed() < -999:
			const.next = -999
		else:
			const.next = instr[11:].signed()
	
	return breakoutProc