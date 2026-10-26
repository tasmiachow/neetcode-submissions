from collections import deque
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #up, down, left, right
        directions = [(-1, 0), (1,0), (0,-1), (0, 1)]
        rows, cols = len(matrix), len(matrix[0])
        queue = deque([])
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] ==0: 
                    queue.append((r,c))
                    visit.add((r,c))
                    
        
        while queue: 

            pos = queue.popleft()
            for (dr,dc) in directions: 
                pos_r = pos[0] + dr 
                pos_c = pos[1] + dc 

                while 0<=pos_r <rows and 0<=pos_c<cols and (pos_r, pos_c) not in visit: 
                    matrix[pos_r][pos_c] = 0 
                    pos_r +=dr 
                    pos_c +=dc
                
           
                    
        
                  
        


        