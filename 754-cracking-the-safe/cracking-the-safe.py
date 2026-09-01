class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seen = set()
        start = "0" * (n - 1)
        result = []
        def dfs(node):
            for digit in map(str, range(k)):
                edge = node + digit
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])  
                    result.append(digit)
        dfs(start)
        return start + "".join(result[::-1])
if __name__ == "__main__":
    solution = Solution()
    def verify(n, k, password_str):
        expected_length = k ** n + n - 1
        assert len(password_str) == expected_length, \
            "Expected length {0}, got {1}".format(expected_length, len(password_str))
        seen_passwords = set()
        for i in range(len(password_str) - n + 1):
            seen_passwords.add(password_str[i:i + n])
        assert len(seen_passwords) == k ** n, \
            "Expected {0} distinct passwords covered, got {1}".format(k ** n, len(seen_passwords))
        return True
    n1, k1 = 1, 2
    result1 = solution.crackSafe(n1, k1)
    print("Example 1: Output = '{0}'".format(result1))
    assert verify(n1, k1, result1)
    n2, k2 = 2, 2
    result2 = solution.crackSafe(n2, k2)
    print("Example 2: Output = '{0}'".format(result2))
    assert verify(n2, k2, result2)
    n3, k3 = 3, 3
    result3 = solution.crackSafe(n3, k3)
    print("Example 3: Output = '{0}' (length {1})".format(result3, len(result3)))
    assert verify(n3, k3, result3)
    print("\nAll test cases passed!")
print(__name__)