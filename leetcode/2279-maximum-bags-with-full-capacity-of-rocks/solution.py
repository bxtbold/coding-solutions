class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        """
        RUNTIME: 929 ms (96.5%)
        MEMORY: 22.1 MB (87.83%)
        """
        for i in range(len(capacity)):
            capacity[i] -= rocks[i]
        capacity.sort(reverse=False)
        cnt = 0
        result = capacity.count(0)
        capacity[:] = capacity[result:]
        for i in capacity:
            cnt += i
            if cnt <= additionalRocks:
                result += 1
            else:
                break
        return result
