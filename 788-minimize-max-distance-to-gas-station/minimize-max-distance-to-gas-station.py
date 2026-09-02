class Solution(object):
    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """
        n = len(stations)
        gaps = [stations[i + 1] - stations[i] for i in range(n - 1)]
        def canAchieve(penalty):
            needed = 0
            for gap in gaps:
                needed += int(gap / penalty)
                if needed > k:
                    return False
            return True
        lo, hi = 0.0, max(gaps)
        while hi - lo > 1e-6:
            mid = (lo + hi) / 2
            if canAchieve(mid):
                hi = mid
            else:
                lo = mid
        return hi
if __name__ == "__main__":
    sol = Solution()
    stations, k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9
    print("Input: stations = {}, k = {}".format(stations, k))
    print("Output: {:.5f}".format(sol.minmaxGasDist(stations, k)))
    print("Expected: 0.50000\n")
    stations, k = [23, 24, 36, 39, 46, 56, 57, 65, 84, 98], 1
    print("Input: stations = {}, k = {}".format(stations, k))
    print("Output: {:.5f}".format(sol.minmaxGasDist(stations, k)))
    print("Expected: 14.00000\n")
print(__name__)