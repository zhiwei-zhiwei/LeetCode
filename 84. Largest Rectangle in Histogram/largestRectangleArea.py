class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        -----------Brute force solution--------------- will cause time out
        dp = [ [0] * (len(heights)) for _ in range(len(heights))]
        res = 0
        for row in range(len(heights)):
            for col in range(row,len(heights)):
                if row == col: dp[row][col] = heights[row]
                else:
                    dp[row][col] =  min(heights[row:col+1])*(col-row+1)
                res = max(res,dp[row][col])
        return res
        '''
        # STACK solution
        res = 0
        stack = [] # store the index and the hight (heights[index])
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                # while statck is not empty and 
                # the previous one is height than current hight
                # do pop
                index, height = stack.pop()
                res = max(res, height * (i - index))
                start = index # update the start point
            stack.append((start,h))

        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
        return res