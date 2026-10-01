class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        

        def dfs(text1, text2, s1, s2, cache):
            if s1>= len(text1) or s2 >= len(text2):
                return 0 
            if (s1,s2) in cache:
                return cache[(s1,s2)]
            
            if text1[s1] == text2[s2]:
                cache[(s1,s2)] = 1 + dfs(text1, text2, s1+1, s2+1, cache)
            else:
                cache[(s1,s2)] = max(dfs(text1, text2, s1+1, s2, cache), dfs(text1, text2, s1, s2+1, cache))
            return cache[(s1,s2)] 
        return dfs(text1, text2, 0,0, cache)