class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        RUNTIME: 25 ms (99.15%)
        MEMORY: 14 MB (12.16%)
        """
        hashmap = {}
        for i in stones:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        total = 0
        for i in jewels:
            if i in hashmap:
                total += hashmap[i]
        return total
