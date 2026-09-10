class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        s = str(n)
        L = len(s)
        D = len(digits)
        count = 0
        for l in range(1, L):
            count += D ** l
        for i in range(L):
            matched = False
            for d in digits:
                if d < s[i]:
                    count += D ** (L - 1 - i)
                elif d == s[i]:
                    matched = True
            if not matched:
                break
        else:
            count += 1
        return count
if __name__ == "__main__":
    solution = Solution()
    digits1, n1 = ["1", "3", "5", "7"], 100
    print("Example 1:")
    print("Input: digits =", digits1, ", n =", n1)
    print("Output:", solution.atMostNGivenDigitSet(digits1, n1))
    print()
    digits2, n2 = ["1", "4", "9"], 1000000000
    print("Example 2:")
    print("Input: digits =", digits2, ", n =", n2)
    print("Output:", solution.atMostNGivenDigitSet(digits2, n2))
    print()
    digits3, n3 = ["7"], 8
    print("Example 3:")
    print("Input: digits =", digits3, ", n =", n3)
    print("Output:", solution.atMostNGivenDigitSet(digits3, n3))
print(__name__)