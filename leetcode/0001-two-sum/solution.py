class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        RUNTIME: 69 ms (88.23%)
        MEMORY: 15.9 MB (9.51%)
        """
        hashmap = {}
        for i, val in enumerate(nums):
            if val not in hashmap.keys():
                hashmap[val] = [i]
            else:
                hashmap[val].append(i)
            find = target - val
            if find in hashmap:
                if val == find and len(hashmap[find]) > 1:
                    return [hashmap[val][0], hashmap[val][1]]
                elif val != find:
                    return [hashmap[val][0], hashmap[find][0]]
