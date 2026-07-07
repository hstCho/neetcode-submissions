class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(": ")", "{": "}", "[": "]"}
        opening_bracket = {"(", "{", "["}
        stack = []

        for c in s:
            if c in opening_bracket:
                stack.append(c)
            else:
                if stack == [] or bracket_dict[stack.pop()] != c:
                    return False
        
        if stack != []:
            return False

        return True
