class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums
        l, r = 0, k
        heap = []
        maxes = []
        for i in range(0, r):
            heap.append((-nums[i], i))
        heapq.heapify(heap)
        maxes.append(-heap[0][0])

        while r < len(nums):
            heapq.heappush(heap, (-nums[r], r))
            l += 1
            r += 1
            while True:
                value, index = heap[0]
                if index >= l and index <= r:
                    maxes.append(-value)
                    break
                else:
                    heapq.heappop(heap)


        return maxes
