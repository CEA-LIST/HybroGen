#!/usr/bin/env python3

from HybroLang.H2Node              import H2Node
from HybroLang.H2NodeType          import H2NodeType

class H2Debug():

    def showTree(self, title, IList):
        """ Show IR tree using graphviz
        # https://graphviz.readthedocs.io/en/stable/
        """
        import graphviz
        d = graphviz.Digraph(title, filename="/tmp/a.dot")
        d.attr(label=title)
        d.attr(fontsize="20")
        d.attr(fontcolor="blue")
        for i in range(len(IList)):
            name = "%d:%s"%(i, IList[i].getNodeName())
            self.addGraphInsn(d, IList[i], i+1) # Avoid 0 as Nro (will disapear when *10
        d.view()
        input ("Enter for next step")

    def genNodeName(self, insnNro, strDescr):
        return "%d_%s"%(insnNro, strDescr)

    def addGraphInsn(self, graph, insnTree, insnId):
        """ Generate graphviz tree
        graph : the graph unde constructions
        insnsTree : the subtree to integrate
        insnId : the Id subgraph to "uniquify" the node name
        Recurse on tree deep first
        - create node
        - recurse
        - create edge
        """
        nodeType = insnTree.getOpType()
        if None != nodeType:
            shortType = nodeType.getShort()
        else:
            shortType = "NoType"
        nodeName = insnTree.getNodeName().split('.')[-1] # Keep only op name
        nodeNameId = self.genNodeName(insnId, nodeName)
        varName = insnTree.getVariableName()
        if insnTree.nodeType == H2NodeType.OPERATOR:  nodeShape = 'invtriangle'
        else:                                         nodeShape = 'oval'
        graph.attr('node', shape=nodeShape)
        finalName = "%s\n%s\n%s"%(nodeName, shortType, varName)
        graph.node (nodeNameId, finalName)
        # print (nodeNameId)
        if len(insnTree.sonsList) > 0: # Not on leaf
            for i in range(len(insnTree.sonsList)):
                son = insnTree.sonsList[i]
                sonName = son.getNodeName().split('.')[-1]
                sonNameId = self.genNodeName(insnId*10+i, sonName)
                self.addGraphInsn(graph, son, insnId*10+i)
                # print (nodeNameId+"->"+sonNameId)
                graph.edge(nodeNameId, sonNameId)
