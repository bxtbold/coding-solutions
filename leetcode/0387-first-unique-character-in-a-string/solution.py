class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        RUNTIME: 423 ms (25.53%)
        MEMORY: 14.1 MB (58.93%)
        """
        hashmap = {}
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1
