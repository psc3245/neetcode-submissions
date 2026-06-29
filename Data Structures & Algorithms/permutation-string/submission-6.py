class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)): return False

        t1 = [0 for i in range(26)]
        t2 = [0 for i in range(26)]

        for s in s1:
            t1[self.ordval(s)] += 1
        for i in range(0, len(s1)):
            t2[self.ordval(s2[i])] += 1
        
        for i in range(len(s1), len(s2)):
            if (t1 == t2):
                return True
            else:
                t2[self.ordval(s2[i - len(s1)])] -= 1
                t2[self.ordval(s2[i])] += 1
        return t1 == t2

    def ordval(self, s: str) -> int:
        return ord(s.lower()) - 97
