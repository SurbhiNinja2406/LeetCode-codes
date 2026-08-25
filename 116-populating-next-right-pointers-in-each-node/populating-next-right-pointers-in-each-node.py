# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        leftmost = root 
        while leftmost.left:  
            head = leftmost 
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next  
            leftmost = leftmost.left  
        return root
def build_perfect_tree(values):
    if not values:
        return None
    nodes = [Node(v) for v in values]
    n = len(nodes)
    for i in range(n):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        if left_idx < n:
            nodes[i].left = nodes[left_idx]
        if right_idx < n:
            nodes[i].right = nodes[right_idx]
    return nodes[0] if nodes else None
def print_with_next(root):
    result = []
    leftmost = root
    while leftmost:
        node = leftmost
        while node:
            result.append(node.val)
            node = node.next
        result.append('#')
        leftmost = leftmost.left
    return result
if __name__ == "__main__":
    sol = Solution()
    root1 = build_perfect_tree([1, 2, 3, 4, 5, 6, 7])
    sol.connect(root1)
    print("Test 1: {}".format(print_with_next(root1)))
    root2 = build_perfect_tree([])
    result2 = sol.connect(root2)
    print("Test 2: {}".format(print_with_next(result2) if result2 else [])) 
print(__name__)