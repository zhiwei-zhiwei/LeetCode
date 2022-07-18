class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        # f[i][0]: buy
        # f[i][1]: sell
        # f[i][2]: cooldown
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            # f[i - 1][0] -> same number from yesterday
            # f[i - 1][2] - prices[i] -> check if it worse to cooldown,
            f[i][1] = f[i - 1][0] + prices[i]
            # always update the number to check the sell
            f[i][2] = max(f[i - 1][1], f[i - 1][2])
            # if it sells yesterday, the cooldown number should be same as the profit made yester day
        
        return max(f[n - 1][1], f[n - 1][2])
