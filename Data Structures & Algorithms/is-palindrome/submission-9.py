class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        palindrome = ""
        
        for i in range(length):
            if s[i].isalnum():
                palindrome += s[i].lower()
        return palindrome == palindrome[::-1]