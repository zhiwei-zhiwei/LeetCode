class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            nums[abs(n)-1] = - abs(nums[abs(n)-1])
        print(nums)
        for i, v in enumerate(nums):
            if v > 0:
                res.append(i+1)
        return res
                
