class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        RUNTIME: 99 ms (96.5%)
        MEMORY: 17.1 MB (95.96%)
        """
        hashmap = {}
        for i in strs:
            tmp = ''.join(sorted(list(i)))
            if tmp not in hashmap:
                hashmap[tmp] = [i]
            else:
                hashmap[tmp].append(i)
        return list(hashmap.values())
