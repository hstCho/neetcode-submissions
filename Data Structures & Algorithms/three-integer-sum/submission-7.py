class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4,-1,-1,0,1,2] -> [4,1,1,0,-1,-2]
        nums.sort()

        # Create a new list of target for twoSum
        target_list = []
        for i in range(len(nums)):
            target_list.append(0 - nums[i])

        res = set()
        for i in range(len(target_list)):
            two_sum_list = self.twoSum(nums[i+1:], target_list[i])
            for two_sum in two_sum_list:
                candidate = [nums[i]] + two_sum
                res.add(tuple(candidate))
        return [list(i) for i in res]
        

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        i, j = 0, len(nums) - 1

        while i < j:
            if nums[i] + nums[j] == target:
                 res.append([nums[i], nums[j]])
            if nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        
        return res