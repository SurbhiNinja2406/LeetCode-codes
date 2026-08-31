import bisect
class MyCalendar(object):
    def __init__(self):
        self.starts = []   
        self.events = []  
    def book(self, startTime, endTime):
        """
        :type startTime: int
        :type endTime: int
        :rtype: bool
        """
        idx = bisect.bisect_left(self.starts, startTime)
        if idx > 0 and self.events[idx - 1][1] > startTime:
            return False
        if idx < len(self.events) and self.events[idx][0] < endTime:
            return False
        self.starts.insert(idx, startTime)
        self.events.insert(idx, (startTime, endTime))
        return True
if __name__ == "__main__":
    def run_test(ops, args, expected):
        outputs = []
        obj = None
        for op, arg in zip(ops, args):
            if op == "MyCalendar":
                obj = MyCalendar()
                outputs.append(None)
            elif op == "book":
                outputs.append(obj.book(*arg))
        return outputs
    ops1 = ["MyCalendar", "book", "book", "book"]
    args1 = [[], [10, 20], [15, 25], [20, 30]]
    expected1 = [None, True, False, True]
    result1 = run_test(ops1, args1, expected1)
    status1 = "PASS" if result1 == expected1 else "FAIL"
    print("Test 1: [%s]" % status1)
    print("  Input:    ops = %s, args = %s" % (ops1, args1))
    print("  Output:   %s" % result1)
    print("  Expected: %s" % expected1)
    print("")
    obj2 = MyCalendar()
    r1 = obj2.book(0, 10)
    r2 = obj2.book(10, 20)  
    r3 = obj2.book(5, 15)  
    result2 = [r1, r2, r3]
    expected2 = [True, True, False]
    status2 = "PASS" if result2 == expected2 else "FAIL"
    print("Test 2 (back-to-back / overlap edge cases): [%s]" % status2)
    print("  Output:   %s" % result2)
    print("  Expected: %s" % expected2)
    print("")
    obj3 = MyCalendar()
    results3 = [obj3.book(i * 10, i * 10 + 10) for i in range(20)]
    expected3 = [True] * 20
    status3 = "PASS" if results3 == expected3 else "FAIL"
    print("Test 3 (20 sequential bookings): [%s]" % status3)
    print("  All True:", results3 == expected3)
print(__name__)
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)