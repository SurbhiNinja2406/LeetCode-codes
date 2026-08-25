class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            result = result * 26 + value
        return result
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("A", 1),
        ("B", 2),
        ("C", 3),
        ("Z", 26),
        ("AA", 27),
        ("AB", 28),
        ("ZY", 701),
        ("AZ", 52),
        ("BA", 53),
        ("ZZ", 702),
        ("AAA", 703),
        ("FXSHRXW", 2147483647),  
    ]
    for columnTitle, expected in test_cases:
        result = solution.titleToNumber(columnTitle)
        status = "PASS" if result == expected else "FAIL"
        print("[{0}] columnTitle={1!r} -> got {2}, expected {3}".format(
            status, columnTitle, result, expected
        ))
print(__name__)