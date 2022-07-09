class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # set the left and right boundary to find the LRU and MRU
        self.left, self.right = Node(0,0), Node(0,0)
        # init a two way list, point to each other
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        # [p] - [self.right]
        #    |
        # [p] - [node] - [self.right]
        p = self.right.prev
        n = self.right
        p.next = n.prev = node
        node.next = n
        node.prev = p

    def remove(self, node):
        # [p] - [node] - [self.right]
        #          |
        # [p] - [self.right]
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def get(self, key: int) -> int:
        if key in self.cache:
            # while can find the key in dict
            # make sure to update the LRU and MRU
            # ensure that LRU is always on the left most and MRU on the right most
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update the LRU and MRU
            self.remove(self.cache[key])
        # put into the cache
        self.cache[key] = Node(key,value)
        # then make sure that the new node is on the right most - MRU
        self.insert(self.cache[key])
        
        # when the cache size out of the size of capactity
        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)