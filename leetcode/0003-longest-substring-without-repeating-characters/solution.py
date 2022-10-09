class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        SLIDING WINDOW
        RUNTIME: 83 ms (81.16%)
        MEMORY: 13 MB (49.67%)
        """

        max_ = 0
        i = len(s)

        while i > 0:
            for k in range(len(s)-i+1):
                current = s[k:k+i]
                if len(current) == len(set(current)):
                    max_ = max(max_, i)
                    break
            if i < max_:
                break
            i -= 1

        return max_

sol = Solution()
sol.lengthOfLongestSubstring('abcabcbb')
