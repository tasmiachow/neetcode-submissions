from collections import deque 
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        queue.append((0,0))
        visit = set()
        visit.add((0,0))
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length

                
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr == rows or c + dc == cols or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1
        return -1