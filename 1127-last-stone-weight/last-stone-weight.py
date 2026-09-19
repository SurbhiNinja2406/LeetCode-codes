import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = -heapq.heappop(heap)   
            x = -heapq.heappop(heap)    
            if y != x:
                heapq.heappush(heap, -(y - x)) 
        return -heap[0] if heap else 0
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([2, 7, 4, 1, 8, 1], 1),
        ([1], 1),
        ([3, 3], 0),           
        ([10, 4, 2, 10], 2),
    ]
    for stones, expected in tests:
        result = sol.lastStoneWeight(stones)
        status = "PASS" if result == expected else "FAIL"
        print("{}: got {}, expected {}".format(status, result, expected))
print(__name__)