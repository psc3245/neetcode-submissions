class Solution:
    def findMin(self, nums: List[int]) -> int:
        # base case
        if len(nums) == 1: return nums[-1]

        # binary search, pointers at ends
        l = 0
        r = len(nums) - 1
        while (l < r):
            # check if we are at the lowest two numbers
            if (r - l < 2):
                if (nums[r] < nums[l]):
                    return nums[r]
                else:
                    return nums[l]

            # determine if mid -> r is sorted
            mid = l + int((r - l) / 2)
            if (nums[r] > nums[mid]):
                # if mid -> r is strictly increasing, the min cannot be in there, so r = mid
                r = mid
            if (nums[r] < nums[mid]):
                # if mid -> r is not strictly increasing, the min is in there so we look between there
                l = mid + 1

        return nums[l]