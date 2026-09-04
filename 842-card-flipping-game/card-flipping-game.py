class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        n = len(fronts)
        banned = set()
        for i in range(n):
            if fronts[i] == backs[i]:
                banned.add(fronts[i])
        best = float('inf')
        for i in range(n):
            if fronts[i] not in banned:
                best = min(best, fronts[i])
            if backs[i] not in banned:
                best = min(best, backs[i])
        return best if best != float('inf') else 0
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 4, 4, 7], [1, 3, 4, 1, 3], 2),
        ([1], [1], 0),
    ]
    for fronts, backs, expected in test_cases:
        result = solution.flipgame(list(fronts), list(backs))
        status = "PASS" if result == expected else "FAIL"
        print("fronts={:<20} backs={:<20} expected={} got={} [{}]".format(
            str(fronts), str(backs), expected, result, status))
print(__name__)