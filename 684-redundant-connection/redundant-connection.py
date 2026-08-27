class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            return True
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        return []
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]])
    print("Example 1:")
    print("Input:  edges = [[1,2],[1,3],[2,3]]")
    print("Output:", result1)
    print("Expected: [2, 3]")
    print()
    result2 = solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
    print("Example 2:")
    print("Input:  edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]")
    print("Output:", result2)
    print("Expected: [1, 4]")
    print()
    result3 = solution.findRedundantConnection([[1, 2], [2, 3], [1, 3]])
    print("Example 3 (extra):")
    print("Input:  edges = [[1,2],[2,3],[1,3]]")
    print("Output:", result3)
    print("Expected: [1, 3]")
    print()
    result4 = solution.findRedundantConnection([[1, 4], [3, 4], [1, 3], [1, 2], [4, 5]])
    print("Example 4 (extra):")
    print("Input:  edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]")
    print("Output:", result4)
print(__name__)