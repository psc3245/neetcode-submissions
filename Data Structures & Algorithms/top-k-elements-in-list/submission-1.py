class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq.keys():
                freq[n] += 1
            else:
                freq[n] = 1
        heap = []
        for key in freq.keys():
            heap.append((-freq[key], key))
        
        heapq.heapify(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result