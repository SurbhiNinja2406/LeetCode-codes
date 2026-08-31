class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        memo = {}
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            if (r1 >= n or c1 >= n or r2 >= n or c2 >= n or
                    grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            key = (r1, c1, r2)
            if key in memo:
                return memo[key]
            cherries = grid[r1][c1]
            if r1 != r2:
                cherries += grid[r2][c2]
            best = float('-inf')
            best = max(best, dp(r1 + 1, c1, r2 + 1))  
            best = max(best, dp(r1 + 1, c1, r2, ))    
            best = max(best, dp(r1, c1 + 1, r2 + 1))
            best = max(best, dp(r1, c1 + 1, r2))
            result = cherries + best if best != float('-inf') else float('-inf')
            memo[key] = result
            return result
        result = dp(0, 0, 0)
        return max(result, 0)
if __name__ == "__main__":
    sol = Solution()
    print(sol.cherryPickup([[0, 1, -1], [1, 0, -1], [1, 1, 1]]))
    print(sol.cherryPickup([[1, 1, -1], [1, -1, 1], [-1, 1, 1]]))
print(__name__)