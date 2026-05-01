class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        def dfs(grid, r,c, visit):
            if (r == rows or c ==cols or r < 0 or c < 0 or grid[r][c]==1 or (r,c) in visit):
                return 0
            if r == rows-1 and c == cols -1:
                return 1 

            visit.add((r,c))
            paths = (
                dfs(grid, r+1, c, visit) + 
                dfs(grid, r-1, c, visit) + 
                dfs(grid, r, c+1, visit) + 
                dfs(grid, r, c-1, visit)
            )
            visit.remove((r,c))

            return paths 
        return dfs(grid, 0, 0, visit)
