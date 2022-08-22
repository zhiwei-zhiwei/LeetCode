class Solution {
    public int maxSubArray(int[] nums) {
        int len = nums.length;
        int[] dp = new int[len];
        dp[0] = nums[0];
        int sol = nums[0];
        for(int i = 1; i < len; i++){
            dp[i] = Math.max(nums[i],nums[i]+dp[i-1]);
            sol = Math.max(sol,dp[i]);
        }
        return sol;
    }
}
