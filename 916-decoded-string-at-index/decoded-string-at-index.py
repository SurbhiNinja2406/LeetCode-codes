class Solution(object):
    def decodeAtIndex(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        size = 0
        for c in s:
            if c.isdigit():
                size *= int(c)
            else:
                size += 1
        for c in reversed(s):
            k %= size
            if k == 0 and c.isalpha():
                return c
            if c.isdigit():
                size //= int(c)
            else:
                size -= 1
        return ""
if __name__ == "__main__":
    sol = Solution()
    s1, k1 = "leet2code3", 10
    result1 = sol.decodeAtIndex(s1, k1)
    print("Example 1: {} (expected o)".format(result1))
    s2, k2 = "ha22", 5
    result2 = sol.decodeAtIndex(s2, k2)
    print("Example 2: {} (expected h)".format(result2))
    s3, k3 = "a2345678999999999999999", 1
    result3 = sol.decodeAtIndex(s3, k3)
    print("Example 3: {} (expected a)".format(result3))
print(__name__)