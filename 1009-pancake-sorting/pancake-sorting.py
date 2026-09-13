class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        result = []
        n = len(arr)        
        def flip(sub_arr, k):
            sub_arr[0:k] = sub_arr[0:k][::-1]        
        for size in range(n, 1, -1):
            idx = arr.index(size)            
            if idx == size - 1:
                continue            
            if idx != 0:
                flip(arr, idx + 1)
                result.append(idx + 1)
            flip(arr, size)
            result.append(size)        
        return result
if __name__ == "__main__":
    sol = Solution()
    def verify_sort(original, flips):
        arr = list(original)
        for k in flips:
            arr[0:k] = arr[0:k][::-1]
        return arr == sorted(original)
    arr1 = [3, 2, 4, 1]
    original1 = list(arr1)
    result1 = sol.pancakeSort(arr1)
    is_sorted1 = verify_sort(original1, result1)
    within_limit1 = len(result1) <= 10 * len(original1)
    print("Input: {}".format(original1))
    print("Output (k values): {}".format(result1))
    print("Sorts correctly: {}".format(is_sorted1))
    print("Within flip limit: {}".format(within_limit1))
    print("Pass: {}\n".format(is_sorted1 and within_limit1))
    arr2 = [1, 2, 3]
    original2 = list(arr2)
    result2 = sol.pancakeSort(arr2)
    is_sorted2 = verify_sort(original2, result2)
    within_limit2 = len(result2) <= 10 * len(original2)
    print("Input: {}".format(original2))
    print("Output (k values): {}".format(result2))
    print("Sorts correctly: {}".format(is_sorted2))
    print("Within flip limit: {}".format(within_limit2))
    print("Pass: {}\n".format(is_sorted2 and within_limit2))
    arr3 = [1]
    original3 = list(arr3)
    result3 = sol.pancakeSort(arr3)
    is_sorted3 = verify_sort(original3, result3)
    print("Input: {}".format(original3))
    print("Output (k values): {}".format(result3))
    print("Sorts correctly: {}".format(is_sorted3))
    print("Pass: {}\n".format(is_sorted3))
    arr4 = [5, 4, 3, 2, 1]
    original4 = list(arr4)
    result4 = sol.pancakeSort(arr4)
    is_sorted4 = verify_sort(original4, result4)
    within_limit4 = len(result4) <= 10 * len(original4)
    print("Input: {}".format(original4))
    print("Output (k values): {}".format(result4))
    print("Sorts correctly: {}".format(is_sorted4))
    print("Within flip limit: {}".format(within_limit4))
    print("Pass: {}\n".format(is_sorted4 and within_limit4))
    arr5 = [7, 1, 5, 3, 6, 2, 4]
    original5 = list(arr5)
    result5 = sol.pancakeSort(arr5)
    is_sorted5 = verify_sort(original5, result5)
    within_limit5 = len(result5) <= 10 * len(original5)
    print("Input: {}".format(original5))
    print("Output (k values): {}".format(result5))
    print("Sorts correctly: {}".format(is_sorted5))
    print("Within flip limit: {}".format(within_limit5))
    print("Pass: {}\n".format(is_sorted5 and within_limit5))
