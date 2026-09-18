class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        ans = [0] * num_people
        give = 1
        i = 0
        while candies > 0:
            idx = i % num_people
            amount = min(give, candies)
            ans[idx] += amount
            candies -= amount
            give += 1
            i += 1
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.distributeCandies(7, 4))   
    print(sol.distributeCandies(10, 3))  
print(__name__)