class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        total = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    total += 1
        for i in range(n):
            total += max(grid[i])
        for j in range(n):
            total += max(grid[i][j] for i in range(n))
        return total
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[1, 2], [3, 4]]
    result1 = sol.projectionArea(grid1)
    print("Example 1: {} (expected 17)".format(result1))
    grid2 = [[2]]
    result2 = sol.projectionArea(grid2)
    print("Example 2: {} (expected 5)".format(result2))
    grid3 = [[1, 0], [0, 2]]
    result3 = sol.projectionArea(grid3)
    print("Example 3: {} (expected 8)".format(result3))