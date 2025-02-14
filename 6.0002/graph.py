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
    g.addEdge(edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g
    
def printpath(pathlist):
    if pathlist == [] or pathlist == None:
        print("[]")
    else:
        pathstr = "["
        for i in pathlist:
            pathstr += i.getName() + ", "   
        print(pathstr[:-2] + "]")
 
    
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
    
    #create a list of paths to search
    #initial path lsit = the first element
    pathQueue = [initPath]
    
    while len(pathQueue) != 0:
        
        #extract first path in queue
        temppath = pathQueue.pop(0) 
        
        if toPrint:
            print('current path:', end = "")
            printpath(temppath)
            print("current Queue:")
            for path in pathQueue:
                    printpath(path)
          
        #extract alst point in path and EXPLORE!!!!
        lastNode = temppath[-1]
        if lastNode == end:
            return temppath
        else:
            #Create a set of new paths to add to the pathqueeu to check
            for node in graph.childrenOf(lastNode):
                newpath = temppath + [node]
                pathQueue.append(newpath)
                
    return None
                
    
    
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

printpath(BFS(example,
              example.getNode("Boston"),
              example.getNode("Phoenix"),
              True))


