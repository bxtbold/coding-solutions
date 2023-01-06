class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        """
        RUNTIME: 1027 ms (74.75%)
        MEMORY: 28.2 MB (82.79%)
        """
        hashmap = {}
        for i in tasks:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        if 1 in hashmap.values(): return -1
        answer = 0
        for i in hashmap:
            if hashmap[i] == 3 or hashmap[i] == 2:
                answer += 1
            elif hashmap[i] % 3 == 0:
                answer += hashmap[i] // 3
            else:
                answer += hashmap[i] // 3 + 1
        return answer
