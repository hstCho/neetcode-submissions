class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while (n not in seen):
            seen.add(n)

            if n == 1:
                return True

            new_num = 0

            while n >= 10:
                new_num += (n % 10) ** 2
                n = n // 10
            
            new_num += n ** 2
            n = new_num

        return False