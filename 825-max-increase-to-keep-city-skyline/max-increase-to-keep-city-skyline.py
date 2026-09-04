class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(grid[r][c] for r in range(n)) for c in range(n)]
        total_increase = 0
        for r in range(n):
            for c in range(n):
                new_height = min(row_max[r], col_max[c])
                total_increase += new_height - grid[r][c]
        return total_increase
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]], 35),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
    ]
    for grid, expected in test_cases:
        grid_copy = [row[:] for row in grid]
        result = solution.maxIncreaseKeepingSkyline(grid_copy)
        status = "PASS" if result == expected else "FAIL"
        print("grid={:<45} expected={} got={} [{}]".format(
            str(grid), expected, result, status))
print(__name__)