class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            freq = [0 for i in range(26)]
            
            for c in s:
                index = ord(c.upper()) - 65
                freq[index] += 1

            key = tuple(freq)
            if key in groups.keys():
                groups[key].append(s)
            else:
                groups[key] = [s]
        
        return list(groups.values())