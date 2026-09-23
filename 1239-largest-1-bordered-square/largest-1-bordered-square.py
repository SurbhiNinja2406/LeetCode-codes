class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        left = [[0] * cols for _ in range(rows)]
        up = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    left[i][j] = (left[i][j - 1] + 1) if j > 0 else 1
                    up[i][j] = (up[i - 1][j] + 1) if i > 0 else 1
        max_side = 0
        for i in range(rows):
            for j in range(cols):
                side = min(left[i][j], up[i][j])
                while side > max_side:
                    top_row, left_col = i - side + 1, j - side + 1
                    if (left[top_row][j] >= side and
                            up[i][left_col] >= side):
                        max_side = side
                        break
                    side -= 1
        return max_side * max_side
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(sol.largest1BorderedSquare(grid1))  
    grid2 = [[1, 1, 0, 0]]
    print(sol.largest1BorderedSquare(grid2))  
print(__name__)