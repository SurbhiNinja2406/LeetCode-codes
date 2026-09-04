import sys
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        sys.setrecursionlimit(10000)
        memo = {}
        def dp(t):
            if t in memo:
                return memo[t]
            if t == 0:
                return 0
            n = t.bit_length()
            if (1 << n) - 1 == t:
                memo[t] = n
                return n
            best = float('inf')
            for m in range(n - 1):
                cur = (1 << (n - 1)) - (1 << m)
                cost = dp(t - cur) + (n - 1) + m + 2
                if cost < best:
                    best = cost
            overshoot = (1 << n) - 1 - t
            if overshoot < t:
                cost = dp(overshoot) + n + 1
                if cost < best:
                    best = cost
            memo[t] = best
            return best
        return dp(target)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (3, 2),
        (6, 5),
    ]
    for target, expected in test_cases:
        result = solution.racecar(target)
        status = "PASS" if result == expected else "FAIL"
        print("target={:<8} expected={} got={} [{}]".format(
            target, expected, result, status))
print(__name__)