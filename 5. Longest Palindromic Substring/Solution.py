class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(2 * len(s) - 1):
            left = i // 2
            right = left + i % 2

            while left >= 0 and right < len(s) and s[left] == s[right]:
                temp = s[left:right+1]
                if len(temp) > len(res):
                    res = temp
                left -= 1
                right += 1
        return res
