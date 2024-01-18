from typing import List

class solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from_left = [1] * len(nums)
        for i in range(1, len(nums)):
            from_left[i] = from_left[i - 1] * nums[i - 1]

        from_right = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            from_right[i] = from_right[i + 1] * nums[i + 1]

        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = from_left[i] * from_right[i]
        return res

nums = input().strip('[]').split(',')
nums = [int(n) for n in nums]
sol = solution()
print(sol.productExceptSelf(nums))

        '''
        org = [1, 2, 3, 4]
        leftMost = 1, 1*nums[0], 1*nums[0]*nums[1], 1*nums[0]*nums[1]*nums[2]
        leftMost = 1, 1*1, 1*1*2, 1*1*2*3
        leftMost = preRes
        preRes = [1, 1*1, 1*1*2, 1*1*2*3] = [1, 1, 2, 6]

        rightMost = 1, 1*nums[3], 1*nums[3]*nums[2], 1*nums[3]*nums[2]*nums[1]
        rightMost = 1, 1*4, 1*4*3, 1*4*3*2
        
        res update from right to left
        res = [1, 1, 2, 6] * rightMost
        res = [1*(1*1*4*3),1*(1*4*3),2*(1*4), 6*1] = [24, 12, 8, 6]
        '''
