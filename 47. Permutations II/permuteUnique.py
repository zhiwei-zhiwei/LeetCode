class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]: continue
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res