class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def largestRectangleArea(self, heights):
            res = 0
            stack = [] # store the index and the hight (heights[index])
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    res = max(res, height * (i - index))
                    start = index # update the start point
                stack.append((start,h))

            for i, h in stack:
                res = max(res, (len(heights) - i) * h)
            return res
        
        
        row, col = len(matrix), len(matrix[0])
        sol = 0
        height = [0 for _ in range(col)]
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == '0':
                    height[c] = 0
                else: 
                    height[c] += 1
            temp = largestRectangleArea(self,height)
            sol = max(sol, temp)

        return sol