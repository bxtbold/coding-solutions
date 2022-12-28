import math
class Solution:
    def numSquares(self, n: int) -> int:
        """
        RUNTIME: 289 ms (72.28%)
        MEMORY: 14.9 MB (29.87%)
        """
        # initialize
        squares = { i**2 for i in range(1, int(math.sqrt(n)) + 1)}
        queue, visited = [n], {n : 1}
        steps = 0
        # bfs
        while queue:
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur in squares:
                    return steps + 1
                for each in squares:
                    if cur - each not in visited and cur > each:
                        visited[cur - each] = 1
                        queue.append(cur - each)
            steps += 1
        return -1
