import random
class Solution(object):
    def __init__(self, n, blacklist):
        """
        :type n: int
        :type blacklist: List[int]
        """
        self.M = n - len(blacklist)
        black_set = set(blacklist)
        self.remap = {}
        free_slots = []
        for i in range(self.M, n):
            if i not in black_set:
                free_slots.append(i)
        free_iter = iter(free_slots)
        for b in blacklist:
            if b < self.M:
                target = next(free_iter)
                self.remap[b] = target
    def pick(self):
        """
        :rtype: int
        """
        idx = random.randint(0, self.M - 1)
        return self.remap.get(idx, idx)
if __name__ == "__main__":
    random.seed(42)
    solution = Solution(7, [2, 3, 5])
    picks = [solution.pick() for _ in range(20)]
    print("Sample picks:", picks)
    print("All picks should only be from {0, 1, 4, 6}:",
          set(picks).issubset({0, 1, 4, 6}))
    from collections import Counter
    random.seed(0)
    solution2 = Solution(7, [2, 3, 5])
    counts = Counter(solution2.pick() for _ in range(40000))
    print("\nFrequency distribution over 40000 picks:")
    for val in sorted(counts):
        print("  {0}: {1}".format(val, counts[val]))
    print("\nEdge case: empty blacklist, n=5")
    solution3 = Solution(5, [])
    print([solution3.pick() for _ in range(10)])
    print("\nEdge case: n=1, blacklist=[]")
    solution4 = Solution(1, [])
    print([solution4.pick() for _ in range(5)])
print(__name__)
# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()