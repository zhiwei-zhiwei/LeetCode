# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(root):
            if not root:
                return None
            leftNode = dfs(root.left)
            rightNode = dfs(root.right)
        
            if root.left:
                leftNode.right = root.right
                root.right = root.left
                root.left = None
            
            res = rightNode or leftNode or root
            return res
        dfs(root)