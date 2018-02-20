__author__ = 'Zylanx'

from myhdl import *

@block
def PCClamper(data_in, data_out):
	
	@always_comb
	def combProc():
		if data_in > 15:
			data_out.next = 15
		elif data_in < 0:
			data_out.next = 0
		else:
			data_out.next = data_in
			
	return combProc