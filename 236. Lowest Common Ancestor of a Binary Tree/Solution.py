# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            # while the current root is equal to one of the search node, 
            # the root will be the ancestor
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p ,q)
        if not left: return right 
        # while it cannot find the node on left, the ancestor should on the right
        if not right: return left
        # while it cannot find the node on right, the ancestor should on the left
        if left and right: return root
        # if find the nodes on both side, look back to the root
