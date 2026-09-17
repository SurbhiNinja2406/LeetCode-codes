class Solution(object):
    def baseNeg2(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return "0"
        digits = []
        while n != 0:
            remainder = n & 1 
            digits.append(str(remainder))
            n = (n - remainder) // -2
        digits.reverse()
        return "".join(digits)
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (2, "110"),
        (3, "111"),
        (4, "100"),
        (0, "0"),
        (1, "1"),
    ]
    for n, expected in test_cases:
        result = sol.baseNeg2(n)
        status = "PASS" if result == expected else "FAIL"
        print("n={0} -> {1} (expected {2}) [{3}]".format(
            n, result, expected, status
        ))
print(__name__)