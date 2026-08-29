import bisect


class RangeModule(object):

    def __init__(self):
        # self.ranges is a sorted list of non-overlapping, merged
        # half-open intervals (start, end), each representing a
        # contiguous block of tracked numbers.
        self.ranges = []

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        ranges = self.ranges

        # Find the first index whose interval could overlap/touch `left`.
        i = bisect.bisect_left(ranges, (left,))
        if i > 0 and ranges[i - 1][1] >= left:
            # The interval just before also overlaps or touches [left, right)
            i -= 1

        # Find the first index whose interval starts strictly after `right`
        # (everything before this index overlaps or touches [left, right)).
        j = bisect.bisect_right(ranges, (right, float('inf')))

        if i < j:
            # Merge with every interval in ranges[i:j]
            left = min(left, ranges[i][0])
            right = max(right, ranges[j - 1][1])

        ranges[i:j] = [(left, right)]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges = self.ranges

        # Find the last interval whose start is <= left.
        i = bisect.bisect_right(ranges, (left, float('inf'))) - 1
        if i < 0:
            return False

        # [left, right) is fully tracked only if it fits entirely
        # within this single merged interval.
        return ranges[i][0] <= left and ranges[i][1] >= right

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        ranges = self.ranges
        i = bisect.bisect_left(ranges, (left,))
        if i > 0 and ranges[i - 1][1] > left:
            i -= 1
        j = bisect.bisect_left(ranges, (right,))
        new_intervals = []
        if i < j:
            if ranges[i][0] < left:
                new_intervals.append((ranges[i][0], left))
            if ranges[j - 1][1] > right:
                new_intervals.append((right, ranges[j - 1][1]))
        ranges[i:j] = new_intervals
if __name__ == "__main__":
    rangeModule = RangeModule()
    rangeModule.addRange(10, 20)
    rangeModule.removeRange(14, 16)
    r1 = rangeModule.queryRange(10, 14)
    r2 = rangeModule.queryRange(13, 15)
    r3 = rangeModule.queryRange(16, 17)
    print("Results:", [None, None, r1, r2, r3])
    print("Expected: [None, None, True, False, True]")
    assert [r1, r2, r3] == [True, False, True], "Mismatch!"
    print("Test passed!\n")
    rm2 = RangeModule()
    print("Extra test 1: empty module query -> ", rm2.queryRange(1, 5)) 
    rm2.addRange(1, 5)
    rm2.addRange(5, 10)  
    print("Extra test 2 (touching merge):", rm2.ranges)
    print("Extra test 2 query(1,10):", rm2.queryRange(1, 10))  
    rm2.removeRange(3, 7)
    print("Extra test 3 (after removeRange(3,7)):", rm2.ranges) 
    print("Extra test 3 query(1,3):", rm2.queryRange(1, 3))  
    print("Extra test 3 query(2,4):", rm2.queryRange(2, 4))  
    rm2.addRange(3, 7) 
    print("Extra test 4 (re-merged):", rm2.ranges) 
    rm3 = RangeModule()
    rm3.addRange(1, 3)
    rm3.addRange(5, 8)
    print("Extra test 5 (disjoint ranges):", rm3.ranges)  
    print("Extra test 5 query(1,8):", rm3.queryRange(1, 8))  
    rm3.removeRange(1, 8)
    print("Extra test 5 (after removing everything):", rm3.ranges)  
print(__name__)