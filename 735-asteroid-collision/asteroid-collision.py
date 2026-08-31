class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            alive = True
            while alive and a < 0 and stack and stack[-1] > 0:
                top = stack[-1]
                if top < -a:
                    stack.pop()
                    continue
                elif top == -a:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(a)
        return stack
if __name__ == "__main__":
    sol = Solution()
    print(sol.asteroidCollision([5, 10, -5]))
    print(sol.asteroidCollision([8, -8]))
    print(sol.asteroidCollision([10, 2, -5]))
    print(sol.asteroidCollision([3, 5, -6, 2, -1, 4]))
print(__name__)