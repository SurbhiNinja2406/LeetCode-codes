class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: List[int]
        """
        n, m = len(workers), len(bikes)
        MAX_DIST = 2000
        buckets = [[] for _ in range(MAX_DIST)]
        for i in range(n):
            wx, wy = workers[i]
            for j in range(m):
                bx, by = bikes[j]
                dist = abs(wx - bx) + abs(wy - by)
                buckets[dist].append((i, j))
        answer = [-1] * n
        bike_taken = [False] * m
        assigned = 0
        for dist in range(MAX_DIST):
            for i, j in buckets[dist]:
                if answer[i] == -1 and not bike_taken[j]:
                    answer[i] = j
                    bike_taken[j] = True
                    assigned += 1
                    if assigned == n:
                        return answer
        return answer
if __name__ == "__main__":
    sol = Solution()
    print(sol.assignBikes([[0, 0], [2, 1]],
                          [[1, 2], [3, 3]]))            
    print(sol.assignBikes([[0, 0], [1, 1], [2, 0]],
                          [[1, 0], [2, 2], [2, 1]]))      
print(__name__)