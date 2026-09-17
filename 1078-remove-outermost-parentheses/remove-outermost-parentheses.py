class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        depth = 0
        for char in s:
            if char == '(':
                if depth > 0:
                    result.append(char)
                depth += 1
            else: 
                depth -= 1
                if depth > 0:
                    result.append(char)
        return "".join(result)
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("(()())(())", "()()()"),
        ("(()())(())(()(()))", "()()()()(())"),
        ("()()", ""),
        ("(())", "()"),
        ("()", ""),
    ]
    for s, expected in test_cases:
        result = sol.removeOuterParentheses(s)
        status = "PASS" if result == expected else "FAIL"
        print("s={0} -> {1} (expected {2}) [{3}]".format(
            s, result, expected, status
        ))