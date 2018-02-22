__author__ = 'Zylanx'

import myhdl._intbv

__all__ = ["generateEnum"]

def generateEnum():
	import inspect
	
	callerModule = inspect.getmodule(inspect.stack()[1][0])
	
	enumItems = getattr(callerModule, "enumItems", None)
	if enumItems:
		for index, name in enumerate(getattr(callerModule, "enumItems")):
			setattr(callerModule, name, index)
	
		_min = 0
		_max = len(enumItems)
		setattr(callerModule, "_min", _min)
		setattr(callerModule, "_max", _max)
	
		# Generate intbv function
		def intbv(default = 0):
			return myhdl._intbv.intbv(default, _min, _max)
		
		def toStr(indexIn):
			return enumItems[indexIn]
		
		setattr(callerModule, "intbv", intbv)
		setattr(callerModule, "toStr", toStr)