class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 2:
            return s
        substrings = []
        count = 0
        start = 0
        for i, ch in enumerate(s):
            if ch == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                inner = self.makeLargestSpecial(s[start + 1:i])
                substrings.append('1' + inner + '0')
                start = i + 1
        substrings.sort(reverse=True)
        return ''.join(substrings)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("11011000", "11100100"),
        ("10", "10"),
        ("1100", "1100"),
        ("1101100010", None),
        ("111000", None),
    ]
    for s, expected in test_cases:
        result = solution.makeLargestSpecial(s)
        status = ""
        if expected is not None:
            status = "PASS" if result == expected else "FAIL"
        print("Input: {}".format(s))
        print("Output: {}".format(result))
        if expected is not None:
            print("Expected: {} -> {}".format(expected, status))
        print("-" * 40)
print(__name__)