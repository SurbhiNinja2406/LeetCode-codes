class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        people = [i for i, seat in enumerate(seats) if seat == 1]
        max_dist = 0
        max_dist = max(max_dist, people[0])
        max_dist = max(max_dist, n - 1 - people[-1])
        for i in range(1, len(people)):
            gap = people[i] - people[i - 1]
            max_dist = max(max_dist, gap // 2)
        return max_dist
if __name__ == "__main__":
    solution = Solution()
    seats1 = [1, 0, 0, 0, 1, 0, 1]
    print(solution.maxDistToClosest(seats1)) 
    seats2 = [1, 0, 0, 0]
    print(solution.maxDistToClosest(seats2))  
    seats3 = [0, 1]
    print(solution.maxDistToClosest(seats3))  
    seats4 = [1, 0, 0, 0, 0, 1]
    print(solution.maxDistToClosest(seats4))  
    seats5 = [0, 0, 0, 1]
    print(solution.maxDistToClosest(seats5))  
    seats6 = [1, 0, 1, 0, 1, 0, 1]
    print(solution.maxDistToClosest(seats6)) 
print(__name__)