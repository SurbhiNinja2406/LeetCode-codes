# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        heap = []
        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode(0)
        current = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next is not None:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
if __name__ == "__main__":
    sol = Solution()
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]
    result = sol.mergeKLists(lists)
    print(linked_list_to_list(result))  
    result = sol.mergeKLists([])
    print(linked_list_to_list(result)) 
    result = sol.mergeKLists([build_linked_list([])])
    print(linked_list_to_list(result))  
    result = sol.mergeKLists([build_linked_list([1, 2, 3])])
    print(linked_list_to_list(result))  
    result = sol.mergeKLists([build_linked_list([]), build_linked_list([1]), build_linked_list([])])
    print(linked_list_to_list(result)) 
    result = sol.mergeKLists([build_linked_list([]), build_linked_list([]), build_linked_list([])])
    print(linked_list_to_list(result))  
    result = sol.mergeKLists([build_linked_list([1, 1]), build_linked_list([1, 1]), build_linked_list([1])])
    print(linked_list_to_list(result))
print(__name__)