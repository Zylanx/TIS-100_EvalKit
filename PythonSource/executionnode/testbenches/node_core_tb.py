__author__ = 'Zylanx'

from random import randrange
from myhdl import *

from executionnode.components import NodeCore
from executionnode.utils import CommInterface

@block
def testbench():
	instrList_1 = (51300, 51220, 1024, 4736, 4160, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	instrList_2 = (0, 51210, 0, 0, 4736, 0, 5184, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	
	clk = Signal(bool(0))
	rst = ResetSignal(bool(1), bool(1), False)
	clkEnable = Signal(bool(1))
	dataOut_1 = Signal(intbv(0, -999, 1000))
	dataOut_2 = Signal(intbv(0, -999, 1000))
	
	rxLeft = CommInterface(-999, 1000)
	txLeft = CommInterface(-999, 1000)
	
	dut_1 = NodeCore(clk, rst, clkEnable, dataOut_1, rxLeft, txLeft, instrList_1)
	dut_2 = NodeCore(clk, rst, clkEnable, dataOut_2, txLeft, rxLeft, instrList_2)
	
	clkPeriod = delay(10)
	
	# @always(clkPeriod)
	@instance
	def clkProc():
		while True:
			clk.next = 0
			yield delay(10)
			clk.next = 1
			yield delay(10)
	
	@instance
	def stimProc():
		rst.next = 1
		yield clk.negedge
		rst.next = 0
		
		for i in range(20):
			yield clk.negedge
		
		raise StopSimulation
	
	# @instance
	# def monitor():
	# 	while 1:
	# 		yield delay(1)
	# 		# print(str(int(data_out)))
	# 		print("input1: {:d}, input2: {:d}, output: {:d}".format(int(input1), int(input2), int(output)))
	# 		print("eq: {}, gt: {}, lt: {}".format(int(eq), int(gt), int(lt)))
	
	return clkProc, stimProc, dut_1, dut_2


# tb = testbench()
# tb.config_sim(trace=True)
# tb.run_sim()
import os.path
from pathlib import Path
convPath = (Path(os.path.dirname(os.path.realpath(__file__))) / "../../../VHDLSource").resolve()
testbench().convert("VHDL", path=convPath)