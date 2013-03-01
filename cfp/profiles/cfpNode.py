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
                  strokeWidth="2", strokeDasharray=False, strokeDasharrayValue="",
                  xSize = 50, ySize = 25):

        self.type = nType
        self.fillColor = fillColor
        self.textColor = textColor
        self.textFont = textFont
        self.textFontSize = textFontSize
        self.borderColor = borderColor
        self.borderStrokeWidth = strokeWidth
        self.borderStrokeDasharray = strokeDasharray
        self.borderStrokeDasharrayValue = strokeDasharrayValue
        self.xSize = xSize
        self.ySize = ySize

    def getType (self):
        "Returns the type of the node"

        return self.type

    def getFillColor (self):
        "Returns the fill color of the node"

        return self.fillColor

    def getTextColor (self):
        "Returns the text color of the node"

        return self.textColor

    def getTextFont (self):
        "Returns the text font of the node"

        return self.textFont

    def getTextFontSize (self):
        "Returns the text font size of the node"

        return self.textFontSize

    def getBorderColor (self):
        "Returns the border color of the node"

        return self.borderColor

    def getBorderStrokeWidth (self):
        "Returns the border stroke width of the node"

        return self.borderStrokeWidth

    def getBorderStrokeDasharray (self):
        "Returns the border stroke dasharray status (boolean) of the node"

        return self.borderStrokeDasharray

    def getBorderStrokeDasharrayValue (self):
        "Returns the border stroke dasharray value of the node"

        return self.borderStrokeDasharrayValue

    def getXSize (self):
        "Returns the size of the X direction for the node"

        return self.xSize

    def getYSize (self):
        "Returns the size of the Y direction for the node"

        return self.ySize
