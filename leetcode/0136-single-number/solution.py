class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        RUNTIME: 394 ms (17.4%)
        MEMORY: 16.5 MB (93.88%)
        """
        if len(nums) == 1: return nums[0]
        hashset = {}
        for num in nums:
            if num not in hashset:
                hashset[num] = 1
            else:
                hashset[num] += 1
        for i in hashset:
            if hashset[i] == 1:
                return i
