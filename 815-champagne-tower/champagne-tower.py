class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        row = [float(poured)]
        for i in range(query_row):
            next_row = [0.0] * (i + 2)
            for j, amount in enumerate(row):
                if amount > 1.0:
                    overflow = (amount - 1.0) / 2.0
                    next_row[j] += overflow
                    next_row[j + 1] += overflow
            row = next_row
        return min(1.0, row[query_glass])
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (1, 1, 1, 0.00000),
        (2, 1, 1, 0.50000),
        (100000009, 33, 17, 1.00000),
    ]
    for poured, query_row, query_glass, expected in test_cases:
        result = solution.champagneTower(poured, query_row, query_glass)
        status = "PASS" if abs(result - expected) < 1e-5 else "FAIL"
        print("poured={:<12} row={:<3} glass={:<3} expected={:<10.5f} got={:<10.5f} [{}]".format(
            poured, query_row, query_glass, expected, result, status))
print(__name__)