__author__ = 'Zylanx'

import os.path
from pathlib import Path

from myhdl import *

from executionnode.components import ControlUnit
from executionnode.utils import StatusBitInterface, PCControlInterface
from executionnode.utils import portType, commOpType, regOpType

def ConvertControlUnit(hdl, path):
	clk = Signal(bool(0))
	rst = ResetSignal(0, 1, False)
	clkEnable = Signal(bool(0))
	
	instr = Signal(intbv(0, 0, 2**16))
	
	commStart = Signal(bool(0))
	commPause = Signal(bool(0))
	commType = Signal(commOpType.RX)
	
	aluOp = Signal(intbv(0, 0, 4))
	aluStatusBits = StatusBitInterface()
	
	pcControlBits = PCControlInterface()
	
	# regOp = Signal(regOpType.NOP)
	regOp = Signal(bool(0))
	
	jmpEnable = Signal(bool(0))
	
	rxPort = Signal(portType.LEFT)
	txPort = Signal(portType.LEFT)
	
	inst = ControlUnit(clk, rst, clkEnable, instr, commPause, commStart, commType, aluOp, aluStatusBits, pcControlBits, regOp, jmpEnable, rxPort, txPort)
	inst.convert(hdl, path=path)


if __name__ == "__main__":
	convPath = (Path(os.path.dirname(os.path.realpath(__file__))) / "../../../VHDLSource").resolve()
	ConvertControlUnit("VHDL", convPath)