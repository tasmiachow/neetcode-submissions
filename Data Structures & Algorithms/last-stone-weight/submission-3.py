import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if (len(stones)<=1):
            return len(stones)
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        print(max_heap)

        while(len(max_heap)>1):
            x = abs(heapq.heappop(max_heap))
            y = abs(heapq.heappop(max_heap))
            if(x>y):
                new_weight = x-y
                heapq.heappush(max_heap, -new_weight)
        
        max_heap.append(0)
        return abs(max_heap[0])