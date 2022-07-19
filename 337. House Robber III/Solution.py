# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # bottom up
        def dfs(root):
            if not root:
                return 0, 0    # money if rob, money if not rob
            left = dfs(root.left)
            right = dfs(root.right)
            # if rob root, we cannot rob left and right subroot
            rob = root.val + left[1] + right[1]
            # if not rob root, we can get max from left (rob or not rob), same for root.right
            not_rob = max(left) + max(right)
            return rob, not_rob
        return max(dfs(root))
