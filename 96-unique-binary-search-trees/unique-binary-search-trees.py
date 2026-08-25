class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1 
        dp[1] = 1 if n >= 1 else 1
        for nodes in range(2, n + 1):
            total = 0
            for root_val in range(1, nodes + 1):
                left = dp[root_val - 1]
                right = dp[nodes - root_val]
                total += left * right
            dp[nodes] = total
        return dp[n]
if __name__ == "__main__":
    sol = Solution()
    print("n=3: {}".format(sol.numTrees(3))) 
    print("n=1: {}".format(sol.numTrees(1)))
    print("n=19: {}".format(sol.numTrees(19))) 