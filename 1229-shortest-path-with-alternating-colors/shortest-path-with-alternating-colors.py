from collections import deque, defaultdict
class Solution(object):
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        """
        :type n: int
        :type redEdges: List[List[int]]
        :type blueEdges: List[List[int]]
        :rtype: List[int]
        """
        red_adj = defaultdict(list)
        blue_adj = defaultdict(list)        
        for a, b in redEdges:
            red_adj[a].append(b)        
        for u, v in blueEdges:
            blue_adj[u].append(v)
        visited = [[False, False] for _ in range(n)]
        answer = [-1] * n
        answer[0] = 0
        queue = deque()
        queue.append((0, 0)) 
        queue.append((0, 1))
        visited[0][0] = True
        visited[0][1] = True        
        steps = 0        
        while queue:
            steps += 1
            for _ in range(len(queue)):
                node, last_color = queue.popleft()
                if last_color == 0:
                    for neighbor in blue_adj[node]:
                        if not visited[neighbor][1]:
                            visited[neighbor][1] = True
                            if answer[neighbor] == -1:
                                answer[neighbor] = steps
                            queue.append((neighbor, 1))
                else:
                    for neighbor in red_adj[node]:
                        if not visited[neighbor][0]:
                            visited[neighbor][0] = True
                            if answer[neighbor] == -1:
                                answer[neighbor] = steps
                            queue.append((neighbor, 0))        
        return answer
if __name__ == "__main__":
    sol = Solution()
    n1, redEdges1, blueEdges1 = 3, [[0, 1], [1, 2]], []
    print("Input: n =", n1, ", redEdges =", redEdges1, ", blueEdges =", blueEdges1)
    print("Output:", sol.shortestAlternatingPaths(n1, redEdges1, blueEdges1)) 
    n2, redEdges2, blueEdges2 = 3, [[0, 1]], [[2, 1]]
    print("\nInput: n =", n2, ", redEdges =", redEdges2, ", blueEdges =", blueEdges2)
    print("Output:", sol.shortestAlternatingPaths(n2, redEdges2, blueEdges2)) 
print(__name__)