class Solution {
    public int minPathSum(int[][] grid) {
        int sum = grid[0][0]; // count the total steps
        // System.out.println(grid.length);
        int row = grid.length;
        int col = grid[0].length;
        int[][] dp = new int[row][col];
        // dp[0][0] = grid[0][0];
        for(int i = 0; i < row; i++){
            for(int j = 0; j < col; j++){
                // System.out.println(Math.min(grid[i-1][j],grid[i][j-1]));
                if(i == 0 && j == 0) {
                    dp[i][j] = grid[0][0];
                    System.out.println("0"+ dp[i][j]);
                }
                if(i == 0 && j != 0) {
                    dp[i][j] = dp[i][j-1] + grid[i][j];
                    System.out.println("1"+ dp[i][j]);
                }
                if(i != 0 && j == 0) {
                    dp[i][j] = dp[i-1][j] +grid[i][j];
                    System.out.println("2"+ dp[i][j]);
                }
                if(i != 0 && j != 0) {
                    dp[i][j] = Math.min(dp[i-1][j],dp[i][j-1]) + grid[i][j];
                    System.out.println("3"+ dp[i][j]);
                }
            }
        }
        return dp[row-1][col -1];
    }
}
