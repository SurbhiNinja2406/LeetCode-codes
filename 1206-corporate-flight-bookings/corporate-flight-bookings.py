class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats 
        answer = [0] * n
        running_sum = 0
        for i in range(n):
            running_sum += diff[i]
            answer[i] = running_sum
        return answer
if __name__ == "__main__":
    sol = Solution()
    bookings1 = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n1 = 5
    print(sol.corpFlightBookings(bookings1, n1))  
    bookings2 = [[1, 2, 10], [2, 2, 15]]
    n2 = 2
    print(sol.corpFlightBookings(bookings2, n2)) 
print(__name__)