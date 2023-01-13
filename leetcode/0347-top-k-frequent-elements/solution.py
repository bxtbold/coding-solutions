class HashSolution:
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
        for i in sorted(repetance, reverse=True):
            result += repetance[i]
            if len(result) >= k:
                break
        return result


from collections import Counter
class OneLineSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        RUNTIME: 107 ms (83.11%)
        MEMORY: 18.6 MB (90.87%)
        """
        return [each[0] for each in Counter(nums).most_common(k)]


import heapq
from collections import Counter
class HeapSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        RUNTIME: 109 ms (79.68%)
        MEMORY: 18.6 MB (69.55%)
        """
        counter = Counter(nums)
        maxHeap = [[-freq, num] for num, freq in counter.items()]
        heapq.heapify(maxHeap)

        ans = []
        for i in range(k):
            _, num = heapq.heappop(maxHeap)
            ans.append(num)
        return ans
