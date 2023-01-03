class BFSSolution:
    def numIslands(self, grid) -> int:
        """
        RUNTIME: 464 ms (66.12%)
        MEMORY: 23.3 MB (13.88%)
        """
        if len(grid) == 0: return 0
        # initialize
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.visited = {}
        self.queue = []
        island = 0
        # bfs
        for i in range(self.m):
            for j in range(self.n):
                # do bfs when not visited and value is 1
                if self.grid[i][j] == '1' and f'{i},{j}' not in self.visited:
                    self.queue.append([i, j])
                    self.visited[f'{i},{j}'] = 1
                    self.bfs()
                    island += 1
        return island

    def bfs(self):
        while len(self.queue) != 0:
            # dequeue
            cur = self.queue.pop(0)
            for dirs in [[0,1], [1,0], [0,-1], [-1,0]]:
                x, y = cur[0] + dirs[0], cur[1] + dirs[1]
                # skip when out of bound or visited or value is 0
                if x < 0 or x >= self.m or y < 0 or y >= self.n or \
                  f'{x},{y}' in self.visited or self.grid[x][y] == '0':
                    continue
                # add visited
                self.visited[f'{x},{y}'] = 1
                # enqueue
                self.queue.append([x,y])


class DFSSolution:
    def numIslands(self, grid) -> int:
        """
        RUNTIME: 920 ms (30.6%)
        MEMORY: 21.4 MB (35.97%)
        """
        if len(grid) == 0: return 0
        # initialize
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.visited = set()
        island = 0
        # dfs
        for i in range(self.m):
            for j in range(self.n):
                # do dfs when not visited and value is 1
                if self.grid[i][j] == '1' and f'{i},{j}' not in self.visited:
                    self.dfs(i, j)
                    island += 1
        return island

    def dfs(self, x, y):
        if x < 0 or x >= self.m or y < 0 or y >= self.n or self.grid[x][y] != '1' or f'{x},{y}' in self.visited:
            return
        self.visited.add(f'{x},{y}')
        self.dfs(x+1, y)
        self.dfs(x-1, y)
        self.dfs(x, y+1)
        self.dfs(x, y-1)


grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]]
a = BFSSolution()
print(a.numIslands(grid))
