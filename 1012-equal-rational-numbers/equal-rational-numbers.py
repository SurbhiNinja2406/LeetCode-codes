from fractions import Fraction
import re
class Solution(object):
    def isRationalEqual(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self._toFraction(s) == self._toFraction(t)
    def _toFraction(self, s):
        match = re.match(r'^(\d+)(?:\.(\d*)(?:\((\d+)\))?)?$', s)
        integer_part, non_repeating, repeating = match.groups()
        non_repeating = non_repeating or ""
        repeating = repeating or ""
        n = len(non_repeating)
        r = len(repeating)
        A = int(integer_part + non_repeating) if (integer_part + non_repeating) else 0
        if r == 0:
            return Fraction(A, 10 ** n)
        else:
            B = int(integer_part + non_repeating + repeating)
            numerator = B - A
            denominator = 10 ** (n + r) - 10 ** n
            return Fraction(numerator, denominator)
if __name__ == "__main__":
    sol = Solution()
    print(sol.isRationalEqual("0.(52)", "0.5(25)"))  
    print(sol.isRationalEqual("0.1666(6)", "0.166(66)"))
    print(sol.isRationalEqual("0.9(9)", "1."))   
    print(sol.isRationalEqual("0.(0)", "0."))  
print(__name__)