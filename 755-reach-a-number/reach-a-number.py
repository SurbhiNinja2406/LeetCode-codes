class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        n = 0
        total = 0
        while total < target:
            n += 1
            total += n
        excess = total - target
        while excess % 2 != 0:
            n += 1
            total += n
            excess = total - target
        return n
if __name__ == "__main__":
    solution = Solution()
    target1 = 2
    result1 = solution.reachNumber(target1)
    print("Example 1: Output = {0}, Expected = 3".format(result1))
    assert result1 == 3
    target2 = 3
    result2 = solution.reachNumber(target2)
    print("Example 2: Output = {0}, Expected = 2".format(result2))
    assert result2 == 2
    target3 = 1
    result3 = solution.reachNumber(target3)
    print("Example 3: target=1, Output = {0}, Expected = 1".format(result3))
    assert result3 == 1
    target4 = -2
    result4 = solution.reachNumber(target4)
    print("Example 4: target=-2, Output = {0}, Expected = 3".format(result4))
    assert result4 == 3
    target5 = 0
    print("\nAll test cases passed!")
print(__name__)