class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        res = []
        nums.sort()
        '''
        [4,4,4,1,4]
        to deal with this situation, wo need to sort the list first to prvenet that when the last 4 generate the duplicated list
        is not, it will not enter the if statement in dfs function
        '''
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
            if i > curr and nums[i] == nums[i-1]: continue 
            path.append(nums[i])
            self.dfs(nums,path,res, i+1)
            # nums is unique, so it will go to next element every time
            path.pop()