__author__ = 'Zylanx'

from myhdl import Signal, intbv

class CommInterface:
	def __init__(self, min=0, max=2):
		self.open = Signal(bool(0))
		self.req = Signal(bool(0))
		self.data = Signal(intbv(0, min, max))