class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        d = 0 
        for ch in instructions:
            if ch == 'G':
                x += dirs[d][0]
                y += dirs[d][1]
            elif ch == 'L':
                d = (d + 3) % 4      
            else:  
                d = (d + 1) % 4      
        return (x == 0 and y == 0) or d != 0
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("GGLLGG", True),
        ("GG", False),
        ("GL", True),
        ("GGRGGRGGRGGR", True),  
    ]
    for instructions, expected in tests:
        result = sol.isRobotBounded(instructions)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)