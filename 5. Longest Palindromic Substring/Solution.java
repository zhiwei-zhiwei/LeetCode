class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        char[] charArr = s.toCharArray();
        if(s.length() < 2){
            return s;
        }
        boolean[][] dp = new boolean[len][len];
        for(int i = 0; i< len; i++){
            dp[i][i] = true;
        }
        int left = 0;
        int max = 1;

        for(int j = 1; j < len; j++){
            for(int i = 0; i < j; i++){
                if(charArr[i] != charArr[j]){
                    dp[i][j] = false; 
                }else{
                    if((j-1) - (i+1) + 1 < 2){
                        dp[i][j] = true;
                    }else{
                        dp[i][j] = dp[i+1][j-1];
                    }
                }
                if(dp[i][j] == true && j-i+1 > max){
                    max = j-i+1;
                    left = i;
                }
            }
        }
    return s.substring(left, left+max);
    }
}
