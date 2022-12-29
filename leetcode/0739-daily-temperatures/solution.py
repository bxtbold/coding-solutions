class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        """
        RUNTIME: 1291 ms (99.87%)
        MEMORY: 27.8 MB (95.4%)
        """
        stack = []
        for i in range(len(temp)):
            while stack and temp[i] > temp[stack[-1]]:
                j = stack.pop()
                temp[j] = i - j
            stack.append(i)
        for i in stack:
            temp[i] = 0
        return temp
