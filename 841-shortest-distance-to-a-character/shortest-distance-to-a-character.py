class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        result = [float('inf')] * n
        distance = float('inf')
        for i in range(n):
            if s[i] == c:
                distance = 0
            else:
                if distance != float('inf'):
                    distance += 1
            result[i] = distance
        distance = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                distance = 0
            else:
                if distance != float('inf'):
                    distance += 1
            result[i] = min(result[i], distance)
        return result
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("loveleetcode", "e", [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]),
        ("aaab", "b", [3, 2, 1, 0]),
    ]
    for s, c, expected in test_cases:
        result = solution.shortestToChar(s, c)
        status = "PASS" if result == expected else "FAIL"
        print("s={:<15} c={:<3} expected={:<30} got={:<30} [{}]".format(
            s, c, str(expected), str(result), status))
print(__name__)