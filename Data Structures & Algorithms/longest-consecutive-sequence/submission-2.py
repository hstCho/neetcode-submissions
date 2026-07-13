class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count, max_count = 1, 1

        if not nums:
            return 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
                max_count = max(max_count, count)
            elif nums[i] - nums[i-1] > 1:
                count = 1
            else:
                continue
        
        print(nums)
        return max_count
