class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_count = 0
        i = 0
        longest = 0

        for j in range(len(s)):
            counts[s[j]] = counts.get(s[j], 0) + 1
            max_count = max(counts.values())
            
            while (j-i+1) - max_count > k:
                counts[s[i]] -= 1
                i += 1
                
            longest = max(longest, j-i+1)
        return longest