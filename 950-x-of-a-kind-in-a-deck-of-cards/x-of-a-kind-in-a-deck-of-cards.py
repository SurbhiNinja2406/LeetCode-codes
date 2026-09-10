from collections import Counter
from functools import reduce
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        counts = Counter(deck).values()
        g = reduce(gcd, counts)
        return g >= 2
if __name__ == "__main__":
    sol = Solution()
    deck1 = [1, 2, 3, 4, 4, 3, 2, 1]
    print("Input: {}".format(deck1))
    print("Output: {}".format(sol.hasGroupsSizeX(deck1)))
    print()
    deck2 = [1, 1, 1, 2, 2, 2, 3, 3]
    print("Input: {}".format(deck2))
    print("Output: {}".format(sol.hasGroupsSizeX(deck2)))
    print()
    deck3 = [1]
    print("Input: {}".format(deck3))
    print("Output: {}".format(sol.hasGroupsSizeX(deck3)))
print(__name__)