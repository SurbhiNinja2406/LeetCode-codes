from collections import defaultdict
class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]        
        if not ones1 or not ones2:
            return 0
        vector_counts = defaultdict(int)
        max_overlap = 0        
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                dr = r2 - r1
                dc = c2 - c1
                vector_counts[(dr, dc)] += 1
                max_overlap = max(max_overlap, vector_counts[(dr, dc)])        
        return max_overlap
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]))  
    print(sol.largestOverlap([[1]], [[1]]))                    
    print(sol.largestOverlap([[0]], [[0]]))         
print(__name__)