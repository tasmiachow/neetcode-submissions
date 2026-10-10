class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = sorted(nums, reverse=True)
        self.k = k
        

    def add(self, val: int) -> int:
        self.heap.append(val)
        self.heap.sort(reverse=True)
        return self.heap[self.k-1]

        
