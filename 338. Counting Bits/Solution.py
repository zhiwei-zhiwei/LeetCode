class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n+1)]
        count = 1
        dp[0] = 0

        for i in range(1, (n+1)):
            if count * 2 == i:
                count = i
            
            dp[i] = dp[i-count] + 1

        return dp
