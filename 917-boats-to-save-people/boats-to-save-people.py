class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats
if __name__ == "__main__":
    sol = Solution()
    people1, limit1 = [1, 2], 3
    result1 = sol.numRescueBoats(people1, limit1)
    print("Example 1: {} (expected 1)".format(result1))
    people2, limit2 = [3, 2, 2, 1], 3
    result2 = sol.numRescueBoats(people2, limit2)
    print("Example 2: {} (expected 3)".format(result2))
    people3, limit3 = [3, 5, 3, 4], 5
    result3 = sol.numRescueBoats(people3, limit3)
    print("Example 3: {} (expected 4)".format(result3))
print(__name__)