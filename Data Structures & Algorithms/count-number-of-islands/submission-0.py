class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0 
        visit = set()
        def dfs(r, c, grid, visit):
            if (min(r,c)<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]=="0"):
                return 
            elif((r,c) in visit):
                return 
                
            visit.add((r,c))
            dfs(r+1, c, grid, visit)
            dfs(r-1, c, grid, visit)
            dfs(r, c+1, grid, visit)
            dfs(r, c-1, grid, visit)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=="1" and ((r,c)) not in visit:
                    dfs(r,c,grid,visit)
                    islands+=1
        return islands
        