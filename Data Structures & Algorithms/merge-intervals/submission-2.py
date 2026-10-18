class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        


        for x,y in intervals:
            prev_x = res[-1][0]
            prev_y = res[-1][1]
           

            if x <= prev_x:
                res[-1][0] = min(prev_x, x)
                res[-1][1] = max(prev_y, y)
               
                continue 
            elif x <= prev_y:
                res[-1][0] = min(prev_x, x)
                res[-1][1] = max(prev_y, y)
                
                continue
            res.append([x,y])
           
        return res