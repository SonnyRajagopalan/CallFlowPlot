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

    def __init__ (self, fillColor="steelblue", fillOpacity="0.5", textColor="black", 
                  textFont="Monospace", textFontSize="20", borderColor="black",
                  strokeWidth="10", strokeDasharray = False, strokeDasharrayValue = "", 
                  endType = EndType.FILLED_ARROW, endStrokeWidth = "10", endShiftFromHoriz = "30",
                  endRaiseFromVert = "20", endFill = "steelblue", endFillOpacity = "0.5",
                  endStrokeDasharray = False, endStrokeDasharrayValue = ""):
        
        self.flowFillColor = fillColor
        self.flowFillOpacity = fillOpacity
        self.flowTextColor = textColor
        self.flowTextFont = textFont
        self.flowTextFontSize = textFontSize
        self.flowBorderColor = borderColor
        self.flowStrokeWidth = strokeWidth
        self.flowStrokeDasharray = strokeDasharray
        self.flowStrokeDasharrayValue = strokeDasharrayValue
        
        self.flowEndType = endType
        self.flowEndStrokeWidth = endStrokeWidth
        # The following two parameters define how the end type juts off the line for the flow
        self.flowEndShiftFromHorizontal = endShiftFromHoriz
        self.flowEndRaiseFromVertical = endRaiseFromVert

        self.flowEndFill = endFill
        self.flowEndFillOpacity = endFillOpacity
        self.flowEndStrokeDasharray = endStrokeDasharray
        self.flowEndStrokeDasharrayValue = endStrokeDasharrayValue
        
