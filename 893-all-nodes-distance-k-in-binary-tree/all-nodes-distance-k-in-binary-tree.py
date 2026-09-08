# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parent_map = {}
        def build_parent_map(node, parent):
            if not node:
                return
            parent_map[node] = parent
            build_parent_map(node.left, node)
            build_parent_map(node.right, node)
        build_parent_map(root, None)
        visited = set()
        queue = deque([target])
        visited.add(target)
        distance = 0
        while queue:
            if distance == k:
                return [node.val for node in queue]
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for neighbor in (node.left, node.right, parent_map[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return []
def build_tree(values):
    """
    Build a binary tree from a LeetCode-style level-order list
    (with 'null' represented as None) and return the root node.
    """
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    n = len(values)
    while queue and i < n:
        node = queue.popleft()
        if i < n:
            left_val = values[i]
            i += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
        if i < n:
            right_val = values[i]
            i += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
    return root
def find_node(root, val):
    if not root:
        return None
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.val == val:
            return node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return None
if __name__ == "__main__":
    sol = Solution()
    values1 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root1 = build_tree(values1)
    target1 = find_node(root1, 5)
    k1 = 2
    result1 = sol.distanceK(root1, target1, k1)
    print("Example 1:")
    print("Input: root = {}, target = 5, k = {}".format(values1, k1))
    print("Output:", result1)
    print("Expected: [7, 4, 1] (any order)")
    print()
    values2 = [1]
    root2 = build_tree(values2)
    target2 = find_node(root2, 1)
    k2 = 3
    result2 = sol.distanceK(root2, target2, k2)
    print("Example 2:")
    print("Input: root = {}, target = 1, k = {}".format(values2, k2))
    print("Output:", result2)
    print("Expected: []")
    print()
    values3 = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root3 = build_tree(values3)
    target3 = find_node(root3, 5)
    k3 = 0
    result3 = sol.distanceK(root3, target3, k3)
    print("Additional test (k=0):")
    print("Input: root = {}, target = 5, k = {}".format(values3, k3))
    print("Output:", result3)
    print("Expected: [5]")
print(__name__)