# Definition for a binary tree node.
from collections import deque, defaultdict
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        graph = defaultdict(list)   
        leaves = set()           
        start = [None]         
        def dfs(node, parent):
            if not node:
                return
            if node.val == k:
                start[0] = node
            if parent is not None:
                graph[node].append(parent)
                graph[parent].append(node)
            if not node.left and not node.right:
                leaves.add(node)
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        start_node = start[0]
        if start_node in leaves:
            return start_node.val
        visited = {start_node}
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            if node in leaves:
                return node.val
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return -1  
if __name__ == "__main__":
    sol = Solution()
    n1 = TreeNode(1, TreeNode(3), TreeNode(2))
    print(sol.findClosestLeaf(n1, 1))  
    n2 = TreeNode(1)
    print(sol.findClosestLeaf(n2, 1))  
    six = TreeNode(6)
    five = TreeNode(5, six, None)
    four = TreeNode(4, five, None)
    two = TreeNode(2, four, None)
    three = TreeNode(3)
    one = TreeNode(1, two, three)
    print(sol.findClosestLeaf(one, 2)) 
print(__name__)