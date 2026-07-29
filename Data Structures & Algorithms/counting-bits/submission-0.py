class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for x in range(n+1):
            tmp  = 0 
            while x > 0: 
                if x & 1 ==1:
                    tmp+=1
                x = x >>1
            res.append(tmp)
        return res