# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        visited = {}        
        def dfs(original):
            if original in visited:
                return visited[original]
            clone = Node(original.val)
            visited[original] = clone
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))            
            return clone        
        return dfs(node)
def build_graph(adjList):
    if not adjList:
        return None    
    nodes = [Node(i + 1) for i in range(len(adjList))]    
    for i, neighbors in enumerate(adjList):
        for n in neighbors:
            nodes[i].neighbors.append(nodes[n - 1])    
    return nodes[0] if nodes else None
def graph_to_adjList(node):
    if not node:
        return []    
    visited = {}    
    def dfs(n):
        if n.val in visited:
            return
        visited[n.val] = sorted(neighbor.val for neighbor in n.neighbors)
        for neighbor in n.neighbors:
            dfs(neighbor)    
    dfs(node)    
    return [visited[i + 1] for i in range(len(visited))]
if __name__ == "__main__":
    sol = Solution()
    adjList1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    graph1 = build_graph(adjList1)
    cloned1 = sol.cloneGraph(graph1)
    print(graph_to_adjList(cloned1))  
    adjList2 = [[]]
    graph2 = build_graph(adjList2)
    cloned2 = sol.cloneGraph(graph2)
    print(graph_to_adjList(cloned2)) 
    adjList3 = []
    graph3 = build_graph(adjList3)
    cloned3 = sol.cloneGraph(graph3)
    print(graph_to_adjList(cloned3))
print(__name__)