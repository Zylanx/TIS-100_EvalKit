__author__ = 'Zylanx'

from myhdl import *


@block
def ALU(input1, input2, opType, output, eq, gt, lt):

	intAcc = Signal(intbv(0, -1998, 1999))
	tempOutput = Signal(intbv(0, -999, 1000))

	@always_comb
	def calcProc():
		if opType == 0:
			intAcc.next = input1 + input2
		elif opType == 1:
			intAcc.next = input2
		elif opType == 2:
			intAcc.next = -input1
		elif opType == 3:
			intAcc.next = input1 - input2
		else:
			intAcc.next = input1

	@always_comb
	def clampProc():
		if intAcc > 999:
			tempOutput.next = 999
		elif intAcc < -999:
			tempOutput.next = -999
		else:
			tempOutput.next = intAcc

	@always_comb
	def statusProc():
		eq.next = 0
		gt.next = 0
		lt.next = 0

		if tempOutput.val == 0:
			eq.next = 1
		if tempOutput.val > 0:
			gt.next = 1
		if tempOutput.val < 0:
			lt.next = 1

	@always_comb
	def tempOutputProc():
		output.next = tempOutput

	return calcProc, clampProc, statusProc, tempOutputProc