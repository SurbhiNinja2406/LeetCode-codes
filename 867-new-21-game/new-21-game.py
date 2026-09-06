class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """
        if k == 0:
            return 1.0
        if n >= k - 1 + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0  
        result = 0.0        
        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts            
            if i < k:
                window_sum += dp[i]
            else:
                result += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]        
        return result
if __name__ == "__main__":
    sol = Solution()
    print(sol.new21Game(10, 1, 10))  
    print(sol.new21Game(6, 1, 10)) 
    print(sol.new21Game(21, 17, 10)) 
print(__name__)