__author__ = 'Zylanx'

class TreeNode:
	def __init__(self, value):
		self.value = value
	
	def __repr__(self):
		return "{}(\"{}\")".format(self.__class__.__name__, self.value)

class LabelNode(TreeNode):
	def __init__(self, value):
		self.value = value

class RegNode(TreeNode):
	pass

class CommPortNode(TreeNode):
	pass

class ConstNode(TreeNode):
	def __repr__(self):
		return "{}({})".format(self.__class__.__name__, self.value)

class LabelMarker:
	def __init__(self, labelName, lineNum):
		self.labelName = labelName
		self.lineNum = lineNum
	
	def __repr__(self):
		return "{}(\"{}\", {})".format(self.__class__.__name__, self.labelName, self.lineNum)