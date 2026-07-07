class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet_hash = {chr(i): 0 for i in range(97, 123)}
        for i in range(len(s)):
            alphabet_hash[s[i]] = alphabet_hash.get(s[i], 0) + 1
        for i in range(len(t)):
            alphabet_hash[t[i]] = alphabet_hash.get(t[i], 0) - 1
        for i in range(97, 123):
            if alphabet_hash.get(chr(i), 0) != 0:
                return False
        return True