class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0 for _ in range(len(nums) + 1)]
        total = 0
        for i in range(len(nums)):
            prefix[i] = total
            total += nums[i]
        prefix[-1] = total

        answers = 0
        for i in range(len(prefix)):
            for j in range(i):
                pre_sum = prefix[i] - prefix[j]
                if pre_sum % k == 0:
                    answers += 1
        return answers
        