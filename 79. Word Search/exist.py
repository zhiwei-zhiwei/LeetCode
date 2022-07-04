class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        apply = set()
        
        def dfs(r,c,count):
            if count == len(word):
                return True
            
            if (r < 0 or c < 0 or r >= row or c >= col or # out of boundary
                word[count] != board[r][c] # didnt find the same one
                or (r,c) in apply): # the one alrady in used
                return False
            
            apply.add((r,c))
            # check all four directions
            res = (dfs(r+1,c,count+1) or
                dfs(r-1,c,count+1) or 
                dfs(r,c+1,count+1) or 
                dfs(r,c-1,count+1)) 
            apply.remove((r,c))
            return res

        for i in range(row):
            for j in range(col):
                if dfs(i,j,0): return True
        return False