__author__ = 'Zylanx'

from myhdl import Signal, intbv

# class RegControlInterface:
# 	def __init__(self):
# 		self.store = Signal(bool(0))
# 		self.sav = Signal(bool(0))
# 		self.swp = Signal(bool(0))
		
class PCControlInterface:
	def __init__(self):
		self.inc = Signal(bool(0))
		self.load = Signal(bool(0))

class StatusBitInterface:
	def __init__(self):
		self.eq = Signal(bool(0))
		self.gt = Signal(bool(0))
		self.lt = Signal(bool(0))

class CommInterface:
	def __init__(self, min=0, max=2):
		self.open = Signal(bool(0))
		self.req = Signal(bool(0))
		self.data = Signal(intbv(0, min, max))