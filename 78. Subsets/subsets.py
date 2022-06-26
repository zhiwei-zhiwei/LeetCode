class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        res = []
        self.dfs(nums,[],res,0)
        return res

    def dfs(self, nums, path, res, curr):
        """
        nums -> current list requires to be solved
        path -> the path that contains the current element
        res -> return value
        curr -> current element that the algo is working on
        """
        res.append(path[:])
        for i in range(curr, len(nums)):
            path.append(nums[i])
            self.dfs(nums,path,res, i+1)
            # nums is unique, so it will go to next element every time
            path.pop()    