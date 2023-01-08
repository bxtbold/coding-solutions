class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        RUNTIME: 654 ms (97.45%)
        MEMORY: 19.3 MB (23.25%)
        """
        total, tank, start = 0, 0, 0
        for i in range(len(gas)):
            tank = tank + gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        if total + tank < 0:
            return -1
        return start
