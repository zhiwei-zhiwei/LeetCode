class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                # check every one before
                '''
                eg. [1, 3, 4, 5] 7
                dp[0] = 0
                dp[1] = 1
                dp[2] = 2
                dp[3] = 1
                dp[4] = 1
                dp[5] = 1
                dp[6] = 2
                dp[7] = 2  <---- min(1+dp[7-1], 1+dp[7-3], 1+DP[7-4], 1+DP[7-5])
                '''
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        if dp[amount] == float('inf'):return -1 #there is no result for the amount
        return dp[amount]
