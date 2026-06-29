class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        while l < r:
            if (numbers[r] + numbers[l] == target):
                break
            if (numbers[r] + numbers[l] < target):
                l += 1
            if (numbers[r] + numbers[l] > target):
                r -= 1

        return [l + 1, r + 1]