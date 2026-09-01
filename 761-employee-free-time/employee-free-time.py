# Definition for an Interval.
class Interval(object):
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end
    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)
class Solution(object):
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        all_intervals = []
        for employee_intervals in schedule:
            for interval in employee_intervals:
                all_intervals.append(interval)
        all_intervals.sort(key=lambda iv: iv.start)
        result = []
        if not all_intervals:
            return result
        end = all_intervals[0].end
        for interval in all_intervals[1:]:
            if interval.start > end:
                result.append(Interval(end, interval.start))
                end = interval.end
            else:
                end = max(end, interval.end)
        return result
if __name__ == "__main__":
    sol = Solution()
    def build_schedule(raw):
        return [[Interval(s, e) for s, e in emp] for emp in raw]
    schedule1 = build_schedule([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]])
    print(sol.employeeFreeTime(schedule1))
    schedule2 = build_schedule([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]])
    print(sol.employeeFreeTime(schedule2))
print(__name__)