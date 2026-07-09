class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        ans_list = []
        
        for i in range(1, len(digits) + 1):
            ans += digits[-i] * 10 ** (i-1)
            
        ans += 1

        while ans > 0:
            ans_list.append(ans % 10)
            ans = ans // 10

        ans_list = ans_list[::-1]

        return ans_list