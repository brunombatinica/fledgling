# writing up a little function that installs 

from graphviz import Digraph

def trace(root):
    # root = starting Value object to build tree from

    #builds a set of all nodes and edges in a graph
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child,v))
                build(child) #recursive call to repeat addition on each child
    build(root)
    return nodes, edges

def draw_dot(root):
    dot = Digraph(format = "svg", graph_attr={"rankdir":"LR"}) #LR = left to right

    nodes, edges = trace(root)

    for n in nodes:
        uid = str(id(n))
        # for any vlaue in hte graph, create a rectuangular ("record") node for it
        dot.node(name = uid, label = "{%s | data %.4f | grad %s}" % (n.label, n.data,n.grad), shape = "record")
        if n._op: #if n is the result of an opertaion
            #if this value is a result of some operation, creat an op node for it
            dot.node(name = uid + n._op, label = n._op)
            #and connect this node to it
            dot.edge(uid+n._op,uid)
    
    for n1, n2 in edges:
            # connect n1 to the op node of n2
            dot.edge(str(id(n1)), str(id(n2)) + n2._op)

    return dot

#draw_dot(L)
