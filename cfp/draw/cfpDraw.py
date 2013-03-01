#!/usr/bin/python

from .. profiles.templates import *
from .. session import *

def writePreamble (session, svgFile):
    "Write the preamble to the SVG file"

    svgFile.write ("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">")

    return

def createNodeGraphicsDefinitions (session, svgFile):
    "Creates the node graphics definitions"

    svgFile.write ("  <defs>")
    svgFile.write ("    <linearGradient id=\"grad1\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"0%\">")
    svgFile.write ("      <stop offset=\"0%\" style=\"stop-color: #D4E7ED;stop-opacity:1\" />")
    svgFile.write ("      <stop offset=\"100%\" style=\"stop-color: #EB8540;stop-opacity:1\" />")
    svgFile.write ("    </linearGradient>")
    svgFile.write ("  </defs>")

    return

def drawNodes (session, svgFile):
    "Draw the nodes"

    cx = session.getProfile ().getCanvasProfile ().getUsableX1 ()
    cy = session.getProfile ().getCanvasProfile ().getUsableY1 ()
    rx = session.getProfile ().getNodeProfile ().getXSize () # 50
    ry = session.getProfile ().getNodeProfile ().getYSize () # 25
    textY = session.getProfile ().getCanvasProfile ().getUsableY1 () + 10
    vertLineLen = cy + (len (session.getFlows ()) * session.getProfile ().getFlowProfile ().getSeparation ()) + 20
    #print "len (flows) = ", len (flows)
    for nodeID in session.getNodeIDs ():
        textX = cx - 20
        #string = "  <ellipse cx=\""+`cx`+"\" cy=\""+`cy`+"\" rx=\""+`rx`+"\" ry=\""+`ry`+"\" fill=\"url(#grad1)\" />"
        string = "  <rect x=\""+`cx-rx`+"\" y=\""+`cy-ry`+"\" width=\""+`rx*2`+"\" height=\""+`ry*2`+"\" rx=\"10\" ry=\"10\" fill=\"url(#grad1)\" />"
        svgFile.write (string)
        svgFile.write ("<line x1=\""+`cx`+"\" y1=\""+`cy+25`+"\" x2=\""+`cx`+"\" y2=\""+`vertLineLen`+"\" ")
        svgFile.write (" style=\"stroke:rgb(128,128,128);stroke-width:5\" stroke-opacity=\"0.5\"/>")
        svgFile.write ("<text fill=\"#ffffff\" font-size=\"20\" font-family=\"Verdana\" x=\""+`textX`+"\" y=\""+`textY`+"\">")
        svgFile.write (nodeID+"</text>")

        cx = cx + session.getProfile ().getNodeStemProfile ().getSeparation ()

    return

def plotAFlow (session, svgFile, fromNode, toNodes, desc, fromToFlag, cy):
    "Plot a flow in the CFP"

    return

def writeEpilogue (session, svgFile):
    "Write the closing comments, tags etc."

    svgFile.write ("</svg>")
    svgFile.close ()

    return
