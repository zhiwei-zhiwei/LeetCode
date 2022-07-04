class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = [] # return value
        self.dfs(1,n,[],k,res)
        return res
        # temp = [] # temp store value


    def dfs(self,curr,n,temp,limit,res):
        # limit -> k
        if len(temp) == limit:
            res.append(temp[:])
            return
        for i in range(curr, n+1):
            temp.append(i)
            self.dfs(i+1,len,temp,limit,res)
            temp.pop()