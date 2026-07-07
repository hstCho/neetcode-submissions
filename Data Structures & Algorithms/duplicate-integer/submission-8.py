class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        candidate = set()
        list_length = len(nums)
        for i in range (list_length):
            if nums[i] not in candidate:
                candidate.add(nums[i])
            else:
                return True
        return False
        