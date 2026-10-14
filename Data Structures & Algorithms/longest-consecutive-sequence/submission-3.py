class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0 
        
        consecutive = set()
        max_count = 0

        for num in nums: 
            consecutive.add(num)

        for num in nums: 
            if num -1 not in consecutive: 
                curr = num 
                i = 1
                while (curr+1) in consecutive: 
                    curr += 1 
                    i+=1
                max_count = max(max_count, i)
        return max_count