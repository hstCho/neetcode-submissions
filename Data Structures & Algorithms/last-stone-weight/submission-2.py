class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = stones
        
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > 1:
            stone1 = heapq.heappop_max(maxHeap)
            stone2 = heapq.heappop_max(maxHeap)

            if stone1 > stone2:
                stone1 = stone1 - stone2
                heapq.heappush_max(maxHeap, stone1)
        
        return maxHeap[0] if len(maxHeap) == 1 else 0