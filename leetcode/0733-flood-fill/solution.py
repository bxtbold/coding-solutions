class Solution:
    def floodFill(self, image, sr, sc, color):
        """
        DFS
        RUNTIME: 116 ms (67.40%)
        MEMORY: 14 MB (89.90%)
        """

        self.image = image
        self.sr = sr
        self.sc = sc
        self.color = color
        self.color2change = image[sr][sc]
        self.row, self.column = len(image), len(image[0])

        # DFS
        self.dfs(sr, sc)

        return self.image

    def dfs(self, r, c):

        # check depth
        if r < 0 or r > self.row - 1: return
        if c < 0 or c > self.column - 1: return
        if self.image[r][c] == self.color or \
            self.image[r][c] != self.color2change: return

        # change color
        self.image[r][c] = self.color

        # radiate in four directions
        self.dfs(r + 1, c)
        self.dfs(r - 1, c)
        self.dfs(r, c + 1)
        self.dfs(r, c - 1)


sol = Solution()
image = sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(image)
