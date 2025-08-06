class TrieNode:
    def __init__(self):
        self.num_pass = 0
        self.num_end = 0
        self.nexts = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        if not word:
            return
        node = self.root
        node.num_pass += 1
        for char in word:
            index = ord(char) - ord('a')
            if node.nexts[index] is None:
                node.nexts[index] = TrieNode()
            node = node.nexts[index]
            node.num_pass += 1    
        node.num_end += 1

    def delete(self, word):
        if self.search(word):
            node = self.root
            node.num_pass -= 1
            for char in word:
                index = ord(char) - ord('a')
                node.nexts[index].num_pass -= 1
                if node.nexts[index].num_pass == 0:
                    node.nexts[index] = None 
                    return
                node = node.nexts[index]
            node.num_end -= 1

    def search(self, word):
        if not word:
            return 0
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.nexts[index]:
                return 0
            node = node.nexts[index]
        return node.num_end
    

    def prefixNumber(self, pre):
        if not pre:
            return 0
        node = self.root
        for char in pre:
            index = ord(char) - ord('a')
            if not node.nexts[index]:
                return 0
            node = node.nexts[index]
        return node.num_pass
    

if __name__ == '__main__':
    trie = Trie()
    trie.insert('abc')
    trie.insert('ab')
    print(trie.search('abc'))
    print(trie.prefixNumber('ab'))
    trie.delete('abc')
    print(trie.search('abc'))







