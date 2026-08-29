class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)
        i = 0
        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        return i == n - 1
if __name__ == "__main__":
    sol = Solution()
    print(sol.isOneBitCharacter([1, 0, 0]))
    print("Expected: True\n")
    print(sol.isOneBitCharacter([1, 1, 1, 0]))
    print("Expected: False\n")
    print(sol.isOneBitCharacter([0]))
    print("Expected: True\n")
    print(sol.isOneBitCharacter([1, 1, 0]))
    print("Expected: True\n")
    print(sol.isOneBitCharacter([1, 0, 1, 0]))
    print("Expected: False\n")
    print(sol.isOneBitCharacter([0, 0]))
    print("Expected: True")
print(__name__)