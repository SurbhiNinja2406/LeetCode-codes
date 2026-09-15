class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        mask = 1
        while mask < n:
            mask = (mask << 1) | 1
        return n ^ mask
if __name__ == "__main__":
    solution = Solution()
    n1 = 5
    result1 = solution.bitwiseComplement(n1)
    print("Example 1: n={}".format(n1))
    print("Output: {}".format(result1))
    print("Expected: 2")
    print("")
    n2 = 7
    result2 = solution.bitwiseComplement(n2)
    print("Example 2: n={}".format(n2))
    print("Output: {}".format(result2))
    print("Expected: 0")
    print("")
    n3 = 10
    result3 = solution.bitwiseComplement(n3)
    print("Example 3: n={}".format(n3))
    print("Output: {}".format(result3))
    print("Expected: 5")
    print("")
    n4 = 0
    result4 = solution.bitwiseComplement(n4)
    print("Example 4: n={}".format(n4))
    print("Output: {}".format(result4))
    print("Expected: 1")
    print("")
    n5 = 1
    result5 = solution.bitwiseComplement(n5)
    print("Example 5: n={}".format(n5))
    print("Output: {}".format(result5))
    print("Expected: 0")
print(__name__)