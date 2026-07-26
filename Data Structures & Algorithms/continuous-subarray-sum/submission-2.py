class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        l, r = 0, 1
        total = 0
        prefix_mod = [0]
        for i in range(1, len(nums) + 1):
            total += nums[i - 1]
            prefix_mod.append(total % k)
        s = {}
        for i in range(len(prefix_mod)):
            if prefix_mod[i] in s.keys():
                if i - s[prefix_mod[i]] > 1:
                    return True
            else:
                s[prefix_mod[i]] = i 
        return False