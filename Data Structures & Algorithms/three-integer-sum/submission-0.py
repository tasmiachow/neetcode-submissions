class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ## l r pointer 
        triplets = set()
        nums.sort()
        for i in range(len(nums)):
            l = i + 1 
            r = len(nums) -1 
            while l < r: 
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == 0: 
                    res = (nums[i], nums[l], nums[r])
                    triplets.add(res)
                    l += 1
                    r -= 1
                elif currSum > 0: 
                    r-=1 
                else: 
                    l+=1
        return [list(t) for t in triplets]