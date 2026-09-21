class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        result = []  
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += arr1[i]
                i -= 1
            if j >= 0:
                total += arr2[j]
                j -= 1
            result.append(total & 1) 
            carry = -(total >> 1)    
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result[::-1]
if __name__ == "__main__":
    sol = Solution()
    tests = [
        ([1, 1, 1, 1, 1], [1, 0, 1]),  
        ([0], [0]),       
        ([0], [1]),          
    ]
    for a, b in tests:
        print("arr1 = {}, arr2 = {} -> {}".format(a, b, sol.addNegabinary(a, b)))
print(__name__)