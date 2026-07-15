class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        max_left, max_right = height[l], height[r]

        area = 0
        while l <= r:
            if max_left < max_right:
                if max_left - height[l] > 0:
                    area += max_left - height[l]  
                max_left = max(max_left, height[l])
                l += 1
            else:
                if max_right - height[r] > 0:
                    area += max_right - height[r] 
                max_right = max(max_right, height[r])
                r -= 1
        
        return area

