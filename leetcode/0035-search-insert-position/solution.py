class Solution:
    def searchInsert(self, nums, target: int) -> int:
        """
        RUNTIME: 109 ms (20.46%)
        MEMORY: 14.7MB (82.39%)
        """
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1

        return low

sol = Solution()
sol.searchInsert([1,3,5,6], 2)