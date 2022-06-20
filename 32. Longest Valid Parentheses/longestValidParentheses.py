class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0]*n
        for i in range(len(s)):
            temp1 = dp[i-1]
            temp2 = i-dp[i-1]-1
            if s[i] == ')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == '(':
                # i-dp[i-1]-1>=0 --> make sure that it will not read the s[-11``]
                dp[i] = dp[i-1] + dp[i-dp[i-1] -2]+2
        
        return max(dp)