class Solution:
    def trap(self, height: List[int]) -> int:
        sum = 0
        # for i in range(10,0,-1):
        #     print(i)
        for i in range(1,len(height)-1):
            left_max = 0
            for j in range(i-1,-1,-1):
                left_max = max(height[j],left_max)
                # print("left +++++ ",left_max)
            # print("left --- ",left_max)
            right_max = 0
            for k in range(i+1,len(height)):
                right_max = max(height[k],right_max)
            # print("right --- ",right_max)
            
            temp = min(left_max,right_max)
            # print("temp --- ",temp)
            if height[i] < temp:
                sum += (temp-height[i])
            # print("sum ===== ",sum)
        return sum