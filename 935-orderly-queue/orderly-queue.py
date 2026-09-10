class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k >= 2:
            return "".join(sorted(s))
        best = s
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated < best:
                best = rotated
        return best
if __name__ == "__main__":
    solution = Solution()
    s1, k1 = "cba", 1
    print("Example 1:")
    print("Input: s =", repr(s1), ", k =", k1)
    print("Output:", repr(solution.orderlyQueue(s1, k1)))
    print()
    s2, k2 = "baaca", 3
    print("Example 2:")
    print("Input: s =", repr(s2), ", k =", k2)
    print("Output:", repr(solution.orderlyQueue(s2, k2)))
print(__name__)