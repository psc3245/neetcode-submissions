class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        most = piles[0]
        for p in piles:
            most = max(p, most)
        return self.eatingSpeedSearch(piles, h, 1, most)

    def eatingSpeedSearch(self, piles, h, l, r):
        if l == r:
            return l

        mid = (r - l) // 2 + l
        hours = 0
        for p in piles:
            # wierd integer divison rounded up formula
            hours += -(p // -mid)
        if hours <= h:
            return self.eatingSpeedSearch(piles, h, l, mid)
        else:
            return self.eatingSpeedSearch(piles, h, mid + 1, r)
        