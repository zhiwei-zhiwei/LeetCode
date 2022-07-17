class Solution {
    public int maxProfit(int[] prices) {
        int len = prices.length;
        int min = Integer.MAX_VALUE;
        int max = 0;
        int count = 0;
        for(int i = 1; i < len; i++){
            if(prices[i-1] < prices[i]){ // 只当右边的比左边的大的时候，更新max和min
                min = Math.min(min,prices[i-1]);
                max = Math.max(max,prices[i]);
            }else{
                if(max - min > 0){ // 在左边比右边大的时候，检查max和min大小，只当为正的时候才加入count
                    count += max - min;
                    max = 0; // 更新max和min 为了新的max和min
                    min = Integer.MAX_VALUE;
                }
            }
            if(i == len - 1 && prices[i-1] < prices[i]){ //应对全部递增的数组，到最后一位时算出最大值
                count += max - min;
            }            
        }
        return count;
    }
}


