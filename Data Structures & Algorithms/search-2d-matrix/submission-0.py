class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened_list = []
        for row in matrix: 
            for item in row:
                flattened_list.append(item)
        
        low = 0
        high = len(flattened_list) -1 

        while(low<=high):
            mid = (low + high)//2
            if flattened_list[mid] == target:
                return True 
            elif(flattened_list[mid]>target):
                high = mid -1 
            else: 
                low = mid +1 
        return False 