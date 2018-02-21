__author__ = 'Zylanx'

from myhdl import block, always_comb, Signal, intbv

from executionnode.utils import StatusBitInterface

@block
def ALU(input1, input2, aluOpType, aluStatusBits: StatusBitInterface, dataOut):

	intAcc = Signal(intbv(0, -1998, 1999))
	outputInt = Signal(intbv(0, -999, 1000))

	@always_comb
	def calcProc():
		if aluOpType == 0:
			intAcc.next = input1 + input2
		elif aluOpType == 1:
			intAcc.next = input2
		elif aluOpType == 2:
			intAcc.next = -input1
		elif aluOpType == 3:
			intAcc.next = input1 - input2
		else:
			intAcc.next = input1

	@always_comb
	def clampProc():
		if intAcc > 999:
			outputInt.next = 999
		elif intAcc < -999:
			outputInt.next = -999
		else:
			outputInt.next = intAcc

	@always_comb
	def statusProc():
		aluStatusBits.eq.next = 0
		aluStatusBits.gt.next = 0
		aluStatusBits.lt.next = 0

		if outputInt.val == 0:
			aluStatusBits.eq.next = 1
		if outputInt.val > 0:
			aluStatusBits.gt.next = 1
		if outputInt.val < 0:
			aluStatusBits.lt.next = 1

	@always_comb
	def tempOutputProc():
		dataOut.next = outputInt

	return calcProc, clampProc, statusProc, tempOutputProc