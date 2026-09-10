class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)
        total = 0
        for i in range(n):
            total += arr[i] * left[i] * right[i]
        return total % MOD
if __name__ == "__main__":
    solution = Solution()
    arr1 = [3, 1, 2, 4]
    print("Example 1:")
    print("Input: arr =", arr1)
    print("Output:", solution.sumSubarrayMins(arr1))
    print()
    arr2 = [11, 81, 94, 43, 3]
    print("Example 2:")
    print("Input: arr =", arr2)
    print("Output:", solution.sumSubarrayMins(arr2))
print(__name__)