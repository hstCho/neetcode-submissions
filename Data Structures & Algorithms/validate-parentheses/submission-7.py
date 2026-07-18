class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        res = []
        for c in s:
            # Edge-case: starting with closing bracket returns false
            if c not in brackets:
                if res == [] or brackets[res[-1]] != c:
                    return False
                else:
                    res.pop()
            else:
                res.append(c)
        if res == []:
            return True
        else:
            return False