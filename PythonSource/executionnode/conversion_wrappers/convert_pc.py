__author__ = 'Zylanx'

import os.path
from pathlib import Path

from myhdl import *

from executionnode.components import PC

def ConvertPC(hdl, path):
	clk = Signal(bool(0))
	rst = ResetSignal(0, 1, False)
	ce = Signal(bool(0))
	inc = Signal(bool(0))
	load = Signal(bool(0))
	load_data = Signal(modbv(0, 0, 16))
	pc_out = Signal(modbv(0, 0, 16))
	
	inst = PC(clk, rst, ce, inc, load, load_data, pc_out)
	inst.convert(hdl, path=path)
	
if __name__ == "__main__":
	convPath = (Path(os.path.dirname(os.path.realpath(__file__))) / "../../../VHDLSource").resolve()
	ConvertPC("VHDL", convPath)