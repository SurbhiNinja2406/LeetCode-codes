class Solution(object):
    def earliestAcq(self, logs, n):
        """
        :type logs: List[List[int]]
        :type n: int
        :rtype: int
        """
        parent = list(range(n))
        rank = [0] * n
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  
                x = parent[x]
            return x
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return False  
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
            return True
        logs.sort(key=lambda log: log[0])
        num_groups = n
        for timestamp, x, y in logs:
            if union(x, y):
                num_groups -= 1
                if num_groups == 1:
                    return timestamp
        return -1
if __name__ == "__main__":
    sol = Solution()
    logs1 = [[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3],
             [20190211, 1, 5], [20190224, 2, 4], [20190301, 0, 3],
             [20190312, 1, 2], [20190322, 4, 5]]
    n1 = 6
    print(sol.earliestAcq(logs1, n1))  
    logs2 = [[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]]
    n2 = 4
    print(sol.earliestAcq(logs2, n2)) 
print(__name__)