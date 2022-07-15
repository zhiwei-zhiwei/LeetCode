class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end   = sorted([i[1] for i in intervals])
        res, tempCount = 0, 0
        startPoint, endPoint = 0, 0

        while startPoint < len(intervals):
            if start[startPoint] < end[endPoint]:
                startPoint += 1
                tempCount += 1
            else:
                endPoint += 1
                tempCount -= 1
            res = max(res,tempCount)
        return res

        '''
        Input: intervals = [[0,30],[5,10],[15,20]]

        0--------------------------------------------30
            5--------10            15--------20
        |       |          |            |         |
        1       2          1            2         1    
        return max
        '''
