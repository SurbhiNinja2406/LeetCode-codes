from collections import deque, defaultdict


class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0
        stop_to_buses = defaultdict(list)
        for bus_idx, route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_idx)
        visited_buses = set()
        visited_stops = set()
        queue = deque()
        for bus_idx in stop_to_buses[source]:
            if bus_idx not in visited_buses:
                visited_buses.add(bus_idx)
                queue.append(bus_idx)
        visited_stops.add(source)
        bus_count = 1
        while queue:
            for _ in range(len(queue)):
                bus_idx = queue.popleft()
                for stop in routes[bus_idx]:
                    if stop == target:
                        return bus_count
                    if stop in visited_stops:
                        continue
                    visited_stops.add(stop)
                    for next_bus in stop_to_buses[stop]:
                        if next_bus not in visited_buses:
                            visited_buses.add(next_bus)
                            queue.append(next_bus)
            bus_count += 1
        return -1
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[1, 2, 7], [3, 6, 7]], 1, 6, 2),
        ([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12, -1),
    ]
    for routes, source, target, expected in test_cases:
        routes_copy = [list(r) for r in routes]
        result = solution.numBusesToDestination(routes_copy, source, target)
        status = "PASS" if result == expected else "FAIL"
        print("routes={:<45} source={} target={} expected={} got={} [{}]".format(
            str(routes), source, target, expected, result, status))
print(__name__)