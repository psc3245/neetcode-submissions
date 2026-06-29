class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {1:1, 2: 2}
        return self.climbStairsRecursive(n, dic)
    def climbStairsRecursive(self, n, dic):
        if (n in dic.keys()):
            return dic[n]
        else:
            dic[n] = self.climbStairsRecursive(n-1, dic) + self.climbStairsRecursive(n-2, dic)
            return dic[n]