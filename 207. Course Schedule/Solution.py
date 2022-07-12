class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        checkMap = {i:[] for i in range(numCourses)}
        for course, prere in prerequisites:
            checkMap[course].append(prere)
        visited = set() # use the set to store the course and prevent the circle case
        # eg: [0,1] [1,2] [2,0]
        
        def dfs(course):
            if course in visited:
                return False
            if checkMap[course] == []:
                # while the map reach the end of the course, which is the first course have to take
                return True
            visited.add(course)
            for pre in checkMap[course]:
                if not dfs(pre):
                    # check each of them
                    return False
            visited.remove(course)
            # after check the path, remove from the visit set
            checkMap[course] = []
            # after check the path, make sure the current pass is the end (the first course have to take)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
