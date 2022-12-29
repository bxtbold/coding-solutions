class Solution:
    def isValid(self, s: str) -> bool:
        """
        RUNTIME: 26 ms (97.89%)
        MEMORY: 13.8 MB (98.51%)
        """
        if len(s) % 2 == 1: return False
        pairs = {'(':')', '{':'}', '[':']' }
        stack = []
        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack) == 0 or pairs[stack.pop()] != char: return False
        return len(stack) == 0
