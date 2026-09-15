class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        remainder_count = [0] * 60
        count = 0
        for t in time:
            r = t % 60
            needed = (60 - r) % 60
            count += remainder_count[needed]
            remainder_count[r] += 1
        return count
if __name__ == "__main__":
    solution = Solution()
    time1 = [30, 20, 150, 100, 40]
    result1 = solution.numPairsDivisibleBy60(time1)
    print("Example 1: time={}".format(time1))
    print("Output: {}".format(result1))
    print("Expected: 3")
    print("")
    time2 = [60, 60, 60]
    result2 = solution.numPairsDivisibleBy60(time2)
    print("Example 2: time={}".format(time2))
    print("Output: {}".format(result2))
    print("Expected: 3")
    print("")
    time3 = [1, 2, 3, 4, 5]
    result3 = solution.numPairsDivisibleBy60(time3)
    print("Example 3: time={}".format(time3))
    print("Output: {}".format(result3))
    print("Expected: 0")
    print("")
    time4 = [60]
    result4 = solution.numPairsDivisibleBy60(time4)
    print("Example 4: time={}".format(time4))
    print("Output: {}".format(result4))
    print("Expected: 0")
    print("")
    time5 = [120, 60, 180, 240]
    result5 = solution.numPairsDivisibleBy60(time5)
    print("Example 5: time={}".format(time5))
    print("Output: {}".format(result5))
    print("Expected: 6")
print(__name__)