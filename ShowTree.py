#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx

class MyTree(wx.TreeCtrl):
    def __init__(self, parent, id, pos, size, style):
        super().__init__(parent, id, pos, size, style)

class TreePanel(wx.Panel):

    def __init__(self, parent, title, program):
        super().__init__(parent)
        self.tree = MyTree(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_HAS_BUTTONS)
        self.root = self.tree.AddRoot(title)
        self.appendChild (self.root, program)
        self.tree.Expand(self.root)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        self.SetSizer(sizer)

    def appendChild (self, itemId, program):
        for insn in program:
            if type(insn) is tuple and len(insn) > 1:
                print (insn[0])
                child = self.tree.AppendItem(itemId, insn[0])
                self.appendChild (child, insn[1])
            else:
                if type(insn) is tuple:
                    child = self.tree.AppendItem(itemId, insn[0])
                else:
                    child = self.tree.AppendItem(itemId, insn)
        self.tree.Expand(itemId)

class FrameIR(wx.Frame):
    """Graphical representation of an HybroGen IR"""
    def __init__(self, title, program):
        super().__init__(parent = None, title=title, size=(20,20))
        TreePanel (self, title, program)
        self.SetSize (600, 600)
        self.Show(True)

P = (
    ("H2NodeType.OPERATOR: =: {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}",
     ("H2NodeType.VARIABLE: h2_00000004",
      "H2NodeType.CONST: (b): {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}"
     )
    ),
    ("H2NodeType.OPERATOR: =: {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}",
     ("H2NodeType.VARIABLE: h2_outputVarName",
      ("H2NodeType.OPERATOR: +: {'arith': 'int', 'wordLen': '32', 'vectorLen': '1'}",
       ("H2NodeType.VARIABLE: a",
	"H2NodeType.VARIABLE: h2_00000004"
       ),
       ),
      ),
     ),
    ("H2NodeType.RTN: RETURN",),
)


if __name__ == "__main__":
    import sys, wx

    app = wx.App (False)
    a = FrameIR("Add-With-Specialization.hl", P)
    app.MainLoop()
