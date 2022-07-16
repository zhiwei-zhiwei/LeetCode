class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        # similar like question 142
        # Floyd's algo
        while 1:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if nums[fast] == nums[slow]:
                fast = 0
                break

        while 1:
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                return slow
        # while 1:
        #     if nums[]
