__author__ = 'Zylanx'

from myhdl import *

@block
def PCClamper(dataIn, dataOut):
	
	@always_comb
	def combProc():
		if dataIn > 15:
			dataOut.next = 15
		elif dataIn < 0:
			dataOut.next = 0
		else:
			dataOut.next = dataIn
			
	return combProc