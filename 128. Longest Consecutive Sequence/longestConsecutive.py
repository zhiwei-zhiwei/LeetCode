class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()  (nlogn)
        numSet = set(nums)
        res = 0
        for i in nums:
            if (i-1) not in numSet:
                # while there is no number small that the current number
                # while the current number is the start of the sequence
                tempLen = 0
                while i+tempLen in numSet:
                    # while the following number in the set
                    # count that into the sequence
                    tempLen += 1
                res = max(res, tempLen)
        
        return res