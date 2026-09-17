class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        number = 0
        for digit in num:
            number = number * 10 + digit
        total = number + k
        return [int(d) for d in str(total)]
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([1, 2, 0, 0], 34, [1, 2, 3, 4]),
        ([2, 7, 4], 181, [4, 5, 5]),
        ([2, 1, 5], 806, [1, 0, 2, 1]),
    ]
    for num, k, expected in test_cases:
        result = sol.addToArrayForm(num, k)
        status = "PASS" if result == expected else "FAIL"
        print("num={0}, k={1} -> {2} (expected {3}) [{4}]".format(
            num, k, result, expected, status
        ))
print(__name__)