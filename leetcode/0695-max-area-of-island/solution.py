class Solution:
    """
    DFS
    RUNTIME: 179 ms (71.64%)
    MEMORY: 16.9 MB (44.42%)
    """
    def maxAreaOfIsland(self, grid):
        self.visited = {}
        self.max_area = 0
        self.grid = grid

        self.row, self.column = len(grid), len(grid[0])

        for i in range(self.row):
            for j in range(self.column):
                if f'{i},{j}' in self.visited:
                    pass
                else:
                    # reset area
                    self.current_area = 0
                    if grid[i][j] == 1:
                        # dfs
                        self.dfs(i, j)
                        # check if current is more than prev max
                        self.max_area = max(self.max_area, self.current_area)
        return self.max_area

    def dfs(self, i, j):
        # finish dfs
        if f'{i},{j}' in self.visited: return
        if i < 0 or i > self.row - 1: return
        if j < 0 or j > self.column - 1: return
        if self.grid[i][j] == 0: return
        # add visited
        self.visited[f'{i},{j}'] = 1
        # increment area by one
        self.current_area += 1
        # radiant in four directions
        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)


sol = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(sol.maxAreaOfIsland(grid))
