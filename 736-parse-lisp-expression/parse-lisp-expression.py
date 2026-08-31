class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        def tokenize(s):
            tokens = []
            i, n = 0, len(s)
            while i < n:
                if s[i] == ' ':
                    i += 1
                    continue
                if s[i] == '(':
                    depth = 1
                    j = i + 1
                    while depth > 0:
                        if s[j] == '(':
                            depth += 1
                        elif s[j] == ')':
                            depth -= 1
                        j += 1
                    tokens.append(s[i:j])
                    i = j
                else:
                    j = i
                    while j < n and s[j] != ' ':
                        j += 1
                    tokens.append(s[i:j])
                    i = j
            return tokens
        def eval_expr(expr, scope):
            if expr[0] != '(':
                if expr[0] == '-' or expr[0].isdigit():
                    return int(expr)
                return scope[expr][-1]  
            inner = expr[1:-1]
            tokens = tokenize(inner)
            op = tokens[0]
            if op == 'add':
                return eval_expr(tokens[1], scope) + eval_expr(tokens[2], scope)
            if op == 'mult':
                return eval_expr(tokens[1], scope) * eval_expr(tokens[2], scope)
            if op == 'let':
                rest = tokens[1:]
                m = len(rest)
                added = [] 
                i = 0
                while i < m - 1:
                    var = rest[i]
                    val_expr = rest[i + 1]
                    val = eval_expr(val_expr, scope)
                    scope.setdefault(var, []).append(val)
                    added.append(var)
                    i += 2
                result = eval_expr(rest[-1], scope)
                for var in added:
                    scope[var].pop()
                return result
        return eval_expr(expression, {})
if __name__ == "__main__":
    sol = Solution()
    print(sol.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"))
    print(sol.evaluate("(let x 3 x 2 x)"))
    print(sol.evaluate("(let x 1 y 2 x (add x y) (add x y))"))
print(__name__)