networkEditor = kwargs ['pane'] 
currentPath = networkEditor.pwd().path() 
context = networkEditor.pwd().childTypeCategory ( ) 
currentContext = context.name()

pos = networkEditor.cursorPosition ( ) 

nodes = hou.node ( currentPath ).children ( ) 
nearestNode = None 
dist = 999999999.0 
for node in nodes: 
    d = ( node.position ( ) + ( node.size ( ) * 0.5 ) ).distanceTo ( pos ) 
    #print "{0} {1} {2}".format(d, node.position(), node.name()) 
    if d < dist: 
        nearestNode = node 
        dist = d 

handled = False 
if nearestNode: 
    if currentContext == 'Object': 
        networkEditor.cd ( nearestNode.path ( ) ) 

    if currentContext == 'Sop': 
        if nearestNode.isDisplayFlagSet ( ): 
            networkEditor.cd ( nearestNode.path ( ) ) 
            handled = True 
        else: 
            nearestNode.setDisplayFlag ( True ) 
            nearestNode.setRenderFlag ( True ) 

    if currentContext != 'Object' and not handled: 
        nearestNode.setSelected ( True, clear_all_selected=True )
        
    if currentContext == 'Dop':
        nearestNode.setDisplayFlag(True)