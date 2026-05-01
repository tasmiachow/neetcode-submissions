class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ##either append lengths that fit the >= target condition and 
        #then check the len(possibleSub) if empty return 0 
        
        subArray = []
        L = 0 
        currSum = 0 
        for R in range(len(nums)):
            currSum += nums[R]
            
            while currSum >= target: 
                subArray.append(R-L + 1)
                currSum -=nums[L]
                L+=1 
        if(len(subArray)==0):
            return 0
        else:
            return min(subArray)