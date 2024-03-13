class Solution {
    public double largestSumOfAverages(int[] nums, int k) {
        double[] prefix_sum = new double[nums.length + 1];
        for(int i = 1; i < prefix_sum.length; i++){
            prefix_sum[i] = nums[i-1] + prefix_sum[i-1];
            System.out.println(prefix_sum[i]);
        }
        double[][] f = new double[nums.length+1][k+1];
        for (int i = 1; i < nums.length + 1; i++){
            for (int j = 1; j < Math.min(i, k) + 1; j++){
                if (j == 1) f[i][j] = prefix_sum[i] / i;
                else{
                    for(int m = 2; m < i+1; m++){
                        f[i][j] = Math.max(f[i][j], f[m-1][j-1] + (prefix_sum[i] - prefix_sum[m-1]) / (i-m+1));
                    }
                }
            }
        }

        return f[nums.length][k];
    }
}
