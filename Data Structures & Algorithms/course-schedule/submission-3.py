class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq = {i: [] for i in range(numCourses)}
        for x, y in prerequisites:
            preq[x].append(y)
           
        visit = set()
        def dfs(crs):
            if crs in visit: 
                return False
            if preq[crs]==[]:
                return True
            visit.add(crs)
            for pre in preq[crs]:
                if dfs(pre) == False:
                    return False
            visit.remove(crs)
            preq[crs] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True