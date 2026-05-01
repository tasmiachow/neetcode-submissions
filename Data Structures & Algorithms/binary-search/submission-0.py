class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0
        high= len(nums) -1 
        while(low<=high):
            mid = (high+low)//2
            if nums[mid]>target:
                high = high-1
            elif nums[mid]<target:
                low = low + 1
            elif nums[mid] == target:
                return mid
        return -1