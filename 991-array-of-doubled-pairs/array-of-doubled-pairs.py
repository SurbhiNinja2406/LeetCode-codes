from collections import Counter
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = Counter(arr)
        for x in sorted(count, key=abs):
            if count[x] == 0:
                continue
            if x == 0:
                if count[x] % 2 != 0:
                    return False
                count[x] = 0
                continue
            need = count[x]
            have = count[2 * x]            
            if have < need:
                return False            
            count[2 * x] -= need
            count[x] = 0        
        return True
if __name__ == "__main__":
    sol = Solution()
    arr1 = [3, 1, 3, 6]
    result1 = sol.canReorderDoubled(arr1)
    print("Input: {}".format(arr1))
    print("Output: {}".format(result1))
    print("Expected: False")
    print("Pass: {}\n".format(result1 == False))
    arr2 = [2, 1, 2, 6]
    result2 = sol.canReorderDoubled(arr2)
    print("Input: {}".format(arr2))
    print("Output: {}".format(result2))
    print("Expected: False")
    print("Pass: {}\n".format(result2 == False))
    arr3 = [4, -2, 2, -4]
    result3 = sol.canReorderDoubled(arr3)
    print("Input: {}".format(arr3))
    print("Output: {}".format(result3))
    print("Expected: True")
    print("Pass: {}\n".format(result3 == True))
    arr4 = [0, 0, 0, 0]
    result4 = sol.canReorderDoubled(arr4)
    print("Input: {}".format(arr4))
    print("Output: {}".format(result4))
    print("Expected: True")
    print("Pass: {}\n".format(result4 == True))
    arr5 = [0, 0, 0, 1]
    result5 = sol.canReorderDoubled(arr5)
    print("Input: {}".format(arr5))
    print("Output: {}".format(result5))
    print("Expected: False")
    print("Pass: {}\n".format(result5 == False))
    arr6 = [1, 2]
    result6 = sol.canReorderDoubled(arr6)
    print("Input: {}".format(arr6))
    print("Output: {}".format(result6))
    print("Expected: True")
    print("Pass: {}\n".format(result6 == True))
    arr7 = [-1, -2]
    result7 = sol.canReorderDoubled(arr7)
    print("Input: {}".format(arr7))
    print("Output: {}".format(result7))
    print("Expected: True")
    print("Pass: {}\n".format(result7 == True))
print(__name__)