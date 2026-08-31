class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            n = num
            while n > 0:
                digit = n % 10
                if digit == 0 or num % digit != 0:
                    return False
                n //= 10
            return True
        return [num for num in range(left, right + 1) if is_self_dividing(num)]
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (1, 22, [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]),
        (47, 85, [48, 55, 66, 77]),
        (1, 1, [1]),
        (10, 10, []),
        (128, 128, [128]),
    ]
    for idx, (left, right, expected) in enumerate(test_cases, 1):
        result = solution.selfDividingNumbers(left, right)
        status = "PASS" if result == expected else "FAIL"
        print("Test %d: [%s]" % (idx, status))
        print("  Input:    left = %d, right = %d" % (left, right))
        print("  Output:   %s" % result)
        print("  Expected: %s" % expected)
        print("")
print(__name__)