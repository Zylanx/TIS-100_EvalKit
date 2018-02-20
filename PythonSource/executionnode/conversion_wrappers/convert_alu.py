__author__ = 'Zylanx'

import os.path
from pathlib import Path

from myhdl import *

from executionnode.components import ALU

def ConvertALU(hdl, path):
	input1 = Signal(intbv(0, -999, 1000))
	input2 = Signal(intbv(0, -999, 1000))
	opType = Signal(intbv(0, 0, 4))
	output = Signal(intbv(0, -999, 1000))
	eq = Signal(bool(0))
	gt = Signal(bool(0))
	lt = Signal(bool(0))
	
	inst = ALU(input1, input2, opType, output, eq, gt, lt)
	inst.convert(hdl, path=path)
	
if __name__ == "__main__":
	convPath = (Path(os.path.dirname(os.path.realpath(__file__))) / "../../../VHDLSource").resolve()
	ConvertALU("VHDL", convPath)