import heapq
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)  
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
if __name__ == "__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))  
    print(kthLargest.add(5))   
    print(kthLargest.add(10))  
    print(kthLargest.add(9))  
    print(kthLargest.add(4))  
    print("---")
    kthLargest2 = KthLargest(4, [7, 7, 7, 7, 8, 3])
    print(kthLargest2.add(2))   
    print(kthLargest2.add(10)) 
    print(kthLargest2.add(9))   
    print(kthLargest2.add(9))  
print(__name__) 
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)