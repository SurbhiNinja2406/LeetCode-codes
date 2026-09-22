from collections import Counter


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = Counter(arr1)        
        result = []
        for num in arr2:
            result.extend([num] * count[num])
            del count[num]  
        remaining = sorted(count.elements())
        result.extend(remaining)        
        return result
if __name__ == "__main__":
    solution = Solution()
    arr1_1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2_1 = [2, 1, 4, 3, 9, 6]
    result1 = solution.relativeSortArray(arr1_1, arr2_1)
    print("Example 1: {} (Expected: [2,2,2,1,4,3,3,9,6,7,19])".format(result1))
    arr1_2 = [28, 6, 22, 8, 44, 17]
    arr2_2 = [22, 28, 8, 6]
    result2 = solution.relativeSortArray(arr1_2, arr2_2)
    print("Example 2: {} (Expected: [22,28,8,6,17,44])".format(result2))
print(__name__)