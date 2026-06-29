class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = []
        for i in range(26):
            letters.append(0)
        for c in s:
            letters[ord(c)-ord('a')] += 1
        for c in t:
            letters[ord(c)-ord('a')] -= 1
        for n in letters:
            if n != 0: return False

        return True