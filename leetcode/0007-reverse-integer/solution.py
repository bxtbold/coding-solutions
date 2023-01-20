class Solution:
    def reverse(self, x: int) -> int:
        """
        RUNTIME: 28 ms (95.40%)
        MEMORY: 13.8MB (60.15%)
        """
        is_negative = True if x < 0 else False
        if is_negative: x *= -1
        queue = []
        while x > 0:
            tmp = x % 10
            queue.append(tmp)
            x = x // 10
        i = len(queue) - 1
        answer = 0
        while len(queue) > 0:
            tmp = queue.pop(0)
            answer += tmp * 10 ** i
            i -= 1
        if - 2 ** 31 < answer < 2**31 -1:
            return -answer if is_negative else answer
        return 0
