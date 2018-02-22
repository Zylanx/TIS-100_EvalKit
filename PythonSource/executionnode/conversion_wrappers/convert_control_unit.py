__author__ = 'Zylanx'

import os.path
from pathlib import Path

from myhdl import *

from executionnode.components import ControlUnit
from executionnode.utils import StatusBitInterface, PCControlInterface
from executionnode.utils import portTypeEnum, commOpEnum, regOpEnum, aluOpEnum, inputPipeSrcEnum

def ConvertControlUnit(hdl, path):
	instr = Signal(intbv(0, 0, 2**16))
	
	commStart = Signal(bool(0))
	commPause = Signal(bool(0))
	commType = Signal(commOpEnum.intbv(commOpEnum.RX))
	
	aluInputPipeSource = Signal(inputPipeSrcEnum.intbv())
	aluOp = Signal(aluOpEnum.intbv(aluOpEnum.ADD))
	aluStatusBits = StatusBitInterface()
	
	pcControlBits = PCControlInterface()
	
	# regOp = Signal(regOpType.NOP)
	regOp = Signal(regOpEnum.intbv(regOpEnum.NOP))
	
	jmpEnable = Signal(bool(0))
	
	rxPort = Signal(portTypeEnum.intbv(portTypeEnum.NIL))
	txPort = Signal(portTypeEnum.intbv(portTypeEnum.NIL))
	
	inst = ControlUnit(instr, commPause, commStart, commType, aluInputPipeSource, aluOp, aluStatusBits, pcControlBits, regOp, jmpEnable, rxPort, txPort)
	inst.convert(hdl, path=path)


if __name__ == "__main__":
	convPath = (Path(os.path.dirname(os.path.realpath(__file__))) / "../../../VHDLSource").resolve()
	ConvertControlUnit("VHDL", convPath)