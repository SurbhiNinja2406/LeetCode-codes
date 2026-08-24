class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        result = []
        for i in range(len(values)):
            while num >= values[i]:
                result.append(symbols[i])
                num -= values[i]
        return ''.join(result)
if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(3749))  
    print(sol.intToRoman(58))  
    print(sol.intToRoman(1994)) 
    print(sol.intToRoman(1))  
    print(sol.intToRoman(3999)) 
    print(sol.intToRoman(3000))  
    print(sol.intToRoman(900))  
    print(sol.intToRoman(400))  
    print(sol.intToRoman(444))
print(__name__)