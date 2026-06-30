class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # base cases
        if len(s) < 2: 
            return len(s)
        if len(s) == 2:
            return 1 if s[0] == s[1] else 2

        max = 1
        l = 0
        r = 1

        chars = set()
        chars.add(s[l])

        while(l < r and r < len(s)):
            if s[r] not in chars:
                if r - l + 1 > max: 
                    max = r - l + 1
            else:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
            chars.add(s[r])
            r += 1
                
        return max
                