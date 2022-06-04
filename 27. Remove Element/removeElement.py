class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        for check in nums:
            if check != val:
                nums[res] = check;
                res += 1
        return res