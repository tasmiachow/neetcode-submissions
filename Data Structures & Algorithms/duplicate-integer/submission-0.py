class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequency_map={}
        for x in nums:
            if x in frequency_map:
                frequency_map[x]+=1
            else:
                frequency_map[x] =1
        for val in frequency_map.values():
            if val>1: 
                return True
        return False