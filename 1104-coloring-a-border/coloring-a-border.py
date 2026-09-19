class Solution(object):
    def colorBorder(self, grid, row, col, color):
        """
        :type grid: List[List[int]]
        :type row: int
        :type col: int
        :type color: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        original = grid[row][col]
        visited = set()
        visited.add((row, col))
        stack = [(row, col)]
        border = []
        while stack:
            r, c = stack.pop()
            is_border = False
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    is_border = True          
                elif grid[nr][nc] != original:
                    is_border = True             
                elif (nr, nc) not in visited:
                    visited.add((nr, nc))       
                    stack.append((nr, nc))
            if is_border:
                border.append((r, c))
        for r, c in border:
            grid[r][c] = color
        return grid
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1, 1], [1, 2]], 0, 0, 3, [[3, 3], [3, 2]]),
        ([[1, 2, 2], [2, 3, 2]], 0, 1, 3, [[1, 3, 3], [2, 3, 3]]),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1, 1, 2,
         [[2, 2, 2], [2, 1, 2], [2, 2, 2]]),
    ]
    for grid, r, c, color, expected in tests:
        result = sol.colorBorder(grid, r, c, color)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)