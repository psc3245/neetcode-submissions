class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = [0 for _ in range(len(nums) + 1)]
        total = 0
        for i in range(len(nums)):
            prefix[i] = total
            total += nums[i]
        prefix[-1] = total

        dic = defaultdict(int)
        count = 0
        for i in range(len(prefix)):
            count += dic[prefix[i] % k]
            dic[prefix[i] % k] += 1
        return count
        