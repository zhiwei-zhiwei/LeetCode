class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       '''
       nums.sort()
       return nums[-k]
       '''
      
        k = len(nums) - k

        def qucikSelect(left, right):
            pivet = nums[right]
            point = left
            for i in range(left, right):
                if nums[i] <= pivet:
                    temp = nums[point]
                    nums[point] = nums[i]
                    nums[i] = temp
                    point += 1
            temp2 = nums[point]
            nums[point] = nums[right]
            nums[right] = temp2

            if point > k: 
                # Kth largest num in the left part
                return qucikSelect(left, point-1)
            elif point < k:
                # Kth largest num in the right part
                return qucikSelect(point+1, right)
            else:
                return nums[point]
        
        return qucikSelect(0, len(nums) - 1)
