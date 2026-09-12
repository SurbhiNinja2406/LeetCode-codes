class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        parent = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) 
            return parent[x]
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        for x, y in stones:
            row_id = ~x  
            col_id = y   
            if row_id not in parent:
                parent[row_id] = row_id
            if col_id not in parent:
                parent[col_id] = col_id
            union(row_id, col_id)
        num_components = len(set(find(node) for node in parent))
        return len(stones) - num_components
if __name__ == "__main__":
    sol = Solution()
    stones1 = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(sol.removeStones(stones1)) 
    stones2 = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    print(sol.removeStones(stones2))  
    stones3 = [[0, 0]]
    print(sol.removeStones(stones3))  
print(__name__)