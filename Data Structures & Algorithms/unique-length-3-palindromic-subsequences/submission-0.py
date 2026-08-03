class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dic = dict()

        for i in range(len(s)):
            c = s[i]
            if c in dic.keys():
                dic[c].append(i)
            else:
                dic[c] = [i]
        ranges = [x for x in list(dic.values()) if len(x) > 1]

        count = 0
        for r in ranges:
            count += len(set(s[r[0] + 1: r[-1]]))

        return count