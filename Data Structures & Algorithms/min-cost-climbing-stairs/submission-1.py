class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step1, step2 = cost[0], cost[1]
        i = 2
        for i in range(i, len(cost)):
            tmp = step1
            step1 = step2
            step2 = cost[i] + min(tmp, step1)

        return min(step1, step2)