class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        letters = []
        for i in range(26):
            letters.append(0)
        for st in strs:
            for c in st:
                letters[ord(c.upper()) - 65] += 1
            key = tuple(letters)
            if key in anagrams.keys():
                anagrams[key].append(st)
            else:
                anagrams[key] = [st]
            for i in range(26):
                letters[i] = 0
        return list(anagrams.values())