class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs.sort(key=lambda x: x[0] - x[1])
        n = len(costs) // 2
        total = 0
        for i in range(n):
            total += costs[i][0]
            total += costs[i + n][1]
        return total
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[10, 20], [30, 200], [400, 50], [30, 20]], 110),
        ([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]], 1859),
        ([[515, 563], [451, 713], [537, 709], [343, 819],
          [855, 779], [457, 60], [650, 359], [631, 42]], 3086),
    ]
    for costs, expected in tests:
        result = sol.twoCitySchedCost(costs)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)