class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        SLIDING WINDOW
        RUNTIME: 3656 ms (11.94%)
        MEMORY: 14 MB (30.94%)
        """
        window = len(s1)
        total = len(s2)
        sorted_ = sorted(s1)

        for i in range(0, total - window + 1):
            current = s2[i:i+window]
            print(set(current), set(s1))
            if set(current) == set(s1):
                if sorted(current) == sorted_:
                    return True

        return False

s1 = "abcdxabcde"
s2 = "abcdeabcdx"

sol = Solution()
sol.checkInclusion(s1, s2)
