# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def orderTree(root):
            nonlocal v
            if root:
                orderTree(root.right)
                v += root.val
                root.val = v
                orderTree(root.left)
        v = 0
        orderTree(root)
        return root
