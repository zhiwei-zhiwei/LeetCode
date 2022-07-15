class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # -------------------------------
        # Time : O(m+n)
        # Space: O(1)
        r, c = 0, cols - 1

        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False

        # -------------------------------
        # -------------------------------
        # Time : O(mn)
        # Space: O(1)
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == target:
                    return True
        return False
