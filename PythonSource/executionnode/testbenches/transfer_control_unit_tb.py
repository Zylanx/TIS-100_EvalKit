__author__ = 'Zylanx'

from random import randrange
from myhdl import *

from executionnode.components import TransferControlUnit
from executionnode.utils import CommInterface
from executionnode.utils import portTypeEnum, commOpEnum

@block
def testbench():
	clk = Signal(bool(0))
	rst = ResetSignal(1, 1, False)
	clkEnable = Signal(bool(1))
	
	commStart = Signal(bool(0))
	commPause = Signal(bool(0))
	commType = Signal(commOpEnum.intbv(commOpEnum.RX))
	
	rxPort = Signal(portTypeEnum.intbv(portTypeEnum.NIL))
	txPort = Signal(portTypeEnum.intbv(portTypeEnum.NIL))
	
	dataIn = Signal(intbv(0, -999, 1000))
	dataOut = Signal(intbv(0, -999, 1000))
	rxLeft = CommInterface(-999, 1000)
	txLeft = CommInterface(-999, 1000)
	
	dut = TransferControlUnit(clk, rst, clkEnable, commStart, commPause, commType, rxPort, txPort, dataIn, dataOut, rxLeft, CommInterface(-999, 1000), CommInterface(-999, 1000), CommInterface(-999, 1000), txLeft, CommInterface(-999, 1000), CommInterface(-999, 1000), CommInterface(-999, 1000))
	
	clkPeriod = delay(10)
	
	@always(clkPeriod)
	def clkProcess():
		clk.next = not clk
	
	@instance
	def stimProcess():
		yield clk.negedge
		rst.next = 0
		
		yield clk.negedge
		rxPort.next = portTypeEnum.LEFT
		txPort.next = portTypeEnum.LEFT
		
		yield clk.negedge
		rxLeft.req.next = 0
		rxLeft.data.next = 57
		commStart.next = 1
		
		yield clk.negedge
		commStart.next = 0
		rxLeft.req.next = 1
		
		yield clk.negedge
		rxLeft.req.next = 0
		rxLeft.data.next = 0
		
		yield clk.negedge
		rxLeft.req.next = 1
		rxLeft.data.next = 87
		commStart.next = 1
		
		yield clk.negedge
		rxLeft.req.next = 0
		rxLeft.data.next = 0
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
			print("commStart: {}, commPause: {}".format(bool(commStart), bool(commPause)))
			print("dataOut: {:d}".format(int(dataOut)))
			print("open: {}, req: {}, data: {:d}".format(bool(rxLeft.open), bool(rxLeft.req), int(rxLeft.data)))
			
	return clkProcess, stimProcess, dut, monitor


tb = testbench()
tb.config_sim(trace=True)
tb.run_sim()