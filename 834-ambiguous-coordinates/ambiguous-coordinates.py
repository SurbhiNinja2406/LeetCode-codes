class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        digits = s[1:-1]  
        def generate_numbers(part):
            n = len(part)
            results = []
            if not (n > 1 and part[0] == '0'):
                results.append(part)
            for i in range(1, n):
                left = part[:i]
                right = part[i:]
                if left != '0' and left[0] == '0':
                    continue
                if right[-1] == '0':
                    continue
                results.append(left + '.' + right)
            return results
        result = []
        n = len(digits)
        for i in range(1, n):
            left_part = digits[:i]
            right_part = digits[i:]
            left_options = generate_numbers(left_part)
            right_options = generate_numbers(right_part)
            for l in left_options:
                for r in right_options:
                    result.append("({}, {})".format(l, r))
        return result
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("(123)", ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"]),
        ("(0123)", ["(0, 1.23)", "(0, 12.3)", "(0, 123)", "(0.1, 2.3)", "(0.1, 23)", "(0.12, 3)"]),
        ("(00011)", ["(0, 0.011)", "(0.001, 1)"]),
    ]
    for s, expected in test_cases:
        result = solution.ambiguousCoordinates(s)
        result_set = set(result)
        expected_set = set(expected)
        status = "PASS" if result_set == expected_set else "FAIL"
        print("s={:<12} got={}".format(s, str(result)))
        print("  expected={} [{}]".format(str(expected), status))
print(__name__)