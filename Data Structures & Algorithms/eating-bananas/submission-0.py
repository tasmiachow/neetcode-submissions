class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            total_hours = 0
            for pile in piles:
                # Ceiling division: math.ceil(pile / speed)
                # or integer arithmetic: (pile + speed - 1) // speed
                total_hours += (pile + speed - 1) // speed
            
            return total_hours <= h
        
        low = 1
        high = max(piles)
        ans = high 
        while low<=high: 
            mid = low + (high-low) //2

            if can_finish(mid):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans
