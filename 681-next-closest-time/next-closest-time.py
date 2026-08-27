class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        allowed_digits = set(time.replace(":", ""))
        cur_h, cur_m = int(time[:2]), int(time[3:])
        cur_total = cur_h * 60 + cur_m
        for offset in range(1, 1441):
            total = (cur_total + offset) % 1440
            h, m = divmod(total, 60)
            candidate = "{:02d}:{:02d}".format(h, m)
            if all(c in allowed_digits for c in candidate if c != ":"):
                return candidate
        return time
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.nextClosestTime("19:34")
    print("Example 1:")
    print('Input:  time = "19:34"')
    print("Output:", result1)
    print('Expected: "19:39"')
    print()
    result2 = solution.nextClosestTime("23:59")
    print("Example 2:")
    print('Input:  time = "23:59"')
    print("Output:", result2)
    print('Expected: "22:22"')
    print()
    result3 = solution.nextClosestTime("11:11")
    print("Example 3 (extra):")
    print('Input:  time = "11:11"')
    print("Output:", result3)
    print('Expected: "11:11"')
    print()
    result4 = solution.nextClosestTime("01:34")
    print("Example 4 (extra):")
    print('Input:  time = "01:34"')
    print("Output:", result4)
    print()
    result5 = solution.nextClosestTime("12:09")
    print("Example 5 (extra):")
    print('Input:  time = "12:09"')
    print("Output:", result5)
print(__name__)