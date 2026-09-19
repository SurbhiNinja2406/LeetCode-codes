class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        (x1, y1), (x2, y2), (x3, y3) = points
        cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
        return cross != 0
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([[1, 1], [2, 3], [3, 2]], True),
        ([[1, 1], [2, 2], [3, 3]], False),
        ([[1, 1], [1, 1], [2, 3]], False),  
        ([[1, 1], [1, 2], [1, 3]], False),  
    ]
    for points, expected in tests:
        result = sol.isBoomerang(points)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)