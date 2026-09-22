class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        changes = [0] * 1001        
        for numPassengers, start, end in trips:
            changes[start] += numPassengers
            changes[end] -= numPassengers        
        current_passengers = 0
        for change in changes:
            current_passengers += change
            if current_passengers > capacity:
                return False        
        return True
if __name__ == "__main__":
    solution = Solution()
    trips1 = [[2, 1, 5], [3, 3, 7]]
    capacity1 = 4
    result1 = solution.carPooling(trips1, capacity1)
    print("Example 1: {} (Expected: False)".format(result1))
    trips2 = [[2, 1, 5], [3, 3, 7]]
    capacity2 = 5
    result2 = solution.carPooling(trips2, capacity2)
    print("Example 2: {} (Expected: True)".format(result2))
print(__name__)