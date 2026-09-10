import bisect


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.leaders = []
        counts = {}
        current_leader = -1
        max_count = 0
        for person in persons:
            counts[person] = counts.get(person, 0) + 1
            if counts[person] >= max_count:
                max_count = counts[person]
                current_leader = person
            self.leaders.append(current_leader)
    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]
if __name__ == "__main__":
    ops = ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
    args = [[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]],
            [3], [12], [25], [15], [24], [8]]
    output = []
    topVotedCandidate = None
    for op, arg in zip(ops, args):
        if op == "TopVotedCandidate":
            topVotedCandidate = TopVotedCandidate(*arg)
            output.append(None)
        elif op == "q":
            output.append(topVotedCandidate.q(*arg))
    print("Example 1:")
    print("Input: ")
    print(ops)
    print(args)
    print("Output:", output)
print(__name__)
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)