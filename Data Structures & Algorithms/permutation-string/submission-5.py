class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = {}
        for c in s1:
            perm[c] = perm.get(c, 0) + 1

        i = 0
        for j in range(len(s2)):
            print(i,s2[i],j,s2[j],perm)
            if s2[j] in perm:
                perm[s2[j]] -= 1
                
                while perm[s2[j]] < 0:
                    perm[s2[i]] = perm.get(s2[i], 0) + 1
                    i += 1

                if sum(perm.values()) == 0:
                    return True
                    
            else:
                while s2[i] in perm:
                    perm[s2[i]] += 1 
                    i += 1
                i += 1
        return False