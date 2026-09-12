from collections import deque
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def get_neighbors(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc
        def dfs(r, c, island_cells):
            stack = [(r, c)]
            grid[r][c] = 2 
            island_cells.append((r, c))
            while stack:
                cr, cc = stack.pop()
                for nr, nc in get_neighbors(cr, cc):
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        island_cells.append((nr, nc))
                        stack.append((nr, nc))
        first_island = []
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, first_island)
                    found = True
                    break
        queue = deque([(r, c, 0) for r, c in first_island])
        visited = set(first_island)
        while queue:
            r, c, dist = queue.popleft()
            for nr, nc in get_neighbors(r, c):
                if (nr, nc) in visited:
                    continue
                if grid[nr][nc] == 1:
                    return dist
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
        return -1  
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[0, 1], [1, 0]]
    print(sol.shortestBridge(grid1)) 
    grid2 = [[0, 1, 0], [0, 0, 0], [0, 0, 1]]
    print(sol.shortestBridge(grid2))  
    grid3 = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]
    print(sol.shortestBridge(grid3)) 
print(__name__)