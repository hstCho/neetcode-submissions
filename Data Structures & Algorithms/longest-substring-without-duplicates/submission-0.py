class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            length = 1
            seen = set()
            seen.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in seen:
                    length += 1
                    seen.add(s[j])
                else:
                    break
            max_length = max(max_length, length)
        return max_length