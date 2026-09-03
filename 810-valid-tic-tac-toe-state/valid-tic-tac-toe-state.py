class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        countX = sum(row.count('X') for row in board)
        countO = sum(row.count('O') for row in board)
        if countX != countO and countX != countO + 1:
            return False
        def wins(board, player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)):  
                    return True
                if all(board[j][i] == player for j in range(3)):  
                    return True
            if all(board[i][i] == player for i in range(3)):    
                return True
            if all(board[i][2 - i] == player for i in range(3)):  
                return True
            return False
        xWins = wins(board, 'X')
        oWins = wins(board, 'O')
        if xWins and oWins:
            return False
        if xWins and countX != countO + 1:
            return False
        if oWins and countX != countO:
            return False
        return True
if __name__ == "__main__":
    sol = Solution()
    print(sol.validTicTacToe(["O  ", "   ", "   "]))     
    print(sol.validTicTacToe(["XOX", " X ", "   "]))   
    print(sol.validTicTacToe(["XOX", "O O", "XOX"]))    
print(__name__)