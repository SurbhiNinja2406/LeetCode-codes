from collections import defaultdict
class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        count = [1] * n
        answer = [0] * n
        def dfs_post_order(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs_post_order(child, node)
                    count[node] += count[child]
                    answer[0] += answer[child] + count[child]
        def dfs_pre_order(node, parent):
            for child in graph[node]:
                if child != parent:
                    answer[child] = answer[node] - count[child] + (n - count[child])
                    dfs_pre_order(child, node)        
        dfs_post_order(0, -1)
        dfs_pre_order(0, -1)
        return answer
if __name__ == "__main__":
    sol = Solution()
    print(sol.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))  
    print(sol.sumOfDistancesInTree(1, []))                              
    print(sol.sumOfDistancesInTree(2, [[1,0]]))                         
print(__name__)