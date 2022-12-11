class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        RUNTIME: 214 ms (84.27%)
        MEMORY: 18.6 MB (18.79%)
        """
        s[:] = s[::-1]

sol = Solution()
sol.reverseString('abcdef')
