class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = float('-inf')
        tempMax = 1
        tempMin = 1
        for i in nums:
            if i < 0:
                # negetive number will cause the max -> min and min -> max
                # then switch them to make sure the algo can get the max value
                temp = tempMin
                tempMin = tempMax
                tempMax = temp
            tempMax = max(i, tempMax*i)
            tempMin = min(i, tempMin*i)

            maxVal = max(maxVal, tempMax)
        return maxVal