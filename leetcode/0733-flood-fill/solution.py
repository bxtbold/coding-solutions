class Solution:
    def floodFill(self, image, sr, sc, color):
        """
        RUNTIME: 72 ms (96.89%)
        MEMORY: 14.1 MB (14.1%)
        """
        self.image = image
        self.row, self.column = len(image), len(image[0])
        # DFS
        self.dfs(sr, sc, color, image[sr][sc])
        return self.image

    def dfs(self, r, c, color, color2change):
        if r < 0 or r > self.row - 1 or \
           c < 0 or c > self.column - 1 or \
           self.image[r][c] == color or \
           self.image[r][c] != color2change:
            return
        # change color
        self.image[r][c] = color
        # radiate in four directions
        self.dfs(r + 1, c, color, color2change)
        self.dfs(r - 1, c, color, color2change)
        self.dfs(r, c + 1, color, color2change)
        self.dfs(r, c - 1, color, color2change)


sol = Solution()
image = sol.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(image)
