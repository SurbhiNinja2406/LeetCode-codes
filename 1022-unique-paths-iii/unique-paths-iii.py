class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        start = None
        empty_count = 0  
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                    empty_count += 1
                elif grid[i][j] == 0 or grid[i][j] == 2:
                    empty_count += 1
        self.count = 0
        def backtrack(i, j, remaining):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1:
                return
            if grid[i][j] == 2:
                if remaining == 1:
                    self.count += 1
                return
            original = grid[i][j]
            grid[i][j] = -1
            backtrack(i + 1, j, remaining - 1)
            backtrack(i - 1, j, remaining - 1)
            backtrack(i, j + 1, remaining - 1)
            backtrack(i, j - 1, remaining - 1)
            grid[i][j] = original
        backtrack(start[0], start[1], empty_count)
        return self.count
if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]])) 
    print(sol.uniquePathsIII([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]))    
    print(sol.uniquePathsIII([[0, 1], [2, 0]]))                           
print(__name__)