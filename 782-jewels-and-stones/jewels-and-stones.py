class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewel_set = set(jewels)
        return sum(1 for stone in stones if stone in jewel_set)
if __name__ == "__main__":
    sol = Solution()
    jewels, stones = "aA", "aAAbbbb"
    print("Input: jewels = {}, stones = {}".format(jewels, stones))
    print("Output: {}".format(sol.numJewelsInStones(jewels, stones)))
    print("Expected: 3\n")
    jewels, stones = "z", "ZZ"
    print("Input: jewels = {}, stones = {}".format(jewels, stones))
    print("Output: {}".format(sol.numJewelsInStones(jewels, stones)))
    print("Expected: 0\n")
print(__name__)