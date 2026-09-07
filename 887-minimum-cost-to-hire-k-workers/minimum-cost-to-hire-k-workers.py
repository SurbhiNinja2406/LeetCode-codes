import heapq
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        n = len(quality)
        workers = sorted(
            (float(wage[i]) / quality[i], quality[i]) for i in range(n)
        )
        max_heap = []
        quality_sum = 0
        min_cost = float('inf')
        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            quality_sum += q
            if len(max_heap) > k:
                removed_q = -heapq.heappop(max_heap)
                quality_sum -= removed_q
            if len(max_heap) == k:
                cost = ratio * quality_sum
                min_cost = min(min_cost, cost)
        return min_cost
if __name__ == "__main__":
    solution = Solution()
    quality1 = [10, 20, 5]
    wage1 = [70, 50, 30]
    k1 = 2
    print(solution.mincostToHireWorkers(quality1, wage1, k1)) 
    quality2 = [3, 1, 10, 10, 1]
    wage2 = [4, 8, 2, 2, 7]
    k2 = 3
    print(solution.mincostToHireWorkers(quality2, wage2, k2))  
    quality3 = [1, 2, 3]
    wage3 = [4, 5, 6]
    k3 = 3
    print(solution.mincostToHireWorkers(quality3, wage3, k3))
    quality4 = [5, 8, 3]
    wage4 = [50, 40, 30]
    k4 = 1
    print(solution.mincostToHireWorkers(quality4, wage4, k4))
print(__name__)