class Solution1:
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

class Solution2:
    def reverse(self, x: int) -> int:
        """
        RUNTIME: 37 ms (65.43%)
        MEMORY: 13.8MB (96.75%)
        """
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        is_negative = True if x < 0 else False
        if is_negative: x *= -1
        answer = 0
        while x != 0:
            tmp = x % 10
            x = x // 10
            if answer > INT_MAX / 10 or (answer == INT_MAX / 10 and tmp > 7):
                return 0
            if answer < INT_MIN / 10 or (answer == INT_MIN / 10 and tmp < -8):
                return 0
            answer = answer * 10 + tmp
        return -answer if is_negative else answer
