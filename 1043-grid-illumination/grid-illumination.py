from collections import defaultdict


class Solution(object):
    def gridIllumination(self, n, lamps, queries):
        """
        :type n: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        row_count = defaultdict(int)
        col_count = defaultdict(int)
        diag_count = defaultdict(int)       
        anti_diag_count = defaultdict(int) 
        lamp_positions = set()
        for row, col in lamps:
            if (row, col) not in lamp_positions:
                lamp_positions.add((row, col))
                row_count[row] += 1
                col_count[col] += 1
                diag_count[row - col] += 1
                anti_diag_count[row + col] += 1
        ans = []
        for row, col in queries:
            illuminated = (
                row_count[row] > 0 or
                col_count[col] > 0 or
                diag_count[row - col] > 0 or
                anti_diag_count[row + col] > 0
            )
            ans.append(1 if illuminated else 0)
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = row + dr, col + dc
                    if (nr, nc) in lamp_positions:
                        lamp_positions.remove((nr, nc))
                        row_count[nr] -= 1
                        col_count[nc] -= 1
                        diag_count[nr - nc] -= 1
                        anti_diag_count[nr + nc] -= 1
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.gridIllumination(5, [[0, 0], [4, 4]], [[1, 1], [1, 0]]))  
    print(sol.gridIllumination(5, [[0, 0], [4, 4]], [[1, 1], [1, 1]])) 
    print(sol.gridIllumination(5, [[0, 0], [0, 4]], [[0, 4], [0, 1], [1, 4]])) 
print(__name__)