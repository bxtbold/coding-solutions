class Solution:
    def sortedSquares(self, nums):
        """
        TWO POINTERS
        RUNTIME: 567 ms (19.72%)
        MEMORY: 16.4 MB (18.6%)
        """

        left_ptr = 0
        right_ptr = len(nums) - 1
        new_array = []

        for i in range(len(nums)):

            start = nums[left_ptr] * nums[left_ptr]
            end = nums[right_ptr] * nums[right_ptr]

            if end >= start:
                new_array.append(end)
                right_ptr -= 1
            else:
                new_array.append(start)
                left_ptr += 1

        return new_array[::-1]

sol = Solution()
sol.sortedSquares([-7,-3,2,3,11])
