from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1
        if n == 1:
            return 1
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]        
        queue = deque()
        queue.append((0, 0, 1))  
        grid[0][0] = 1 
        while queue:
            row, col, dist = queue.popleft()            
            if row == n - 1 and col == n - 1:
                return dist            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc                
                if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                    grid[new_row][new_col] = 1 
                    queue.append((new_row, new_col, dist + 1))        
        return -1
if __name__ == "__main__":
    solution = Solution()
    grid1 = [[0, 1], [1, 0]]
    result1 = solution.shortestPathBinaryMatrix(grid1)
    print("Example 1: {} (Expected: 2)".format(result1))
    grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    result2 = solution.shortestPathBinaryMatrix(grid2)
    print("Example 2: {} (Expected: 4)".format(result2))
    grid3 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    result3 = solution.shortestPathBinaryMatrix(grid3)
    print("Example 3: {} (Expected: -1)".format(result3))
print(__name__)