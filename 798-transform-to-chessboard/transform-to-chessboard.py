class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1
        row_sum = sum(board[0])
        col_sum = sum(board[i][0] for i in range(n))
        if not (n // 2 <= row_sum <= (n + 1) // 2):
            return -1
        if not (n // 2 <= col_sum <= (n + 1) // 2):
            return -1
        col_mismatch = sum(1 for i in range(n) if board[0][i] == i % 2)
        row_mismatch = sum(1 for i in range(n) if board[i][0] == i % 2)
        if n % 2 == 1:
            if col_mismatch % 2 == 1:
                col_mismatch = n - col_mismatch
            if row_mismatch % 2 == 1:
                row_mismatch = n - row_mismatch
        else:
            col_mismatch = min(col_mismatch, n - col_mismatch)
            row_mismatch = min(row_mismatch, n - row_mismatch)
        return (col_mismatch + row_mismatch) // 2
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]], 2),
        ([[0, 1], [1, 0]], 0),
        ([[1, 0], [1, 0]], -1),
    ]
    for i, (board, expected) in enumerate(test_cases, 1):
        result = sol.movesToChessboard(board)
        status = "PASS" if result == expected else "FAIL"
        print("Test " + str(i) + ": board=" + str(board) +
              " -> got=" + str(result) + ", expected=" + str(expected) +
              " [" + status + "]")
print(__name__)