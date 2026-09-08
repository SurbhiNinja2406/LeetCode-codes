import heapq
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        max_heap = []        
        current_fuel = startFuel
        stops = 0
        i = 0
        n = len(stations)
        while current_fuel < target:
            while i < n and stations[i][0] <= current_fuel:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1
            if not max_heap:
                return -1
            current_fuel += -heapq.heappop(max_heap)
            stops += 1
        return stops
if __name__ == "__main__":
    sol = Solution()
    target1, startFuel1, stations1 = 1, 1, []
    result1 = sol.minRefuelStops(target1, startFuel1, stations1)
    print("Example 1:")
    print("Input: target = {}, startFuel = {}, stations = {}".format(target1, startFuel1, stations1))
    print("Output:", result1)
    print("Expected: 0")
    print()
    target2, startFuel2, stations2 = 100, 1, [[10, 100]]
    result2 = sol.minRefuelStops(target2, startFuel2, stations2)
    print("Example 2:")
    print("Input: target = {}, startFuel = {}, stations = {}".format(target2, startFuel2, stations2))
    print("Output:", result2)
    print("Expected: -1")
    print()
    target3, startFuel3, stations3 = 100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]
    result3 = sol.minRefuelStops(target3, startFuel3, stations3)
    print("Example 3:")
    print("Input: target = {}, startFuel = {}, stations = {}".format(target3, startFuel3, stations3))
    print("Output:", result3)
    print("Expected: 2")
    print()
    target4, startFuel4, stations4 = 50, 50, []
    result4 = sol.minRefuelStops(target4, startFuel4, stations4)
    print("Additional test (exact reach, no stations needed):")
    print("Input: target = {}, startFuel = {}, stations = {}".format(target4, startFuel4, stations4))
    print("Output:", result4)
    print("Expected: 0")
print(__name__)