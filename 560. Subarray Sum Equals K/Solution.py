class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res = 0
        
        # for i in range(len(nums)):
        #     total = 0
        #     for j in range(i, len(nums)):
        #         total += nums[j]
        #         # if total > k:
        #         #     break
        #         if total == k:
        #             res += 1
                    
                
        # return res
        res = 0
        curr = 0
        prefix = {0: 1}
        for i in nums:
            curr += i
            diff = curr - k
            
            res += prefix.get(diff,0)
            prefix[curr] = 1 + prefix.get(curr, 0)

        return res  
