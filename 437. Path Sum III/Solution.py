# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def findPath(node, targetS):
            if not node:
                return 0
            count = 0
            if node.val == targetS:
                count += 1
            count += findPath(node.left, targetS - node.val)
            count += findPath(node.right, targetS - node.val)
            return count
        
        if not root:
            return 0

        ret = findPath(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret

