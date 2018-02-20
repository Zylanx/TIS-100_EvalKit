__author__ = 'Zylanx'

from myhdl import enum, block, always_seq, always_comb, Signal, intbv

from executionnode.utils import CommInterface
from executionnode.utils.enums import commOpType, portType

stateType = enum("IDLE", "RX_TRANSFER", "TX_TRANSFER")


# TODO: THIS IS A BIG TODO!!! Remove the infered latchs

@block
def TransferControlUnit(clk, rst, clkEnable, commStart, commPause, commType, rxPort, txPort, dataIn, dataOut, rxLeft: CommInterface, rxRight: CommInterface, rxUp: CommInterface, rxDown: CommInterface, txLeft: CommInterface, txRight: CommInterface, txUp: CommInterface, txDown: CommInterface):
	
	state = Signal(stateType.IDLE)
	lastPort = Signal(portType.LAST)
	rxPortEquiv = Signal(portType.NIL)
	txPortEquiv = Signal(portType.NIL)
	
	receivedData = Signal(intbv(0, -999, 1000))
	
	rxOpen = Signal(bool(0))
	rxReq = Signal(bool(0))
	rxReady = Signal(bool(0))
	rxData = Signal(intbv(0, -999, 1000))
	
	txOpen = Signal(bool(0))
	txReq = Signal(bool(0))
	txReady = Signal(bool(0))
	txData = Signal(intbv(0, -999, 1000))
	
	@always_comb
	def transferPortSelectProc():
		rxLeft.open.next = 0
		rxRight.open.next = 0
		rxUp.open.next = 0
		rxDown.open.next = 0
		rxReq.next = 0
		rxData.next = 0
		rxPortEquiv.next = rxPort
		
		txOpen.next = 0
		txLeft.req.next = 0
		txRight.req.next = 0
		txUp.req.next = 0
		txDown.req.next = 0
		txLeft.data.next = txData
		txRight.data.next = txData
		txUp.data.next = txData
		txDown.data.next = txData
		txPortEquiv.next = txPort
		
		""" TODO: make it use the equivelent port so the any and last can be simplified
		 by the use of simply having it say which port to use and the normal routine
		 takes over as usual """
		if rxPort == portType.LEFT:
			rxLeft.open.next = rxOpen
			rxReq.next = rxLeft.req
			rxData.next = rxLeft.data
		elif rxPort == portType.RIGHT:
			rxRight.open.next = rxOpen
			rxReq.next = rxRight.req
			rxData.next = rxRight.data
		elif rxPort == portType.UP:
			rxUp.open.next = rxOpen
			rxReq.next = rxUp.req
			rxData.next = rxUp.data
		elif rxPort == portType.DOWN:
			rxDown.open.next = rxOpen
			rxReq.next = rxDown.req
			rxData.next = rxDown.data
		elif rxPort == portType.ANY:
			if rxLeft.req:
				rxLeft.open.next = rxOpen
				rxReq.next = rxLeft.req
				rxData.next = rxLeft.data
				rxPortEquiv.next = portType.LEFT
			elif rxRight.req:
				rxRight.open.next = rxOpen
				rxReq.next = rxRight.req
				rxData.next = rxRight.data
				rxPortEquiv.next = portType.RIGHT
			elif rxUp.req:
				rxUp.open.next = rxOpen
				rxReq.next = rxUp.req
				rxData.next = rxUp.data
				rxPortEquiv.next = portType.UP
			elif rxDown.req:
				rxDown.open.next = rxOpen
				rxReq.next = rxDown.req
				rxData.next = rxDown.data
				rxPortEquiv.next = portType.DOWN
			""" TODO: Check if this needs an extra clause for none requesting """
		elif rxPort == portType.LAST:
			rxPortEquiv.next = lastPort
			
			if lastPort == portType.LEFT:
				rxLeft.open.next = rxOpen
				rxReq.next = rxLeft.req
				rxData.next = rxLeft.data
			elif lastPort == portType.RIGHT:
				rxRight.open.next = rxOpen
				rxReq.next = rxRight.req
				rxData.next = rxRight.data
			elif lastPort == portType.UP:
				rxUp.open.next = rxOpen
				rxReq.next = rxUp.req
				rxData.next = rxUp.data
			elif lastPort == portType.DOWN:
				rxDown.open.next = rxOpen
				rxReq.next = rxDown.req
				rxData.next = rxDown.data
			""" TODO: Check if this needs an extra clause for no last port """
		else:
			pass
		
		""" TODO: make it use the equivelent port so the any and last can be simplified
		 by the use of simply having it say which port to use and the normal routine
		 takes over as usual """
		if txPort == portType.LEFT:
			txOpen.next = txLeft.open
			txLeft.req.next = txReq
		elif txPort == portType.RIGHT:
			txOpen.next = txRight.open
			txRight.req.next = txReq
		elif txPort == portType.UP:
			txOpen.next = txUp.open
			txUp.req.next = txReq
		elif txPort == portType.DOWN:
			txOpen.next = txDown.open
			txDown.req.next = txReq
		elif txPort == portType.ANY:
			""" Tx makes itself known to all ports first then
			chooses the port based on its priority. """
			txLeft.req.next = txReq
			txRight.req.next = txReq
			txUp.req.next = txReq
			txDown.req.next = txReq
			
			if txLeft.open:
				txLeft.req.next = txReq
				txRight.req.next = 0
				txUp.req.next = 0
				txDown.req.next = 0
				txOpen.next = txLeft.open
				txPortEquiv.next = portType.LEFT
			elif txRight.open:
				txLeft.req.next = 0
				txRight.req.next = txReq
				txUp.req.next = 0
				txDown.req.next = 0
				txOpen.next = txRight.open
				txPortEquiv.next = portType.RIGHT
			elif txUp.open:
				txLeft.req.next = 0
				txRight.req.next = 0
				txUp.req.next = txReq
				txDown.req.next = 0
				txOpen.next = txLeft.open
				txPortEquiv.next = portType.UP
			elif txDown.open:
				txLeft.req.next = 0
				txRight.req.next = 0
				txUp.req.next = 0
				txDown.req.next = txReq
				txOpen.next = txLeft.open
				txPortEquiv.next = portType.DOWN
		elif txPort == portType.LAST:
			txPortEquiv.next = lastPort
			
			if lastPort == portType.LEFT:
				txOpen.next = txLeft.open
				txLeft.req.next = txReq
			elif lastPort == portType.RIGHT:
				txOpen.next = txRight.open
				txRight.req.next = txReq
			elif lastPort == portType.UP:
				txOpen.next = txUp.open
				txUp.req.next = txReq
			elif lastPort == portType.DOWN:
				txOpen.next = txDown.open
				txDown.req.next = txReq
		else:
			pass
	
	@always_comb
	def transferStatusBitsProc():
		""" This is a work around for
		'myhdl.AlwaysCombError: signal ({'rxReq', 'txOpen'}) used as inout in always_comb function argument' """
		rxReady.next = 0
		txReady.next = 0
		
		if rxOpen and rxReq:
			rxReady.next = 1
		if txOpen and txReq:
			txReady.next = 1
	
	@always_seq(clk.posedge, reset=rst)
	def fsmProc():
		if clkEnable:
			if state == stateType.IDLE:
				if commStart:
					if commType == commOpType.Rx:
						if not rxReady:
							state.next = stateType.RX_TRANSFER
						else:
							lastPort.next = rxPortEquiv
					elif commType == commOpType.Tx:
						state.next = stateType.TX_TRANSFER
					elif commType == commOpType.RxTx:
						if not rxReady:
							state.next = stateType.RX_TRANSFER
						else:
							receivedData.next = rxData
							lastPort.next = rxPortEquiv
							state.next = stateType.TX_TRANSFER
					# TODO: Add an else that locks everything up
			elif state == stateType.RX_TRANSFER:
				if rxReady:
					lastPort.next = rxPortEquiv
					if commType == commOpType.Rx:
						state.next = stateType.IDLE
					else: # commType == commOpType.RxTx
						receivedData.next = rxData
						state.next = stateType.TX_TRANSFER
			elif state == stateType.TX_TRANSFER:
				if txReady:
					lastPort.next = txPortEquiv
					state.next = stateType.IDLE
	
	@always_comb
	def fsmOutputProc():
		commPause.next = 0
		rxOpen.next = 0
		txReq.next = 0
		dataOut.next = 0
		txData.next = 0
		
		if state == stateType.IDLE:
			if commStart:
				commPause.next = 1
				
				if rxReady:
					dataOut.next = rxData
				
				if commType == commOpType.Rx:
					rxOpen.next = 1
					
					if rxReady:
						commPause.next = 0
				elif commType == commOpType.RxTx:
					rxOpen.next = 1
		elif state == stateType.RX_TRANSFER:
			commPause.next = 1
			rxOpen.next = 1
			
			if rxReady:
				dataOut.next = rxData
				if commType == commOpType.Rx:
					commPause.next = 0
		elif state == stateType.TX_TRANSFER:
			commPause.next = 1
			txReq.next = 1
			
			if commType == commOpType.Tx:
				txData.next = dataIn
			elif commType == commOpType.RxTx:
				txData.next = receivedData
				
			if txReady:
				commPause.next = 0
	
	
	return transferPortSelectProc, transferStatusBitsProc, fsmProc, fsmOutputProc