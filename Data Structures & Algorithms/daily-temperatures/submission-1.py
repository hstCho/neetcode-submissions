class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                pop_day = stack.pop()
                res[pop_day[1]] = i - pop_day[1]
            stack.append((temperatures[i], i))
        return res