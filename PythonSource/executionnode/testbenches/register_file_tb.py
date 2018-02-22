__author__ = 'Zylanx'

from random import randrange
from myhdl import *

from executionnode.components import RegisterFile

from executionnode.utils import regOpEnum

@block
def testbench():
	clk = Signal(bool(0))
	rst = ResetSignal(1, 1, False)
	clkEnable = Signal(bool(1))
	
	regOp = Signal(regOpEnum.intbv(regOpEnum.NOP))
	data_in = Signal(intbv(0, -999, 1000))
	data_out = Signal(intbv(0, -999, 1000))
	
	acc = Signal(intbv(0, -999, 1000))
	bak = Signal(intbv(0, -999, 1000))
	
	dut = RegisterFile(clk, rst, clkEnable, regOp, data_in, data_out, acc, bak)
	
	clkPeriod = delay(10)
	
	@always(clkPeriod)
	def clkProcess():
		clk.next = not clk
	
	@instance
	def stimProcess():
		yield clk.negedge
		rst.next = 0
		
		regOp.next = regOpEnum.STORE
		data_in.next = 20
		yield clk.negedge
		
		regOp.next = regOpEnum.SWP
		yield clk.negedge
		
		regOp.next = regOpEnum.STORE
		data_in.next = 999
		yield clk.negedge
		
		regOp.next = regOpEnum.SWP
		yield clk.negedge
		
		regOp.next = regOpEnum.SAV
		yield clk.negedge
		
		regOp.next = regOpEnum.NOP
		yield clk.negedge
		
		raise StopSimulation
	
	@instance
	def monitor():
		yield rst.negedge
		while 1:
			yield clk.posedge
			yield delay(1)
			# print(str(int(data_out)))
			print("regOp: {}".format(regOpEnum.toStr(regOp.val)))
			print("acc: {:d}, bak: {:d}".format(int(acc), int(bak)))
			
	return clkProcess, stimProcess, dut, monitor


tb = testbench()
# tb.config_sim(trace=True)
tb.run_sim()