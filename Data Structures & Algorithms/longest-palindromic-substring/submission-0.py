class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ''
        length = 0 
        for i in range(len(s)):
            l, r = i,i 

            #odd length
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l +1) > length: 
                    length = (r-l +1)
                    substring = s[l:r+1]
                l -=1
                r +=1
            
            #even legnth 

            l, r = i, i+1

            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l +1) > length: 
                    length = (r-l +1)
                    substring = s[l:r+1]
                l -=1
                r +=1
        return substring 