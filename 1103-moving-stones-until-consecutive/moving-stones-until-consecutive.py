class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        x, y, z = sorted([a, b, c])
        max_moves = z - x - 2
        if z - x == 2:
            min_moves = 0                
        elif y - x <= 2 or z - y <= 2:
            min_moves = 1             
        else:
            min_moves = 2       
        return [min_moves, max_moves]
if __name__ == "__main__":
    sol = Solution()
    tests = [
        (1, 2, 5, [1, 2]),
        (4, 3, 2, [0, 0]),
        (3, 5, 1, [1, 2]),
    ]
    for a, b, c, expected in tests:
        result = sol.numMovesStones(a, b, c)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)