class Solution(object):
    def threeSum(self, nums):
        # """
        # :type nums: List[int]
        # :rtype: List[List[int]]
        # """
        res = []
        nums.sort() # sort the list first, put the pointers besides the current number and the end of the list
        # [-1,0,1,2,-1,-4] --> [-4,-1,-1,0,1,2]

        for index,value in enumerate(nums):
            # enumerate helps to count the value by index from 0
            # {0,-4}, {1,-1}, {2,-1}, {3,0}, {4,1}, {5,2}
            if index > 0 and value == nums[index-1]:
                # skip the same value to prevet the same soluation exist in res
                continue
            
            l = index+1
            r = len(nums) -1
            # set the boundary of the left and right pointers

            while l < r:
                threeSum = value + nums[l]+nums[r]
                if threeSum < 0:
                    l += 1
                    # lest most is the smallest in a sorted array
                    #  when 3 sum is lest than 0, move the left pointer to increase the sum value
                elif threeSum > 0:
                    r -= 1
                    # similar like above, when 3 sum is bigger than 0, move right to decrease the sum
                else:
                    # when found
                    res.append([value,nums[l],nums[r]])
                    l += 1
                    # update the left pointer
                    while nums[l] == nums[l-1] and l < r:
                        # when the new left pointer same like previous one, move one more step
                        l += 1
        
        return res