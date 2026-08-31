class MyCalendarThree(object):
    def __init__(self):
        self.delta = {}
    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        self.delta[startTime] = self.delta.get(startTime, 0) + 1
        self.delta[endTime] = self.delta.get(endTime, 0) - 1
        max_overlap = 0
        current = 0
        for t in sorted(self.delta.keys()):
            current += self.delta[t]
            if current > max_overlap:
                max_overlap = current
        return max_overlap
if __name__ == "__main__":
    def run_calls(events):
        obj = MyCalendarThree()
        outputs = [None]
        for s, e in events:
            outputs.append(obj.book(s, e))
        return outputs
    events1 = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    expected1 = [None, 1, 1, 2, 3, 3, 3]
    result1 = run_calls(events1)
    status1 = "PASS" if result1 == expected1 else "FAIL"
    print("Test 1: [%s]" % status1)
    print("  Input:    events = %s" % events1)
    print("  Output:   %s" % result1)
    print("  Expected: %s" % expected1)
    print("")
    events2 = [[0, 10], [10, 20], [20, 30]]
    expected2 = [None, 1, 1, 1]
    result2 = run_calls(events2)
    status2 = "PASS" if result2 == expected2 else "FAIL"
    print("Test 2 (touching intervals): [%s]" % status2)
    print("  Output:   %s" % result2)
    print("  Expected: %s" % expected2)
    print("")
    events3 = [[0, 10]] * 5
    expected3 = [None, 1, 2, 3, 4, 5]
    result3 = run_calls(events3)
    status3 = "PASS" if result3 == expected3 else "FAIL"
    print("Test 3 (5 identical events): [%s]" % status3)
    print("  Output:   %s" % result3)
    print("  Expected: %s" % expected3)
    print("")
    events4 = [[1, 10], [2, 9], [3, 8], [11, 12]]
    expected4 = [None, 1, 2, 3, 3]
    result4 = run_calls(events4)
    status4 = "PASS" if result4 == expected4 else "FAIL"
    print("Test 4 (nested intervals): [%s]" % status4)
    print("  Output:   %s" % result4)
    print("  Expected: %s" % expected4)
print(__name__)
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)