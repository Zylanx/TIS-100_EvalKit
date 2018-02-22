__author__ = 'Zylanx'

from myhdl import enum, block, always_seq, always_comb, Signal, intbv

from executionnode.utils import CommInterface
from executionnode.utils.enums import commOpEnum, portTypeEnum

# Note: This has been done, but will be kept as an ongoing check
# TODO: THIS IS A BIG TODO!!! Remove the inferred latches


# TODO: Change rxData to always pulling in the data from the assumed port, regardless of if the transfer is ready


# TODO: Check the holding of Receiving ports .open. May need to be extended?


# TODO: Definitely needs optimisations.
# 128 multiplexers seems a bit much? Although there is a ton of data being multiplexed

@block
def TransferControlUnit(clk, rst, clkEnable, commStart, commPause, commType, rxPort, txPort, dataIn, dataOut, rxLeft: CommInterface, rxRight: CommInterface, rxUp: CommInterface, rxDown: CommInterface, txLeft: CommInterface, txRight: CommInterface, txUp: CommInterface, txDown: CommInterface):
	stateType = enum("IDLE", "RX_TRANSFER", "TX_TRANSFER")
	
	state = Signal(stateType.IDLE)
	lastPort = Signal(portTypeEnum.intbv(portTypeEnum.LAST))
	rxPortEquiv = Signal(portTypeEnum.intbv())
	txPortEquiv = Signal(portTypeEnum.intbv())
	
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
		if rxPort == portTypeEnum.LEFT:
			rxLeft.open.next = rxOpen
			rxReq.next = rxLeft.req
			rxData.next = rxLeft.data
		elif rxPort == portTypeEnum.RIGHT:
			rxRight.open.next = rxOpen
			rxReq.next = rxRight.req
			rxData.next = rxRight.data
		elif rxPort == portTypeEnum.UP:
			rxUp.open.next = rxOpen
			rxReq.next = rxUp.req
			rxData.next = rxUp.data
		elif rxPort == portTypeEnum.DOWN:
			rxDown.open.next = rxOpen
			rxReq.next = rxDown.req
			rxData.next = rxDown.data
		elif rxPort == portTypeEnum.ANY:
			if rxLeft.req:
				rxLeft.open.next = rxOpen
				rxReq.next = rxLeft.req
				rxData.next = rxLeft.data
				rxPortEquiv.next = portTypeEnum.LEFT
			elif rxRight.req:
				rxRight.open.next = rxOpen
				rxReq.next = rxRight.req
				rxData.next = rxRight.data
				rxPortEquiv.next = portTypeEnum.RIGHT
			elif rxUp.req:
				rxUp.open.next = rxOpen
				rxReq.next = rxUp.req
				rxData.next = rxUp.data
				rxPortEquiv.next = portTypeEnum.UP
			elif rxDown.req:
				rxDown.open.next = rxOpen
				rxReq.next = rxDown.req
				rxData.next = rxDown.data
				rxPortEquiv.next = portTypeEnum.DOWN
			""" TODO: Check if this needs an extra clause for none requesting """
		elif rxPort == portTypeEnum.LAST:
			rxPortEquiv.next = lastPort
			
			if lastPort == portTypeEnum.LEFT:
				rxLeft.open.next = rxOpen
				rxReq.next = rxLeft.req
				rxData.next = rxLeft.data
			elif lastPort == portTypeEnum.RIGHT:
				rxRight.open.next = rxOpen
				rxReq.next = rxRight.req
				rxData.next = rxRight.data
			elif lastPort == portTypeEnum.UP:
				rxUp.open.next = rxOpen
				rxReq.next = rxUp.req
				rxData.next = rxUp.data
			elif lastPort == portTypeEnum.DOWN:
				rxDown.open.next = rxOpen
				rxReq.next = rxDown.req
				rxData.next = rxDown.data
			else:
				pass
			""" TODO: Check if this needs an extra clause for no last port """
		else:
			pass
		
		""" TODO: make it use the equivelent port so the any and last can be simplified
		 by the use of simply having it say which port to use and the normal routine
		 takes over as usual """
		if txPort == portTypeEnum.LEFT:
			txOpen.next = txLeft.open
			txLeft.req.next = txReq
		elif txPort == portTypeEnum.RIGHT:
			txOpen.next = txRight.open
			txRight.req.next = txReq
		elif txPort == portTypeEnum.UP:
			txOpen.next = txUp.open
			txUp.req.next = txReq
		elif txPort == portTypeEnum.DOWN:
			txOpen.next = txDown.open
			txDown.req.next = txReq
		elif txPort == portTypeEnum.ANY:
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
				txPortEquiv.next = portTypeEnum.LEFT
			elif txRight.open:
				txLeft.req.next = 0
				txRight.req.next = txReq
				txUp.req.next = 0
				txDown.req.next = 0
				txOpen.next = txRight.open
				txPortEquiv.next = portTypeEnum.RIGHT
			elif txUp.open:
				txLeft.req.next = 0
				txRight.req.next = 0
				txUp.req.next = txReq
				txDown.req.next = 0
				txOpen.next = txLeft.open
				txPortEquiv.next = portTypeEnum.UP
			elif txDown.open:
				txLeft.req.next = 0
				txRight.req.next = 0
				txUp.req.next = 0
				txDown.req.next = txReq
				txOpen.next = txLeft.open
				txPortEquiv.next = portTypeEnum.DOWN
		elif txPort == portTypeEnum.LAST:
			txPortEquiv.next = lastPort
			
			if lastPort == portTypeEnum.LEFT:
				txOpen.next = txLeft.open
				txLeft.req.next = txReq
			elif lastPort == portTypeEnum.RIGHT:
				txOpen.next = txRight.open
				txRight.req.next = txReq
			elif lastPort == portTypeEnum.UP:
				txOpen.next = txUp.open
				txUp.req.next = txReq
			elif lastPort == portTypeEnum.DOWN:
				txOpen.next = txDown.open
				txDown.req.next = txReq
			else:
				pass
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
					if commType == commOpEnum.RX:
						if not rxReady:
							state.next = stateType.RX_TRANSFER
						else:
							lastPort.next = rxPortEquiv
							receivedData.next = rxData
					elif commType == commOpEnum.TX:
						state.next = stateType.TX_TRANSFER
					elif commType == commOpEnum.RX_TX:
						if not rxReady:
							state.next = stateType.RX_TRANSFER
						else:
							lastPort.next = rxPortEquiv
							receivedData.next = rxData
							state.next = stateType.TX_TRANSFER
					# TODO: Add an else that locks everything up
			elif state == stateType.RX_TRANSFER:
				if rxReady:
					lastPort.next = rxPortEquiv
					receivedData.next = rxData
					if commType == commOpEnum.RX:
						state.next = stateType.IDLE
					else: # commType == commOpType.RxTx
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
				
				if commType == commOpEnum.RX:
					rxOpen.next = 1
					
					if rxReady:
						commPause.next = 0
				elif commType == commOpEnum.RX_TX:
					rxOpen.next = 1
		elif state == stateType.RX_TRANSFER:
			commPause.next = 1
			rxOpen.next = 1
			
			if rxReady:
				dataOut.next = rxData
				if commType == commOpEnum.RX:
					commPause.next = 0
		elif state == stateType.TX_TRANSFER:
			commPause.next = 1
			txReq.next = 1
			
			if commType == commOpEnum.TX:
				txData.next = dataIn
			elif commType == commOpEnum.RX_TX:
				txData.next = receivedData
				
			if txReady:
				commPause.next = 0
	
	
	return transferPortSelectProc, transferStatusBitsProc, fsmProc, fsmOutputProc