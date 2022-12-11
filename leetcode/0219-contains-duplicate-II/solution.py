class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        RUNTIME: 685 ms (84.35%)
        MEMORY: 32 MB (13.4%)
        """
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = [i]
            else:
                hashmap[nums[i]].append(i)
            if len(hashmap[nums[i]]) > 1:
                if hashmap[nums[i]][1] - hashmap[nums[i]][0] <= k:
                    return True
                hashmap[nums[i]] = hashmap[nums[i]][1:]
        return False
