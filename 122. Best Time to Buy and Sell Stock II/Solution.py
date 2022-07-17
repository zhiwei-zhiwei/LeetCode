class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal = 0
        minVal = float('inf')
        res = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                maxVal = max(maxVal, prices[i])
                minVal = min(minVal, prices[i-1])
            else:
                if maxVal - minVal > 0:
                    res += (maxVal-minVal)
                    maxVal = 0
                    minVal = float('inf')
            if i == (len(prices) - 1) and prices[i-1] < prices[i]:
                res += maxVal - minVal
        return res
