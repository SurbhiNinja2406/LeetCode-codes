class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        def matches(query, pattern):
            i, j = 0, 0
            n, m = len(query), len(pattern)
            while i < n:
                if j < m and query[i] == pattern[j]:
                    j += 1
                elif query[i].isupper():
                    return False
                i += 1
            return j == m
        return [matches(q, pattern) for q in queries]
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FB",
         [True, False, True, True, False]),
        (["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBa",
         [True, False, True, False, False]),
        (["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBaT",
         [False, True, False, False, False]),
    ]
    for queries, pattern, expected in test_cases:
        result = sol.camelMatch(queries, pattern)
        status = "PASS" if result == expected else "FAIL"
        print("queries={0}, pattern={1} -> {2} (expected {3}) [{4}]".format(
            queries, pattern, result, expected, status
        ))
print(__name__)