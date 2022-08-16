class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        temp = [[0]*l for _ in range(l)]
        for n in range(l):
            for m in range(l):
                temp[m][l-n-1] = matrix[n][m]
        matrix[:] = temp

        
        
        
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # print(n)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # n = 4
                # i = 0, j = 1
                # [0][1] -> [1][3]
                # [1][3] -> [3][2]
                # [3][2] -> [2][0]
                # [2][0] -> [0][1]
                matrix[i][j], matrix[n-j-1][i], matrix[n-i-1][n-j-1],matrix[j][n-i-1] = matrix[n-j-1][i], matrix[n-i-1][n-j-1], matrix[j][n-i-1], matrix[i][j]
