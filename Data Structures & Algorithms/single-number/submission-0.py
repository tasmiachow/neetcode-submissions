class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frequency_map = {}

        for i in range(len(nums)):
            if nums[i] not in frequency_map:
                frequency_map[nums[i]] =1
            else:
                frequency_map[nums[i]] +=1
        
        for x in frequency_map:
            if frequency_map[x]==1:
                return int(x)