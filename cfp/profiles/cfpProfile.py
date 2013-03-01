#!/usr/bin/python

import cfpNode
import cfpNodeStem
import cfpCanvas
import cfpFlow

class CFPProfile:
    
    def __init__ (self, profName=None, profCanvas=None, profNode=None, profNodeStem=None, profFlow=None):
        "Initializes a profile object"
        self.name = profName
        self.canvas = profCanvas
        self.node = profNode
        self.nodeStem = profNodeStem
        self.flow = profFlow

        return

    def getName (self):
        "Returns the name of the profile"

        return self.name

    def getFlowProfile (self):
        "Returns the flow profile"

        return self.flow

    def getCanvasProfile (self):
        "Returns the canvas profile"

        return self.canvas

    def getNodeProfile (self):
        "Returns the node profile"

        return self.node

    def getNodeStemProfile (self):
        "Returns the node stem profile"

        return self.nodeStem
