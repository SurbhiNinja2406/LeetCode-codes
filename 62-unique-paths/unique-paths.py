class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n        
        for row in range(1, m):
            for col in range(1, n):
                dp[col] += dp[col - 1]        
        return dp[n - 1]
if __name__ == "__main__":
    solution = Solution()
    m1, n1 = 3, 7
    print(solution.uniquePaths(m1, n1))  
    m2, n2 = 3, 2
    print(solution.uniquePaths(m2, n2)) 
print(__name__)