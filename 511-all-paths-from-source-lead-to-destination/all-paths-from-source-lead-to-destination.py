from collections import defaultdict
class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
        WHITE, GRAY, BLACK = 0, 1, 2   
        state = [WHITE] * n
        next_idx = [0] * n           
        stack = [source]
        state[source] = GRAY
        while stack:
            node = stack[-1]
            if not graph[node]:
                if node != destination:
                    return False
                state[node] = BLACK
                stack.pop()
                continue
            if next_idx[node] < len(graph[node]):
                nxt = graph[node][next_idx[node]]
                next_idx[node] += 1
                if state[nxt] == GRAY:
                    return False
                if state[nxt] == WHITE:
                    state[nxt] = GRAY
                    stack.append(nxt)
            else:
                state[node] = BLACK
                stack.pop()
        return True
if __name__ == "__main__":
    sol = Solution()
    print(sol.leadsToDestination(3, [[0, 1], [0, 2]], 0, 2))                
    print(sol.leadsToDestination(4, [[0, 1], [0, 3], [1, 2], [2, 1]], 0, 3))  
    print(sol.leadsToDestination(4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3)) 
    print(sol.leadsToDestination(1, [], 0, 0))                  
    print(sol.leadsToDestination(1, [[0, 0]], 0, 0))    
print(__name__)