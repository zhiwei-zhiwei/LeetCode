class Solution:
    def canJump(self, nums: List[int]) -> bool:
        temp = 0
        for i,v in enumerate(nums):
            if temp >= i and i + v > temp:
                temp = i + v
        return temp >= len(nums)-1
