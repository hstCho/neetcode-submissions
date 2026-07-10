class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            letter_list = [0] * 26
            for char in word:
                letter_list[ord(char) - ord('a')] += 1
            ans[tuple(letter_list)].append(word)
        
        return list(ans.values())
