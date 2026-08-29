class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        new_node = Node(insertVal)
        if head is None:
            new_node.next = new_node
            return new_node
        if head.next == head:
            head.next = new_node
            new_node.next = head
            return head
        prev, curr = head, head.next
        inserted = False
        while curr != head:
            if prev.val <= insertVal <= curr.val:
                inserted = True
                break
            if prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    inserted = True
                    break
            prev, curr = curr, curr.next
        prev.next = new_node
        new_node.next = curr
        return head
if __name__ == "__main__":
    def build_circular(vals, head_index=0):
        if not vals:
            return None
        nodes = [Node(v) for v in vals]
        n = len(nodes)
        for i in range(n):
            nodes[i].next = nodes[(i + 1) % n]
        return nodes[head_index]
    def to_list(head):
        if head is None:
            return []
        vals = [head.val]
        curr = head.next
        while curr != head:
            vals.append(curr.val)
            curr = curr.next
        return vals
    sol = Solution()
    head1 = build_circular([3, 4, 1], head_index=0)
    result1 = sol.insert(head1, 2)
    print("Example 1 output:", to_list(result1))
    print("Example 1 expected: [3, 4, 1, 2]\n")
    head2 = build_circular([], head_index=0)
    result2 = sol.insert(head2, 1)
    print("Example 2 output:", to_list(result2))
    print("Example 2 expected: [1]\n")
    head3 = build_circular([1], head_index=0)
    result3 = sol.insert(head3, 0)
    print("Example 3 output:", to_list(result3))
    print("Example 3 expected: [1, 0]\n")
    head4 = build_circular([1, 3, 5], head_index=0)
    result4 = sol.insert(head4, 10)
    print("Extra test (insert max) output:", to_list(result4))
    head5 = build_circular([3, 3, 3], head_index=0)
    result5 = sol.insert(head5, 0)
    print("Extra test (all duplicates) output:", to_list(result5))
print(__name__)