# https://leetcode.cn/problems/generate-parentheses/solution/hui-su-suan-fa-by-liweiwei1419/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # dfs algorithm
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            if left == 0 and right == 0:
                res.append(cur_str)
                # apply dfs as long as the it reach the leave of the tree
                return
            if right < left:
                # not allow the invalid parentheses
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res