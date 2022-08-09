class Solution {
    public int maxArea(int[] height) {
        int len = height.length;
        int res = 0;
        int right = len-1;
        int left = 0;
        while(left != right){            
            // System.out.println(left+" - "+right);
            int temp = Math.min(height[left], height[right]) * (right-left);
            // System.out.println(temp);
            if(height[left] < height[right]) {
                left++;
            }else {
                right--;
            }
            res = Math.max(temp, res);
        }
    
        return res;
    }
}
