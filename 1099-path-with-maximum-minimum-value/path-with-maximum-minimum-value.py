import heapq
class Solution(object):
    def maximumMinimumPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        heap = [(-grid[0][0], 0, 0)]
        visited[0][0] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while heap:
            neg_score, r, c = heapq.heappop(heap)
            score = -neg_score
            if r == m - 1 and c == n - 1:
                return score
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    new_score = min(score, grid[nr][nc])
                    heapq.heappush(heap, (-new_score, nr, nc))
        return -1  
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
    print(sol.maximumMinimumPath(grid1)) 
    grid2 = [[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]
    print(sol.maximumMinimumPath(grid2)) 
    grid3 = [[3, 4, 6, 3, 4],
              [0, 2, 1, 1, 7],
              [8, 8, 3, 2, 7],
              [3, 2, 4, 9, 8],
              [4, 1, 2, 0, 0],
              [4, 6, 5, 4, 3]]
    print(sol.maximumMinimumPath(grid3)) 
print(__name__)