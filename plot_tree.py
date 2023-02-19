import matplotlib.pyplot as plt

# define nodeType Leaf node, distinguish node, definition of arrow type

decisionNode=dict(boxstyle="sawtooth",fc="0.8")
leafNode=dict(boxstyle="round4",fc="0.8")
arrow_args=dict(arrowstyle="<-")

# Define node function

def plotNode(nodeText,centerPt,parentPt,nodeType):
    createPlot.ax1.annotate(nodeText,xy=parentPt,xycoords='axes fraction',xytext=centerPt,textcoords='axes fraction',
                           va='center',ha='center',bbox=nodeType,arrowprops=arrow_args)
    # This parameter is a bit scary. did not understand

# Plots text between child and parent
def plotMidText(cntrPt,parentPt,txtString):
    xMid=(parentPt[0]-cntrPt[0])/2.0+cntrPt[0]
    yMid=(parentPt[1]-cntrPt[1])/2.0+cntrPt[1]
    createPlot.ax1.text(xMid,yMid,txtString)

# Perform graphic display
def createPlot(inTree):
    fig=plt.figure(1,facecolor='white')
    fig.clf()
    axprops=dict(xticks=[],yticks=[])
    createPlot.ax1=plt.subplot(111,frameon=False,**axprops)
    # plotTree.totalW=float(getNumLeafs(inTree))
    # plotTree.totalD=float(getTreeDepth(inTree))
    # plotTree.xOff=-0.5/plotTree.totalW
    # plotTree.yOff=1.0
    # plotTree(inTree,(0.5,1.0),'')
    plt.show()
    
def displayTree(root, tot_dep, tot_leaf, nodes):
    fig=plt.figure(1,facecolor='white')
    fig.clf()
    axprops=dict(xticks=[],yticks=[])
    createPlot.ax1=plt.subplot(111,frameon=False,**axprops)
    totalW=float(tot_leaf)
    totalD=float(tot_dep)
    x = float(1/2)
    y = float(1)    
    display_dtl(root, "", (x,y), (x,y), 1, 1, nodes)
    #plotNode(root.data, (x,y), (x,y), decisionNode)
    plt.show()
    
def display_dtl(node, edge, cntrPt, parentPt, w, d, nodes): 
    # global nodes
    #print("nodes: %d" % (nodes))
    if nodes == 0:
        return
    else:
        if node.leaf == "Y":
            plotNode(node.data, cntrPt, parentPt, leafNode)
            plotMidText(cntrPt,parentPt,edge)
            nodes = nodes - 1
        else:
            plotNode(node.data, cntrPt, parentPt, decisionNode)
            plotMidText(cntrPt,parentPt,edge)
            nodes = nodes - 1
            numCh = len(node.ch) 
            y = float(d-0.2)
            #print("y: %d" % (y))
            xp = float(w/(numCh+1))
            #print("xp: %d" % (xp))              
            x = (cntrPt[0] - float(w/2)) + xp
            #print("x,y: {}" .format((x,y)))  
            w = 2*xp
            #print("w,w/2: %f %f" %(w, float(w/2)))
            for ele in node.ch:
                chedge = ele[0]
                chnode = ele[1]
                display_dtl(chnode, chedge, (x,y), cntrPt, w, y, nodes)
                x = x + xp
        return