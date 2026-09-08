class Solution(object):
    def nthMagicalNumber(self, n, a, b):
        """
        :type n: int
        :type a: int
        :type b: int
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        lcm = a * b // gcd(a, b)
        lo, hi = 1, n * min(a, b)
        while lo < hi:
            mid = (lo + hi) // 2
            count = mid // a + mid // b - mid // lcm
            if count < n:
                lo = mid + 1
            else:
                hi = mid
        return lo % MOD
def build_solution_and_test(n, a, b):
    solution = Solution()
    result = solution.nthMagicalNumber(n, a, b)
    print("Input:  n = {}, a = {}, b = {}".format(n, a, b))
    print("Output: {}".format(result))
    print("")
if __name__ == "__main__":
    build_solution_and_test(1, 2, 3)   
    build_solution_and_test(4, 2, 3)  
    build_solution_and_test(1, 40000, 40000) 
print(__name__)