# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)
        # add the node to the q all the time, and pop the first (first in first out)
        while q:
            l = len(q)
            levelList = []
            for i in range(l):
                node = q.popleft()
                if node:
                    levelList.append(node.val)
                    # add to the list and check the leave of the node
                    q.append(node.left)
                    q.append(node.right)
            if levelList:
                res.append(levelList)
        
        return res