class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) < 2): return len(s)
        longest = 0
        chars = set()
        l, r = 0, 0
        while r < len(s):
            if (s[r] in chars):
                while (s[r] in chars):
                    chars.remove(s[l])
                    l += 1
                chars.add(s[r])
                r += 1
            else:
                chars.add(s[r])
                r += 1 
            longest = max(longest, r - l)
        longest = max(longest , r-l)
        return longest