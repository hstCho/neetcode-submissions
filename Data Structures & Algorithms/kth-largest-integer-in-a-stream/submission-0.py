import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.length = len(nums)


    def track_top_k_elements(self, k: int, nums: List[int]) -> List[int]:
        min_heap = []
        
        for item in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, item)
            else:
                heapq.heappushpop(min_heap, item)
                
        return min_heap

    def add(self, val: int) -> int:
        self.nums.append(val)

        new_min_heap = self.track_top_k_elements(self.k, self.nums)

        return new_min_heap[0]

        
        
