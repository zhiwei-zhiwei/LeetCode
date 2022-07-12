# DFS solution
class TireNode:
    def __init__(self):
        self.children = {}
        # store the node by letters
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = TireNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for i in word:
            if i not in curr.children:
                # while the root node doest have the letter
                # generate a new one
                curr.children[i] = TireNode()
            curr = curr.children[i] # keep adding the new letters
        curr.isEnd = True # as long as reach the end of the word, make that place

    def search(self, word: str) -> bool:
        # DFS seaching
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.isEnd #make sure that is the end of that path

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
