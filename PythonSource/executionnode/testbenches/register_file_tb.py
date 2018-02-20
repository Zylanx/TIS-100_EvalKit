__author__ = 'Zylanx'

from random import randrange
from myhdl import *

from executionnode.components import RegisterFile

@block
def testbench():
	clk = Signal(bool(0))
	rst = ResetSignal(1, 1, False)
	ce = Signal(bool(1))
	
	load = Signal(bool(0))
	sav = Signal(bool(0))
	swp = Signal(bool(0))
	data_in = Signal(intbv(0, -999, 1000))
	data_out = Signal(intbv(0, -999, 1000))
	
	acc = Signal(intbv(0, -999, 1000))
	bak = Signal(intbv(0, -999, 1000))
	
	dut = RegisterFile(clk, rst, ce, load, sav, swp, data_in, data_out, acc, bak)
	
	clkPeriod = delay(10)
	
	@always(clkPeriod)
	def clkProcess():
		clk.next = not clk
	
	@instance
	def stimProcess():
		yield clk.negedge
		rst.next = 0
		
		load.next = 1
		data_in.next = 20
		yield clk.negedge
		
		load.next = 0
		swp.next = 1
		yield clk.negedge
		
		swp.next = 0
		load.next = 1
		data_in.next = 999
		yield clk.negedge
		
		load.next = 0
		swp.next = 1
		yield clk.negedge
		
		swp.next = 0
		sav.next = 1
		yield clk.negedge
		
		sav.next = 0
		yield clk.negedge
		
		raise StopSimulation
	
	@instance
	def monitor():
		yield rst.negedge
		while 1:
			yield clk.posedge
			yield delay(1)
			# print(str(int(data_out)))
			print("load: {}, sav: {}, swp: {}".format(bool(load), bool(sav), bool(swp)))
			print("acc: {:d}, bak: {:d}".format(int(acc), int(bak)))
			
	return clkProcess, stimProcess, dut, monitor


tb = testbench()
# tb.config_sim(trace=True)
tb.run_sim()