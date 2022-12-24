class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        RUNTIME: 128 ms (80%)
        MEMORY: 14.2 MB (18.48%)
        """
        hashmap = {}
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for i in s:
            if hashmap[i] == 1:
                return s.find(i)
        return -1
