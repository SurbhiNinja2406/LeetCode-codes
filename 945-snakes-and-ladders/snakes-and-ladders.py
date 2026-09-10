from collections import deque
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        def get_position(square):
            quot, rem = divmod(square - 1, n)
            row = n - 1 - quot
            if quot % 2 == 0:
                col = rem
            else:
                col = n - 1 - rem
            return row, col
        visited = [False] * (n * n + 1)
        visited[1] = True
        queue = deque([(1, 0)]) 
        while queue:
            square, moves = queue.popleft()
            if square == n * n:
                return moves
            for next_square in range(square + 1, min(square + 6, n * n) + 1):
                row, col = get_position(next_square)
                dest = board[row][col]
                actual = dest if dest != -1 else next_square
                if not visited[actual]:
                    visited[actual] = True
                    queue.append((actual, moves + 1))
        return -1
if __name__ == "__main__":
    solution = Solution()
    board1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    print("Example 1:")
    print("Input: board =", board1)
    print("Output:", solution.snakesAndLadders(board1))
    print()
    board2 = [[-1, -1], [-1, 3]]
    print("Example 2:")
    print("Input: board =", board2)
    print("Output:", solution.snakesAndLadders(board2))
print(__name__)