class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_total = 1
        suffix_total = 1
        prefix = [1 for i in range(len(nums))]
        suffix = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix_total
            prefix_total *= nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix_total
            suffix_total *= nums[i + 1]
        ret = []
        for i in range(len(nums)):
            ret.append(prefix[i] * suffix[i])
        return ret