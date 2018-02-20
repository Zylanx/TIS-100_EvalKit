__author__ = 'Zylanx'

from random import randrange
from myhdl import *

from executionnode.components import PC

@block
def testbench():
	clk = Signal(bool(0))
	rst = ResetSignal(bool(1), bool(1), False)
	ce = Signal(bool(0))
	
	inc = Signal(bool(0))
	load = Signal(bool(0))
	
	load_data = Signal(intbv(0, 0, 16))
	pc_out = Signal(intbv(0, 0, 16))
	
	dut = PC(clk, rst, ce, inc, load, load_data, pc_out)
	
	clkPeriod = delay(10)
	
	@always(clkPeriod)
	def clkProcess():
		clk.next = not clk
	
	@instance
	def stimProcess():
		yield clk.negedge
		rst.next = 0
		ce.next = 1
		inc.next = 1
		
		for _ in range(50):
			inc.next = min(1, randrange(3))
			yield clk.negedge
		
		raise StopSimulation
	
	@instance
	def monitorProc():
		yield rst.negedge
		print(" inc | out")
		while True:
			yield clk.posedge
			yield delay(1)
			print("{!s:^5}|{!s:^5}".format(inc, int(pc_out)))
	
	return clkProcess, stimProcess, dut, monitorProc

tb = testbench()
# tb.config_sim(trace=True)
tb.run_sim()