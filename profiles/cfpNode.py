#!/usr/bin/python

class CFPNode:
    # default values

    class Type:
        SQUARE = 1
        RECTANGLE = 2
        ROUNDED_SQUARE = 3
        ROUNDED_RECTANGLE = 4
        CIRCLE = 5
        ELLIPSE = 6

    def __init__ (self, nType = Type.SQUARE, fillColor="white", textColor="black", 
                  textFont="Monospace", textFontSize="20", borderColor="black", 
                  strokeWidth="2", strokeDasharray=False, strokeDasharrayValue=""):

        self.nodeType = nType
        self.nodeFillColor = fillColor
        self.nodeTextColor = textColor
        self.nodeTextFont = textFont
        self.nodeTextFontSize = textFontSize
        self.nodeBorderColor = borderColor
        self.nodeStrokeWidth = strokeWidth
        self.nodeStrokeDasharray = strokeDasharray
        self.nodeStrokeDasharrayValue = strokeDasharrayValue
