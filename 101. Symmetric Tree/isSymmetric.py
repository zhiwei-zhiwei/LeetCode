# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def comp(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            return comp(leftNode.left, rightNode.right) and comp(leftNode.right, rightNode.left)

        if not root:
            return True
        return comp(root.left, root.right)
            