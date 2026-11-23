class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq = {i:[] for i in range(numCourses)}
        for x, y in prerequisites: 
            preq[x].append(y)
        
        visit = set()
        order = []
        def dfs(crs):
            if crs in visit:
                order.append(-1)
                return 
            if preq[crs] == []:
                return
            visit.add(crs)
            for pre in preq[crs]:
                dfs(pre)
                if -1 in order:
                    return 
                if pre in order: 
                    continue
                order.append(pre)
            visit.remove(crs)
            preq[crs] = []
            return 
        
        for i in range(numCourses):
            dfs(i)
            if -1 in order:
                return []
        for j in range(numCourses):
            if j not in order:
                order.append(j)
        return order
            
                