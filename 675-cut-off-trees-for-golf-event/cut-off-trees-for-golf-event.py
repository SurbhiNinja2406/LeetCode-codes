from collections import deque
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        if not forest or not forest[0]:
            return -1
        m, n = len(forest), len(forest[0])
        trees = []
        for r in range(m):
            for c in range(n):
                if forest[r][c] > 1:
                    trees.append((forest[r][c], r, c))
        trees.sort()
        def bfs(start_r, start_c, target_r, target_c):
            """
            Standard BFS shortest path on the grid from (start_r, start_c)
            to (target_r, target_c), where forest[r][c] == 0 is blocked.
            Returns the minimum number of steps, or -1 if unreachable.
            """
            if start_r == target_r and start_c == target_c:
                return 0
            visited = [[False] * n for _ in range(m)]
            visited[start_r][start_c] = True
            queue = deque([(start_r, start_c, 0)])
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue:
                r, c, steps = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n
                            and not visited[nr][nc]
                            and forest[nr][nc] != 0):
                        if nr == target_r and nc == target_c:
                            return steps + 1
                        visited[nr][nc] = True
                        queue.append((nr, nc, steps + 1))
            return -1
        total_steps = 0
        cur_r, cur_c = 0, 0
        for height, tr, tc in trees:
            dist = bfs(cur_r, cur_c, tr, tc)
            if dist == -1:
                return -1  
            total_steps += dist
            cur_r, cur_c = tr, tc
        return total_steps
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]])
    print("Example 1:")
    print("Input:  forest = [[1,2,3],[0,0,4],[7,6,5]]")
    print("Output:", result1)
    print("Expected: 6")
    print()
    result2 = solution.cutOffTree([[1, 2, 3], [0, 0, 0], [7, 6, 5]])
    print("Example 2:")
    print("Input:  forest = [[1,2,3],[0,0,0],[7,6,5]]")
    print("Output:", result2)
    print("Expected: -1")
    print()
    result3 = solution.cutOffTree([[2, 3, 4], [0, 0, 5], [8, 7, 6]])
    print("Example 3:")
    print("Input:  forest = [[2,3,4],[0,0,5],[8,7,6]]")
    print("Output:", result3)
    print("Expected: 6")
    print()
    result4 = solution.cutOffTree([[1]])
    print("Example 4 (extra):")
    print("Input:  forest = [[1]]")
    print("Output:", result4)
    print("Expected: 0")
    print()
    result5 = solution.cutOffTree([[2, 3, 4]])
    print("Example 5 (extra):")
    print("Input:  forest = [[2,3,4]]")
    print("Output:", result5)
    print("Expected: 3")
print(__name__)