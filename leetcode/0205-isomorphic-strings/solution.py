class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        RUNTIME: 54 ms (80.12%)
        MEMORY: 14.2 MB (89.54%)
        """
        if len(s) != len(t): return False
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                if t[i] in hashmap.values():
                    return False
                hashmap[s[i]] = t[i]
            else:
                if hashmap[s[i]] != t[i]:
                    return False
        return True
