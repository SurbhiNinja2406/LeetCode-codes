# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None        
        slow = head
        fast = head
        has_cycle = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next            
            if slow == fast:
                has_cycle = True
                break        
        if not has_cycle:
            return None
        pointer1 = head
        pointer2 = slow
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next        
        return pointer1
def build_linked_list(values, pos):
    if not values:
        return None    
    nodes = [ListNode(v) for v in values]    
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]    
    if pos != -1:
        nodes[-1].next = nodes[pos]    
    return nodes[0]
if __name__ == "__main__":
    sol = Solution()
    head1 = build_linked_list([3, 2, 0, -4], 1)
    result1 = sol.detectCycle(head1)
    print(result1.val if result1 else None)  
    head2 = build_linked_list([1, 2], 0)
    result2 = sol.detectCycle(head2)
    print(result2.val if result2 else None) 
    head3 = build_linked_list([1], -1)
    result3 = sol.detectCycle(head3)
    print(result3.val if result3 else None)
print(__name__)