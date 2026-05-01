class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]
        for x in s: 
            if x in "({[": 
                stack.append(x)
            elif stack:
                if(self.validMatch(stack.pop(), x)==False):
                    return False
            else:
                return False
        return not stack
                    

    

    def validMatch(self, opening, closing) ->bool: 
        if(opening=="(" and closing ==")"):
            return True 
        elif(opening=="[" and closing =="]"):
            return True 
        elif(opening =="{" and closing=="}"):
            return True 
        else:
            return False