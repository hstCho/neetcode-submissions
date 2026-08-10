class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_elem = nums[0]
        if nums[0] <= nums[-1]:
            return min_elem

        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < min_elem:
                min_elem = nums[mid]
                j = mid
            else:
                i = mid + 1
        
        return min_elem
