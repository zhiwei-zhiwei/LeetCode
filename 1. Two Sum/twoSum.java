class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] temp = new int[2];
        for(int i =0; i < nums.length; i++){
            for(int j = 0; j < nums.length; j++){
                if(i == j){
                    continue;
                }else{
                    if(nums[i]+nums[j] == target){
                        temp[0] = i;
                        temp[1] = j;
                        return temp;
                    }
                }
            }
        }
        return temp;
    }
}