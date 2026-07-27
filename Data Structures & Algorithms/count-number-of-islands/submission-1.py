class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not seen[i][j]:
                    islands += self.dfs(grid, seen, i, j)
        return islands

    def dfs(self, grid, seen, i, j):
        seen[i][j] = True

        if grid[i][j] == "1":
            # we are on an island, mark all as seen
            if i > 0 and not seen[i - 1][j]:
                self.dfs(grid, seen, i - 1, j)
            if j > 0 and not seen[i][j - 1]:
                self.dfs(grid, seen, i, j - 1)
            if i < len(grid) - 1 and not seen[i + 1][j]:
                self.dfs(grid, seen, i + 1, j)
            if j < len(grid[0]) - 1 and not seen[i][j + 1]:
                self.dfs(grid, seen, i, j + 1)
            return 1
        return 0
