__author__ = 'Zylanx'

from myhdl import enum

portType = enum("NIL", "ACC", "LEFT", "RIGHT", "UP", "DOWN", "ANY", "LAST")

commOpType = enum("Rx", "Tx", "RxTx")