class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 1
        best = 1
        freq = {}
        for r in range(len(s)):
            if s[r] in freq.keys():
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            while (r - l) + 1 - max(freq.values()) > k:
                # def alr in freq, we alr saw it
                freq[s[l]] -= 1
                l += 1
            r += 1
            best = max(r - l, best)
        return best
            