import math
class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        if n >= 4800:
            return 1.0
        n = int(math.ceil(n / 25.0))
        memo = {}
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            key = (a, b)
            if key in memo:
                return memo[key]
            result = 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )
            memo[key] = result
            return result
        return dp(n, n)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (50, 0.62500),
        (100, 0.71875),
    ]
    for n, expected in test_cases:
        result = solution.soupServings(n)
        status = "PASS" if abs(result - expected) < 1e-5 else "FAIL"
        print("n={:<10} expected={:<10.5f} got={:<10.5f} [{}]".format(
            n, expected, result, status))
print(__name__)