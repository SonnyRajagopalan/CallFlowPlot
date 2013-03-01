#!/usr/bin/python

# Python module imports
import xml.dom.minidom
from xml.dom.minidom import parseString
from xml.dom.minidom import Node
import sys

# CFP specific
from cfp.session.cfpSession import CFPSession
from cfp.draw import cfpDraw

def setProfileToUse (dom):
    "Gets the information about the correct profile to use"
        
    try:
        profXml = dom.getElementsByTagName ("Profile")
        prof = ((profXml[0].childNodes)[0].nodeValue).strip ()
    
        if prof.upper () == "DEFAULT":
            import cfp.profiles.templates.cfpDefault
            session.setProfile (cfp.profiles.templates.cfpDefault.getProfile ()) # Get profile from singleton object
            #print "My profile name is " + session.getProfile ().getName ()
        elif prof.upper () == "TANGO": # TBD profile
            pass
        elif prof.upper () == "BORING": # TBD profile
            pass
        elif prof.upper () == "BLAH": # TBD profile
            pass

    except IndexError:
        print "No user defined profile information found. Set to default."
        import cfp.profiles.templates.cfpDefault
        session.setProfile (cfp.profiles.templates.cfpDefault.getProfile ()) # Get profile from singleton object
        
    return

def setOutput (dom):
    "Sets the output for the call flow"

    try:
        outputXml = dom.getElementsByTagName ("Output")
        output = ((outputfXml[0].childNodes)[0].nodeValue).strip ()
        session.setTitle (output)
    except IndexError:
        pass
        
    return

def setTitle (dom):
    "Sets the title for the call flow"

    try:
        titleXml = dom.getElementsByTagName ("Title")
        title = ((titlefXml[0].childNodes)[0].nodeValue).strip ()
        session.setTitle (title)
    except IndexError:
        session.setTitle (session.output)
        
    return

def getNodes (dom):
    "Get the nodes in the plot"

    nodeList = dom.getElementsByTagName ("Node")

    if nodeList == []:
        sys.exit ("No <Node/> elements found? Check *.cff file. Aborting!")
            
    for node in nodeList:

        try:
            children = node.getElementsByTagName ("Name")[0].childNodes
            for child in children:
                nodeNameValue = children[0].nodeValue
                nodeNameValue = nodeNameValue.strip ()
                #nodeNames.append (nodeNameValue)
                session.addANodeName (nodeNameValue)
        except IndexError:
            sys.exit ("No <Name/> tag for Node? Check *.cff file. Aborting!")

        try:
            children = node.getElementsByTagName ("ID")[0].childNodes
            for child in children:
                nodeIDValue = children[0].nodeValue
                nodeIDValue = nodeIDValue.strip ()
                #session.getNodeIDs ().append (nodeIDValue)
                session.addANodeID (nodeIDValue)
        except IndexError:
            sys.exit ("No <ID/> tag for Node? Check *.cff file. Aborting!")

    return

def getFlows (dom):
    "Get all the flows in the call flow"
    
    try:
        plotXML = dom.getElementsByTagName ("Plot")[0]
    #print flowList, flowList.length
    except IndexError:
        sys.exit ("No <Plot/> tag found in *.cff file! Aborting")
    
    for flow in plotXML.childNodes:
        if flow.nodeType != Node.TEXT_NODE:
            if flow.nodeName == "Flow":
                fromNode = ""
                toNodes = []
                for item in flow.childNodes:
                    if item.nodeName == "From":
                        fromNode = item.childNodes[0].nodeValue.strip ()
                    elif item.nodeName == "To":
                        toNode  = item.childNodes[0].nodeValue.strip ()
                        toNodes.append (toNode)
                    elif item.nodeName == "Description":
                        desc  = item.childNodes[0].nodeValue.strip ()
                #print fromNode, "->", toNodes, "(", desc, ")"
            session.addAFlow (flow)
            #flows.append (flow)

    return

def plotAFlow (svgFile, fromNode, toNodes, desc, fromToFlag, cy):
    "Plots one flow"
    #print fromNode, "->", toNodes, "(", desc, ")"
    # Write 100 px below last
    # cx = from node
    # cy = first to node
    # What will you do if from == to?

    startx = session.getProfile ().getCanvasProfile ().getUsableX1 ()
    cx = session.getProfile ().getCanvasProfile ().getUsableX1 ()
    endx = cx + (len (session.getNodeIDs ()) - 1) * session.getProfile ().getNodeStemProfile ().getSeparation ()
    #fromIndex = getNodeIDIndex (fromNode)
    fromIndex = session.getNodeIndex (fromNode)
    fromX = startx + (fromIndex * session.getProfile ().getNodeStemProfile ().getSeparation ())

    for toNode in toNodes:
        #toIndex = getNodeIDIndex (toNode)    
        toIndex = session.getNodeIndex (toNode)    
        toX   = startx + (toIndex * session.getProfile ().getNodeStemProfile ().getSeparation ())

        #print "Trying to plot..."
    
        if fromToFlag == False:
            #print "False"
            if toIndex > fromIndex: # right to left arrow
                toIndex = toIndex - 5
                fromIndex = fromIndex + 5
                # Draw the line
                svgFile.write ("<path d=\"M "+`fromX`+" "+`cy`+" L "+`toX-40`+" "+`cy`+"\"")
                svgFile.write (" fill=\"none\" stroke=\"steelblue\" stroke-width=\"10\" stroke-opacity=\"0.5\" />")
                # Draw the arrow head
                svgFile.write ("<path d=\"M "+`toX-40`+" "+`cy`+ " L "+`toX-40`+ " " + `cy-10`+ " L " + `toX` + " " 
                               + `cy` + " L " + `toX-40` + " " + `cy + 10` + " z \"")
                svgFile.write (" fill=\"steelblue\" fill-opacity=\"0.5\" stroke=\"steelblue\"  stroke-opacity=\"0.5\" />")
                # Add the text description
                svgFile.write ("<text font-family=\"Monospace\" font-size=\"20\" x=\""+`fromX+10`+"\" y=\""+`cy-15`+
                               "\" style=\"stroke: #EB8540; fill: #EB8540\">")
                svgFile.write (desc)
                svgFile.write ("</text>")
            elif toIndex < fromIndex: # left to right arrow
                toIndex = toIndex + 5
                fromIndex = fromIndex - 5
                # Draw the line
                svgFile.write ("<path d=\"M "+`toX+40`+" "+`cy`+" L "+`fromX`+" "+`cy`+"\"")
                svgFile.write (" fill=\"none\" stroke=\"steelblue\" stroke-width=\"10\" stroke-opacity=\"0.5\" />")
                # Draw the arrow head
                svgFile.write ("<path d=\"M "+`toX+40`+" "+`cy`+ " L "+`toX+40`+ " " + `cy-10`+ " L " + `toX` + " " +
                               `cy` + " L " + `toX+40` + " " + `cy + 10` + " z \"")
                svgFile.write (" fill=\"steelblue\" fill-opacity=\"0.5\" stroke=\"steelblue\"  stroke-opacity=\"0.5\" />")
                # Add the text description
                svgFile.write ("<text font-family=\"Monospace\" font-size=\"20\" x=\""+`toX+10`+"\" y=\""+`cy-15`+
                               "\" style=\"stroke: #EB8540; fill: #EB8540\">")
                svgFile.write (desc)
                svgFile.write ("</text>")
            elif toIndex == fromIndex:
                # Internal flow: span (toX + 10, cy + 40) to (toX + 10, cy - 40)
                svgFile.write ("<path d=\"M " + `toX+10` + " " + `cy+20` + " C " + `toX+80` + " " + `cy+20` + " " + 
                               `toX+80` + " " + `cy-20` + " " + `toX+10` + " " + `cy-20` + 
                               "\" stroke=\"steelblue\" stroke-width=\"10\" stroke-opacity=\"0.5\" fill=\"none\"/>")
                svgFile.write ("<path d=\"M " + `toX+10` + " " + `cy-25` + " L " + `toX` + " " + `cy-20` + " " 
                               + `toX + 10` + " " + `cy - 15` + 
                               "\" stroke=\"steelblue\" stroke-width=\"6\" stroke-opacity=\"0.5\"" + 
                               " fill=\"steelblue\" fill-opacity=\"0.5\"/>")
                # Add the text description
                svgFile.write ("<text font-family=\"Monospace\" font-size=\"20\" x=\""+`toX+70`+"\" y=\""+`cy+10`+
                               "\" style=\"stroke: #EB8540; fill: #EB8540\">")
                svgFile.write (desc)
                svgFile.write ("</text>")

        elif fromToFlag == True:

            startX = -1
            endX   = -1

            if toIndex < fromIndex:
                startX = toX + 5
                endX   = fromX - 5
            elif toIndex > fromIndex:
                startX = fromX + 5
                endX   = toX - 5
            else:
                # Error
                pass

            #print "For FromTo: startX = ",startX,", endX = ", endX

            # Draw the line
            svgFile.write ("<path d=\"M "+`startX+40`+" "+`cy`+" L "+`endX-40`+" "+`cy`+"\"")
            svgFile.write (" fill=\"none\" stroke=\"green\" stroke-width=\"20\" stroke-opacity=\"0.5\" />")
            # Draw the arrow head to the left
            svgFile.write ("<path d=\"M "+`startX+40`+" "+`cy`+ " L "+`startX+40`+ " " + `cy-15`+ " L " + `startX` + " " +
                           `cy` + " L " + `startX+40` + " " + `cy + 15` + " z \"")
            svgFile.write (" fill=\"green\" fill-opacity=\"0.5\" stroke=\"green\"  stroke-opacity=\"0.5\" />")

            # Draw the arrow head to the right
            svgFile.write ("<path d=\"M "+`endX-40`+" "+`cy`+ " L "+`endX-40`+ " " + `cy-15`+ " L " + `endX` + " " +
                           `cy` + " L " + `endX-40` + " " + `cy + 15` + " z \"")
            svgFile.write (" fill=\"green\" fill-opacity=\"0.5\" stroke=\"green\"  stroke-opacity=\"0.5\" />")
            # Add the text description
            svgFile.write ("<text font-family=\"Monospace\" font-size=\"20\" x=\""+`startX+10`+"\" y=\""+`cy-15`+
                           "\" style=\"stroke: #EB8540; fill: #EB8540\">")
            svgFile.write (desc)
            svgFile.write ("</text>")
            
    return

def plotTheFlows (dom, svgFile):
    "Plot the flows between the nodes"

    cy = session.getProfile ().getCanvasProfile ().getUsableY1 () + (session.getProfile ().getNodeProfile ().getYSize () * 5)
    fromToFlag = False

    try:
        plotXML = dom.getElementsByTagName ("Plot")[0]
        # print flowList, flowList.length
        for plot in plotXML.childNodes:
            if plot.nodeType != Node.TEXT_NODE:
                if plot.nodeName == "Flow":
                    fromNode = ""
                    toNodes = []
                    fromToFlag = False

                    for item in plot.childNodes:
                        if item.nodeName == "From":
                            fromNode = item.childNodes[0].nodeValue.strip ()
                        elif item.nodeName == "To":
                            toNode  = item.childNodes[0].nodeValue.strip ()
                            toNodes.append (toNode)
                        elif item.nodeName == "Description":
                            desc  = item.childNodes[0].nodeValue.strip ()
                        elif item.nodeName == "FromTo":
                            fromToFlag = True
                        elif item.nodeName == "SoonAfterPrevious":
                            #print "SoonAfterPrevious"
                            soonAfterPreviousFlag = True
                            # 40% of separation between flows
                            cy = cy - 0.6 * session.getProfile ().getFlowProfile ().getSeparation ()
                        elif item.nodeName == "LongAfterPrevious":
                            longAfterPreviousFlag = True
                            # 60% more than usual
                            cy = cy + session.getProfile ().getFlowProfile ().getSeparation ()
                        elif item.nodeName == "AlongWithPrevious":
                            alongWithPreviousFlag = True

                            if cy == session.getProfile ().getCanvasProfile ().getUsableY1 () + (session.getProfile ().getNodeProfile ().getYSize () * 2):
                                print "There cannot be an <AlongWithPrevious/> as the first flow. Check flows. Discarding tag!"
                            elif cy > session.getProfile ().getCanvasProfile ().getUsableY1 () + (session.getProfile ().getNodeProfile ().getYSize () * 2):
                                cy = cy - session.getProfile ().getFlowProfile ().getSeparation ()
                            else:
                                sys.exit ("Error with separation value in flow profile (check the flow profile). Aborting!")

                # Great place for validity checks
                # Cannot have multiple "From" items.
                # Should have atleast one "From" item
                # If fromToFlag == True, then cannot have multiple "To" items
                # Description cannot be null or empty string
                # Cannot have multiple description items
                #print "Calling plotAFlow with",svgFile, fromNode, toNodes, desc, fromToFlag, cy
                plotAFlow (svgFile, fromNode, toNodes, desc, fromToFlag, cy)

                cy = cy + session.getProfile ().getFlowProfile ().getSeparation ()

    except IndexError:
        sys.exit ("No <Plot/> tag found in *.cff file (should have been caught earlier?). Aborting!")

    return

# Main....

session = CFPSession ()

callFlowFile = open (sys.argv[1], "r")
data = callFlowFile.read ()
callFlowFile.close ()

callFlowFileDom = parseString (data)

setProfileToUse (callFlowFileDom)
getNodes (callFlowFileDom)

getFlows (callFlowFileDom)
#svgFile = open (session.getOutput (), "w")
svgFile = open ("/tmp/output.svg", "w")

cfpDraw.writePreamble (session, svgFile)
cfpDraw.createNodeGraphicsDefinitions (session, svgFile)
cfpDraw.drawNodes (session, svgFile)

plotTheFlows (callFlowFileDom, svgFile)

cfpDraw.writeEpilogue (session, svgFile)

# Set up session
# Plot the flows
# Perform requisite conversions
# Done
