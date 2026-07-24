class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, end = 0, 1
        best = end - start
        while end < len(fruits):
            types = set(fruits[start:end])
            toadd = fruits[end]
            if toadd in types:
                end += 1
            if toadd not in types:
                if len(types) <= 1:
                    end += 1
                else:
                    start += 1
            best = max(best, end - start)
            
        return best