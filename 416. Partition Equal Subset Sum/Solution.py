class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            temp = set()
            for t in dp:
                if (t + nums[i] == target):
                    return True
                temp.add(t + nums[i])
                temp.add(t)
            dp = temp
        return False
   

#-----------------------------------------------------------
# dp solution Knapsack problem
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = [[False] * (target + 1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
            
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for r in range(1, len(nums)):
            check = nums[r]
            for c in range(target + 1):
                if c <= check:
                    dp[r][c] = dp[r-1][c]
                else:
                    dp[r][c] = dp[r-1][c] | dp[r-1][c-nums[r]]
        return dp[len(nums)-1][target]
