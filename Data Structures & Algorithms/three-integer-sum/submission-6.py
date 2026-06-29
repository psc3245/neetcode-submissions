class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        seen = set()

        if (len(nums) == 3):
            if (nums[0] + nums[1] + nums[2] == 0): 
                return [nums] 
            else:
                return []

        for i in range(len(nums) - 2):
            target = nums[i]
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                combo = -1 * (nums[l] + nums[r])
                if (target == combo):
                    seen.add((target, nums[l], nums[r]))
                    l += 1
                    r -= 1
                if (target > combo):
                    r -= 1
                if (target < combo):
                    l += 1
                    
        return [list(t) for t in seen]