class Graph:
    def __init__(self):
        self.nodes = dict()
        self.edges = set()

class Node:
    def __init__(self, val=0, in_=0, out_=0, nexts=[], edges=set()):
        self.val = val
        self.in_ = in_
        self.out_ = out_
        self.nexts = nexts
        self.edges = edges

class Edge:
    def __init__(self, weight=0, from_=None, to=None):
        self.weight = weight
        self.from_ = from_
        self.to_ = to


def Graphgenerator(matrix):
    graph = Graph()
    for i in range(len(matrix)):
        weight = matrix[i][0]
        from_ = matrix[i][1]
        to_ = matrix[i][2]
        if from_ not in graph.nodes:
            graph.nodes[from_] = Node(val=from_)
        if to_ not in graph.nodes:
            graph.nodes[to_] = Node(val=to_)
        fromNode = graph.nodes[from_]
        toNode = graph.nodes[to_]
        newEdge = Edge(weight, fromNode, toNode)
        fromNode.nexts.append(toNode)
        fromNode.out_ += 1
        toNode.in_ += 1
        fromNode.edges.add(newEdge)
        graph.edges.add(newEdge)
    return graph