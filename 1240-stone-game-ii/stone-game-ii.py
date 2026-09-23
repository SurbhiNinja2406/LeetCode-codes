class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        memo = {}        
        def dp(i, M):
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix_sum[i]            
            if (i, M) in memo:
                return memo[(i, M)]            
            best = 0
            for X in range(1, 2 * M + 1):
                opponent_gets = dp(i + X, max(M, X))
                current_gets = suffix_sum[i] - opponent_gets
                best = max(best, current_gets)            
            memo[(i, M)] = best
            return best        
        return dp(0, 1)
if __name__ == "__main__":
    sol = Solution()
    print(sol.stoneGameII([2, 7, 9, 4, 4])) 
    print(sol.stoneGameII([1, 2, 3, 4, 5, 100])) 
print(__name__)