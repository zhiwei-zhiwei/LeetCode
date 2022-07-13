class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        res = 0
        dp = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                    res = max(res, dp[r][c])
        return res*res
