class UnionFind:
    def __init__(self):
        self.setSizeMap = dict()
        self.parentMap = dict()

    def findparent(self, node):
        path = []
        while self.parentMap[node] != node:
            path.append(node)
            node = self.parentMap[node]
        while path:
            tmp_node = path.pop()
            self.parentMap[tmp_node] = node
        return node
    
    def makeSet(self, nodes):
        for node in nodes:
            self.parentMap[node] = node
            self.setSizeMap[node] = 1
    
    def isSameSet(self, node1, node2):
        return self.findparent(node1) == self.findparent(node2)


    def union(self, node1, node2):
        if not node1 or not node2:
            return
        
        parent1 = self.findparent(node1)
        parent2 = self.findparent(node2)
        if parent1 != parent2:
            parent1_size = self.setSizeMap[parent1]
            parent2_size = self.setSizeMap[parent2]
            if parent1_size > parent2_size:
                self.parentMap[parent2] = parent1
                self.setSizeMap[parent1] += parent2_size
                del self.setSizeMap[parent2]
            else:
                self.parentMap[parent1] = parent2
                self.setSizeMap[parent2] += parent1_size
                del self.setSizeMap[parent1] 


class Solution:
    def kruskalMST(self, graph):
        uninfind = UnionFind()
        uninfind.makeSet(graph.nodes.values())
        edges = list(graph.edges)
        edges.sort(key=lambda edge: edge.weight)
        res = []
        for edge in edges:
            if not uninfind.isSameSet(edge.from_, edge.to_):
                res.append(edge)
                uninfind.union(edge.from_, edge.to_)
        return res