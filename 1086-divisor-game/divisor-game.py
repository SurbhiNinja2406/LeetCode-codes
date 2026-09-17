class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n % 2 == 0
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (2, True),
        (3, False),
        (1, False),
        (4, True),
        (1000, True),
        (999, False),
    ]
    for n, expected in test_cases:
        result = sol.divisorGame(n)
        status = "PASS" if result == expected else "FAIL"
        print("n={0} -> {1} (expected {2}) [{3}]".format(
            n, result, expected, status
        ))
print(__name__)