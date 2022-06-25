class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        winHave, tNeed = 0, len(countT)
        left = 0
        res = [-1,-1]
        minW = float("infinity")
        for r in range(len(s)):
            curr = s[r]
            window[curr] = 1 + window.get(curr, 0)

            if curr in countT and window[curr] == countT[curr]:
                winHave += 1
                # eg. "ADAOBECODEBANCA"
                #     "ABCA"
                # r = 2, curr = A
                # when the curr is same as one in t and the number that window have is same as countT has
                # num of A in T is 2; num of A in S is 2;
                # fulfill the t, so A is fulfilled
            
            while winHave == tNeed:
                # while the total number of have is same as tNeed, 
                # which means the current window already contains all elemnt that t reqired
                if (r - left + 1) < minW:
                    # compare with the last window's length
                    res = [left,r] # window
                    minW = r - left + 1
                    # update the new length as long as it smaller than last one
                window[s[left]] -= 1 # pop tthe window from left 
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    # when the removed element same as the element in t
                    # due to removing, it is the first time that element less than the count in t
                    winHave -= 1
                left += 1
        left, r = res

        return s[left:r+1] if minW != float("infinity") else ""