from collections import deque


class Solution(object):
    def isEscapePossible(self, blocked, source, target):
        """
        :type blocked: List[List[int]]
        :type source: List[int]
        :type target: List[int]
        :rtype: bool
        """
        SIZE = 10 ** 6
        blocked_set = set(map(tuple, blocked))
        n = len(blocked)
        limit = n * (n - 1) // 2
        def bfs(start, end):
            start, end = tuple(start), tuple(end)
            seen = set([start])
            queue = deque([start])
            while queue:
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < SIZE and 0 <= ny < SIZE):
                        continue                
                    if (nx, ny) in blocked_set or (nx, ny) in seen:
                        continue
                    if (nx, ny) == end:
                        return True          
                    seen.add((nx, ny))
                    queue.append((nx, ny))
                if len(seen) > limit:
                    return True
            return False             
        return bfs(source, target) and bfs(target, source)
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[0, 1], [1, 0]], [0, 0], [0, 2], False),
        ([], [0, 0], [999999, 999999], True),
    ]
    for blocked, s, t, expected in tests:
        result = sol.isEscapePossible(blocked, s, t)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)