class Solution:
    def romanToInt(self, s: str) -> int:
        """
        RUNTIME: 50 ms (74.62%)
        MEMORY: 13.8MB (70.93%)
        """
        convert = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
        answer = 0
        for i in s:
            answer += convert[i]
        return answer
