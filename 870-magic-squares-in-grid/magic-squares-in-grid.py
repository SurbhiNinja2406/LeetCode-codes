class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])        
        if row < 3 or col < 3:
            return 0
        def is_magic_square(top_r, top_c):
            vals = []
            for r in range(top_r, top_r + 3):
                for c in range(top_c, top_c + 3):
                    vals.append(grid[r][c])
            if sorted(vals) != list(range(1, 10)):
                return False
            target = sum(grid[top_r][top_c:top_c + 3])            
            for r in range(top_r, top_r + 3):
                if sum(grid[r][top_c:top_c + 3]) != target:
                    return False
            for c in range(top_c, top_c + 3):
                col_sum = grid[top_r][c] + grid[top_r + 1][c] + grid[top_r + 2][c]
                if col_sum != target:
                    return False
            diag1 = grid[top_r][top_c] + grid[top_r + 1][top_c + 1] + grid[top_r + 2][top_c + 2]
            diag2 = grid[top_r][top_c + 2] + grid[top_r + 1][top_c + 1] + grid[top_r + 2][top_c]
            if diag1 != target or diag2 != target:
                return False
            return True        
        count = 0
        for r in range(row - 2):
            for c in range(col - 2):
                if is_magic_square(r, c):
                    count += 1        
        return count
if __name__ == "__main__":
    sol = Solution()
    print(sol.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))  
    print(sol.numMagicSquaresInside([[8]]))                  
print(__name__)