#!/usr/bin/python

class CFPFlow:
    # default values

    class EndType:
        SQUARE = 1
        RECTANGLE = 2
        ROUNDED_SQUARE = 3
        ROUNDED_RECTANGLE = 4
        CIRCLE = 5
        ELLIPSE = 6
        UNFILLED_ARROW = 7
        FILLED_ARROW = 8
        CLASSIC_ARROW = 9

    def __init__ (self, flowSep = 75, fillColor="steelblue", fillOpacity="0.5", textColor="black", 
                  textFont="Monospace", textFontSize="20", borderColor="black",
                  strokeWidth="10", strokeDasharray = False, strokeDasharrayValue = "", 
                  endType = EndType.FILLED_ARROW, endStrokeWidth = "10", endShiftFromHoriz = "30",
                  endRaiseFromVert = "20", endFill = "steelblue", endFillOpacity = "0.5",
                  endStrokeDasharray = False, endStrokeDasharrayValue = ""):
        
        self.separation = flowSep
        self.fillColor = fillColor
        self.fillOpacity = fillOpacity
        self.textColor = textColor
        self.textFont = textFont
        self.textFontSize = textFontSize
        self.borderColor = borderColor
        self.borderstrokeWidth = strokeWidth
        self.borderstrokeDasharray = strokeDasharray
        self.borderstrokeDasharrayValue = strokeDasharrayValue
        
        self.endType = endType
        self.endStrokeWidth = endStrokeWidth
        # The following two parameters define how the end type juts off the line for the flow
        self.endShiftFromHorizontal = endShiftFromHoriz
        self.endRaiseFromVertical = endRaiseFromVert

        self.endFill = endFill
        self.endFillOpacity = endFillOpacity
        self.endStrokeDasharray = endStrokeDasharray
        self.endStrokeDasharrayValue = endStrokeDasharrayValue

    def getSeparation (self):
        "Returns the flow separation value, in unitless Y dimensions"

        return self.separation

    def getFillColor (self):
        "Returns the fill color of the flow"

        return self.fillColor

    def getFillOpacity (self):
        "Returns the fill opacity for the flow"

        return fillOpacity

    def getTextColor (self):
        "Returns the text color of the flow"

        return self.textColor

    def getTextFont (self):
        "Returns the text font of the flow"

        return self.textFont

    def getTextFontSize (self):
        "Returns the text font size of the flow"

        return self.textFontSize

    def getBorderColor (self):
        "Returns the border color of the flow"

        return self.borderColor

    def getBorderStrokeWidth (self):
        "Returns the border stroke width of the flow"

        return self.borderStrokeWidth

    def getBorderStrokeDasharray (self):
        "Returns the border stroke dasharray status (boolean) of the flow"

        return self.borderStrokeDasharray

    def getBorderStrokeDasharrayValue (self):
        "Returns the border stroke dasharray value of the flow"

        return self.borderStrokeDasharrayValue

    def getEndType (self):
        "Returns the end type of the flow"

        return self.endType

    def getEndStrokeWidth (self):
        "Returns the end stroke width"

        return self.endStrokeWidth

    def getEndShiftFromHorizontal (self):
        "Returns the end shift from horizontal"

        return self.endShiftFromHoriz

    def getEndRaiseFromVertical (self):
        "Returns the end raise from vertical"

        return self.endRaiseFromVert

    def getFill (self):
        "Returns the fill color"
        
        return self.endFill

    def getFillOpacity (self):
        "Returns the fill opacity"

        return self.fillOpacity

    def getStrokeEndDasharray (self):
        "Returns the end stroke dasharray presence (boolean)"

        return self.endStrokeDasharray

    def getStrokeEndDasharrayValue (self):
        "Returns the end stroke dasharray value"

        return self.endStrokeDasharrayValue
