class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        
        p1, p2 = -1, -1
        def binarySeach(nums, target):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right - left)//2
                if nums[mid] > target:
                    right = mid -1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1

        index = binarySeach(nums, target)

        if index == -1: return [-1,-1]

        left, right= index, index

        while left-1 >= 0 and nums[left-1] == target:
            left -= 1
        
        while right+1 <= len(nums)-1 and nums[right+1] == target:
            right += 1
        
        return [left, right]
