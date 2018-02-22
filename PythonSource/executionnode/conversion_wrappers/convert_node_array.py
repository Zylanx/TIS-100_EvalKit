__author__ = 'Zylanx'

import os.path
from pathlib import Path

from myhdl import *

from executionnode.components import NodeCore

from executionnode.utils import CommInterface

def ConvertNodeArray(hdl, path):
	instrList_1 = (51300, 51220, 1024, 4736, 4160, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	instrList_2 = (0, 51210, 0, 0, 4736, 0, 5184, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	
	clk = Signal(bool(0))
	rst = ResetSignal(bool(0), bool(1), False)
	clkEnable = Signal(bool(0))
	dataOut_1 = Signal(intbv(0, -999, 1000))
	dataOut_2 = Signal(intbv(0, -999, 1000))
	
	@block
	def NodeArray(clk, rst, clkEnable, dataOut_1, dataOut_2):
		rxLeft = CommInterface(-999, 1000)
		txLeft = CommInterface(-999, 1000)
		node_1 = NodeCore(clk, rst, clkEnable, dataOut_1, rxLeft, txLeft, instrList_1)
		node_2 = NodeCore(clk, rst, clkEnable, dataOut_2, txLeft, rxLeft, instrList_2)
		
		return node_1, node_2
	
	inst = NodeArray(clk, rst, clkEnable, dataOut_1, dataOut_2)
	inst.convert(hdl, path=path)


if __name__ == "__main__":
	convPath = (Path(os.path.dirname(os.path.realpath(__file__))) / "../../../VHDLSource").resolve()
	ConvertNodeArray("VHDL", convPath)