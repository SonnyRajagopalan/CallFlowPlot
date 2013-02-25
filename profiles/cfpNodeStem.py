#!/usr/bin/python

class CFPNodeStem:

    #default values
    def __init__ (self, stemFillColor="white", stemTextFontColor="black", stemTextFontSize="20",
                  stemBorderColor="black", stemStrokeWidth="2", stemStrokeDasharray = False, 
                  stemStrokeDasharrayValue=""):

        self.nodeStemFillColor = stemFillColor
        self.nodeStemTextColor = stemTextFontColor
        self.nodeStemTextSize = stemTextFontSize
        self.nodeStemBorderColor = stemBorderColor
        self.nodeStemStrokeWidth = stemStrokeWidth
        self.nodeStemStrokeDasharray = stemStrokeDasharray
        self.nodeStemStrokeDasharrayValue = stemStrokeDasharrayValue
