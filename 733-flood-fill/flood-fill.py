class Solution(object):
    def floodFill(self, image, sr, sc, color):
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]
        if start_color == color:
            return image
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != start_color:
                return
            image[r][c] = color
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr, sc)
        return image
if __name__ == "__main__":
    sol = Solution()
    image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(sol.floodFill(image1, 1, 1, 2))
    image2 = [[0, 0, 0], [0, 0, 0]]
    print(sol.floodFill(image2, 0, 0, 0))
print(__name__)