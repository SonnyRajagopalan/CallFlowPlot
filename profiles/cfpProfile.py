#!/usr/bin/python

import cfpNode
import cfpNodeStem
import cfpCanvas
import cfpFlow

class CFPProfile:
    
    def __init__ (self, profName=None, profCanvas=None, profNode=None, profNodeStem=None, profFlow=None):
        "Initializes a profile object"
        self.profileName = profName
        self.profileCanvas = profCanvas
        self.profileNode = profNode
        self.profileNodeStem = profNodeStem
        self.profileFlow = profFlow

        return

    def getName ():
        "Returns the name of the profile"

        return self.profileName
