class MyCalendarTwo(object):

    def __init__(self):
        self.bookings = []    # all single bookings: list of (start, end)
        self.overlaps = []    # all regions currently double-booked: list of (start, end)

    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        for os, oe in self.overlaps:
            if startTime < oe and os < endTime:
                return False
        for bs, be in self.bookings:
            overlap_start = max(startTime, bs)
            overlap_end = min(endTime, be)
            if overlap_start < overlap_end:
                self.overlaps.append((overlap_start, overlap_end))
        self.bookings.append((startTime, endTime))
        return True
if __name__ == "__main__":
    def run_calls(events):
        obj = MyCalendarTwo()
        outputs = [None]
        for s, e in events:
            outputs.append(obj.book(s, e))
        return outputs
    events1 = [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
    expected1 = [None, True, True, True, False, True, True]
    result1 = run_calls(events1)
    status1 = "PASS" if result1 == expected1 else "FAIL"
    print("Test 1: [%s]" % status1)
    print("  Input:    events = %s" % events1)
    print("  Output:   %s" % result1)
    print("  Expected: %s" % expected1)
    print("")
    events2 = [[0, 10], [10, 20], [5, 15]]
    expected2 = [None, True, True, True]
    result2 = run_calls(events2)
    status2 = "PASS" if result2 == expected2 else "FAIL"
    print("Test 2 (touching intervals): [%s]" % status2)
    print("  Output:   %s" % result2)
    print("  Expected: %s" % expected2)
    print("")
    events3 = [[0, 10], [0, 10], [0, 10]]
    expected3 = [None, True, True, False]
    result3 = run_calls(events3)
    status3 = "PASS" if result3 == expected3 else "FAIL"
    print("Test 3 (three identical events): [%s]" % status3)
    print("  Output:   %s" % result3)
    print("  Expected: %s" % expected3)
    print("")
    events4 = [[i * 10, i * 10 + 10] for i in range(20)]
    result4 = run_calls(events4)
    expected4 = [None] + [True] * 20
    status4 = "PASS" if result4 == expected4 else "FAIL"
    print("Test 4 (20 sequential bookings): [%s]" % status4)
    print("  All True:", result4 == expected4)
print(__name__)
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)