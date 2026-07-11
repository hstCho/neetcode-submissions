class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            length = len(word)
            encoded_word = str(length) + '#' + word
            encoded_string += encoded_word
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length
            decoded_list.append(s[i:j])
            i = j

        return decoded_list

        