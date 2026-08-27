class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        parent = [0] * (n + 1) 
        edge1 = None
        edge2 = None
        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                edge1 = [parent[v], v]
                edge2 = [u, v]         
                break
        uf_parent = list(range(n + 1))
        def find(x):
            if uf_parent[x] != x:
                uf_parent[x] = find(uf_parent[x])
            return uf_parent[x]
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False  
            uf_parent[root_x] = root_y
            return True
        for u, v in edges:
            if edge2 is not None and [u, v] == edge2:
                continue
            if not union(u, v):
                if edge1 is not None:
                    return edge1
                else:
                    return [u, v]
        return edge2
if __name__ == "__main__":
    solution = Solution()
    result1 = solution.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]])
    print("Example 1:")
    print("Input:  edges = [[1,2],[1,3],[2,3]]")
    print("Output:", result1)
    print("Expected: [2, 3]")
    print()
    result2 = solution.findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]])
    print("Example 2:")
    print("Input:  edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]")
    print("Output:", result2)
    print("Expected: [4, 1]")
    print()
    result3 = solution.findRedundantDirectedConnection([[4, 2], [1, 3], [1, 4], [2, 3]])
    print("Example 3 (extra):")
    print("Input:  edges = [[4,2],[1,3],[1,4],[2,3]]")
    print("Output:", result3)
    print("Expected: [2, 3]")
    print()
    result4 = solution.findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2], [1, 4]])
    print("Example 4 (extra):")
    print("Input:  edges = [[2,1],[3,1],[4,2],[1,4]]")
    print("Output:", result4)
    print("Expected: [3, 1]")
print(__name__)