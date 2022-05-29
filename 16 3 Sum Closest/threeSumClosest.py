class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # similar like the question 15 (3Sum),
        # but need to deal with very small target situation

        res = None
        nums.sort()
        temp = nums[0]+nums[1]+nums[2]
        # set the first three number as the temp cloest number

        for index, value in enumerate(nums):
            l = index + 1
            r = len(nums) - 1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if abs(target - threeSum) < abs(target - temp):
                    # when the threeSum is more cloes than the temp
                    # update the value of current temp value
                    # which helps to find the best return value
                    temp = threeSum

                # the rest part is similar to the question 15
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return temp
            
        
        return temp