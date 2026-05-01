class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #use a set?
        
        if(len(s)<=0):
            return 0 
        L = 0 
        longest = 1 
        currSet = set()
        for R in range(len(s)):
            while s[R] in currSet:
                currSet.remove(s[L])
                L+=1
            currSet.add(s[R])
            longest = max(R - L + 1, longest)


        return longest