class Solution:
    def rotate(self, nums, k):
        """
        RUNTIME: 210 ms (98.70%)
        MEMORY: 25.4 ms (75.28%)
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

sol = Solution()
sol.rotate([-1,-100,3,99], 2)
