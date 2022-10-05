class Solution:
    def moveZeroes(self, nums):
        """
        TWO POINTERS
        RUNTIME: 1292 ms (11.73%)
        MEMORY: 15.5 MB (64.50%)
        """

        left_ptr = 0
        right_ptr = len(nums) - 1

        while left_ptr != right_ptr:

            if nums[left_ptr] == 0:
                del nums[left_ptr]
                nums[:] = nums + [0]
                right_ptr -= 1
            else:
                left_ptr += 1

            if nums[right_ptr] == 0:
                del nums[right_ptr]
                nums[:] = nums + [0]
            else:
                right_ptr -= 1


sol = Solution()
sol.moveZeroes([-58, -33, 0, 0, 0, 0, 0, -76, 42, 48, 0, 95, -91, 60, 0, -34, 0, -88])
