class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s
        self.n = len(s)
        self.i = 0
        return self.parseExpression()
    def parseExpression(self):
        result = self.parseTerm()
        while self.i < self.n:
            self.skipSpaces()
            if self.i < self.n and self.s[self.i] in '+-':
                op = self.s[self.i]
                self.i += 1
                term = self.parseTerm()
                result = result + term if op == '+' else result - term
            else:
                break
        return result
    def parseTerm(self):
        result = self.parseFactor()
        while self.i < self.n:
            self.skipSpaces()
            if self.i < self.n and self.s[self.i] in '*/':
                op = self.s[self.i]
                self.i += 1
                factor = self.parseFactor()
                if op == '*':
                    result = result * factor
                else:
                    result = self.truncDivide(result, factor)
            else:
                break
        return result
    def parseFactor(self):
        self.skipSpaces()
        if self.i < self.n and self.s[self.i] == '(':
            self.i += 1
            result = self.parseExpression()
            self.skipSpaces()
            self.i += 1 
            return result
        else:
            return self.parseNumber()
    def parseNumber(self):
        self.skipSpaces()
        start = self.i
        while self.i < self.n and self.s[self.i].isdigit():
            self.i += 1
        return int(self.s[start:self.i])
    def skipSpaces(self):
        while self.i < self.n and self.s[self.i] == ' ':
            self.i += 1
    def truncDivide(self, a, b):
        quotient = abs(a) // abs(b)
        if (a < 0) != (b < 0):
            quotient = -quotient
        return quotient
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ("1+1", 2),
        ("6-4/2", 4),
        ("2*(5+5*2)/3+(6/2+8)", 21),
        ("(0-3)/4", 0),
        ("0-2147483647", -2147483647),
    ]
    for s, expected in tests:
        result = sol.calculate(s)
        status = "PASS" if result == expected else "FAIL"
        print("Input: s = {}".format(s))
        print("Output: {}  Expected: {}  [{}]\n".format(result, expected, status))
print(__name__)