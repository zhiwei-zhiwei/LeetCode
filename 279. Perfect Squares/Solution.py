class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        square = 2
        for i in range(1, n+1):
            dp[i] = i
            for square in range(2,n):
                if i - square * square < 0:
                    break
                dp[i] = min(dp[i-square*square]+1,dp[i])
        return dp[-1]
