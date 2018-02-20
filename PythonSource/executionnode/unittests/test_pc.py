__author__ = 'Zylanx'

from myhdl import *
import myhdl

from ..components import PC

import unittest
from unittest import TestCase

class TestProgramCounter(TestCase):
	
	def testNormalIncrementing(self):
		""" Check that it increments correctly """
		
		clkPeriod = 10

		def stimulus(clk, rst, ce, load, addr, out):
			def toggleClock():
				yield delay(clkPeriod)
				clk.next = not clk
			
			def cycleClock():
				yield from toggleClock()
				yield from toggleClock()
			
			for count in range(50):
				self.assertEqual(out, count)
				yield from cycleClock()

		clk = Signal(0)
		rst = ResetSignal(0, 1, False)
		ce = Signal(1)
		load = Signal(0)
		addr = Signal(0)
		out = Signal(0)
		
		dut = PC(clk, rst, ce, load, addr, out)
		check = stimulus(clk, rst, ce, load, addr, out)
		sim = Simulation(dut, check)
		
		sim.run(quiet=1)