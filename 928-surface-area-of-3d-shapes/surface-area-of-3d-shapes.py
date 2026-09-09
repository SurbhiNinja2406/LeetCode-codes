class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        total = 0
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v == 0:
                    continue
                total += 2
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        neighbor = grid[ni][nj]
                    else:
                        neighbor = 0
                    total += max(0, v - neighbor)
        return total
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[1, 2], [3, 4]]
    result1 = sol.surfaceArea(grid1)
    print("Example 1: {} (expected 34)".format(result1))
    grid2 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    result2 = sol.surfaceArea(grid2)
    print("Example 2: {} (expected 32)".format(result2))
    grid3 = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    result3 = sol.surfaceArea(grid3)
    print("Example 3: {} (expected 46)".format(result3))
print(__name__)