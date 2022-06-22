class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sum = 0
        hashMap = dict()
        temp = 0
        for i in range(len(s)):
            if s[i] in hashMap:
                temp = max(hashMap[s[i]]+1,temp)
            hashMap[s[i]] = i
            # temp += 1
            sum = max(i-temp+1,sum)
        return sum
