class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        cells = [[r, c] for r in range(rows) for c in range(cols)]
        cells.sort(key=lambda cell: abs(cell[0] - rCenter) + abs(cell[1] - cCenter))
        return cells
if __name__ == "__main__":
    sol = Solution()
    tests = [
        (1, 2, 0, 0, [0, 1]),
        (2, 2, 0, 1, [0, 1, 1, 2]),
        (2, 3, 1, 2, [0, 1, 1, 2, 2, 3]),
    ]
    for rows, cols, rc, cc, expected in tests:
        result = sol.allCellsDistOrder(rows, cols, rc, cc)
        dists = [abs(r - rc) + abs(c - cc) for r, c in result]
        status = "PASS" if dists == expected else "FAIL"
        print("{}: cells {}, distances {}".format(status, result, dists))
print(__name__)