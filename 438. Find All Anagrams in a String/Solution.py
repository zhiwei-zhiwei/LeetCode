class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        sCount, pCount = {}, {}

        for i in range(len(p)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
        
        res = [0] if sCount == pCount else []
        # deal with first p items first
        left = 0
        for right in range(len(p), len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            sCount[s[left]] -= 1

            if sCount[s[left]] == 0:
                sCount.pop(s[left])          
            left += 1
            if sCount == pCount:
                res.append(left)
        return res

        
        # brute force solution
        # res = []
        # for i in range(len(s)):
        #     temp = len(p)
        #     tempStore = list(p)
        #     if i <= len(s) - len(p):
        #         for j in range(i,i+temp):
        #             if s[j] in p and s[j] in tempStore:
        #                 tempStore.remove(s[j])
        #                 temp-=1
        #         if temp == 0:
        #             res.append(i)
        # return res
