class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return 
            for i in range(len(nums)):
                # q = nums[:i]
                # w = nums[i+1:]
                qw = nums[:i] + nums[i+1:]
                # e = tmp
                # r = [nums[i]]
                er = tmp + [nums[i]]
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res