class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    if ty == 0:
                        return False
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    if tx == 0:
                        return False
                    return (ty - sy) % tx == 0
        return False
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (1, 1, 3, 5, True),
        (1, 1, 2, 2, False),
        (1, 1, 1, 1, True),
        (1, 1, 1000000000, 1, True),
        (3, 5, 1, 1, False),
        (2, 3, 5, 3, True),
    ]
    for i, (sx, sy, tx, ty, expected) in enumerate(test_cases, 1):
        result = sol.reachingPoints(sx, sy, tx, ty)
        status = "PASS" if result == expected else "FAIL"
        print("Test " + str(i) + ": sx=" + str(sx) + ", sy=" + str(sy) +
              ", tx=" + str(tx) + ", ty=" + str(ty) +
              " -> got=" + str(result) + ", expected=" + str(expected) +
              " [" + status + "]")
print(__name__)