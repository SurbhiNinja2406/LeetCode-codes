class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)        
        def backtrack(index):
            if index == len(empty_cells):
                return True
            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)            
            for num in "123456789":
                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    continue
                board[r][c] = num
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)                
                if backtrack(index + 1):
                    return True
                board[r][c] = '.'
                rows[r].remove(num)
                cols[c].remove(num)
                boxes[box_index].remove(num)            
            return False        
        backtrack(0)
def print_board(board):
    for row in board:
        print(" ".join(row))
if __name__ == "__main__":
    solution = Solution()    
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]    
    solution.solveSudoku(board)
    print_board(board)
print(__name__)