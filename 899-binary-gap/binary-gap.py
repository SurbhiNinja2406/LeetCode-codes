class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        binary_str = bin(n)[2:] 
        one_positions = []
        for i, bit in enumerate(binary_str):
            if bit == '1':
                one_positions.append(i)
        if len(one_positions) < 2:
            return 0
        max_distance = 0
        for i in range(1, len(one_positions)):
            distance = one_positions[i] - one_positions[i - 1]
            max_distance = max(max_distance, distance)        
        return max_distance
if __name__ == "__main__":
    sol = Solution()
    n1 = 22
    result1 = sol.binaryGap(n1)
    print("Example 1:")
    print("Input: n = {}".format(n1))
    print("Output:", result1)
    print("Expected: 2")
    print()
    n2 = 8
    result2 = sol.binaryGap(n2)
    print("Example 2:")
    print("Input: n = {}".format(n2))
    print("Output:", result2)
    print("Expected: 0")
    print()
    n3 = 5
    result3 = sol.binaryGap(n3)
    print("Example 3:")
    print("Input: n = {}".format(n3))
    print("Output:", result3)
    print("Expected: 2")
    print()
    n4 = 1
    result4 = sol.binaryGap(n4)
    print("Additional test (n=1):")
    print("Input: n = {}".format(n4))
    print("Output:", result4)
    print("Expected: 0")
    print()
    n5 = 1041
    result5 = sol.binaryGap(n5)
    print("Additional test (n=1041):")
    print("Input: n = {}".format(n5))
    print("Output:", result5)
    print("Expected: 5 (1041 in binary is '10000010001')")
print(__name__)