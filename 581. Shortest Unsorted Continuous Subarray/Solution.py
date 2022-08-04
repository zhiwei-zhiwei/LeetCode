class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        minVal = nums[length-1]
        maxVal = nums[0]
        begin, end = 0 , -1
        for i in range(length):
            if nums[i] < maxVal:
                end = i
            else:
                maxVal = nums[i]
            
            if nums[length - i - 1] > minVal:
                begin = length - i - 1
            else:
                minVal = nums[length-i-1]
        return end - begin + 1
