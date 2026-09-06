class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            row.reverse()         
            for i in range(len(row)):
                row[i] ^= 1        
        return image
if __name__ == "__main__":
    sol = Solution()
    print(sol.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
    print(sol.flipAndInvertImage([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
print(__name__)