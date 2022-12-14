class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        RUNTIME: 105 ms (95.8%)
        MEMORY: 18.5 MB (98.91%)
        """
        mp = {}
        for i in nums:
            if i not in mp:
                mp[i] = 0
            mp[i] += 1
        repetance = {}
        for i in mp:
            if mp[i] not in repetance:
                repetance[mp[i]] = []
            repetance[mp[i]].append(i)
        result = []
        for i in sorted(repetance)[::-1]:
            result += repetance[i]
            if len(result) >= k:
                break
        return result
