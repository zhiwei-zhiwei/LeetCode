class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        lremove, rremove = 0, 0
        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        def isValid(str):
            cnt = 0
            for c in str:
                if c == '(':
                    cnt += 1
                elif c == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        def helper(s, start, lremove, rremove):
            if lremove == 0 and rremove == 0:
                if isValid(s):
                    res.append(s)
                return

            for  i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue

                # while there is no char can be removed
                if lremove + rremove > len(s) - i:
                    break

                if lremove > 0 and s[i] == '(':
                    helper(s[:i] + s[i + 1:], i, lremove - 1, rremove);

                if rremove > 0 and s[i] == ')':
                    helper(s[:i] + s[i + 1:], i, lremove, rremove - 1);

        helper(s, 0, lremove, rremove)
        return res
