class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        cols = [False] * n
        diag1 = [False] * (2 * n - 1)
        diag2 = [False] * (2 * n - 1)        
        def backtrack(row):
            if row == n:
                self.count += 1
                return            
            for c in range(n):
                d1 = row - c + n - 1
                d2 = row + c
                if cols[c] or diag1[d1] or diag2[d2]:
                    continue
                cols[c] = diag1[d1] = diag2[d2] = True                
                backtrack(row + 1)
                cols[c] = diag1[d1] = diag2[d2] = False        
        backtrack(0)
        return self.count
if __name__ == "__main__":
    solution = Solution()
    n1 = 4
    print(solution.totalNQueens(n1))
    n2 = 1
    print(solution.totalNQueens(n2))  
print(__name__)