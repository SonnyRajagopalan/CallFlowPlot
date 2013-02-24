#!/usr/bin/python

import xml.dom.minidom
from xml.dom.minidom import parseString
from xml.dom.minidom import Node
import sys

nodeNames = []
nodeIDs = []
flows = []
svgFile = ""

def getNodes (dom):
    "Get the nodes in the plot"
    nodeList = dom.getElementsByTagName ("Node")
    #print nodeList
    for node in nodeList:
        children = node.getElementsByTagName ("Name")[0].childNodes
        for child in children:
            nodeNameValue = children[0].nodeValue
            nodeNameValue = nodeNameValue.strip ()
            nodeNames.append (nodeNameValue)

        children = node.getElementsByTagName ("ID")[0].childNodes
        for child in children:
            nodeIDValue = children[0].nodeValue
            nodeIDValue = nodeIDValue.strip ()
            nodeIDs.append (nodeIDValue)
    return

def getNodeIDIndex (nID):
    "Returns the nodeID index"
    nodeIDIndex = 0

    for nodeID in nodeIDs:
        if nodeID == nID:
            return nodeIDIndex
        else:
            nodeIDIndex = nodeIDIndex + 1
            
    return -1

def getFlows (dom):
    "Get all the flows in the call flow"
    
    plotXML = dom.getElementsByTagName ("Plot")[0]
    #print flowList, flowList.length
    if plotXML == None:
        print "Error"
    else:
        for plot in plotXML.childNodes:
            if plot.nodeType != Node.TEXT_NODE:
                if plot.nodeName == "Flow":
                    fromNode = ""
                    toNodes = []
                    for item in plot.childNodes:
                        if item.nodeName == "From":
                            fromNode = item.childNodes[0].nodeValue.strip ()
                        elif item.nodeName == "To":
                            toNode  = item.childNodes[0].nodeValue.strip ()
                            toNodes.append (toNode)
                        elif item.nodeName == "Description":
                            desc  = item.childNodes[0].nodeValue.strip ()
                print fromNode, "->", toNodes, "(", desc, ")"
                flows.append (plot)

    return
                            

# Generate the SVG
def writePreamble (svgFile):
    "Write the SVG preambles to output.svg"

    svgFile.write ("<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\">")

    return


def createNodeGraphics (svgFile):
    "Create the defs for the nodes"

    svgFile.write ("  <defs>")
    svgFile.write ("    <linearGradient id=\"grad1\" x1=\"0%\" y1=\"0%\" x2=\"100%\" y2=\"0%\">")
    svgFile.write ("      <stop offset=\"0%\" style=\"stop-color:rgb(255,255,0);stop-opacity:1\" />")
    svgFile.write ("      <stop offset=\"100%\" style=\"stop-color:rgb(255,0,0);stop-opacity:1\" />")
    svgFile.write ("    </linearGradient>")
    svgFile.write ("<marker id=\"Triangle\"")
    svgFile.write (" viewBox=\"0 0 10 10\" refX=\"0\" refY=\"5\"")
    svgFile.write (" markerUnits=\"strokeWidth\"")
    svgFile.write (" markerWidth=\"14\" markerHeight=\"2\"")
    svgFile.write (" orient=\"auto\">")
    svgFile.write ("<path d=\"M 0 0 L 10 5 L 0 10 z\" />")
    svgFile.write ("</marker>")
    svgFile.write ("  </defs>")

    return

def drawNodes (svgFile):
    "Draw the nodes"

    cx = 100
    cy = 100
    rx = 50
    ry = 25
    strx = 100
    stry = 110
    vertLineLen = cy + (len (flows) * 100) + 20
    print "len (flows) = ", len (flows)
    for nodeID in nodeIDs:
        strx = cx - 20
        string = "  <ellipse cx=\""+`cx`+"\" cy=\""+`cy`+"\" rx=\""+`rx`+"\" ry=\""+`ry`+"\" fill=\"url(#grad1)\" />"
        svgFile.write (string)
        svgFile.write ("<line x1=\""+`cx`+"\" y1=\""+`cy+25`+"\" x2=\""+`cx`+"\" y2=\""+`vertLineLen`+"\" ")
        svgFile.write (" style=\"stroke:rgb(128,128,128);stroke-width:5\" stroke-opacity=\"0.5\"/>")
        svgFile.write ("<text fill=\"#ffffff\" font-size=\"25\" font-family=\"Verdana\" x=\""+`strx`+"\" y=\""+`stry`+"\">")
        svgFile.write (nodeID+"</text>")

        cx = cx + 400

    return

def plotTheFlows (dom, svgFile):
    "Plot the flows between the nodes"

    startx = 100
    cx = 100
    cy = 200
    endx = 100 + (len (nodeIDs) - 1) * 400
    plotXML = dom.getElementsByTagName ("Plot")[0]
    #print flowList, flowList.length
    if plotXML == None:
        print "Error"
    else:
        for plot in plotXML.childNodes:
            if plot.nodeType != Node.TEXT_NODE:
                if plot.nodeName == "Flow":
                    fromNode = ""
                    toNodes = []
                    fromToArrowFlag = False

                    for item in plot.childNodes:
                        if item.nodeName == "From":
                            fromNode = item.childNodes[0].nodeValue.strip ()
                        elif item.nodeName == "To":
                            toNode  = item.childNodes[0].nodeValue.strip ()
                            toNodes.append (toNode)
                        elif item.nodeName == "Description":
                            desc  = item.childNodes[0].nodeValue.strip ()

                #print fromNode, "->", toNodes, "(", desc, ")"
                # Write 100 px below last
                # cx = from node
                # cy = first to node
                # What will you do if from == to?
                fromIndex = getNodeIDIndex (fromNode)
                toIndex = getNodeIDIndex (toNodes[0])

                fromX = startx + (fromIndex * 400)
                toX   = startx + (toIndex * 400)

                if fromToArrowsFlag == False:
                    if toIndex > fromIndex: # right to left arrow
                        # Draw the line
                        svgFile.write ("<path d=\"M "+`fromX`+" "+`cy`+" L "+`toX-40`+" "+`cy`+"\"")
                        svgFile.write (" fill=\"none\" stroke=\"steelblue\" stroke-width=\"10\" stroke-opacity=\"0.5\" />")
                        # Draw the arrow head
                        svgFile.write ("<path d=\"M "+`toX-40`+" "+`cy`+ " L "+`toX-40`+ " " + `cy-10`+ " L " + `toX` + " " + `cy` + " L " + `toX-40` + " " + `cy + 10` + " z \"")
                        svgFile.write (" fill=\"steelblue\" fill-opacity=\"0.5\" stroke=\"steelblue\"  stroke-opacity=\"0.5\" />")
                        # Add the text description
                        svgFile.write ("<text font-family=\"Monospace\" font-size=\"12\" x=\""+`fromX+10`+"\" y=\""+`cy-15`+"\" style=\"stroke: peru; fill: peru\">")
                    else: # left to right arrow
                        # Draw the line
                        svgFile.write ("<path d=\"M "+`toX+40`+" "+`cy`+" L "+`fromX`+" "+`cy`+"\"")
                        svgFile.write (" fill=\"none\" stroke=\"steelblue\" stroke-width=\"10\" stroke-opacity=\"0.5\" />")
                        # Draw the arrow head
                        svgFile.write ("<path d=\"M "+`toX+40`+" "+`cy`+ " L "+`toX+40`+ " " + `cy-10`+ " L " + `toX` + " " + `cy` + " L " + `toX+40` + " " + `cy + 10` + " z \"")
                        svgFile.write (" fill=\"steelblue\" fill-opacity=\"0.5\" stroke=\"steelblue\"  stroke-opacity=\"0.5\" />")
                        # Add the text description
                        svgFile.write ("<text font-family=\"Monospace\" font-size=\"12\" x=\""+`toX+10`+"\" y=\""+`cy-15`+"\" style=\"stroke: peru; fill: peru\">")
                    
                    svgFile.write (desc)
                    svgFile.write ("</text>")

                    cy = cy + 100
                elif fromToArrowsFlag == True:
                    # Nothing
    return


file = open (sys.argv[1], "r")
data = file.read ()
file.close ()

dom = parseString (data)

getNodes (dom)
print "Here are the nodes"
print nodeNames
print nodeIDs

getFlows (dom)
svgFile = open ("/tmp/output.svg", "w")
writePreamble (svgFile)
createNodeGraphics (svgFile)
drawNodes (svgFile)
plotTheFlows (dom, svgFile)

svgFile.write ("</svg>")

svgFile.close ()

#print nodes

        
#xmlTags = dom.getElementsByTagName (\"Flow\").size

#print xmlTag
