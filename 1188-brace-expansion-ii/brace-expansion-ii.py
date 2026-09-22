class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        self.expr = expression
        self.pos = 0
        result = self._parse_expr()
        return sorted(result)
    def _parse_expr(self):
        """
        Parses a comma-delimited list of terms (union of sets).
        expr -> term (',' term)*
        """
        sets = [self._parse_term()]        
        while self.pos < len(self.expr) and self.expr[self.pos] == ',':
            self.pos += 1  
            sets.append(self._parse_term())
        result = set()
        for s in sets:
            result |= s
        return result
    def _parse_term(self):
        """
        Parses a concatenation of factors (cartesian product of sets).
        term -> factor+
        Stops at ',', '}', or end of string.
        """
        factors = []        
        while self.pos < len(self.expr) and self.expr[self.pos] not in ',}':
            factors.append(self._parse_factor())
        result = {""}
        for factor_set in factors:
            new_result = set()
            for prefix in result:
                for word in factor_set:
                    new_result.add(prefix + word)
            result = new_result        
        return result
    def _parse_factor(self):
        """
        Parses a single factor: either a '{' expr '}' group or a single letter.
        factor -> '{' expr '}' | letter
        """
        if self.expr[self.pos] == '{':
            self.pos += 1 
            s = self._parse_expr()
            self.pos += 1 
            return s
        else:
            c = self.expr[self.pos]
            self.pos += 1
            return {c}
if __name__ == "__main__":
    solution = Solution()
    expression1 = "{a,b}{c,{d,e}}"
    result1 = solution.braceExpansionII(expression1)
    print("Example 1: {} (Expected: ['ac','ad','ae','bc','bd','be'])".format(result1))
    expression2 = "{{a,z},a{b,c},{ab,z}}"
    result2 = solution.braceExpansionII(expression2)
    print("Example 2: {} (Expected: ['a','ab','ac','z'])".format(result2))
print(__name__)