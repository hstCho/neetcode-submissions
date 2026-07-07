import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        for item in nums:
            if len(self.min_heap) < k:
                heapq.heappush(self.min_heap, item)
            else:
                heapq.heappushpop(self.min_heap, item)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]
        
