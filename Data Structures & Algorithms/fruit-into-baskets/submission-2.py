class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, end = 0, 0
        counts = {}
        best = 0

        while end < len(fruits):
            counts[fruits[end]] = counts.get(fruits[end], 0) + 1

            while len(counts) > 2:
                counts[fruits[start]] -= 1
                if counts[fruits[start]] == 0:
                    del counts[fruits[start]]
                start += 1

            best = max(best, end - start + 1)
            end += 1

        return best