class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        g = gcd(p, q)
        p //= g
        q //= g
        if p % 2 == 1 and q % 2 == 1:
            return 1
        elif p % 2 == 1 and q % 2 == 0:
            return 0
        else:
            return 2
if __name__ == "__main__":
    sol = Solution()
    print(sol.mirrorReflection(2, 1))
    print(sol.mirrorReflection(3, 1))
    print(sol.mirrorReflection(4, 2))
    print(sol.mirrorReflection(1, 1))
    print(sol.mirrorReflection(1000, 1))
print(__name__)