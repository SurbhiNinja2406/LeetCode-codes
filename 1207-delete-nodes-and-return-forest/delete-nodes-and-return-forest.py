# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        to_delete_set = set(to_delete)
        result = []
        def helper(node, is_root):
            if node is None:
                return None
            deleted = node.val in to_delete_set
            if is_root and not deleted:
                result.append(node)
            node.left = helper(node.left, deleted)
            node.right = helper(node.right, deleted)
            return None if deleted else node
        helper(root, True)
        return result
def build_tree(values):
    if not values or values[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kid_index = 1
    for node in nodes:
        if node is None:
            continue
        if kid_index < len(nodes):
            node.left = nodes[kid_index]
            kid_index += 1
        if kid_index < len(nodes):
            node.right = nodes[kid_index]
            kid_index += 1
    return nodes[0]
def tree_to_list(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result
if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([1, 2, 3, 4, 5, 6, 7])
    to_delete1 = [3, 5]
    forest1 = sol.delNodes(root1, to_delete1)
    print([tree_to_list(t) for t in forest1])
    root2 = build_tree([1, 2, 4, None, 3])
    to_delete2 = [3]
    forest2 = sol.delNodes(root2, to_delete2)
    print([tree_to_list(t) for t in forest2])
print(__name__)