class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        rank = {char: i for i, char in enumerate(order)}
        return ''.join(sorted(s, key=lambda c: rank.get(c, len(order))))
if __name__ == "__main__":
    sol = Solution()
    print(sol.customSortString("cba", "abcd"))   
    print(sol.customSortString("bcafg", "abcd")) 
print(__name__)