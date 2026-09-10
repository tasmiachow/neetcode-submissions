class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        def helper(i, strs, m, n): 
            if i >= len(strs): 
                return 0 
            if (i,m,n) in memo: 
                return memo[(i, m, n)]
            #skip item at i 
            skip=helper(i+1, strs, m, n)
            take = 0
            
            newM = m - strs[i].count('0')
            newN = n - strs[i].count('1')
            if newM >=0 and newN >= 0: 
                take = 1+ helper(i+1, strs, newM, newN)

            largest=max(skip, take)
            memo[(i, m, n)] = largest
            return largest
        return helper(0,strs, m,n)


        