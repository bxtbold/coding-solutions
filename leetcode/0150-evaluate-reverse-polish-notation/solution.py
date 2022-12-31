class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        RUNTIME: 61 ms (96.61%)
        MEMORY: 14.3 MB (96.21%)
        """
        stack = []
        for cur in tokens:
            if cur in {'+', '-', '*', '/'}:
                f, s = stack.pop(), stack.pop()
                if cur == '+': cur = s + f
                elif cur == '-': cur = s - f
                elif cur == '*': cur = s * f
                elif cur == '/': cur = s / f
            stack.append(int(cur))
        return stack.pop()