class TireNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TireNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for i in word:
            if i not in curr.children:
                curr.children[i] = TireNode()
            curr = curr.children[i]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)




# easy solution
# but high time complexity
'''class Trie:

    def __init__(self):
        self.stack = set()

    def insert(self, word: str) -> None:
        self.stack.add(word)

    def search(self, word: str) -> bool:
        return word in self.stack

    def startsWith(self, prefix: str) -> bool:
        for val in self.stack:
            if val[0:len(prefix)] == prefix:
                return True
        return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)'''
