class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        exclude_front, total_front = [], 1
        for i in range(length):
            exclude_front.append(total_front)
            total_front = total_front * nums[i]
        
        exclude_back, total_back = [], 1
        for i in range(length-1, -1, -1):
            exclude_back.append(total_back)
            total_back = total_back * nums[i]

        res = []
        for i in range(length):
            res.append(exclude_front[i] * exclude_back[length - 1 - i])
        
        return res
