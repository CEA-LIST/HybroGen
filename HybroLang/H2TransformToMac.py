#!/usr/bin/env python3

from HybroLang.H2Node import H2Node

class H2TransformToMac():
	"""
	Transform add and mul to mac if posible
	- Author: Thaddee BRICOUT, CEA Grenoble, 2023
	"""

	def __init__(self, insnList, verbose):
		self.oldList = insnList
		self.nbMac = 0
		self.newList = []
		for insn in insnList:
			self.detectMac(insn)
		if verbose:
			print ("Transform to mac optimize : %d MAC found"%self.nbMac)


	def detectMac(self, insn):
		"""
		Detect if the tree represents a Mac insn
		Operation is dest = s1 * s2 + dest
		"""
		if not insn.isOperator or len(insn.sonsList) < 2:
			self.newList += [insn]
			return
		destination = insn.sonsList[0]
		sources = insn.sonsList[1]
		if sources.isOperator() and sources.getOpName() == "+":
			acc = sources.sonsList[1]
			mul = sources.sonsList[0]
			if mul.isOperator() and mul.getOpName() == "*":
				if destination.isSameTree(acc):
					self.nbMac += 1
					self.doTransformToMac(insn)
				return
		self.newList += [insn]

	def doTransformToMac(self, insn):
		insn.sonsList[1] = insn.sonsList[1].sonsList[0]
		insn.sonsList[1].setOpName("MAC")
		self.newList += [insn]

	def getNewInsnList(self):
		return self.newList
