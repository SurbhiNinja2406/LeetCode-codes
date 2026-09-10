from collections import deque


class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        MOUSE_TURN, CAT_TURN = 0, 1
        color = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        for mouse in range(n):
            for cat in range(n):
                degree[mouse][cat][MOUSE_TURN] = len(graph[mouse])
                degree[mouse][cat][CAT_TURN] = len(graph[cat])
                if 0 in graph[cat]:
                    degree[mouse][cat][CAT_TURN] -= 1
        queue = deque()
        for cat in range(1, n):
            for turn in range(2):
                color[0][cat][turn] = MOUSE_WIN
                queue.append((0, cat, turn, MOUSE_WIN))
            for mouse in range(n):
                for turn in range(2):
                    if mouse == cat:
                        color[mouse][cat][turn] = CAT_WIN
                        queue.append((mouse, cat, turn, CAT_WIN))
        def get_prev_states(mouse, cat, turn):
            prev_turn = 1 - turn
            result = []
            if prev_turn == MOUSE_TURN:
                for prev_mouse in graph[mouse]:
                    result.append((prev_mouse, cat, prev_turn))
            else:
                for prev_cat in graph[cat]:
                    if prev_cat != 0:
                        result.append((mouse, prev_cat, prev_turn))
            return result
        while queue:
            mouse, cat, turn, result = queue.popleft()
            for prev_mouse, prev_cat, prev_turn in get_prev_states(mouse, cat, turn):
                if color[prev_mouse][prev_cat][prev_turn] != DRAW:
                    continue
                if (prev_turn == MOUSE_TURN and result == MOUSE_WIN) or \
                   (prev_turn == CAT_TURN and result == CAT_WIN):
                    color[prev_mouse][prev_cat][prev_turn] = result
                    queue.append((prev_mouse, prev_cat, prev_turn, result))
                else:
                    degree[prev_mouse][prev_cat][prev_turn] -= 1
                    if degree[prev_mouse][prev_cat][prev_turn] == 0:
                        color[prev_mouse][prev_cat][prev_turn] = result
                        queue.append((prev_mouse, prev_cat, prev_turn, result))
        return color[1][2][MOUSE_TURN]
if __name__ == "__main__":
    solution = Solution()
    graph1 = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
    print("Example 1:")
    print("Input: graph =", graph1)
    print("Output:", solution.catMouseGame(graph1))
    print()
    graph2 = [[1, 3], [0], [3], [0, 2]]
    print("Example 2:")
    print("Input: graph =", graph2)
    print("Output:", solution.catMouseGame(graph2))
print(__name__)