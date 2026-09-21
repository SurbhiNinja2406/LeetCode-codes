from collections import Counter

class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        counts = Counter(tiles)
        def backtrack():
            total = 0
            for ch in counts:
                if counts[ch] > 0:
                    counts[ch] -= 1          
                    total += 1 + backtrack()  
                    counts[ch] += 1       
            return total
        return backtrack()
if __name__ == "__main__":
    sol = Solution()
    tests = [
        "AAB",  
        "AAABBC", 
        "V",   
    ]
    for t in tests:
        print('tiles = "{}" -> {}'.format(t, sol.numTilePossibilities(t)))
print(__name__)