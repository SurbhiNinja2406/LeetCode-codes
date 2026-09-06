class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        total_profit = 0
        best_profit_so_far = 0
        i = 0 
        n = len(jobs)
        for ability in worker:
            while i < n and jobs[i][0] <= ability:
                best_profit_so_far = max(best_profit_so_far, jobs[i][1])
                i += 1
            total_profit += best_profit_so_far
        return total_profit
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])) 
    print(sol.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]))          
print(__name__)