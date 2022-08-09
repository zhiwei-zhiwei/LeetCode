class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def comb(num, combinations):
            if len(combinations) == len(digits):
                res.append(combinations)
                return
            for i in phoneMap[digits[num]]:
                comb(num+1, combinations + i)

        if digits:
            comb(0, "")
        return res
