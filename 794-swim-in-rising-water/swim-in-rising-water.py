import heapq
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        max_elevation = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            elevation, r, c = heapq.heappop(heap)
            max_elevation = max(max_elevation, elevation)
            if r == n - 1 and c == n - 1:
                return max_elevation
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
        return max_elevation
if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 2], [1, 3]]
    print("Input: grid = {}".format(grid))
    print("Output: {}".format(sol.swimInWater(grid)))
    print("Expected: 3\n")
    grid = [[0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6]]
    print("Input: grid = {}".format(grid))
    print("Output: {}".format(sol.swimInWater(grid)))
    print("Expected: 16\n")
print(__name__)