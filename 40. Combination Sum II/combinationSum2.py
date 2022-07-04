class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(index, temp, total):
            if total == target:
                res.append(temp[:])
                return
            if total > target or index >= len(candidates) :
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]: continue 
                temp.append(candidates[i])
                dfs(i+1, temp, total + candidates[i])
                temp.pop()
        
        dfs(0,[],0)
        return res