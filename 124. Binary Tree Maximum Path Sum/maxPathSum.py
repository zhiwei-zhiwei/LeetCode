# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]
        # print(res[0])
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # incase to deal with the negative number
            # eg:    3
            #      /   \
            #    -1    -4    the max should be 3 instad of 2

            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # calculate the split situation
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # calculate the one single branch situation
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]