class Solution:
    def intToRoman(self, num: int) -> str:
        """
        RUNTIME: 47 ms (88.61%)
        MEMORY: 13.9MB (75.58%)
        """
        s1 = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
        s2 = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
        s3 = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
        s4 = ('', 'M', 'MM', 'MMM')
        return s4[num // 1000] + s3[(num % 1000) // 100] + s2[(num % 100) // 10] + s1[num % 10]
