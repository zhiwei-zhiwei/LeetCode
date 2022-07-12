# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
#         rows, cols = len(grid), len(grid[0])
#         visit = set()
#         island = 0

#         def dfs(r,c):
#             q = collections.deque()
#             visit.add((r,c))
#             q.append((r,c))
#             while q:
#                 row, col = q.pop()
#                 directions = [[1,0],[-1,0],[0,1],[0,-1]]
#                 for dr,dc in directions:
#                     r,c = row + dr, col+dc
#                     if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit):
#                         q.append((r,c))
#                         visit.add((r,c))

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r,c) not in visit:
#                     dfs(r,c)
#                     island += 1 
#         return island

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if (not 0<=i < m) or (not 0<=j< n) or grid[i][j] == '0':
                return
            else:
                grid[i][j] = '0'
                dfs(i+1,j) or dfs(i-1, j) or dfs(i, j+1) or dfs(i, j-1)

        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res