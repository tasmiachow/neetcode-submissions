from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0 
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visit = set()
        fresh_fruit =0 
        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] ==1:
                    fresh_fruit +=1
        print(queue)
        print(fresh_fruit)
        if(fresh_fruit <=0):
            return 0
        while queue: 
            
            for i in range(len(queue)):
                r,c =queue.popleft()
                
                neighbors = [ [0,1], [1,0], [0,-1], [-1,0] ]

                for dr, dc in neighbors:
                    if(min(r+ dr, c+ dc)< 0 or 
                        r+dr>=ROWS or c+dc>=COLS or 
                        (r+ dr, c+ dc) in visit or
                        grid[r+dr][c+dc]==0):
                        continue 
                    if(grid[r+dr][c+dc]==1):
                        queue.append((r+dr, c+dc))
                        visit.add((r+dr, c+ dc))
                        fresh_fruit-=1
                        if (fresh_fruit ==0):
                            return minutes +1  
            minutes+=1
        return -1
