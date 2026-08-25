class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)
        queen_positions = [-1] * n
        def backtrack(row):
            if row == n:
                board = []
                for r in range(n):
                    row_str = ['.'] * n
                    row_str[queen_positions[r]] = 'Q'
                    board.append(''.join(row_str))
                result.append(board)
                return
            for c in range(n):
                d1 = row - c + n - 1
                d2 = row + c                
                if cols[c] or diag1[d1] or diag2[d2]:
                    continue
                cols[c] = diag1[d1] = diag2[d2] = True
                queen_positions[row] = c                
                backtrack(row + 1)
                cols[c] = diag1[d1] = diag2[d2] = False
                queen_positions[row] = -1        
        backtrack(0)
        return result
if __name__ == "__main__":
    solution = Solution()
    n1 = 4
    result1 = solution.solveNQueens(n1)
    for board in result1:
        print(board)
    print()
    n2 = 1
    result2 = solution.solveNQueens(n2)
    print(result2) 