__author__ = 'Zylanx'

__author__ = 'Zylanx'

from random import randrange
from myhdl import *

from executionnode.components import ALU

@block
def testbench():
	input1 = Signal(intbv(0, -999, 1000))
	input2 = Signal(intbv(0, -999, 1000))
	opType = Signal(intbv(0, 0, 4))
	output = Signal(intbv(0, -999, 1000))
	eq = Signal(bool())
	gt = Signal(bool())
	lt = Signal(bool())
	
	dut = ALU(input1, input2, opType, output, eq, gt, lt)
	
	@instance
	def stimProcess():
		yield delay(1)
		input1.next = 100
		
		yield delay(1)
		input1.next = -100
		
		yield delay(1)
		input1.next = 0
		
		yield delay(1)
		input1.next = -999
		
		yield delay(1)
		input1.next = 999
		
		yield delay(1)
		input2.next = -999
		
		yield delay(1)
		input1.next = 0
		
		yield delay(1)
		input1.next = -999
		
		yield delay(2)
		
		raise StopSimulation
	
	@instance
	def monitor():
		while 1:
			yield delay(1)
			# print(str(int(data_out)))
			print("input1: {:d}, input2: {:d}, output: {:d}".format(int(input1), int(input2), int(output)))
			print("eq: {}, gt: {}, lt: {}".format(int(eq), int(gt), int(lt)))
	
	return stimProcess, dut, monitor


tb = testbench()
# tb.config_sim(trace=True)
tb.run_sim()