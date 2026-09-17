class Solution(object):
    def queryString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: bool
        """
        max_possible_substrings = len(s) * (len(s) + 1) // 2
        if n > max_possible_substrings:
            return False
        for i in range(1, n + 1):
            binary = bin(i)[2:]  
            if binary not in s:
                return False
        return True
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("0110", 3, True),
        ("0110", 4, False),
        ("1", 1, True),
        ("1", 2, False),
        ("0000000000000000000", 1, False),
    ]
    for s, n, expected in test_cases:
        result = sol.queryString(s, n)
        status = "PASS" if result == expected else "FAIL"
        print("s={0}, n={1} -> {2} (expected {3}) [{4}]".format(
            s, n, result, expected, status
        ))
print(__name__)