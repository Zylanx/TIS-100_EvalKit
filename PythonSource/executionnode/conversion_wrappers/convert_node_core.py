__author__ = 'Zylanx'

import os.path
from pathlib import Path

from myhdl import *

from executionnode.components import NodeCore

from executionnode.utils import CommInterface

def ConvertNodeCore(hdl, path):
	instrList = (51300, 51220, 1024, 4736, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	
	clk = Signal(bool(0))
	rst = ResetSignal(bool(0), bool(1), False)
	clkEnable = Signal(bool(0))
	dataOut = Signal(intbv(0, -999, 1000))
	rxLeft = CommInterface(-999, 1000)
	txLeft = CommInterface(-999, 1000)
	
	inst = NodeCore(clk, rst, clkEnable, dataOut, rxLeft, txLeft, instrList)
	inst.convert(hdl, path=path)

if __name__ == "__main__":
	convPath = (Path(os.path.dirname(os.path.realpath(__file__))) / "../../../VHDLSource").resolve()
	ConvertNodeCore("VHDL", convPath)