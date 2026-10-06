class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        cache = {}
        def dfs(i, j, cache):
            if j == len(t):
                return 1             
            if i >= len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            
            if s[i] == t[j]:
                cache[(i, j)] = dfs(i+1, j+1, cache) + dfs(i+1,j, cache)
            else:
                cache[(i, j)] = dfs(i+1, j, cache)
            return cache[(i, j)]
        return dfs(0,0, cache) 
        
           