class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        res = []
        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in words: 
                words[sorted_word] = []
                words[sorted_word].append(word)
            else: 
                words[sorted_word].append(word)
        
        for key in words.keys():
            new_list = []
            new_list.extend(words[key])
            res.append(new_list)
        return res