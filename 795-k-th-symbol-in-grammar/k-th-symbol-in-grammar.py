import sys
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        k -= 1
        result = 0
        while k > 0:
            result ^= (k & 1)
            k >>= 1
        return result
if __name__ == "__main__":
    sol = Solution()
    n, k = 1, 1
    print("Input: n = {}, k = {}".format(n, k))
    print("Output: {}".format(sol.kthGrammar(n, k)))
    print("Expected: 0\n")
    n, k = 2, 1
    print("Input: n = {}, k = {}".format(n, k))
    print("Output: {}".format(sol.kthGrammar(n, k)))
    print("Expected: 0\n")
    n, k = 2, 2
    print("Input: n = {}, k = {}".format(n, k))
    print("Output: {}".format(sol.kthGrammar(n, k)))
    print("Expected: 1\n")
    print("Row 3 (expected 0 1 1 0):")
    for k in range(1, 5):
        sys.stdout.write(str(sol.kthGrammar(3, k)) + " ")
    print()
print(__name__)