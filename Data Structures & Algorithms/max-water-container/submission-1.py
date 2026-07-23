class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            water = min([height[l], height[r]]) * (r - l)
            best = max([water, best])
            if (height[l] > height[r]):
                r -= 1
            else:
                l += 1

        return best