import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
    
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        
        mid = math.floor((l+r)/2)

        print(mid)

        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            return self.binary_search(l, mid - 1, nums, target)
        
        if nums[mid] < target:
            return self.binary_search(mid + 1, r, nums, target)
