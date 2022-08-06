class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (index, temperatures)
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > temperatures[stack[-1]]:
                position = stack.pop()
                res[position] = i - position
            stack.append(i)
        return res



        '''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            count = 0
            for j in range(i,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    count = j - i
                    res.append(count)
                    break
            if count == 0:
                res.append(0)
        return res
        '''
