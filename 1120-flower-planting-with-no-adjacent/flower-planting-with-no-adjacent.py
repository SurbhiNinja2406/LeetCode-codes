class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n + 1)]
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        answer = [0] * (n + 1)  
        for garden in range(1, n + 1):
            used = set(answer[nb] for nb in graph[garden])
            for flower in range(1, 5):
                if flower not in used:
                    answer[garden] = flower
                    break
        return answer[1:]
if __name__ == "__main__":
    sol = Solution()
    def is_valid(n, paths, answer):
        if len(answer) != n:
            return False
        if any(f not in (1, 2, 3, 4) for f in answer):
            return False
        return all(answer[x - 1] != answer[y - 1] for x, y in paths)
    tests = [
        (3, [[1, 2], [2, 3], [3, 1]]),
        (4, [[1, 2], [3, 4]]),
        (4, [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]),
        (1, []),
    ]
    for n, paths in tests:
        result = sol.gardenNoAdj(n, paths)
        status = "PASS" if is_valid(n, paths, result) else "FAIL"
        print("{}: got {}".format(status, result))
print(__name__)