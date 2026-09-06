class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = [0] * 121
        for age in ages:
            count[age] += 1
        total_requests = 0
        for ageX in range(1, 121):
            if count[ageX] == 0:
                continue
            for ageY in range(1, ageX + 1):
                if count[ageY] == 0:
                    continue
                if ageY <= 0.5 * ageX + 7:
                    continue
                if ageY > ageX:
                    continue  
                if ageY > 100 and ageX < 100:
                    continue
                if ageX == ageY:
                    total_requests += count[ageX] * (count[ageX] - 1)
                else:
                    total_requests += count[ageX] * count[ageY]
        return total_requests
if __name__ == "__main__":
    sol = Solution()
    print(sol.numFriendRequests([16, 16]))        
    print(sol.numFriendRequests([16, 17, 18]))        
    print(sol.numFriendRequests([20, 30, 100, 110, 120]))
print(__name__)