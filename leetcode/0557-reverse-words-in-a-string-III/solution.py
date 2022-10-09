class Solution:
    def reverseWords(self, s: str) -> str:
        """
        RUNTIME: 79 ms (34.62%)
        MEMORY: 14.7 MB (46.79%)
        """
        new_array = []

        for word in s.split():
            new_array.append(word[::-1])

        return ' '.join(new_array)

sol = Solution()
sol.reverseWords("Let's take LeetCode contest")
