class Solution(object):
    def brokenCalc(self, startValue, target):
        """
        :type startValue: int
        :type target: int
        :rtype: int
        """
        operations = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            operations += 1
        operations += startValue - target
        return operations
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (2, 3, 2),
        (5, 8, 2),
        (3, 10, 3),
        (1, 1, 0),
        (1000000000, 1, 999999999),
    ]
    for startValue, target, expected in test_cases:
        result = sol.brokenCalc(startValue, target)
        status = "PASS" if result == expected else "FAIL"
        print("startValue={0}, target={1} -> {2} (expected {3}) [{4}]".format(
            startValue, target, result, expected, status
        ))
print(__name__)