__author__ = 'Zylanx'

from random import randrange
from myhdl import *

from executionnode.components import TransferControlUnit
from executionnode.utils import CommInterface

@block
def testbench():
	clk = Signal(bool(0))
	rst = ResetSignal(1, 1, False)
	clkEnable = Signal(bool(1))
	
	commStart = Signal(bool(0))
	commPause = Signal(bool(0))
	dataOut = Signal(intbv(0, -999, 1000))
	rxPort = CommInterface(-999, 1000)
	
	dut = TransferControlUnit(clk, rst, clkEnable, commStart, commPause, dataOut, rxPort)
	
	clkPeriod = delay(10)
	
	@always(clkPeriod)
	def clkProcess():
		clk.next = not clk
	
	@instance
	def stimProcess():
		yield clk.negedge
		rst.next = 0
		
		yield clk.negedge
		rxPort.req.next = 0
		rxPort.data.next = 57
		commStart.next = 1
		
		yield clk.negedge
		commStart.next = 0
		rxPort.req.next = 1
		
		yield clk.negedge
		rxPort.req.next = 0
		rxPort.data.next = 0
		
		yield clk.negedge
		rxPort.req.next = 1
		rxPort.data.next = 87
		commStart.next = 1
		
		yield clk.negedge
		rxPort.req.next = 0
		rxPort.data.next = 0
		commStart.next = 0
		
		yield clk.negedge
		
		raise StopSimulation
	
	@instance
	def monitor():
		yield rst.negedge
		while True:
			yield clk.posedge
			yield delay(1)
			print("---------")
			# print(str(int(data_out)))
			print("commStart: {}, commPause: {}".format(bool(commStart), bool(commPause)))
			print("dataOut: {:d}".format(int(dataOut)))
			print("open: {}, req: {}, data: {:d}".format(bool(rxPort.open), bool(rxPort.req), int(rxPort.data)))
			
	return clkProcess, stimProcess, dut, monitor


tb = testbench()
# tb.config_sim(trace=True)
tb.run_sim()