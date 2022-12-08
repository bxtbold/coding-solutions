class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        RUNTIME: 594 ms (75.2%)
        MEMORY: 26 MB (28.51%)
        """
        if len(nums) == 0: return False
        hashset = {}
        for i in nums:
            if i not in hashset:
                hashset[i] = 1
            else:
                return True
        return False
