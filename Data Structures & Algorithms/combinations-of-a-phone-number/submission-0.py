class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digit_map = {
            "1": [], 
            "2": ["a", "b", "c"], 
            "3": ["d", "e", "f"], 
            "4" : ["g", "h", "i"], 
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w","x", "y", "z"],
        }

        res = []
        currComb = []
        
        if digits: 
            self.helper(0, currComb, res, digit_map, digits)
        return res

    def helper(self, i, currComb, res, digit_map, digits):
        if len(currComb) >= len(digits): 
            res_str = "".join(currComb)
            res.append(res_str)
            return 
            
        for c in digit_map[digits[i]]:
            currComb.append(c)
            self.helper(i+1, currComb, res, digit_map, digits)
            currComb.pop()
            
        


