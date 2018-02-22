__author__ = 'Zylanx'

import os.path
from pathlib import Path

from myhdl import Signal, ResetSignal, intbv

from executionnode.components import TransferControlUnit
from executionnode.utils import CommInterface
from executionnode.utils import portTypeEnum, commOpEnum

def ConvertTransferControlUnit(hdl, path):
	clk = Signal(bool(0))
	rst = ResetSignal(bool(0), bool(1), False)
	clkEnable = Signal(bool(0))
	commStart = Signal(bool(0))
	commPause = Signal(bool(0))
	commType = Signal(commOpEnum.intbv(commOpEnum.RX))
	
	rxPort = Signal(portTypeEnum.intbv())
	txPort = Signal(portTypeEnum.intbv())
	
	dataIn = Signal(intbv(0, -999, 1000))
	dataOut = Signal(intbv(0, -999, 1000))

	rxLeft = CommInterface(-999, 1000)
	rxRight = CommInterface(-999, 1000)
	rxUp = CommInterface(-999, 1000)
	rxDown = CommInterface(-999, 1000)
	txLeft = CommInterface(-999, 1000)
	txRight = CommInterface(-999, 1000)
	txUp = CommInterface(-999, 1000)
	txDown = CommInterface(-999, 1000)
	
	inst = TransferControlUnit(clk, rst, clkEnable, commStart, commPause, commType, rxPort, txPort, dataIn, dataOut, rxLeft, rxRight, rxUp, rxDown, txLeft, txRight, txUp, txDown)
	inst.convert(hdl, path=path)


if __name__ == "__main__":
	convPath = (Path(os.path.dirname(os.path.realpath(__file__))) / "../../../VHDLSource").resolve()
	ConvertTransferControlUnit("VHDL", convPath)