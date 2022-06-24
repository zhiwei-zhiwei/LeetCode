class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row = len(word1)
        col = len(word2)
        # if there is an empty word, it can only always add or delete a letter
        if row * col == 0:
            return row + col

        dp = [ [0] * (col + 1) for _ in range(row + 1)]
        
        for i in range(row + 1):
            dp[i][0] = i
        for j in range(col + 1):
            dp[0][j] = j
        #  init the dp array
        #  ---------> add new letter
        # |        ""  r  o  s
        # | D  "" [[0, 1, 2, 3], 
        # | E  h  [1, 0, 0, 0], 
        # | L  o  [2, 0, 0, 0], 
        # | E  r  [3, 0, 0, 0], 
        # | T  s  [4, 0, 0, 0], 
        # ⇩ E  e  [5, 0, 0, 0]]
        #                      ↘ REPLACE LETTE

        for i in range(1,row+1):
            for j in range(1,col+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        # [[0, 1, 2, 3],
        #  [1, 1, 2, 3],
        #  [2, 2, 1, 2], 
        #  [3, 2, 2, 2], 
        #  [4, 3, 3, 2], 
        #  [5, 4, 4, 3]]
        #            * return the last one

        return dp[row][col]