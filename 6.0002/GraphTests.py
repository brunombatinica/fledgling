#starting graph theory

#digraphs

class node(object):
    def __init__(self,name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def __str__(self):
        return self.name
    
class edge(object):
    def __init__(self,source,destination):
        #assume the arguments passed in are node objects
        self.src = source
        self.dest = destination
        
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() + "->" + \
            self.dest.getname()
            
            
#how to create digraphs
#Adjacency matrix - not efficient often

#Adjacency list



#Digraph
class digraph(object):
    #make a disctionary
    #Keys = sources
    #Values = destinations
    
    def __init__(self):
        self.edges = {}
        
    def addNode(self,node):
        if node in self.edges:
            raise ValueError('duplicate node')
        else:
            #initialize and empty list
            #the key is the node itself, not the name
            self.edges[node] = []
            
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        
        #check if destination and source exist
        if not (src in self.edges and dest in self.edges):
            raise ValueError("Node not in graph")
        
        #append list of destinations 
        self.edges[src].append(dest)
        
    #helper functions
    def childrenOf(self, node):
        #Returns the children of a given node
        return self.edges[node]
    
    def hasNode(self,node):
        return node in self.edges
    
    def getNode(self,name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
        
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + " -> " \
                    + dest.getName() + "\n"
        return result[:-1] #omit final newline
    

#Graph
class graph(digraph):
    #inherets digraph attributes
    
    #rewrite masks addEdge
    def addEdge(self,edge):
        #just doubles all edges to be bidirectional
        
        Digraph.addedge(self,edge)
        #reverse the edge
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
        
   
####PATHFINDING EXAMPLE
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(node(name))
    g.addEdge(edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(edge(g.getNode('Denver'), g.getNode('New York')))
    #REVERSED HTE LAST EDGE
    g.addEdge(edge(g.getNode('Boston'), g.getNode('Los Angeles')))
    return g
    
def printpath(pathlist):
    if pathlist == [] or pathlist == None:
        print("[]")
    else:
        pathstr = "["
        for i in pathlist:
            pathstr += i.getName() + ", "   
        print(pathstr[:-2] + "]")
        
################MY IMPLEMENTATION - CRAP        
# def DFS(graph,start,end,path = [],shortest = [],toPrint = False):
#     #Depth first search
#     #Recursive implementation    
    
#     #graph = grpah
#     #start and end are nodes
#     #path = list of nodes previously searched
#     #shortest = shortest current solution
#     # - to prevent overlap

#     print("START:",start)
#     print("END:",end)
#     printpath(path)
    
#     if start == end:
#         #we have found the destination
#         print("SOLVED:")
        
#         printpath(path)
#         path.append(start)
#         return path
        
#     elif graph.childrenOf(start) == []:
#         #dead end
#         return False
    
#     elif start in path:
#         #loop
#         return False
    
#     else:
#         #we need to go deeper
        
#         path.append(start)
#         print("WE NEED TO GO DEEPER")
        
#         for i in graph.childrenOf(start):
#             tempresult = DFS(graph,i,end,path,shortest,toPrint = False)           
#             print("tempresults:",tempresult)            
            
#             if tempresult:        
#                 #indicator of solution
#                 solved = 1
#                 if shortest == [] or len(path) < len(shortest):
#                     shortest = path
#                     path.pop()
#                 else:
#                     pass
#                 return shortest
                
#         #if no path is found - remove the added path node
#         path.pop()
#         return False
  

    
def myDFS(graph,start,end,path,shortest = {}):
    #not efficient but just for my knowledge of variable scopes
    
    print("START CURRENT NODE:",start)
    print("GOAL:",end)
    print("SHORTEST:",shortest)
    printpath(path)
    
    if start == end:
        print("SOLUTION")
        #check solution and return full path
        return path + [start]
    
    elif start in path:
        print("ALREADY IN PATH")
        #check if start is in path
        return None
    
    elif graph.childrenOf(start) == []:
        #check if dead end
        return None
    
    else:
        
        print("WE NEED TO GO DEEPER")
        path.append(start)

        for node in graph.childrenOf(start):
            temppath = myDFS(graph,node,end,path)
            
            if temppath != None:                
                if shortest == None or len(temppath) < len(shortest):                  
                    print("NEW SHORTEST PATH")
                    shortest = [*temppath]
                temppath = None
        
        path.pop() 
        return shortest
    
    
    
    
    
def myDFS2(graph,start,end,path,shortest):
    #not efficient but just for my knowledge of variable scopes
    
    print("START CURRENT NODE:",start)
    print("GOAL:",end)
    print("PATH:")
    printpath(path)
    print("SHORTEST:")
    printpath(shortest[1])
    
    if start == end:
        print("SOLUTION")
        #check solution and return full path
        
        
        return path + [start]
    
    elif start in path:
        print("ALREADY IN PATH")
        #check if start is in path
        return None
    
    elif graph.childrenOf(start) == []:
        #check if dead end
        return None
    
    else:     
        print("WE NEED TO GO DEEPER")
        path.append(start)

        for node in graph.childrenOf(start):
            temppath = myDFS2(graph,node,end,path,shortest)
            
            
            
            #THIS RECURSION MEANS IT GOES ALL THE WAY BACK TO THE START
            if temppath != None:                
                if shortest == None or len(path) < len(shortest):                  
                    print("NEW SHORTEST PATH")
                    shortest = [*temppath]
                    
        
        path.pop() 
        return shortest
    
  
def myDFS3(graph,start,end,path,shortest = {}):
      #not efficient but just for my knowledge of variable scopes
      
    print("START CURRENT NODE:",start)
    print("GOAL:",end)
    print("PATH:") 
    printpath(path)
    print("SHORTEST:")
    try:
        printpath(shortest[1])
    except:
        pass
    
    if start == end:
        print("###########SOLUTION")
        try:
            printpath(shortest[1])
        except:
            print("CANT PRINT SHORTEST")
        printpath(path)
        #check solution and return full path
        if shortest == {} or len(path) < len(shortest[1]):                  
            print("NEW SHORTEST PATH")
            shortest[1] = path + [start]
            
            #print(shortest)
            printpath(shortest[1])   
            
        return None
    
    elif start in path:
        print("ALREADY IN PATH")
        #check if start is in path
        return None
    
    elif graph.childrenOf(start) == []:
        #check if dead end
        return None
    
    else:     
        print("WE NEED TO GO DEEPER")
        path.append(start)

        for node in graph.childrenOf(start):
            print("LOOP BASE:",start)
            myDFS3(graph,node,end,path,shortest)
           
        path.pop() 
        return shortest[1] 
   
def myDFS4(graph,start,end,path):
    global shortest
    
    #not efficient but just for my knowledge of variable scopes
    print("START CURRENT NODE:",start)
    print("GOAL:",end)
    print("PATH:") 
    printpath(path)
    print("SHORTEST:")
    printpath(shortest)
    

    
    if start == end:
        print("###########SOLUTION")

        #check solution and return full path
        if shortest == [] or len(path) < len(shortest):                  
            print("NEW SHORTEST PATH")
            shortest = path + [start]
            #print(shortest)
            printpath(shortest)           
        return None
    
    elif start in path:
        print("ALREADY IN PATH")
        #check if start is in path
        return None
    
    elif graph.childrenOf(start) == []:
        #check if dead end
        return None
    
    else:     
        print("WE NEED TO GO DEEPER")
        path.append(start)

        for node in graph.childrenOf(start):
            print("LOOP BASE:",start)
            myDFS4(graph,node,end,path)
           
        path.pop() 
        return shortest 
   
    
def DFS(graph,start,end,path,shortest,toPrint = False):
    path = path + [start]
    
    #If print
    if toPrint:
        print("current DFS path:",printpath(path))
        
        
    if start == end:
        return path
    
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest == None or len(path) < len(shortest):
                #only check if shortest is empty or current path is
                #Shorter than the solution you have
                
                newPath = DFS(graph,node,end,path,shortest, toPrint)
                if newPath != None:
                    shortest = newPath
                    
        elif toPrint:
            #only executed if toPrint is "enabled"
            print("already visited", node)
    
    return shortest



def shortestPath(graph, start, end, toPrint = False):
    return DFS(graph, start, end, [], None, toPrint)
    


def BFS(graph,start,end,toPrint = False):
    initPath = [start]
    pathQueue = [initPath]
    while len(pathQueue) != 0:
        for node in pathQueue:
            for child in node.getChildren():
                print("TEMP")
    
    
example = buildCityGraph(digraph)
# printpath( shortestPath(example,
#                         example.getNode("Boston"),
#                         example.getNode("Phoenix"),
#                         toPrint = True))

# printpath(myDFS(example,
#                 example.getNode("Boston"),
#                 example.getNode("Phoenix"),
#                 [],
#                 {}))

# sol = myDFS3(example,
#                 example.getNode("Boston"),
#                 example.getNode("Phoenix"),
#                 [])

global shortest
shortest = []

sol = myDFS4(example,
                example.getNode("Boston"),
                example.getNode("Phoenix"),
                [])


printpath(sol)


