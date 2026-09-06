class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        arr.sort()
        dp = {}  
        for i, x in enumerate(arr):
            total = 1  
            for j in range(i):
                left = arr[j]
                if x % left == 0:
                    right = x // left
                    if right in dp:
                        total += dp[left] * dp[right]
            dp[x] = total % MOD
        return sum(dp.values()) % MOD
if __name__ == "__main__":
    sol = Solution()
    print(sol.numFactoredBinaryTrees([2, 4]))         
    print(sol.numFactoredBinaryTrees([2, 4, 5, 10]))  
print(__name__)