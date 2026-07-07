class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # <- For one edge case
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s) # In python, key cannot be list & appends string as a list in key
        return list(res.values()) # We just want to return the values (after making it list)
            