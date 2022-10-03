# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        RUNTIME: 37 ms (81.33%)
        MEMORY: 13.9 MB (62.14%)
        """

        if n == 1: return 1

        low, high = 0, n - 1

        while low <= high:
            mid = (high + low) // 2

            if not isBadVersion(mid):
                low = mid + 1

            else:
                high = mid - 1

        if low > high: return low
        return mid

sol = Solution()
sol.firstBadVersion(5)