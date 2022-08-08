class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        lenS, lenP = len(s), len(p)

        dp = [[False] * (lenP+1) for _ in range(lenS + 1)]
        dp[0][0] = True
        

        for i in range(1, lenP+1):
            if p[i-1] == '*':
                # skip two place and check for star
                dp[0][i] = dp[0][i-2]
        
        for i in range(1, lenS + 1):
            for j in range(1, lenP + 1):
                if p[j - 1] in {s[i -1], '.'}:
                    # match
                    dp[i][j] = dp[i-1][j-1]
                elif p[j - 1] == '*':
                    # star situation
                    if p[j - 2] in {s[i -1], '.'}:
                        # match
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        # skip two for star
                        dp[i][j] = dp[i][j - 2]
        return dp[lenS][lenP]
