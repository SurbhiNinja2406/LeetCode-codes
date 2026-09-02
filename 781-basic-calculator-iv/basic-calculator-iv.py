import collections
class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        """
        self.evalmap = dict(zip(evalvars, evalints))
        spaced = expression.replace('(', '( ').replace(')', ' )')
        self.tokens = spaced.split()
        self.pos = 0
        poly = self.parseExpression()
        return self.formatPoly(poly)
    def parseExpression(self):
        poly = self.parseTerm()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('+', '-'):
            op = self.tokens[self.pos]
            self.pos += 1
            term = self.parseTerm()
            if op == '-':
                term = self.negate(term)
            poly = self.add(poly, term)
        return poly
    def parseTerm(self):
        poly = self.parseFactor()
        while self.pos < len(self.tokens) and self.tokens[self.pos] == '*':
            self.pos += 1
            factor = self.parseFactor()
            poly = self.multiply(poly, factor)
        return poly
    def parseFactor(self):
        if self.tokens[self.pos] == '(':
            self.pos += 1  
            poly = self.parseExpression()
            self.pos += 1  
            return poly
        else:
            tok = self.tokens[self.pos]
            self.pos += 1
            return self.expand(tok)
    def expand(self, tok):
        if tok.isdigit():
            return {(): int(tok)}
        if tok in self.evalmap:
            return {(): self.evalmap[tok]}
        return {(tok,): 1}
    def negate(self, poly):
        return {k: -v for k, v in poly.items()}
    def add(self, p1, p2):
        result = dict(p1)
        for k, v in p2.items():
            result[k] = result.get(k, 0) + v
            if result[k] == 0:
                del result[k]
        return result
    def multiply(self, p1, p2):
        result = collections.defaultdict(int)
        for k1, v1 in p1.items():
            for k2, v2 in p2.items():
                key = tuple(sorted(k1 + k2))
                result[key] += v1 * v2
        return {k: v for k, v in result.items() if v != 0}
    def formatPoly(self, poly):
        items = [(k, v) for k, v in poly.items() if v != 0]
        items.sort(key=lambda x: (-len(x[0]), x[0]))
        result = []
        for k, v in items:
            if k:
                term = str(v) + '*' + '*'.join(k)
            else:
                term = str(v)
            result.append(term)
        return result
if __name__ == "__main__":
    sol = Solution()
    expression, evalvars, evalints = "e + 8 - a + 5", ["e"], [1]
    print("Input: expression = {}, evalvars = {}, evalints = {}".format(expression, evalvars, evalints))
    print("Output: {}".format(sol.basicCalculatorIV(expression, evalvars, evalints)))
    print("Expected: ['-1*a', '14']\n")
    expression, evalvars, evalints = "e - 8 + temperature - pressure", ["e", "temperature"], [1, 12]
    print("Input: expression = {}, evalvars = {}, evalints = {}".format(expression, evalvars, evalints))
    print("Output: {}".format(sol.basicCalculatorIV(expression, evalvars, evalints)))
    print("Expected: ['-1*pressure', '5']\n")
    expression, evalvars, evalints = "(e + 8) * (e - 8)", [], []
    print("Input: expression = {}, evalvars = {}, evalints = {}".format(expression, evalvars, evalints))
    print("Output: {}".format(sol.basicCalculatorIV(expression, evalvars, evalints)))
    print("Expected: ['1*e*e', '-64']\n")
print(__name__)