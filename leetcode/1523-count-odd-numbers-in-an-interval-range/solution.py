class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high - low == 1: return 1
        if low % 2 == 1 or high % 2 == 1:
            return (high - low) // 2 + 1
        return (high - low) // 2


sol = Solution()
print(sol.countOdds(13, 18))
