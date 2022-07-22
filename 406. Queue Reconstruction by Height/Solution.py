class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        for i in people:
            if len(res) <= i[1]:
                res.append(i)
            else:
                res.insert(i[1], i)
        return res
        '''
        after sort -> [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]

        res-[[7, 0]]
            [[7, 0], [7,1]]
            [[7, 0], [6, 1], [7,1]]
            [[5, 0], [7, 0], [6, 1], [7,1]]
            [[5, 0], [7, 0], [5, 2], [6, 1], [7,1]]
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7,1]]
        '''
                
