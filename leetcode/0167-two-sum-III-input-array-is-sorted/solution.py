class Solution:
    def twoSum(self, numbers, target: int):
        """
        TWO POINTERS
        RUNTIME: 164 ms (78.30%)
        MEMORY: 14.9 MB (88.81%)
        """

        left, right = 0, len(numbers) - 1

        while left != right:
            sum_ = numbers[left] + numbers[right]

            if sum_ > target:
                right -= 1
            elif sum_ < target:
                left += 1
            else:
                return [left+1, right+1]


sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
