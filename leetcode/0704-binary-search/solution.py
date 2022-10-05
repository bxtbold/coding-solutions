class Solution:
    def search(self, nums, target: int) -> int:
        # init
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

        return -1

solution = Solution()
print(solution.search([-1,0,3,5,9,12], 13))
