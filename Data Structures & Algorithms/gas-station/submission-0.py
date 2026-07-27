class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n * 2:
            gas_left = 0
            for j in range(i, i + len(gas)):
                gas_left += gas[j % n] - cost[j % n]
                if gas_left < 0:
                    i = j
                    break
            if gas_left >= 0:
                return i % n
            i += 1
                
        return -1