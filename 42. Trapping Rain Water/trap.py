class Solution1:
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
    
    
class Solution2:
    def trap(self, height: List[int]) -> int:
        res = 0
        for i in range(1,len(height)):
            leftMax = max(height[:i])
            
            rightMax = max(height[i:])

            # print(leftMax, "   ", rightMax)
            minHeight = min(leftMax, rightMax)
            if minHeight > height[i]:
                res = res + (minHeight - height[i])
        
        return res
    
    
    
class Solution3:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h1 = 0
        h2 = 0
        for i in range(len(height)):
            h1 = max(h1,height[i])
            h2 = max(h2,height[-i-1])
            ans = ans + h1 + h2 -height[i]
        temp = len(height)*h1
        return  ans - len(height)*h1
    
    
    
    
    
