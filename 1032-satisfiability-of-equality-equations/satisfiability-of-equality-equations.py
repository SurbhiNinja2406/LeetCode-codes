class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        parent = list(range(26))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        for eq in equations:
            if eq[1] == '=':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                union(a, b)
        for eq in equations:
            if eq[1] == '!':
                a = ord(eq[0]) - ord('a')
                b = ord(eq[3]) - ord('a')
                if find(a) == find(b):
                    return False
        return True
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        (["a==b", "b!=a"], False),
        (["b==a", "a==b"], True),
        (["a==b", "b==c", "a==c"], True),
        (["a==b", "b!=c", "c==a"], False),
        (["c==c", "b==d", "x!=z"], True),
    ]
    for equations, expected in test_cases:
        result = sol.equationsPossible(equations)
        status = "PASS" if result == expected else "FAIL"
        print("equations={0} -> {1} (expected {2}) [{3}]".format(
            equations, result, expected, status
        ))
print(__name__)