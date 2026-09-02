from collections import deque
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        start = "".join(str(num) for row in board for num in row)
        target = "123450"
        if start == target:
            return 0
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }
        visited = {start}
        queue = deque([(start, 0)])
        while queue:
            state, moves = queue.popleft()
            zero_pos = state.index('0')
            for neighbor_pos in neighbors[zero_pos]:
                new_state = list(state)
                new_state[zero_pos], new_state[neighbor_pos] = new_state[neighbor_pos], new_state[zero_pos]
                new_state = "".join(new_state)
                if new_state == target:
                    return moves + 1
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, moves + 1))
        return -1
if __name__ == "__main__":
    sol = Solution()
    board = [[1, 2, 3], [4, 0, 5]]
    print("Input: board = {}".format(board))
    print("Output: {}".format(sol.slidingPuzzle(board)))
    print("Expected: 1\n")
    board = [[1, 2, 3], [5, 4, 0]]
    print("Input: board = {}".format(board))
    print("Output: {}".format(sol.slidingPuzzle(board)))
    print("Expected: -1\n")
    board = [[4, 1, 2], [5, 0, 3]]
    print("Input: board = {}".format(board))
    print("Output: {}".format(sol.slidingPuzzle(board)))
    print("Expected: 5\n")
print(__name__)