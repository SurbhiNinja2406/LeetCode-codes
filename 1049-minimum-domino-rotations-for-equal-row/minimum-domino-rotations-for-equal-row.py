class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        n = len(tops)
        def check(x):
            rotations_top = 0
            rotations_bottom = 0
            for i in range(n):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)
        result = check(tops[0])
        if result != -1:
            return result
        result = check(bottoms[0])
        return result if result != -1 else -1
if __name__ == "__main__":
    solution = Solution()
    tops1 = [2, 1, 2, 4, 2, 2]
    bottoms1 = [5, 2, 6, 2, 3, 2]
    result1 = solution.minDominoRotations(tops1, bottoms1)
    print("Example 1: tops={}, bottoms={}".format(tops1, bottoms1))
    print("Output: {}".format(result1))
    print("Expected: 2")
    print("")
    tops2 = [3, 5, 1, 2, 3]
    bottoms2 = [3, 6, 3, 3, 4]
    result2 = solution.minDominoRotations(tops2, bottoms2)
    print("Example 2: tops={}, bottoms={}".format(tops2, bottoms2))
    print("Output: {}".format(result2))
    print("Expected: -1")
    print("")
    tops3 = [1, 1, 1, 1]
    bottoms3 = [2, 2, 2, 2]
    result3 = solution.minDominoRotations(tops3, bottoms3)
    print("Example 3: tops={}, bottoms={}".format(tops3, bottoms3))
    print("Output: {}".format(result3))
    print("Expected: 0")
    print("")
    tops4 = [1, 2]
    bottoms4 = [2, 1]
    result4 = solution.minDominoRotations(tops4, bottoms4)
    print("Example 4: tops={}, bottoms={}".format(tops4, bottoms4))
    print("Output: {}".format(result4))
    print("Expected: 1")
print(__name__)