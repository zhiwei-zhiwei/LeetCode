class Solution {
    public int lengthOfLIS(int[] nums) {
        int len = nums.length;
        int maxSol = 0;
        int[] dp = new int[len+1];
        for(int i = 0; i< len; i++){   
            dp[i] = 1;        
            for(int j = 0; j< i; j++){
                if(nums[i] > nums[j]){
                    dp[i] = Math.max(dp[j]+1,dp[i]);
                }
            }
            maxSol = Math.max(maxSol,dp[i]);
        }
        // System.out.print(dp[1]);
        return maxSol;
    }
}
