class Solution(object):
    def superEggDrop(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        dp = [0] * (k + 1)
        moves = 0
        while dp[k] < n:
            moves += 1
            for eggs in range(k, 0, -1):
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1
        return moves
if __name__ == "__main__":
    sol = Solution()
    k1, n1 = 1, 2
    result1 = sol.superEggDrop(k1, n1)
    print("Example 1: {} (expected 2)".format(result1))
    k2, n2 = 2, 6
    result2 = sol.superEggDrop(k2, n2)
    print("Example 2: {} (expected 3)".format(result2))
    k3, n3 = 3, 14
    result3 = sol.superEggDrop(k3, n3)
    print("Example 3: {} (expected 4)".format(result3))
print(__name__)