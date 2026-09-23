class Solution(object):
    def minimumCost(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        parent = list(range(n + 1))  
        rank = [0] * (n + 1)
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False  
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            if rank[root_x] == rank[root_y]:
                rank[root_x] += 1
            return True
        connections.sort(key=lambda edge: edge[2])
        total_cost = 0
        edges_used = 0
        for x, y, cost in connections:
            if union(x, y):
                total_cost += cost
                edges_used += 1
                if edges_used == n - 1:
                    break  
        return total_cost if edges_used == n - 1 else -1
if __name__ == "__main__":
    sol = Solution()
    n1 = 3
    connections1 = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]
    print(sol.minimumCost(n1, connections1)) 
    n2 = 4
    connections2 = [[1, 2, 3], [3, 4, 4]]
    print(sol.minimumCost(n2, connections2))  
print(__name__)