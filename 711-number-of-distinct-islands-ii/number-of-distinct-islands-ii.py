class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        def get_island_cells(r, c):
            cells = []
            stack = [(r, c)]
            visited[r][c] = True
            while stack:
                x, y = stack.pop()
                cells.append((x, y))
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        stack.append((nx, ny))
            return cells
        def transform(cells):
            transformations = []
            funcs = [
                lambda x, y: (x, y),
                lambda x, y: (x, -y),
                lambda x, y: (-x, y),
                lambda x, y: (-x, -y),
                lambda x, y: (y, x),
                lambda x, y: (y, -x),
                lambda x, y: (-y, x),
                lambda x, y: (-y, -x),
            ]
            for f in funcs:
                transformed = [f(x, y) for x, y in cells]
                min_x = min(p[0] for p in transformed)
                min_y = min(p[1] for p in transformed)
                normalized = sorted((x - min_x, y - min_y) for x, y in transformed)
                transformations.append(tuple(normalized))
            return min(transformations)
        distinct_shapes = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    cells = get_island_cells(i, j)
                    canonical_shape = transform(cells)
                    distinct_shapes.add(canonical_shape)
        return len(distinct_shapes)
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[1, 1, 0, 0, 0],
              [1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1],
              [0, 0, 0, 1, 1]]
    print("Example 1 output:", sol.numDistinctIslands2(grid1))
    print("Example 1 expected: 1\n")
    grid2 = [[1, 1, 0, 0, 0],
              [1, 1, 0, 0, 0],
              [0, 0, 0, 1, 1],
              [0, 0, 0, 1, 1]]
    print("Example 2 output:", sol.numDistinctIslands2(grid2))
    print("Example 2 expected: 1\n")
    grid3 = [[1, 1, 0],
              [0, 1, 0],
              [0, 0, 0],
              [0, 0, 1]] 
    print("Extra test output:", sol.numDistinctIslands2(grid3))
    print("Extra test expected: 2\n")
    grid4 = [[1, 1],
              [1, 1]]
    print("Single square island output:", sol.numDistinctIslands2(grid4))
    print("Expected: 1\n")
    grid5 = [[0, 0], [0, 0]]
    print("No islands output:", sol.numDistinctIslands2(grid5))
    print("Expected: 0")
print(__name__)