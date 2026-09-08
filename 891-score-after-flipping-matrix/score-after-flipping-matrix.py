class Solution(object):
    def matrixScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] ^= 1
        for j in range(1, n):
            count_ones = sum(grid[i][j] for i in range(m))
            if count_ones < m - count_ones:
                for i in range(m):
                    grid[i][j] ^= 1
        total = 0
        for i in range(m):
            row_val = 0
            for j in range(n):
                row_val = (row_val << 1) | grid[i][j]
            total += row_val        
        return total
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    result1 = sol.matrixScore(grid1)
    print("Example 1:")
    print("Input: grid =", [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
    print("Output:", result1)
    print("Expected: 39")
    print()
    grid2 = [[0]]
    result2 = sol.matrixScore(grid2)
    print("Example 2:")
    print("Input: grid =", [[0]])
    print("Output:", result2)
    print("Expected: 1")
    print()
    grid3 = [[1, 0, 0], [1, 0, 1], [0, 1, 0]]
    result3 = sol.matrixScore(grid3)
    print("Additional test:")
    print("Input: grid =", [[1, 0, 0], [1, 0, 1], [0, 1, 0]])
    print("Output:", result3)
print(__name__)