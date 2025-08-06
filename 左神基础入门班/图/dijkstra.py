class Solution:
    def Dijkstra(self, head):
        distanceMap = {head:0}
        selectedNodes = set()
        def getMindistanceAndUnselectedNode(distanceMap, selectedNodes):
            minNode = None
            minDistance = float('inf')
            for node, distance in distanceMap.items():
                if node not in selectedNodes and distance < minDistance:
                    minNode = node
                    minDistance = distance
            return minNode
        minNode = getMindistanceAndUnselectedNode(distanceMap, selectedNodes)
        while minNode:
            distance = distanceMap[minNode]
            for edge in minNode.edges:
                if edge.to not in distanceMap:
                    distanceMap[edge.to] = distance + edge.weight
                else:
                    distanceMap[edge.to] = min(distanceMap[edge.to], distance + edge.weight)
            selectedNodes.add(minNode)
            minNode = getMindistanceAndUnselectedNode(distanceMap, selectedNodes)
        return distanceMap
    
    def Dijkstrav1(self, head):
        class NodeHeap:
            def __init__(self):
                self.distanceMap = {}
                self.headIndexMap = {}
                self.nodes = []
                self.size = 0

            def swap(self, index1, index2):
                self.headIndexMap[self.nodes[index1]] = index2
                self.headIndexMap[self.nodes[index2]] = index1
                self.nodes[index1], self.nodes[index2] = self.nodes[index2], self.nodes[index1]

            def insertAndheapify(self, index):
                while index >= 1 and self.distanceMap[self.nodes[index]] < self.distanceMap[self.nodes[(index - 1) // 2]]:
                    self.swap(index, (index - 1) // 2)
                    index = (index - 1) // 2
                
            def addOrUpdateOrIgnore(self, node, distance):
                if node in self.headIndexMap and self.headIndexMap[node] != -1:
                    self.distanceMap[node] = min(self.distanceMap[node], distance)
                if node not in self.headIndexMap:
                    self.distanceMap[node] = distance
                    self.headIndexMap[node] = self.size
                    self.nodes.append(node)
                    self.size += 1
                self.insertAndheapify(self.headIndexMap[node])

            def pop(self):
                node = self.nodes[0]
                distance = self.distanceMap[node]
                self.swap(0, self.size - 1)
                self.headIndexMap[node] = -1
                del self.distanceMap[node]
                self.nodes[self.size - 1] = None
                self.size -= 1
                self.heapify(0)
                return node, distance
            
            def heapify(self, index):
                left = index * 2 + 1
                while left < self.size:
                    smallest = left + 1 if left + 1 < self.size and self.distanceMap[self.nodes[left + 1]] < self.distanceMap[self.nodes[left]] \
                        else left
                    smallest = smallest if self.distanceMap[self.nodes[smallest]] < self.distanceMap[self.nodes[index]] else index
                    if smallest == index:
                        break
                    self.swap(smallest, index)
                    index = smallest
                    left = index * 2 + 1

        nodeHeap = NodeHeap()
        nodeHeap.addOrUpdateOrIgnore(head, 0)
        res = {}
        while nodeHeap.size > 0:
            node, distance = nodeHeap.pop()
            res[node] = distance
            for edge in node.edges:
                nodeHeap.addOrUpdateOrIgnore(edge.to, distance + edge.weight)
        return res
            