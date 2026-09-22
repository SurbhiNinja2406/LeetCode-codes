from collections import defaultdict
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        count = defaultdict(int)
        result = 0        
        for a, b in dominoes:
            key = (a, b) if a <= b else (b, a)
            result += count[key]
            count[key] += 1        
        return result
if __name__ == "__main__":
    sol = Solution()
    dominoes1 = [[1, 2], [2, 1], [3, 4], [5, 6]]
    print("Input:", dominoes1)
    print("Output:", sol.numEquivDominoPairs(dominoes1))  
    dominoes2 = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
    print("\nInput:", dominoes2)
    print("Output:", sol.numEquivDominoPairs(dominoes2)) 
print(__name__)