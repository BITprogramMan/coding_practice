class RandomPool:
    def __init__(self):
        self.key2index = dict()
        self.index2key = dict()
        self.size = 0
    
    def insert(self, key):
        if key not in self.key2index:
            self.key2index[key] = self.size
            self.index2key[self.size] = key
            self.size += 1
            
    def delete(self, key):
        if key in self.key2index:
            deleteIndex = self.key2index[key]
            lastIndex = self.size - 1
            lastKey = self.index2key[lastIndex]
            self.key2index[lastKey] = deleteIndex
            self.index2key[deleteIndex] = lastKey
            del self.key2index[key]
            del self.index2key[lastIndex]

    def getRandom(self):
        if self.size == 0:
            return None
        import random
        randomIndex = int(random.random() * self.size)
        return self.index2key[randomIndex]