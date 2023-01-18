class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        RUNTIME: 36 ms (99.96%)
        MEMORY: 14MB (49.69%)
        """
        if numRows == 1: return s
        each = ['' for _ in range(numRows)]
        n = (numRows - 1) * 2
        for i in range(len(s)):
            index = i % n
            if index >= numRows:
                each[2 * (numRows - 1) - index] += s[i]
            else:
                each[index] += s[i]
        return ''.join(each)
