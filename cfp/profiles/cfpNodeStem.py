#!/usr/bin/python

class CFPNodeStem:

    #default values
    def __init__ (self, stemFillColor="white", stemTextFont="Monospace", stemTextFontColor="black", stemTextFontSize="20",
                  sep = 300, stemBorderColor="black", stemStrokeWidth="2", stemStrokeDasharray = False, 
                  stemStrokeDasharrayValue=""):

        self.fillColor = stemFillColor
        self.textColor = stemTextFontColor
        self.textFont = stemTextFont
        self.textSize = stemTextFontSize
        self.separation = sep
        self.borderColor = stemBorderColor
        self.borderStrokeWidth = stemStrokeWidth
        self.borderStrokeDasharray = stemStrokeDasharray
        self.borderStrokeDasharrayValue = stemStrokeDasharrayValue

    def getFillColor (self):
        "Returns the fill color of the node stem"

        return self.fillColor

    def getTextColor (self):
        "Returns the text color of the node stem"

        return self.textColor

    def getTextFont (self):
        "Returns the text font of the node stem"

        return self.textFont

    def getTextFontSize (self):
        "Returns the text font size of the node stem"

        return self.textFontSize
    
    def getSeparation (self):
        "Returns the separation between the node stems"

        return self.separation

    def getBorderColor (self):
        "Returns the border color of the node stem"

        return self.borderColor

    def getBorderStrokeWidth (self):
        "Returns the border stroke width of the node stem"

        return self.borderStrokeWidth

    def getBorderStrokeDasharray (self):
        "Returns the border stroke dasharray status (boolean) of the node stem"

        return self.borderStrokeDasharray

    def getBorderStrokeDasharrayValue (self):
        "Returns the border stroke dasharray value of the node stem"

        return self.borderStrokeDasharrayValue
