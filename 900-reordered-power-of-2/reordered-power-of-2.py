class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """        
        def digit_count(num):
            return tuple(sorted(str(num)))        
        target_signature = digit_count(n)
        power = 1
        for i in range(32): 
            if digit_count(power) == target_signature:
                return True
            power *= 2        
        return False
if __name__ == "__main__":
    sol = Solution()
    n1 = 1
    result1 = sol.reorderedPowerOf2(n1)
    print("Example 1:")
    print("Input: n = {}".format(n1))
    print("Output:", result1)
    print("Expected: True")
    print()
    n2 = 10
    result2 = sol.reorderedPowerOf2(n2)
    print("Example 2:")
    print("Input: n = {}".format(n2))
    print("Output:", result2)
    print("Expected: False")
    print()
    n3 = 46
    result3 = sol.reorderedPowerOf2(n3)
    print("Additional test (n=46):")
    print("Input: n = {}".format(n3))
    print("Output:", result3)
    print("Expected: True")
    print()
    n4 = 24
    result4 = sol.reorderedPowerOf2(n4)
    print("Additional test (n=24):")
    print("Input: n = {}".format(n4))
    print("Output:", result4)
    print("Expected: False")
    print()
    n5 = 1801989896
    result5 = sol.reorderedPowerOf2(n5)
    print("Additional test (n=1801989896):")
    print("Input: n = {}".format(n5))
    print("Output:", result5)
    print("Expected: True")
print(__name__)