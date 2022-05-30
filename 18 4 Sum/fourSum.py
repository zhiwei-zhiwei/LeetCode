class Solution:
    # similar like 3 sum
    # extra for loop than 3 sum -> force loop for tow element in the array
    # then update the left and right pointers to find the 4 sum
    def fourSum(self, nums, target):
        if not nums or len(nums) < 4:
            # whne the length of the array is not 4, return empty result
            return []
        nums.sort()
        # sort the array first in order to adjust the sum of 4 numbers
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                # prvenet the same elemnt in the resolution list
                continue
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    # prvenet the same element in the resolution list
                    continue
                l = j+1
                # put the left pointer just after the second element 
                r = len(nums)-1
                # put the right pointer form the end of the list
                while l < r:
                    sum = nums[i]+nums[j]+nums[l]+nums[r]
                    if sum == target:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l] == nums[l+1]: 
                            # prvenet the same element in the resolution list
                            l += 1
                        while l<r and nums[r] == nums[r-1]:
                            # prvenet the same element in the resolution list
                            r -= 1
                        # update the pointer
                        l += 1
                        r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1
        return res