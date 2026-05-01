class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip_s = s.replace(" ", "")
        lower_s = strip_s.lower()
        normalize = ""
        for x in lower_s: 
            if x.isalnum(): 
                normalize+=x
        print(normalize)
        l = 0 
        r = len(normalize) -1 
        while(l<r): 
            if normalize[l] == normalize[r]:
                l+=1
                r-=1 
            else: 
                return False 
        return True 
        