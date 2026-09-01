from collections import defaultdict


class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        pair_count = defaultdict(int)
        total = 0
        for row in grid:
            ones = [c for c in range(n) if row[c] == 1]
            length = len(ones)
            for i in range(length):
                for j in range(i + 1, length):
                    key = (ones[i], ones[j])
                    total += pair_count[key]
                    pair_count[key] += 1
        return total
if __name__ == "__main__":
    solution = Solution()
    grid1 = [
        [1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ]
    result1 = solution.countCornerRectangles(grid1)
    print("Example 1: Output = {0}, Expected = 1".format(result1))
    assert result1 == 1
    grid2 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    result2 = solution.countCornerRectangles(grid2)
    print("Example 2: Output = {0}, Expected = 9".format(result2))
    assert result2 == 9
    grid3 = [[1, 1, 1, 1]]
    result3 = solution.countCornerRectangles(grid3)
    print("Example 3: Output = {0}, Expected = 0".format(result3))
    assert result3 == 0
    print("\nAll test cases passed!")
print(__name__)