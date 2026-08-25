class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        result = []
        if (numerator < 0) != (denominator < 0):
            result.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)
        integer_part = numerator // denominator
        result.append(str(integer_part))
        remainder = numerator % denominator
        if remainder == 0:
            return "".join(result)
        result.append(".")
        remainder_map = {}
        fractional_part = []
        while remainder != 0:
            if remainder in remainder_map:
                start = remainder_map[remainder]
                fractional_part.insert(start, "(")
                fractional_part.append(")")
                break
            remainder_map[remainder] = len(fractional_part)
            remainder *= 10
            fractional_part.append(str(remainder // denominator))
            remainder %= denominator
        result.append("".join(fractional_part))
        return "".join(result)
if __name__ == "__main__":
    sol = Solution()
    print(sol.fractionToDecimal(1, 2))    
    print(sol.fractionToDecimal(2, 1))    
    print(sol.fractionToDecimal(4, 333))  
print(__name__)