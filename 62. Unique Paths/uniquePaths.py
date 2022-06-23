class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j]+arr[i][j-1]
        return arr[m-1][n-1]