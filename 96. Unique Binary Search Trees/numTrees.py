class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n+1)
        for i in range(2,n+1):
            count = 0
            for root in range(1,i+1):
                left = root - 1 # the node start form 1 to n, so the first count will start with -- left: 0, right n - root
                right = i - root
                count += dp[left]*dp[right]
            dp[i] =count
        return dp[n]