class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n for _ in range(n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            dp[i] = i
            for square in range(2,n):
                if i - square * square < 0:
                    break
                dp[i] = min(dp[i-square*square]+1,dp[i])
        return dp[-1]
