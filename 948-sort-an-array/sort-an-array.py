class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        def heapify(size, root):
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2
            if left < size and nums[left] > nums[largest]:
                largest = left
            if right < size and nums[right] > nums[largest]:
                largest = right
            if largest != root:
                nums[root], nums[largest] = nums[largest], nums[root]
                heapify(size, largest)
        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            heapify(end, 0)
        return nums
if __name__ == "__main__":
    solution = Solution()
    nums1 = [5, 2, 3, 1]
    print("Example 1:")
    print("Input: nums =", nums1)
    print("Output:", solution.sortArray(nums1[:]))
    print()
    nums2 = [5, 1, 1, 2, 0, 0]
    print("Example 2:")
    print("Input: nums =", nums2)
    print("Output:", solution.sortArray(nums2[:]))
print(__name__)