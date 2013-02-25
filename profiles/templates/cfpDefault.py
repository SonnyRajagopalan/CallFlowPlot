#!/usr/bin/python

# import sys
# sys.path.append ("..")
from .. import *

def getProfile ():
    "Returns a profile object that is composed of the default parameters"
    canvas = cfpCanvas.CFPCanvas ()
    node   = cfpNode.CFPNode ()
    nodeStem = cfpNodeStem.CFPNodeStem ()
    flow = cfpFlow.CFPFlow ()
    
    profile = cfpProfile.CFPProfile ("Default", canvas, node, nodeStem, flow)

    return profile
