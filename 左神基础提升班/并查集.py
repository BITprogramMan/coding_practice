class Element:
    def __init__(self, val=0):
        self.val = val

class UnionFindSet:
    def __init__(self, nums):
        self.elementMap = dict()
        self.parentMap = dict()
        self.setSizeMap = dict()
        for val in nums:
            element = Element(val)
            self.elementMap[val] = element
            self.parentMap[element] = element
            self.setSizeMap[element] = 1

    def findHead(self, node):
        path = []
        while node != self.parentMap[node]:
            path.append(node)
            node = self.parentMap[node]
        res = node
        while path:
            node = path.pop()
            self.elementMap[node] = res
        return res

    
    def isSameSet(self, v1 , v2):
        if v1 not in self.elementMap or v2 not in self.elementMap:
            return False
        return self.findHead(self.elementMap[v1]) == self.findHead(self.elementMap[v2])
    
    def union(self, v1, v2):
        if v1 not in self.elementMap or v2 not in self.elementMap:
            return 
        node1, node2 = self.elementMap[v1], self.elementMap[v2]
        parent1 = self.findHead(node1)
        parent2 = self.findHead(node2)
        if parent1 != parent2:
            big = parent1 if self.setSizeMap[parent1] >= self.setSizeMap[parent2] else parent2
            small = parent2 if big == parent1 else parent1
            self.parentMap[small] = big
            self.setSizeMap[big] += self.setSizeMap[small]
            del self.setSizeMap[small]
            
            



    
