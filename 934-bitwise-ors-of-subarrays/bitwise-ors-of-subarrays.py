class Solution(object):
    def subarrayBitwiseORs(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = set()
        prev = set() 
        for num in arr:
            cur = {num}
            for p in prev:
                cur.add(p | num)
            result |= cur
            prev = cur
        return len(result)
if __name__ == "__main__":
    solution = Solution()
    arr1 = [0]
    print("Example 1:")
    print("Input: ", arr1)
    print("Output:", solution.subarrayBitwiseORs(arr1))
    print()
    arr2 = [1, 1, 2]
    print("Example 2:")
    print("Input: ", arr2)
    print("Output:", solution.subarrayBitwiseORs(arr2))
    print()
    arr3 = [1, 2, 4]
    print("Example 3:")
    print("Input: ", arr3)
    print("Output:", solution.subarrayBitwiseORs(arr3))