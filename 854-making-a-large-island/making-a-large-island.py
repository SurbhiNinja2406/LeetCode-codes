class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        def neighbors(r, c):
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    yield nr, nc
        island_id = 2
        island_area = {} 
        def dfs(r, c, island_id):
            stack = [(r, c)]
            grid[r][c] = island_id
            area = 0
            while stack:
                cr, cc = stack.pop()
                area += 1
                for nr, nc in neighbors(cr, cc):
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = island_id
                        stack.append((nr, nc))
            return area
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area = dfs(r, c, island_id)
                    island_area[island_id] = area
                    island_id += 1
        max_island = max(island_area.values()) if island_area else 0
        found_zero = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    found_zero = True
                    seen_ids = set()
                    total = 1  
                    for nr, nc in neighbors(r, c):
                        nid = grid[nr][nc]
                        if nid > 1 and nid not in seen_ids:
                            seen_ids.add(nid)
                            total += island_area[nid]
                    max_island = max(max_island, total)
        if not found_zero:
            max_island = n * n
        return max_island
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestIsland([[1, 0], [0, 1]]))  
    print(sol.largestIsland([[1, 1], [1, 0]])) 
    print(sol.largestIsland([[1, 1], [1, 1]]))  
print(__name__)