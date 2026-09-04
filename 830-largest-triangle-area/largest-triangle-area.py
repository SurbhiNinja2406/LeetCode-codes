class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(points)
        max_area = 0.0
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    area = 0.5 * abs(
                        x1 * (y2 - y3) +
                        x2 * (y3 - y1) +
                        x3 * (y1 - y2)
                    )
                    if area > max_area:
                        max_area = area
        return max_area
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]], 2.00000),
        ([[1, 0], [0, 0], [0, 1]], 0.50000),
    ]
    for points, expected in test_cases:
        result = solution.largestTriangleArea([list(p) for p in points])
        status = "PASS" if abs(result - expected) < 1e-5 else "FAIL"
        print("points={:<45} expected={:<10.5f} got={:<10.5f} [{}]".format(
            str(points), expected, result, status))
print(__name__)