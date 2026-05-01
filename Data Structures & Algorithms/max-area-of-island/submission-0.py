class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0 
        visited = set()

        def dfs(r,c, grid, visited):
            if min(r,c)<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]==0:
                return 0
            
            elif ((r,c)) in visited: 
                return 0
            
            visited.add((r,c))
            area= 1
            area += dfs(r+1, c, grid, visited)
            area += dfs(r-1, c, grid, visited)
            area += dfs(r, c+1, grid, visited)
            area += dfs(r, c-1, grid, visited)
            return area 
        for r in range(ROWS):
            for c in range(COLS):
                if(grid[r][c]==1 and ((r,c) not in visited)):
                    new_area=dfs(r,c,grid, visited)
                    maxArea = max(maxArea, new_area)
        return maxArea

