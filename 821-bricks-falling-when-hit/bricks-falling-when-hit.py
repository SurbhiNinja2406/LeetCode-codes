class DSU(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n  
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]] 
            x = self.parent[x]
        return x
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
    def size_of(self, x):
        return self.size[self.find(x)]
    def connected(self, x, y):
        return self.find(x) == self.find(y)
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        if not grid or not grid[0]:
            return [0] * len(hits)
        m = len(grid)
        n = len(grid[0])
        top = m * n  
        final_grid = [row[:] for row in grid]
        for r, c in hits:
            final_grid[r][c] = 0
        dsu = DSU(m * n + 1)
        def index(r, c):
            return r * n + c
        for r in range(m):
            for c in range(n):
                if final_grid[r][c] == 1:
                    if r == 0:
                        dsu.union(index(r, c), top)
                    if r > 0 and final_grid[r - 1][c] == 1:
                        dsu.union(index(r, c), index(r - 1, c))
                    if c > 0 and final_grid[r][c - 1] == 1:
                        dsu.union(index(r, c), index(r, c - 1))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        num_hits = len(hits)
        result = [0] * num_hits
        for i in range(num_hits - 1, -1, -1):
            r, c = hits[i]
            if grid[r][c] == 0:
                result[i] = 0
                continue
            before = dsu.size_of(top)
            final_grid[r][c] = 1
            if r == 0:
                dsu.union(index(r, c), top)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and final_grid[nr][nc] == 1:
                    dsu.union(index(r, c), index(nr, nc))
            after = dsu.size_of(top)
            if dsu.connected(index(r, c), top):
                fall = after - before - 1
                result[i] = max(0, fall)
            else:
                result[i] = 0
        return result
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]], [2]),
        ([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]], [0, 0]),
    ]
    for grid, hits, expected in test_cases:
        grid_copy = [row[:] for row in grid]
        hits_copy = [list(h) for h in hits]
        result = solution.hitBricks(grid_copy, hits_copy)
        status = "PASS" if result == expected else "FAIL"
        print("grid={:<30} hits={:<20} expected={:<12} got={:<12} [{}]".format(
            str(grid), str(hits), str(expected), str(result), status))
print(__name__)