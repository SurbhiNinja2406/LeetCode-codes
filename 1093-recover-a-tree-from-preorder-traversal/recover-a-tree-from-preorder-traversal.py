# Definition for a binary tree node.
'''
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        :type traversal: str
        :rtype: Optional[TreeNode]
        """
        stack = []
        i = 0
        n = len(traversal)
        while i < n:
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            j = i
            while j < n and traversal[j] != '-':
                j += 1
            val = int(traversal[i:j])
            i = j
            node = TreeNode(val)
            while len(stack) > depth:
                stack.pop()
            if stack:
                parent = stack[-1]
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node
            stack.append(node)
        return stack[0] if stack else None
def tree_to_list(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("1-2--3--4-5--6--7", [1, 2, 5, 3, 4, 6, 7]),
        ("1-2--3---4-5--6---7", [1, 2, 5, 3, None, 6, None, 4, None, None, 7]),
        ("1-401--349---90--88", [1, 401, None, 349, 88, 90]),
    ]
    for traversal, expected in test_cases:
        root = sol.recoverFromPreorder(traversal)
        result = tree_to_list(root)
        status = "PASS" if result == expected else "FAIL"
        print("traversal={0!r} -> {1} (expected {2}) [{3}]".format(
            traversal, result, expected, status
        ))
print(__name__)