class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftMost, rightMost = 1, 1
        res = []
        res.append(leftMost)
        for i in range(1,len(nums)):
            leftMost = leftMost * nums[i-1]
            res.append(leftMost)
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * rightMost
            rightMost = rightMost * nums[i]
        return res
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
