from collections import deque
class Solution:
    def updateMatrix(self, matrix):
        """
        RUNTIME: 700 ms (77.90%)
        MEMORY: 17.4 MB (43.75%)
        """
        row, col = len(matrix), len(matrix[0])
        visited, queue = set(), deque()
        count = 0
        # add all cell that is 0 to queue
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    queue.append((i, j))

        # BFS
        while queue:
            # take out the 1st element coordinate in the queue
            for _ in range(len(queue)):
                current = queue.popleft()
                # find the neighbor
                for dirs in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = current[0] + dirs[0], current[1] + dirs[1]
                    if (x, y) in visited or \
                        x < 0 or x >= row or \
                        y < 0 or y >= col:
                        continue
                    queue.append((x, y))
                    visited.add((x, y))
                # update cell
                if matrix[current[0]][current[1]] != 0:
                    matrix[current[0]][current[1]] = matrix[current[0]][current[1]] + count - 1
            count += 1
        return matrix


mat = [[0,0,0],
       [0,1,0],
       [1,1,1]]
sol = Solution()
sol.updateMatrix(mat)
