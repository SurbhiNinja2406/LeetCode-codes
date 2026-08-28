class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def dfs(r, c, r0, c0, shape):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if visited[r][c] or grid[r][c] != 1:
                return
            visited[r][c] = True
            shape.append((r - r0, c - c0))
            dfs(r + 1, c, r0, c0, shape)
            dfs(r - 1, c, r0, c0, shape)
            dfs(r, c + 1, r0, c0, shape)
            dfs(r, c - 1, r0, c0, shape)
        shapes = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    shape = []
                    dfs(i, j, i, j, shape)
                    shapes.add(tuple(sorted(shape)))
        return len(shapes)
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[1,1,0,0,0],
              [1,1,0,0,0],
              [0,0,0,1,1],
              [0,0,0,1,1]]
    print(sol.numDistinctIslands(grid1)) 
    grid2 = [[1,1,0,1,1],
              [1,0,0,0,0],
              [0,0,0,0,1],
              [1,1,0,1,1]]
    print(sol.numDistinctIslands(grid2)) 
print(__name__)