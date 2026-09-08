class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacle_set = set()
        for x, y in obstacles:
            obstacle_set.add((x, y))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0
        x, y = 0, 0
        max_dist_squared = 0        
        for command in commands:
            if command == -2:
                dir_index = (dir_index - 1) % 4
            elif command == -1:
                dir_index = (dir_index + 1) % 4
            else:
                dx, dy = directions[dir_index]
                for _ in range(command):
                    next_x = x + dx
                    next_y = y + dy
                    if (next_x, next_y) in obstacle_set:
                        break
                    x, y = next_x, next_y
                    max_dist_squared = max(max_dist_squared, x * x + y * y)        
        return max_dist_squared
if __name__ == "__main__":
    sol = Solution()
    commands1, obstacles1 = [4, -1, 3], []
    result1 = sol.robotSim(commands1, obstacles1)
    print("Example 1:")
    print("Input: commands = {}, obstacles = {}".format(commands1, obstacles1))
    print("Output:", result1)
    print("Expected: 25")
    print()
    commands2, obstacles2 = [4, -1, 4, -2, 4], [[2, 4]]
    result2 = sol.robotSim(commands2, obstacles2)
    print("Example 2:")
    print("Input: commands = {}, obstacles = {}".format(commands2, obstacles2))
    print("Output:", result2)
    print("Expected: 65")
    print()
    commands3, obstacles3 = [6, -1, -1, 6], [[0, 0]]
    result3 = sol.robotSim(commands3, obstacles3)
    print("Example 3:")
    print("Input: commands = {}, obstacles = {}".format(commands3, obstacles3))
    print("Output:", result3)
    print("Expected: 36")
    print()
    commands4, obstacles4 = [-1, -1, -2, -2], []
    result4 = sol.robotSim(commands4, obstacles4)
    print("Additional test (only turns, no movement):")
    print("Input: commands = {}, obstacles = {}".format(commands4, obstacles4))
    print("Output:", result4)
    print("Expected: 0")
print(__name__)