class Solution {
    public int removeDuplicates(int[] nums) {
        int check = 1;
        int count = 1;
        int len = nums.length;
        if(len == 0) {
            return 0;
        }
        while(check < len){
            if(nums[check] != nums[check-1]){
                nums[count] = nums[check];
                count++;
            }
            check++;
        }
        return count;
    }
}