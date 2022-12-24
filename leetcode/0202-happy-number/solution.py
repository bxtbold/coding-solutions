class Solution:
    def isHappy(self, n: int) -> bool:
        """
        RUNTIME: 34 ms (93.99%)
        MEMORY: 13.8 MB (62.35%)
        """
        if n == 1: return True
        hashset = {}
        while n != 1:
            if n < 10:
                n = n * n
            else:
                sum = 0
                while True:
                    sum += (n % 10) * (n % 10)
                    if n // 10 == 0:
                        break
                    n = n // 10
                n = sum
                if n == 1:
                    return True
            if n not in hashset:
                hashset[n] = 1
            else:
                return False

a = Solution()
print(a.isHappy(19))
