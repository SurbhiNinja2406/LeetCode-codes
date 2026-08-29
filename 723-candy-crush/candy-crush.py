class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(board), len(board[0])
        while True:
            to_crush = set()
            for i in range(m):
                j = 0
                while j < n - 2:
                    val = board[i][j]
                    if val != 0 and val == board[i][j + 1] == board[i][j + 2]:
                        k = j
                        while k < n and board[i][k] == val:
                            to_crush.add((i, k))
                            k += 1
                        j = k
                    else:
                        j += 1
            for j in range(n):
                i = 0
                while i < m - 2:
                    val = board[i][j]
                    if val != 0 and val == board[i + 1][j] == board[i + 2][j]:
                        k = i
                        while k < m and board[k][j] == val:
                            to_crush.add((k, j))
                            k += 1
                        i = k
                    else:
                        i += 1
            if not to_crush:
                break
            for (i, j) in to_crush:
                board[i][j] = 0
            for j in range(n):
                write_row = m - 1
                for i in range(m - 1, -1, -1):
                    if board[i][j] != 0:
                        board[write_row][j] = board[i][j]
                        write_row -= 1
                for i in range(write_row, -1, -1):
                    board[i][j] = 0
        return board
if __name__ == "__main__":
    sol = Solution()
    board1 = [
        [110, 5, 112, 113, 114],
        [210, 211, 5, 213, 214],
        [310, 311, 3, 313, 314],
        [410, 411, 412, 5, 414],
        [5, 1, 512, 3, 3],
        [610, 4, 1, 613, 614],
        [710, 1, 2, 713, 714],
        [810, 1, 2, 1, 1],
        [1, 1, 2, 2, 2],
        [4, 1, 4, 4, 1014]
    ]
    result1 = sol.candyCrush(board1)
    expected1 = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [110, 0, 0, 0, 114],
        [210, 0, 0, 0, 214],
        [310, 0, 0, 113, 314],
        [410, 0, 0, 213, 414],
        [610, 211, 112, 313, 614],
        [710, 311, 412, 613, 714],
        [810, 411, 512, 713, 1014]
    ]
    print("Example 1 output:")
    for row in result1:
        print(row)
    print("Match:", result1 == expected1)
    print()

    # Example 2
    board2 = [
        [1, 3, 5, 5, 2],
        [3, 4, 3, 3, 1],
        [3, 2, 4, 5, 2],
        [2, 4, 4, 5, 5],
        [1, 4, 4, 1, 1]
    ]
    result2 = sol.candyCrush(board2)
    expected2 = [
        [1, 3, 0, 0, 0],
        [3, 4, 0, 5, 2],
        [3, 2, 0, 3, 1],
        [2, 4, 0, 5, 2],
        [1, 4, 3, 1, 1]
    ]
    print("Example 2 output:")
    for row in result2:
        print(row)
    print("Match:", result2 == expected2)
    print()
    board3 = [
        [1, 2, 3],
        [3, 1, 2],
        [2, 3, 1]
    ]
    import copy
    board3_copy = copy.deepcopy(board3)
    result3 = sol.candyCrush(board3_copy)
    print("Extra test (already stable):", result3)
    print("Should equal original:", result3 == board3)
print(__name__)