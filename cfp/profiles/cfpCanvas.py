#!/usr/bin/python

class CFPCanvas:
    # default values
    def __init__ (self, w="11in", h="8.5in", usableX1 = 100, usableY1 = 100, usableX2 = 10000, usableY2 = 10000):
        self.width = w
        self.height = h
        self.usableX1 = usableX1
        self.usableY1 = usableY1
        self.usableX2 = usableX2
        self.usableY2 = usableY2

    def getWidth (self):
        "Returns the width of the canvas"

        return self.width

    def getHeight (self):
        "Returns the height of the canvas"
        
        return self.height
            

    def getUsableX1 (self):
        "Returns usableX1, the start X value of the call flow"

        return self.usableX1

    def getUsableY1 (self):
        "Returns usableY1, the start Y value of the call flow"

        return self.usableY1

    def getUsableX2 (self):
        "Returns usableX2, the start X value of the call flow"

        return self.usableX1

    def getUsableY2 (self):
        "Returns usableY2, the start Y value of the call flow"

        return self.usableY1
