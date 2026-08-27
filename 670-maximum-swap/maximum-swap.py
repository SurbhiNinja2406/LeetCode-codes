class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        n = len(digits)
        last = {int(d): i for i, d in enumerate(digits)}
        for i in range(n):
            cur_digit = int(digits[i])
            for d in range(9, cur_digit, -1):
                if last.get(d, -1) > i:
                    j = last[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))
        return num
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.maximumSwap(2736)
    print("Example 1:")
    print("Input:  num = 2736")
    print("Output:", result1)
    print("Expected: 7236")
    print()
    result2 = solution.maximumSwap(9973)
    print("Example 2:")
    print("Input:  num = 9973")
    print("Output:", result2)
    print("Expected: 9973")
    print()
    result3 = solution.maximumSwap(0)
    print("Example 3 (extra):")
    print("Input:  num = 0")
    print("Output:", result3)
    print("Expected: 0")
    print()
    result4 = solution.maximumSwap(98368)
    print("Example 4 (extra):")
    print("Input:  num = 98368")
    print("Output:", result4)
    print("Expected: 98863")
    print()
    result5 = solution.maximumSwap(1993)
    print("Example 5 (extra):")
    print("Input:  num = 1993")
    print("Output:", result5)
    print("Expected: 9913")
print(__name__)