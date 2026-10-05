class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        cache = [[0]*cols for _ in range(rows)]

        def dfs(r,c,rows,cols, cache):
            if r >= rows or c >= cols or obstacleGrid[r][c]==1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r==rows-1 and c == cols-1:
                return 1
            
            cache[r][c] = (dfs(r+1, c, rows, cols, cache) + dfs(r, c+1, rows, cols, cache))
            return cache[r][c]
        return dfs(0, 0, rows, cols, cache)


