class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, temp, total):
            if total == target:
                res.append(temp[:])
                return
            if total > target or index >= len(candidates):
                return
            
            temp.append(candidates[index])
            dfs(index, temp, total + candidates[index])
            temp.pop()
            dfs(index+1, temp, total)
            # index+1 here -> in order to make sure that the next backtrace will not go throught the same element that already used before
            # eg. candidates = [2,3,6,7], target = 7
            #          [2,2]
            #         /     \ (index+i) make sure it will not read the 2 again
            #    [2,2,2]    [2,2,3]
        
        dfs(0,[],0)
        return res
