class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        exclude_front, total_front = [1] * len(nums), 1
        for i in range(len(nums)):
            exclude_front[i] = total_front
            total_front = total_front * nums[i]
        
        exclude_back, total_back = [1] * len(nums), 1
        for i in range(len(nums)-1, -1, -1):
            exclude_back[i] = total_back
            total_back = total_back * nums[i]

        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = exclude_front[i] * exclude_back[i]
        
        return res


# X123 [0]: 1 []: 1
# 0X23 [0,1]: 2 [0]: 1
# 01X3 [0,1,2]: 8 [0,1]: 2
# 012X [0,1,2,3]: 48 [0,1,2]: 8

# 012X [3]: 6 []: 1
# 01X3 [3,2]: 24 [3]: 6
# 0X23 [3,2,1]: 48 [3,2]: 24
# X123 [3,2,1,0]: 48, [3,2,1] = 48

