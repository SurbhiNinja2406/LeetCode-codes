class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        parent = list(range(26))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return
            if root_a < root_b:
                parent[root_b] = root_a
            else:
                parent[root_a] = root_b
        for c1, c2 in zip(s1, s2):
            union(ord(c1) - ord('a'), ord(c2) - ord('a'))
        result = []
        for ch in baseStr:
            root = find(ord(ch) - ord('a'))
            result.append(chr(root + ord('a')))
        return "".join(result)

if __name__ == "__main__":
    sol = Solution()
    print(sol.smallestEquivalentString("parker", "morris", "parser"))    
    print(sol.smallestEquivalentString("hello", "world", "hold"))      
    print(sol.smallestEquivalentString("leetcode", "programs", "sourcecode")) 
print(__name__)