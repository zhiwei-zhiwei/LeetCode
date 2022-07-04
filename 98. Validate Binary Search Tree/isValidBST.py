# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            # update the left and right boundary every time to make sure that every node fits the root
            if not node:
                # reach the end of the tree, which means all nodes are suitable for the algorithmm
                return True
            if not (left < node.val and node.val < right):
                # while the node's value out of the boundary
                return False
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
            # recursively call the dfs and update the left and right boundary
        return dfs(root, float("-inf"), float("inf"))