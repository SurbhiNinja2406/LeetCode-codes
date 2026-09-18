class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        n = len(books)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            width = 0
            height = 0
            dp[i] = float('inf')
            j = i
            while j >= 1:
                thickness, h = books[j - 1]
                width += thickness
                if width > shelfWidth:
                    break
                height = max(height, h)
                dp[i] = min(dp[i], dp[j - 1] + height)
                j -= 1
        return dp[n]
if __name__ == "__main__":
    sol = Solution()
    books1 = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
    shelfWidth1 = 4
    print(sol.minHeightShelves(books1, shelfWidth1)) 
    books2 = [[1, 3], [2, 4], [3, 2]]
    shelfWidth2 = 6
    print(sol.minHeightShelves(books2, shelfWidth2))  
print(__name__)