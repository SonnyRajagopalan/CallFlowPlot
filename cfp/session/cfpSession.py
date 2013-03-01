#!/usr/bin/python

import uuid

class CFPSession:
    "The plotting session has some parameters. This object stores them. Useful handle \
    to pass around in modules"

    def __init__ (self):
        self.myID = uuid.uuid1 ()
        self.output = "/tmp/" + str(self.myID) + ".svg"
        self.profile = None
        self.title = None
        self.nodeIDs = []
        self.nodeNames = []
        self.flows = []

        return

    def setOutput (self, out):
        "Sets the output file name for the session"

        self.output = out

        return

    def getOutput (self):
        "Gets the output file name"

        return self.output


    def setProfile (self, prof):
        "Set the self.profile"

        self.profile = prof

        return

    def getProfile (self):
        "Gets the self.profile"
        
        return self.profile

    def addANodeID (self, id):
        "Adds a node ID to the self.nodeIDs in the session"

        self.nodeIDs.append (id)

        return
    
    def setNodeIDs (self, ids):
        "Sets the nodeNames value in the session"

        self.nodeIDs = ids

        return

    def getNodeIDs (self):
        "Gets the node names"

        return self.nodeIDs


    def addANodeName (self, name):
        "Adds a node name to the self.nodeNames in the session"
        
        self.nodeNames.append (name)

        return

    def setNodeNames (self, names):
        "Sets the self.nodeNames value in the session"

        self.nodeNames = names

        return

    def getNodeNames (self):
        "Gets the node names"

        return self.nodeNames

    def addAFlow (self, flow):
        "Adds a flow to the flows in the session"

        self.flows.append (flow)

        return


    def setFlows (self, fl):
        "Sets the self.nodeNames value in the session"

        self.flows = fl

        return

    def getFlows (self):
        "Gets the node names"

        return self.flows

    def setTitle (self, t):
        "Sets the title"
        
        self.title = t

        return

    def getTitle (self):
        "Gets the title"

        return self.title

    def getNodeIndex (self, nID):
        "Given a nodeID, returns the nodeIndex"

        nodeIDIndex = 0

        for nodeID in self.nodeIDs:
            if nodeID == nID:
                return nodeIDIndex
            else:
                nodeIDIndex = nodeIDIndex + 1
            
        return -1
