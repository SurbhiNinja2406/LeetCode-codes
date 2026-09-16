class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        def get_powers(base, bound):
            powers = [1] 
            if base == 1:
                return powers  
            while powers[-1] * base <= bound:
                powers.append(powers[-1] * base)
            return powers
        x_powers = get_powers(x, bound)
        y_powers = get_powers(y, bound)
        result = set()
        for xi in x_powers:
            for yj in y_powers:
                total = xi + yj
                if total <= bound:
                    result.add(total)
        return list(result)
if __name__ == "__main__":
    sol = Solution()
    print(sorted(sol.powerfulIntegers(2, 3, 10)))  
    print(sorted(sol.powerfulIntegers(3, 5, 15)))  
    print(sorted(sol.powerfulIntegers(1, 1, 2)))  
print(__name__)