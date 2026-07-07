class Solution:
    def isPalindrome(self, s: str) -> bool:  
        filtered_s = ''.join([char.lower() for char in s if char.isalnum()])
        length = len(filtered_s)

        for i in range (length // 2):
            if (filtered_s[i] != filtered_s[length - 1 - i]):
                return False

        return True
