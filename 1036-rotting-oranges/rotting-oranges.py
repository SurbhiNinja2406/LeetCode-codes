from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue and fresh_count > 0:
            minutes += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
        return minutes if fresh_count == 0 else -1
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(sol.orangesRotting(grid1))  
    grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print(sol.orangesRotting(grid2))  
    grid3 = [[0, 2]]
    print(sol.orangesRotting(grid3))  
print(__name__)