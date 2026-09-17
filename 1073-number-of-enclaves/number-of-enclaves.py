class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        def flood_fill(r, c):
            stack = [(r, c)]
            grid[r][c] = 0  
            while stack:
                row, col = stack.pop()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        stack.append((nr, nc))
        for r in range(m):
            for c in range(n):
                is_boundary = (r == 0 or r == m - 1 or c == 0 or c == n - 1)
                if is_boundary and grid[r][c] == 1:
                    flood_fill(r, c)
        count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    count += 1
        return count
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 3),
        ([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]], 0),
        ([[1]], 0),
        ([[0]], 0),
        ([[1, 1], [1, 1]], 0),
    ]
    for grid, expected in test_cases:
        grid_copy = [row[:] for row in grid]
        result = sol.numEnclaves(grid_copy)
        status = "PASS" if result == expected else "FAIL"
        print("grid={0} -> {1} (expected {2}) [{3}]".format(
            grid, result, expected, status
        ))
print(__name__)