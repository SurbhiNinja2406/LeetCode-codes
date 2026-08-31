from collections import Counter
class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        n = len(formula)
        def parse_name(i):
            start = i
            i += 1
            while i < n and formula[i].islower():
                i += 1
            return formula[start:i], i
        def parse_count(i):
            start = i
            while i < n and formula[i].isdigit():
                i += 1
            if start == i:
                return 1, i
            return int(formula[start:i]), i
        def parse(i):
            stack = [Counter()]
            while i < n:
                if formula[i] == '(':
                    stack.append(Counter())
                    i += 1
                elif formula[i] == ')':
                    i += 1
                    count, i = parse_count(i)
                    top = stack.pop()
                    for atom, c in top.items():
                        stack[-1][atom] += c * count
                else:
                    name, i = parse_name(i)
                    count, i = parse_count(i)
                    stack[-1][name] += count
            return stack[0], i
        counts, _ = parse(0)
        result = []
        for atom in sorted(counts.keys()):
            result.append(atom)
            if counts[atom] > 1:
                result.append(str(counts[atom]))
        return "".join(result)
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("H2O", "H2O"),
        ("Mg(OH)2", "H2MgO2"),
        ("K4(ON(SO3)2)2", "K4N2O14S4"),
        ("H2O2", "H2O2"),
        ("H2O2He3Mg4", "H2He3Mg4O2"),
    ]
    for i, (formula, expected) in enumerate(test_cases, 1):
        result = solution.countOfAtoms(formula)
        status = "PASS" if result == expected else "FAIL"
        print("Test %d: [%s]" % (i, status))
        print("  Input:    formula = \"%s\"" % formula)
        print("  Output:   \"%s\"" % result)
        print("  Expected: \"%s\"" % expected)
        print("")
print(__name__)