class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for n in nums:
            if n in s and n-1 not in s:
                case = [n]
                s.remove(n)
                while case[-1]+1 in s:
                    case.append(case[-1] + 1)
                    s.remove(case[-1])
                best = max(len(case), best)

        return best   
                